import boto3
import os
from pathlib import Path

# Configuration
bucket_name = 'your-s3-bucket-name'
s3_folder = 'server-backups/'  # Optional: prefix in S3 bucket
local_paths = [
    '/etc/nginx/nginx.conf'
]

# Initialize S3 client
s3 = boto3.client('s3')

def upload_file(file_path, bucket, s3_key):
    try:
        s3.upload_file(file_path, bucket, s3_key)
        print(f"Uploaded: {file_path} -> s3://{bucket}/{s3_key}")
    except Exception as e:
        print(f"Failed to upload {file_path}: {e}")

for path in local_paths:
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, start=path)
                s3_key = os.path.join(s3_folder, Path(path).name, relative_path)
                upload_file(full_path, bucket_name, s3_key)
    elif os.path.isfile(path):
        s3_key = os.path.join(s3_folder, Path(path).name)
        upload_file(path, bucket_name, s3_key)
    else:
        print(f"Path not found: {path}")
