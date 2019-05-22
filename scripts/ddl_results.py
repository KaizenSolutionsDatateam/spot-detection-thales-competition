import requests as rq
import shutil
import os
import getpass
from bs4 import BeautifulSoup
import pandas as pd
import tqdm
from zipfile import ZipFile
import re

# logging
import logging
logger = logging.getLogger("ddl_result")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("ddl_results.log", mode="w")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info("Start")

# for SE access
if os.name == 'posix':
    os.environ['REQUESTS_CA_BUNDLE'] = \
        "/etc/ssl/certs/ca-certificates.crt"

## get the password
login = getpass.getpass(prompt='Codalab login?')
pw = getpass.getpass(prompt='Codalab password?')
logger.info(f'login {login}')

# params
base_url = "https://competitions.codalab.org/accounts/login/"

## ts
s = rq.Session()
r = s.get(base_url)
r = s.post(base_url, data={'login': login, 'password': pw},
           headers={'Referer': base_url})
# login
r = s.post(base_url, data={'login': login, 'password': pw,
                           'csrfmiddlewaretoken': r.request.headers["Cookie"].split("=")[1]},
           headers={'Referer': base_url})
logger.info(r)
# get all the submissions ans scrores
dfs = []
for page in tqdm.tqdm(range(1, 34)):
    table_url = f'https://competitions.codalab.org/my/competition/21639/submissions/?page={page}&phase=36559'
    logger.info(f'table url: {table_url}')
    r = s.get(table_url)
    soup = BeautifulSoup(r.content,'lxml')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    df = df[['SUBMITTED', 'SUBMITTED BY', 'SUBMISSION ID', 'FILENAME', 'STATUS',
             'LEADERBOARD', 'Results']]

    # download the zip files
    for d, row in df.iterrows():
        i = row['SUBMISSION ID']
        if row["STATUS"] == "Finished":
            to_ddl_url = f'https://competitions.codalab.org/my/competition/submission/{i}/private_output.zip'
            path = f'ddl/{i}_private_output.zip'
            unzip_path = path.split(".")[0]
            if os.path.isfile(path):
                logger.info("Get it from CACHE")
            else:
                logger.info("DOWLOAD the zip res")
                logger.info(f'ddl: {to_ddl_url}')
                r = s.get(to_ddl_url)
                open(path, 'wb').write(r.content)
                # extract all the scrore
                with ZipFile(path, 'r') as zipObj:
                    # Extract all the contents of zip file in different directory
                    zipObj.extractall(unzip_path)

            # read the scores (ugly way but it works)
            res = [re.findall('The score on this part is .*', line) \
                        for line in open(f'{unzip_path}/private/priv.txt')]
            res = [r for r in res if (len(r) != 0)]
            public_score = float(re.findall('[.|0-9]+', res[0][0])[0])
            assert isinstance(public_score, float)
            assert public_score > 0.0
            # the is suposed to be same that the Results column
            assert abs(float(row["Results"]) - public_score) < 1e-5
            # private scores
            res = [re.findall('The score on all data is .*', line) \
                        for line in open(f'{unzip_path}/private/priv.txt')]
            res = [r for r in res if (len(r) != 0)]
            private_score = float(re.findall('[.|0-9]+', res[0][0])[0])
            assert isinstance(private_score, float)
            assert public_score > 0.0
            dfs.append({"status": row["STATUS"],
                        "competitor":row["SUBMITTED BY"],
                        "submission_id": row["SUBMISSION ID"],
                        "public_score": public_score,
                        "private_score": private_score})
# close the connection
s.close()

# dump the results
all_res_df = pd.DataFrame(dfs)
all_res_df.to_csv("all_res_df.csv", index = False)
