
# Overview

This tools helps in migrating kudu table schema and data to BigQuery. 


## Prerequisite: 
1. Download below jars
    - kudu-spark3_2.12-1.17.0.jar - https://repo1.maven.org/maven2/org/apache/kudu/kudu-spark3_2.12/1.17.0/kudu-spark3_2.12-1.17.0.jar ,

    - spark-bigquery_2.13-0.36.1.jar  -  https://repo1.maven.org/maven2/com/google/cloud/spark/spark-bigquery_2.13/0.36.1/spark-bigquery_2.13-0.36.1.jar
2. Create dataset in bigquery to load the kudu tables
3. Create dataproc cluster to submit the spark job to migrate .
4. Check the dataproc cluster is able to connect to kudu cluster via jdbc .


## Run command: 

```
pyspark --jars gs://spark-code-jars/kudu-spark3_2.12-1.15.0.7.1.7.2000-305.jar,gs://spark-code-jars/spark-3.1-bigquery-0.34.0.jar app.py
```

```
gcloud dataproc jobs submit pyspark --cluster <dataproc-cluster-name> --region <dataproc-region> --jars gs://cfr-legacy-jar-repo/kudu-spark3_2.12-1.15.0.7.1.7.2000-305.jar,gs://cfr-legacy-jar-repo/spark-3.1-bigquery-0.34.0.jar <gs-bucket-path>/app.py -- <project_id> <process_table> <master_ip> <temp_gcs_staging>
```

### parameters: 
- project_id = gcp project id
- process_table = kudu table name 
- master_ip = kudu master ip in comma separated
- temp_gcs_staging =  gcs bucket for staging files for spark job