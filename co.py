#!/usr/bin/python
import os, glob
import shutil
import pycurl
import time

BASEDIR  = "/var/archivematica/sharedDirectory/watchedDirectories/activeTransfers/standardTransfer"
USERNAME = "<your username>"
API_KEY  = "<your api key from archivematica>"

### list all files in the directory
MyList = glob.glob("./*.zip")

### for each file, transfer it to Archivematica activeTransfers directory
### and approuve it

for file in MyList:
    print file
    directory = BASEDIR + "/" + file.replace(".zip","").replace("./","")
    source = file 
    target = directory + "/" + file
    if not os.path.exists(directory):

            print "\t create directory " + directory
            os.makedirs(directory)

            print "\t copy file..."
            shutil.copy2(source,target)

            # print "\t send approuval to Archivematica..."
            command = "curl --data 'username="+USERNAME+"&api_key="+API_KEY+"&type=standard&directory="+file.replace('.zip','').replace('./','')+"' http://127.0.0.1/api/transfer/approve"
            print command
            time.sleep(2)
            os.system(command)

