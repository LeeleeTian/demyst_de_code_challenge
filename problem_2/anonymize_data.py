from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType
from faker import Faker
import sys
import os
import shutil

def anonymize_data(input_file, output_file):
    fake = Faker()
    spark = SparkSession.builder.appName("Anonymize Data").getOrCreate()
    
    df = spark.read.csv(input_file, header=True, inferSchema=True)
    
    # UDFs for anonymization
    fixed_first_name = udf(lambda: "JOHN", StringType())
    fixed_last_name = udf(lambda: "DOE", StringType())
    fixed_address = udf(lambda: "123 Main Street, City, State", StringType())
    
    anonymized_df = df.withColumn("first_name", fixed_first_name()) \
                      .withColumn("last_name", fixed_last_name()) \
                      .withColumn("address", fixed_address())
    
    # Use coalesce to write to a single file
    temp_output_dir = "temp_output"
    anonymized_df.coalesce(1).write.option("header", True).csv(temp_output_dir, mode='overwrite')

    # Find the part file in the temporary directory
    part_file = next((f for f in os.listdir(temp_output_dir) if f.startswith('part-')), None)
    if part_file:
        temp_part_file = os.path.join(temp_output_dir, part_file)
        # Use shutil.move to move across file systems
        shutil.move(temp_part_file, output_file)

    # Clean up the temporary directory
    shutil.rmtree(temp_output_dir)

    # Stop the Spark session
    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python anonymize_data.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        anonymize_data(input_file, output_file)
