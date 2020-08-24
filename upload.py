from google.oauth2 import service_account
import googleapiclient as google
from googleapiclient.http import MediaFileUpload, HttpRequest
from googleapiclient.discovery import build
from datetime import datetime
from glob import glob
import os

import clean
import compress

compress.zip_files()

SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file('./service-credentials.json', scopes=SCOPES)



service = build('drive', 'v3', credentials=credentials)
try:
    for file_name in glob('./database/*.zip'):
        print(f"uploading {file_name}...")

        now = datetime.now().strftime('%Y-%m-%d--%H:%M:%S')
        db_name = f'DB-{now}.zip'
        file_metadata = {'name' : db_name, 'parents': ['1CFOqw4-g5wo02nnFXK2hVmH4RuJhT4kV']}
        media = MediaFileUpload(file_name, mimetype='application/zip')
        file_up = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        os.system(f'mv {file_name} ./uploaded/{db_name}')

    print("Uploaded!")
except FileNotFoundError:
    print("There's no file to upload")

clean.clean_uploaded()