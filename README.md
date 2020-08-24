# Backup to Google Drive
A simple script to automatically upload your database/media backups from your server directly to google drive



## Register for Google Drive API
Follow these steps prior to implementing the code:

1. Firstly, you need to create a project for this in your [Google Cloud Platform](https://console.cloud.google.com/)

2. Then, you should search for Google Drive API and enable it for your project

3. Head to the API & Services tab and navigate to credentials. From there, try to create a credential: You want the Service Account since this API is going to get called only by server and not your end users

4. Create a key from your service account detail page and download the credentials file in format of JSON and be careful not to lose nor expose it

5. Rename the JSON file to **service-credentials.json** and put it in your working directory


## Install Dependencies

Create a virtual environment for the project, I would recommend **venv**. Install the dependencies within the *requirements.txt* file. If you're on Windows, search for dealing with virtual environments in Windows but for Linux/MacOS this should work:

```
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

## Usage

you only need to execute the *upload.py* file:
```
(env) $ python update.py
```
This process can be concluded into 3 steps and it's OS independent:

- Every file within the *database/raw* directory would be zipped to *database* directory and removed from *raw* directory 

- Each zip file within the *database* directory then would be uploaded to your Google service account Drive and moved to the *uploaded* directory with a name that represents the exact time of upload

- Finally, the script would clean the *uploaded* directy, meaning, it would check if any files are uploaded more than 2 weeks ago. If so, it will delete those files to prevent the local storage from getting full

The best case of usage for this script is to run it on an automated schedule like a cronjob on your server. Also, you need another cronjob just before this to get a database backup from your database into the *database/raw* directory.
