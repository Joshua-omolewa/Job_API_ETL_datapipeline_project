# Scraping_API_csvdata_to_S3_project

# PROJECT: Toronto climate data pipeline to combine climate data files using python and shell script

# Author: 👤 **Joshua Omolewa**

## 1. Business Scenario
Company requires data engineer to obtain Toronto climate data from Canadian Climate API and concatenate them into a single file and also generate log files for error tracking . To download the weather data manually, visit https://climate.weather.gc.ca/historical_data/search_historic_data_e.html.

## 2. Business Requirements
Download the data from Canadian Climate API. Concatenate the downloaded data files into one final csv file, called all_years.csv as ouput. Upload the scripts and final csv file all_years.csv to Github repository.

## 3. Deliverable
Upload shell script, python script and all_years.csv to the github repository .

Shell script: The shell script will control every operation, including data downloading, log setting, python script running.

Python script: The Python script is used to concatenate all the data into one file.

all_years.csv: The output file to be generated after concatenating the files.

## 4. Specification Detail
The data required is from Station ID = 48549. The year range of the data we want is from 2020 to 2022. We only want the data in February. The data will be downloaded in hourly format. The output file will be named as all_years.csv.

# 5. STEPS USED TO COMPLETE THIS PROJECT
* Download data with shell script and automate log generation process
* Execute python script from shell script to concatenate the data into one file
* Save output file in the python script
* Print out SUCCESS when runing shells script if all operations are completed successfuly.
* Upload files to the github repo using git.
### Note: Pipeline can be automated using chronjob if needed

## PROJECT FILES

* [SHELL SCRIPT](https://github.com/Joshua-omolewa/Climate_bash_python_project/blob/main/shell_script.sh)

* [PYTHON SCRIPT](https://github.com/Joshua-omolewa/Climate_bash_python_project/blob/main/python_script.py)

* [INPUT DATA FOLDER](https://github.com/Joshua-omolewa/Climate_bash_python_project/tree/main/input)

* [OUPTUT DATA FOLDER](https://github.com/Joshua-omolewa/Climate_bash_python_project/tree/main/output)

* [LOG FOLDER](https://github.com/Joshua-omolewa/Climate_bash_python_project/tree/main/logs)

## PROJECT BEING EXECUTED ON SHELL

![FINAL SCRIPT IMAGE](https://github.com/Joshua-omolewa/Climate_bash_python_project/blob/main/img/Project%20completed.jpg)

# Follow Me On
  
* LinkedIn: [@omolewajoshua](https://www.linkedin.com/in/joshuaomolewa/)  
* Github: [@joshua-omolewa](https://github.com/Joshua-omolewa)


## Show your support

Give a ⭐️ if this project helped you!
