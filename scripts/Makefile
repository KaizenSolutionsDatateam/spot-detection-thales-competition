ddl_results: all_result_df.csv # download private result

all_result_df.csv: ddl_results.py
	python ddl_results.py

clear_cache: # clear cache
	find ./ddl/*_output* -exec rm -rf {} +

final_rank:
	python final_rank.py
