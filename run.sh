#!/bin/bash

#Created by Joshua Omolewa

### SETTING DATE FORMAT TO BE CONCATENATED  WITH LOG FILES ###
log_date=$(date +"%d_%m_%Y_%H-%M-%S")
##########################################


###Creating environment variable for log file####
export LOG_FOLDER=./log
export LOG_FILE_NAME="shell_script"
export LOG_FILE="${LOG_FOLDER}/${LOG_FILE_NAME}_${log_date}.log"
#################################


#### SETTING LOG RULES FOR AUTOMATIC LOGGING #####

exec > >(tee ${LOG_FILE}) 2>&1

# PART 5: RUN SCRIPT
source project_venv/bin/activate

echo "Start to run Python Script"

###run python script####
./run.py


#checking if scripts run

if [ $? -eq 0 ]
then
 echo "Script execution SUCCESS"
 exit 0
else
 echo "Script Failure"
 exit 1
fi

echo "working"
