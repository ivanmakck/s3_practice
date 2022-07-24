import requests
import json
import toml
import pandas as pd
import subprocess

app_config = toml.load("config.toml")

response = requests.get(app_config["api"]["url"])
data = response.json()

# get job info
print("Getting data...")
company_list = [data["results"][i]["company"]["name"] for i in range(len(data["results"]))]
location_list = [data["results"][i]["locations"][0]["name"] for i in range(len(data["results"]))]
job_name_list = [data["results"][i]["name"] for i in range(len(data["results"]))]
job_type_list = [data["results"][i]["type"] for i in range(len(data["results"]))]
pub_date_list = [data["results"][i]["publication_date"] for i in range(len(data["results"]))]

# clean up data as per requirements
print("Creating dataframe...")
df = pd.DataFrame(list(zip(company_list, location_list, job_name_list, job_type_list, pub_date_list)), columns=["company_name", "location", "job", "job_type", "publication_date"])

df["country"] = df["location"].str.split(",").str[1]
df["city"] = df["location"].str.split(",").str[0]
df["date"] = df["publication_date"].str.split("T").str[0]
df.drop(["location", "publication_date"], axis=1, inplace=True)

# export to csv and upload to s3
print("Exporting to csv...")
df.to_csv("jobs.csv", index=False)

bucket=app_config["aws"]["bucket_full"]
folder=app_config["aws"]["folder_s3cp"]
subprocess.run(["aws", "s3", "cp", "jobs.csv", f"{bucket}/{folder}/jobs.csv"])

print("File Uploaded to S3!")