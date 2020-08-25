from google.oauth2 import service_account
import googleapiclient as google
from googleapiclient.http import MediaFileUpload, HttpRequest
from googleapiclient.discovery import build
from datetime import datetime
from glob import glob
import os, shutil

import clean
import compress

from config import BASE_DIR, FOLDER_ID



compress.zip_files()

SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(BASE_DIR + '/service-credentials.json', scopes=SCOPES)



service = build('drive', 'v3', credentials=credentials)
try:
    for file_name in glob(BASE_DIR + '/database/*.zip'):
        print(f"uploading {file_name}...")

        now = datetime.now().strftime('%Y-%m-%d--%H:%M:%S')
        db_name = f'DB-{now}.zip'
        file_metadata = {'name' : db_name, 'parents': [FOLDER_ID]} ## parents value should be the Folder ID of a sharable folder with your service account email
        media = MediaFileUpload(file_name, mimetype='application/zip')
        file_up = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        shutil.move(file_name, BASE_DIR + f"/uploaded/{db_name}")
        
    print("Uploaded!")
except FileNotFoundError:
    print("There's no file to upload")

clean.clean_uploaded()