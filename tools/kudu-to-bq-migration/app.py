"""
  Copyright 2024 Google LLC. This software is provided as-is, without warranty
  or representation for any use or purpose. Your use of it is subject to your
  agreement with Google.
"""

import sys


sc = SparkContext().getOrCreate()

spark = SparkSession(sc)

project_id = sys.argv[1]
process_table = sys.argv[2]
master_ip = sys.argv[3]
temp_gcs_staging = sys.argv[4]


kudu_source_table = f"impala::{process_table}"
bq_target_table = f"{project_id}:{process_table}"

print(f"source kudu table: {kudu_source_table}")
print(f"target bq table : {bq_target_table}")

kd_op = {"kudu.master":master_ip, "kudu.table":kudu_source_table}

kuduDF = spark.read.format('org.apache.kudu.spark.kudu').options(**kd_op).load()

spark.conf.set("temporaryGcsBucket",temp_gcs_staging)


kuduDF.write.format('bigquery') \
          .option('table', bq_target_table).mode("overwrite") \
            .save()