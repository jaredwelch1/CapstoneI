import pandas as pd
import psycopg2
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from scipy import sparse
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import os

# How many clusters we want
true_k = 5


# this will be used when converted to real script to maintain ID ordering when we cluster and label 
# just need to change target table 

# conn = psycopg2.connect("dbname='cap' user='postgres' host='ec2-52-27-114-159.us-west-2.compute.amazonaws.com' port=9000 password ='secret'")
# data = pd.read_sql_query("SELECT * FROM articles ORDER BY id ASC LIMIT 100", conn)

if __name__ == '__main__':
	if not os.path.exists('model'):
		os.makedirs('model')

	data = pd.read_csv('nlp_dim_1000.csv')

	print('Data has been read into a dataframe. Starting TFIDF conversion.')

	# transforms data into tfidf matrix representation
	vectorizer = TfidfVectorizer(max_df=0.5, max_features=100,
		                         min_df=2, use_idf=True)

	print('Saving TFIDF vectorizer object since it has term information')
	joblib.dump(vectorizer, 'model/tf_vectorizer_obj.pkl')

	# fit our data (list of article bodies) to a tfidf representation
	X = vectorizer.fit_transform(data.lemmatized_body)

	# verify we have a sparse matrix of 100 tfidf features for each article 
	# should be 5*100 sparse matrix
	# X
	print('Saving sparse matrix of TFIDF vectors to a file')
	# Store the data that we have of TFIDF vectors into a file
	sparse.save_npz('model/tf_idf_matrix.npz', X)
	
	# create the KMeans object with initial settings
	km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1,
		        verbose=False)

	print('Beginning KMeans fit and training')

	# fit our tfidf data to the kmeans model
	km.fit(X)

	print('KMeans model finished. Saving to file.')
	joblib.dump(km, 'model/kmeans_model.pkl')


	terms = vectorizer.get_feature_names()
	order_centroids = km.cluster_centers_.argsort()[:, ::-1]
	labels = km.labels_

	# Since the labels attribute is in the order that the sparse matrix was in when it was passed in
	# We should be able just insert the label value as a dataframe column
	t = pd.Series(labels)
	data['cluster_label'] = t
	
	print('Cluster labels appended to dataframe rows')

	print('Beginning prediction of unknown article')

	# Test a prediction 
	tfidf = TfidfVectorizer(max_features=100)
	X_test = tfidf.fit_transform([data.lemmatized_body[98]])
	z = km.predict(X_test)
	print(z)
