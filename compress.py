from zipfile import ZipFile
from glob import glob
from datetime import datetime
import os

from config import BASE_DIR


def zip_files():

    for filename in glob(BASE_DIR + '/database/raw/*'):
        print("zipping ", filename)
        ts = datetime.timestamp(datetime.now())
        zipObj = ZipFile(BASE_DIR + f"/database/DB-{ts}.zip",'w')
        zipObj.write(filename)
        zipObj.close()
        os.remove(filename)

