[![Build Status](https://travis-ci.org/PeterclaverKimuli/andellachallenges1.svg?branch=master)](https://travis-ci.org/PeterclaverKimuli/andellachallenges1)
[![Coveralls](https://img.shields.io/coveralls/PeterclaverKimuli/andellachallenges1.svg?branch=master)]()

This site helps you design your shopping list for the several items you want to buy both online and offline. You can save your shopping list afterwards on your git account for further retence and you can even edit the shopping list in the later stages.

Features

The application has a couple of features as listed below:-

A user is able to Register and get an account in the app
A user is able to Login into the app using their credentials already supplied
A user is able to create, edit, update and delete shopping lists
A user is also able to create, edit, update and delete shopping list Items
Setup

To start using this application, first clone it to your local machine by running

git clone https://github.com/PeterclaverKimuli/andellachallenges1.git
cd andellachallenges1
Create the virtual environment and activate it

virtualenv env
source env/bin/activate
Then install all the required dependencies

pip install -r requirements.txt
Then run the application

python run.py
To now view the application head over to

http://127.0.0.1:5000/
UML

The application also has a UML diagram. For the structure of the app check it out here

Testing

You can then run the application tests using

cd andellachallenges1
nosetests tests

