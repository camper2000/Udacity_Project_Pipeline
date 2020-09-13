#Disaster Response Pipeline Project

This project is to build a model for an API that classifies disaster messages.

###Instructions of Python scripts and web app:
1. Run the following commands in the project's root directory to set up database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv sqlite:///InsertDatabaseName.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py sqlite:///InsertDatabaseName.db models/pickle_model.pkl`

2. Run the following command in the app's directory to run your web app.
    `python app/run.py`

3. Type env|grep WORK to get SPACEID and SPACEDOMAIN
	Go to https://SPACEID-3001.SPACEDOMAIN



###Files Explanation:

- InsertDatabaseName.db   # database to save clean data to

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py

- models
|- train_classifier.py
|- pickle_model.pkl  # saved model 
