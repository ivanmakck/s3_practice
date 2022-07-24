# Data Engineering - Transforming data and uploading to AWS S3

This repository contains code where I get data from [The Muse](https://www.themuse.com/developers/api/v2) and do simple data transformations with the purpose of practicing data manipulation using pandas, shell scripting, and uploading to S3.

There are two python run files (`run_boto3.py` and `run_s3cp.py`) that perform the data transformations, however one is done using boto3 to upload to S3, while the other is a direct copy using the AWS CLI.
The `init.sh` script initializes the environment by creating a virtual environment and installing all libraries and dependencies.
The `run.sh` script runs the python script and provides additional functionality such as logging.