# Backup to Google Drive
A simple script to automatically upload your database/media backups from your server directly to google drive



## Register for Google Drive API
Follow these steps prior to implementing the code:

1. Firstly, you need to create a project for this in your [Google Cloud Platform](https://console.cloud.google.com/)

2. Then, you should search for Google Drive API and enable it for your project

3. Head to the API & Services tab and navigate to credentials. From there, try to create a credential: You want the Service Account since this API is going to get called only by server and not your end users

4. Create a key from your service account detail page and download the credentials file in format of JSON and be careful not to lose nor expose it

5. Rename the JSON file to 'service-credentials.json' and put it in your working directory
