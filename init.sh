#!/bin/bash

#Created by Joshua Omolewa

#This script  installs python package, creates the python virtual environment,
#installs the requirements for the project and create a log folder

# install specific python version to make sure all the work env for various server are the same.

sudo add-apt-repository ppa:deadsnakes/ppa -y # adding all python version repositiory to apt-get package manager

sudo apt-get update

sudo apt-get install python3.8  

sudo apt install python3.8-distutils -y


# install awscli
sudo apt-get  install awscli -y

# Create a virtual environment for specific python3.8 version 
sudo apt-get install python3-virtualenv -y #

virtualenv --python='/usr/bin/python3.8' project_venv #creating python  virtual environment with project_venv name

source project_venv/bin/activate  #activating virtual environment

#Install dependencies for virtual environment
pip install -r requirements.txt
pip install geocoder # library use to get country name from from city

deactivate #deactivating the virtual environment

chmod a+x run.sh # make run.sh executable by adding execution permission

mkdir -p log #create log directory if it doesn't exist






