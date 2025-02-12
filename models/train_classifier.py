import sys

import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

import re
import sqlite3
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, HashingVectorizer

from sqlalchemy import create_engine

from sklearn.datasets import make_multilabel_classification
from sklearn.multioutput import MultiOutputClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report
import pickle

def load_data(database_filepath):
# read data from DB
    engine = create_engine(database_filepath)
    df = pd.read_sql_table('Disaster_Data', con=engine)
    X = df.message.values
    Y = df.iloc[:,4:].values
    return X, Y

def tokenize(text):
# Tokenize text
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
# build pipeline with feature union 
    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('vect', CountVectorizer(tokenizer=tokenize)),
                ('tfidf', TfidfTransformer())
            ])),

            ('hash', HashingVectorizer())
        ])),

        ('clf', RandomForestClassifier())
    ])
    parameters = {
        'features__text_pipeline__vect__ngram_range': ((1, 1), (1, 2)),
        'features__text_pipeline__tfidf__use_idf': (True, False)
    }
    cv = GridSearchCV(pipeline, param_grid=parameters)    
    return cv    


def evaluate_model(model, X_test, Y_test):
## def evaluate_model(model, X_test, Y_test, category_names):
    Y_pred = model.predict(X_test)
    print(classification_report(Y_test, Y_pred))


def save_model(model, model_filepath):
    with open(model_filepath, 'wb') as file:
        pickle.dump(model, file)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        ## X, Y, category_names = load_data(database_filepath)
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        print("Best parameters: ")
        print(model.best_params_)
        
        print('Evaluating model...')
        ## evaluate_model(model, X_test, Y_test, category_names)
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
