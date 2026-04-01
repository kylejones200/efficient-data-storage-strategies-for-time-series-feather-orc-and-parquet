# Description: Short example for Efficient Data Storage Strategies for Time Series Feather ORC and Parquet.



from data_io import read_csv
import logging
import os
import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import pyarrow.orc as orc
import pyarrow.parquet as pq
import time

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)



# Define file names
file_formats = {
    "CSV": "movies.csv",
    "Parquet": "movies.parquet",
    "Feather": "movies.feather",
    "ORC": "movies.orc",
}

# Save the dataset in different formats
df.to_csv(file_formats["CSV"], index=False)
df.to_parquet(file_formats["Parquet"], index=False)
df.to_feather(file_formats["Feather"])

# ORC requires pyarrow Table format
table = pa.Table.from_pandas(df)
orc.write_table(table, file_formats["ORC"])

# Function to measure loading time
def measure_load_time(file_format, load_func):
    start_time = time.time()
    df_loaded = load_func()
    end_time = time.time()
    size = os.path.getsize(file_formats[file_format]) / (1024**2)  # Convert to MB
    return size, end_time - start_time

# Load functions for each format
load_functions = {
    "CSV": lambda: read_csv(file_formats["CSV"]),
    "Parquet": lambda: pd.read_parquet(file_formats["Parquet"]),
    "Feather": lambda: pd.read_feather(file_formats["Feather"]),
    "ORC": lambda: orc.read_table(file_formats["ORC"]).to_pandas(),  
}

# Measure load times and sizes
results = []
for fmt, func in load_functions.items():
    size, load_time = measure_load_time(fmt, func)
    results.append({"Format": fmt, "Size (MB)": size, "Load Time (s)": load_time})

# Convert results to DataFrame and display
results_df = pd.DataFrame(results)
logger.info(results_df)

#     Format  Size (MB)  Load Time (s)
# 0      CSV  41.373181       0.395387
# 1  Parquet  18.819997       0.160249
# 2  Feather  33.856363       0.149243
# 3      ORC  33.806019       0.187391
