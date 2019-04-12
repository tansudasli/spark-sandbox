# jupiter notebooks for Amazon EMR Spark
AWS EMR is same as apache spark concepts. Use s3 buckets for data lake.

## How to start in Amazon EMR 
- [0] Create an aws account, <br>
    Install AWS CLI: `brew install awscli` <br>
    Configure your profile: `aws configure --profile profile_name`
- [1] Add a cluster in EMR via UI
- [2] Create a S3 bucket for datasets. Change `spark-dataset-sandbox` this name to make unique! <br>
    `aws s3 mb s3://spark-dataset-sandbox/datasets --profile ....`
- [3] Add dataset folder from your local where your `cd spark-sandbox` <br>
    `aws s3 cp datasets/ s3://spark-dataset-sandbox/datasets/ --recursive --profile profile_name`
- [4] Create a jupiter notebook

So we can write jupiter-notebooks in EMR UI and access our datasets from in it.