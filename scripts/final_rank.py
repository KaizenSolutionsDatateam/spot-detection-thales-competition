"""
And the winner is...
"""
import pandas as pd
# logging
import logging
logger = logging.getLogger("final_rank")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("final_rank.log", mode="w")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.info("Start")

logger.info("Load data")
all_res_df = pd.read_csv("all_res_df.csv")

# remove duplicated submission
clean_res_df = all_res_df.drop_duplicates(["competitor", "private_score"])

idx = (clean_res_df.groupby(['competitor'])['private_score'].transform(min) ==
       clean_res_df['private_score'])
final_rank = clean_res_df[idx].sort_values("private_score")
print(final_rank)
