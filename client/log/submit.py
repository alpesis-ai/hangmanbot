import os.path

import settings

def save_submits(submit, filepath=settings.SUBMIT_LOG_PATH):
    thisSubmit = "%s\n" % submit
    open(filepath, 'a+').write(thisSubmit)
