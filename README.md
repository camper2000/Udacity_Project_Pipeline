Disaster Response Pipeline Project

This project is to build a model for an API that classifies disaster messages. It can quickly recognize the type of disaster and contribute to instructing the relevant rescue.

Instructions of Python scripts and web app:
1. Run the following commands in the project's root directory to set up database and model.

    - To run ETL pipeline that cleans data and stores in database
        ``python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv sqlite:///data/Disaster.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py sqlite:///data/Disaster.db models/pickle_model.pkl`

2. Run the following command in the app's directory to run your web app.
    `python app/run.py`

3. Type env|grep WORK to get SPACEID and SPACEDOMAIN
	Go to https://SPACEID-3001.SPACEDOMAIN



Files Explanation:

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py	# python file to get, clean and save the data
|- Disaster.db	# database to save clean data to

- models
|- train_classifier.py	# python file to build, evaluate and save the model
|- pickle_model.pkl  # saved model 
