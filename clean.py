import os, time
from glob import glob
from datetime import datetime, timedelta

from config import BASE_DIR, CLEAN_TIME


def clean_uploaded():
    """
    The uploaded files stack up after a while and can take enormous amount of storage.
    this function deletes files that have been uploaded more than 14 days ago.
    """

    for filename in glob(BASE_DIR + '/uploaded/*.zip'):
        modified = time.ctime(os.path.getmtime(filename))
        modified_dt = datetime.strptime(modified, '%a %b %d %H:%M:%S %Y')
        if datetime.now() > modified_dt + timedelta(days=CLEAN_TIME):
            os.remove(filename)
            print("sucsessfuly deleted",filename)

