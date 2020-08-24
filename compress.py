from zipfile import ZipFile
from glob import glob
from datetime import datetime
import os


def zip_files():

    for filename in glob('./database/raw/*'):
        print("zipping ", filename)
        ts = datetime.timestamp(datetime.now())
        zipObj = ZipFile(f"./database/DB-{ts}.zip",'w')
        zipObj.write(filename)
        zipObj.close()
        os.remove(filename)

