# jupiter notebooks for databricks spark-sandbox
Below serverless options are same regarding spark perspective. They all use Databrick's Workshop UI. Just Register cloud account and open your workhop UI.


## How to start in Databricks Workshop UI
- [1] Add a cluster on databricks workshop.
- [3] Add a dataset from your local system
   - [ ] Manually upload file to DBFS 
   - [ ] Manually upload file to DBFS and import as a Table (not meaningful for all scenarions)
   - [ ] Manually upload file to DBFS within jupiter-notebook using DBFS commands or `%fs` blocks (not supoorts everything) 
   - [ ] Upload many files/file to DBFS w/ Databricks CLI
   - [x] Upload many files/file to Azure Data Lake Storage w/ manually or Azure CLI (This is **datalake** architecture and much more suitable for Big Data Architectural approaches)

And start developin in jupiter-notebooks.
