import logging
from datetime import *
import os
WORKDIR = "\housingLogs"

currentTimeStamp = f'{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}'

logFileName = f"log_{currentTimeStamp}.log"
try:
    os.makedirs(WORKDIR)
except:
    pass

# filen = "rutvik.log"
logFilePath = os.getcwd()+ os.path.join(WORKDIR,logFileName)

logging.basicConfig(filename=logFilePath,filemode="w",format='[%(asctime)s -%(name)s -%(levelname)s -%(message)s]',level=logging.INFO)


