# server-backup-to-s3

A simple Python script to back up server files and directories to an Amazon S3 bucket using Boto3.

---

## Features

- Uploads files and folders recursively to S3
- Easy configuration of local paths and S3 bucket
- Supports backing up multiple files/directories
- Lightweight and customizable
- Includes error handling for reliable operation
- Optional compression for faster uploads

---

## Prerequisites

- Python 3.6 or higher
- AWS account with access to an S3 bucket
- AWS CLI installed and configured with credentials (`aws configure`)
- Boto3 Python package

---

## AWS CLI Installation

### Ubuntu / Linux

```bash
sudo apt update
sudo apt install unzip -y
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
# Verify installation
aws --version
```

### macOS

```bash
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
# Verify installation
aws --version
```

### Windows

1. Download the AWS CLI MSI installer from: https://awscli.amazonaws.com/AWSCLIV2.msi
2. Run the installer and follow the prompts.
3. Verify installation:
   ```bash
   aws --version
   ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/server-backup-to-s3.git
   cd server-backup-to-s3
   ```

2. Install the required Python package:
   ```bash
   pip install boto3
   ```

3. Configure AWS credentials:
   ```bash
   aws configure
   ```
   Provide your AWS Access Key ID, Secret Access Key, region, and output format when prompted.

---

## Configuration

1. Edit the `config.json` file to specify your backup settings:
   ```json
   {
       "bucket_name": "your-s3-bucket-name",
       "local_paths": [
           "/path/to/your/folder1",
           "/path/to/your/folder2"
       ],
       "s3_prefix": "backups/",
       "compress": true
   }
   ```
   - `bucket_name`: Your S3 bucket name.
   - `local_paths`: List of local files or directories to back up.
   - `s3_prefix`: S3 folder path to store backups (optional).
   - `compress`: Set to `true` to compress files before upload (optional).

---

## Usage

Run the backup script:
```bash
python main.py
```

### Example

To back up `/var/www/html` and `/etc/nginx` to an S3 bucket named `my-backup-bucket`:
1. Update `config.json`:
   ```json
   {
       "bucket_name": "my-backup-bucket",
       "local_paths": [
           "/var/www/html",
           "/etc/nginx"
       ],
       "s3_prefix": "server-backups/",
       "compress": true
   }
   ```
2. Execute:
   ```bash
   python main.py
   ```

The script will upload the specified files and directories to `s3://my-backup-bucket/server-backups/`.

---

## Script Overview

The `main.py` script:
- Reads configuration from `config.json`
- Compresses files/directories into `.zip` files if `compress` is enabled
- Uploads files to the specified S3 bucket using Boto3
- Preserves directory structure in S3
- Logs progress and errors to the console
