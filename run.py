#!/usr/bin/env python3

#Created by Joshua Omolewa 

#importing rquired libraries
import requests
import json
import pandas as pd
import boto3
from dotenv import load_dotenv
import toml
from geopy.geocoders import Nominatim
import os


def read_api(url):
    """
    Reads the API and returns the response
    """
    response = requests.get(url)
    return response.json()

def read_country(city):
    """
    Convert cities and returns the country
    """
    geolocator = Nominatim(user_agent="google") #user agent can be any user agent 
    location = geolocator.geocode(city, language="en") #specified the language as some countries are in other lanaguages
    country= location.address.split(',')[-1] #split the string based on comma and retruns the last element (country)
    return country


### I used this website https://jsonformatter.curiousconcept.com/  to look into the json data hierarchy to effectiely target required data

if __name__=='__main__':

    app_config = toml.load('config.toml') #loading configuration files
    url = app_config['api']['url'] #accessing api url from config file

    #importing credentials for access to S3 bucket
    bucket = app_config['s3']['BUCKET']
    folder = app_config['s3']['FOLDER']

    #Importing secrets from .env file
    access_key=os.getenv('access_key') #accessing access id key stored in .env file loaded as environment variables
    secret_access_key=os.getenv('secret_access_key') #accessing secrete access key ic stored in .env file loaded as environment variables

    result = read_api(url)  #convert response to json dictionary

    #print(result.keys()) # to see all keys in the json dictionary

    #data_input = result.get("results") alternative way to get value of dictionary key but returns none if key is not found

    data_input2 = result["results"] #returns a list of all results from the API

    # print(type(data_input2)) #confirming data type


    #####  sorting DATA from API based on requirement for csv file ########

    #### Sorting company name using 2 methods i.e. for loop or list comprehnsion #### (DATA 1)

    # ## METHOD 1 FOR LOOP ###
    # compname1 = []
    # for i in range(len(data_input2)):

    #     comp_name = data_input2[i]['company']['name']
    #     compname1.append(comp_name)
    # #print(compname1)
    # companynames1 ={"company":compname1}  # creating a dictionary for combining dataframe later
    
    ### METHOD 2 LIST COMPREHENSION ###
    compname = [data_input2[i]['company']['name'] for i in range(len(data_input2))] #storing the company name data needed in list format
    # print(compname) checking results
    companynames ={"company":compname}  # creating a dictionary for combining dataframe later


    ##### Sorting LOCATION using  LIST COMPREHENSION #### (DATA2)
    """
    storing the company location data needed in list format. note the .split() method breaks the string into list based on delimiter specified
    """
    comp_location_dummy = [(data_input2[i]['locations'][0]['name']).split(",") for i in range(len(data_input2))] 
    # print(comp_location_dummy) checking results


    """
    some data from  API does not have the correct country but have the cities as seen from the print funtion for the company location dummy variable
    I decided to extract only the cities and use geopy library to extract country information information. See documentation https://geopy.readthedocs.io/en/latest/
    Note the strip() method removes all white spaces and .split() method breaks the string into list based on delimiter specified
    """
    comp_city = [(data_input2[i]['locations'][0]['name']).split(",")[0].strip() for i in range(len(data_input2))] 
    # print()# printing a blanc line
    # print()
    # print(comp_city) checking results
    company_cities = {"city":comp_city}

    #creating a loop to convert all cities to their respective countries and store in a list
    comp_location_country =[] #using list to preserve the order for the data frame

    for city in comp_city:
        city_country = read_country(city)
        comp_location_country.append(city_country) #appending result from function to empty list
    # print()
    # print(comp_location_country) checking results

    company_country ={"country":comp_location_country}# creating a dictionary for combining dataframe later



    ##### Sorting JOBNAME using  LIST COMPREHENSION #### (DATA3)
    job_name = [(data_input2[i]['name']) for i in range(len(data_input2))] 
    # print()# printing a blanc line
    # print()
    # print(job_name) checking results

    job ={"job":job_name}  # creating a dictionary for combining dataframe later

    ##### Sorting JOBTYPE using  LIST COMPREHENSION #### (DATA4)
    job_typ = [(data_input2[i]['type']) for i in range(len(data_input2))] 
    # print()# printing a blanc line
    # print()
    # print(job_typ) checking results

    job_type ={"job_type":job_typ}  # creating a dictionary for combining dataframe later

     ##### Sorting PUBLICATION DATE using  LIST COMPREHENSION #### (DATA5)
    pub_date = [(data_input2[i]['publication_date']).split("T")[0] for i in range(len(data_input2))] #splitting at T and extracting only the date information
    # print()# printing a blanc line
    # print()
    # print(pub_date) checking results

    publication_date ={"publication_date":pub_date}  # creating a dictionary for combining dataframe later

    #storing all required dictionary data in list to create required dataframe
    requirement_data = [publication_date, job_type, job, companynames, company_cities, company_country] 

    dataframes = [] #creating and empty list to store dataframes

    for data in requirement_data:
        dataframes.append(pd.DataFrame(data))

    """
    Concatenating the data frames in the dataframes list, axis =1 is to concatenate data frames along the columns, 
    ignore_index= False is to  the use of  index values along the concatenation axis i.e. including the use default pandas axis along the 
    row and creating a new axis when combining files.
    """

    df = pd.concat(dataframes,axis=1, ignore_index=False)

    #print(df) to take a look into the dataframe

    """
    ouputing the concatenated data as a csv file with a specific file name, index =false is to  ignore pandas default index when outputting the file 
    """

    df.to_csv("job.csv",index= False)

    print("Succesfully created job.csv file")


    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key)

    print('Uploading to AWS S3...') 

    s3.upload_file('job.csv', bucket, folder+'/job.csv')

    print("File upload to S3 successful!") #Print success if file upload is successful




        




    
    

    











    






