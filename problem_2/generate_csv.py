from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
import sys
import os
import shutil

def generate_csv(file_size_gb, output_file):
    # Initialize Spark session
    spark = SparkSession.builder.appName("GenerateCSV").getOrCreate()

    # Calculate the number of rows based on approximate size
    # Assuming average row size to be around 200 bytes, adjust as needed
    bytes_per_row = 200
    num_rows = int(file_size_gb * (1024**3) / bytes_per_row)

    # Generate a DataFrame with synthetic data
    df = spark.range(num_rows).select(
        expr("CAST(id AS STRING) as first_name"),
        expr("CAST(id + 1 AS STRING) as last_name"),
        expr("CAST(id + 2 AS STRING) as address"),
        expr("DATE_FORMAT(CURRENT_DATE(), 'yyyy-MM-dd') as date_of_birth")
    )
    
    # Use coalesce to write to a single file
    df.coalesce(1).write.option("header", True).csv(output_file, mode='overwrite')

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    # Expecting two arguments: file_size_gb and output_file
    file_size_gb = float(sys.argv[1])
    output_file = sys.argv[2]
    generate_csv(file_size_gb, output_file)
