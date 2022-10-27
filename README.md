# PROJECT: Data Pipeline that collects job data from API and transform data into csv file  based on business requirements and upload transformed data to Amazon S3 bucket

# Author: 👤 **Joshua Omolewa**

## 1. Business Scenario
Data engineer is required to build a data pipeline on amazon EC2 that transform job data from API to a job.csv file for data analysis by data analyst and store transformed data in S3 and also generate log files for error tracking . API for job data  https://www.themuse.com/developers/api/v2

## 2. Business Requirements
Download the data from API. Transformed data should include publication date, job name, job type, job location (i.e city and country) &company name. Store data in S3 for use by data analyst

## 3. Deliverable
shell scripts, python script and job.csv to S3.

Shell script: The shell script will control every operation, setting virtual environment, log setting, python script running.

Python script: The Python script is used to transform the data and upload dat to s3 bucket.

job.csv: The final transformed data file based on business requirement.

## 4. Specification Detail
The data required is gotten from API by querying jobs from the first 50 pages  https://www.themuse.com/api/public/jobs?page=50

## 5. Project Architecture

![project architecture](https://github.com/Joshua-omolewa/Scraping_API_csvdata_to_S3_project/blob/main/img/Architecture.jpg)


## 5. Project Diagram
 The diagram shows the folder structure for the project and the how the shell scripts create virtual enviroment containing dependecies contained in the requirements.txt file. The run.sh shell script activates the virtual enviroment and run the run.py python script which connect to the API, transform the dat using pandas and then upload the transform job.csv file to S3 bucket for the data analyst
 
![project image](https://github.com/Joshua-omolewa/Scraping_API_csvdata_to_S3_project/blob/main/img/Python_project.png)

# 5. STEPS USED TO COMPLETE THIS PROJECT
* Create Amazon AWS account, create Amazon elastic compute (EC2) instance and S3 bucket with directory to store transformed csv file
<img src="https://github.com/Joshua-omolewa/Scraping_API_csvdata_to_S3_project/blob/main/img/final%20EC2%20S3.jpg"  width="50%" height="50%">
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
