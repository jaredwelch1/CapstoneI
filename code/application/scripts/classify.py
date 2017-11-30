from nlp import cluster_prep
import pandas as pd
import psycopg2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.externals import joblib

def predict_cluster(article_string, km, vectorizer):
        '''
        Takes in a string which is the article body to be processed and cluster value predicted
        article_string - string 
        returns the integer label for the cluster the text fits in
        '''
        z = cluster_prep(article_string)
        # reformat the result for tfidf
        z = ' '.join(z)
        x_test = vectorizer.transform([z])
        res = km.predict(x_test)
        return res[0]	
