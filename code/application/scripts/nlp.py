# -*- coding: UTF-8 -*-
from __future__ import division
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import string

'''
Remove stopwords from article body.
'''
def stopword_article(body):
	stop_words = stopwords.words('english')
	stop_words = stop_words + [',', '.', '!', '?', '"','\'', '/', '\\', '-', '--', '—', '(', ')', '[', ']', '\'s', '\'t', '\'ve',
	 '\'d', '\'ll', '\'re', 'image']
	stop_words = set(stop_words) # making this a set increases performance for large documents

	stopworded_body =  [w.lower() for w in body if w not in stop_words]

	return stopworded_body

'''
Tokenize article by word.
'''
def tokenize_article(body):
	#text = body.encode('utf-8', errors="ignore")
	tokens = nltk.word_tokenize(text)
	return tokens


'''
Lemmatize (get common root words) from stopworded article.
'''

def lemmatize_article(stopworded_body):
	wnl = nltk.WordNetLemmatizer()
	lemmatized_words = []
	# We need to tag words with their parts of speech before the WordNet lemmatizer will work properly
	pos_tagged_body = nltk.pos_tag(stopworded_body)
	lemmatized_words = []
	for word, tag in pos_tagged_body:
		wntag = tag[0].lower()
		wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
		if not wntag:
			lemma = word
		else:
			lemma = wnl.lemmatize(word, wntag)
		lemmatized_words.append(lemma)

	return lemmatized_words

'''
We need to tokenize at the sentence level for our sentiment analysis.
'''
def get_sentence_tokens(body):
	#text = body.decode('utf-8')
	sentences = sent_tokenize(text)
	return sentences


'''
Our sentiment analysis process is based on find a sentiment analysis score for
each sentence in an article so to get the average score for an article
we need to divide each individual sum by the number of sentences in the article
'''
def average_sentiment(neg, neu, pos, compound, length):
	result = {}
	result['neg'] = neg/length
	result['neu'] = neu/length
	result['pos'] = pos/length
	result['compound'] = compound/length
	return result

'''
Calculate sentiment scores from article.
'''
def calculate_sentiment(body):
	text = get_sentence_tokens(body)
	sid = SentimentIntensityAnalyzer()
	neg = 0
	neu = 0
	pos = 0
	compound = 0
	try:
		for sent in text:
			ss = sid.polarity_scores(sent)
			neg += ss['neg']
			neu += ss['neu']
			pos += ss['pos']
			compound += ss['compound']
		result = average_sentiment(neg, neu, pos, compound, len(text))
	except:
		result = {'neg': 0, 'neu': 0, 'pos': 0, 'compound': 0}
	return result

'''
Pass in the sentiment score for our article to assign a binary positive or negative value.
'''
def assign_sentiment(score):
	if score['compound'] > 0:
		binary_sentiment = 1
	else:
		binary_sentiment = 0
	return binary_sentiment

'''
Perform sentiment analysis on a single user-supplied article.
Return an integer: 0 for negative sentiment, 1 for positive sentiment.
'''
def analyze_sentiment(text):
	sentiment_score = calculate_sentiment(text)
	binary_sentiment = assign_sentiment(sentiment_score)
	print('binary_sentiment = ' + str(binary_sentiment))
	return binary_sentiment

'''
Transform a single user-supplied article to lemmatized version for clustering.
Returns a list of lemmatized words from the original article.
'''
def cluster_prep(text):
	#text = text.encode('string-escape')
	#printable = set(string.printable)
	#text = ''.join(filter(lambda x: x in string.printable, text))
	text = text.encode("ascii", errors="ignore").decode()
	#text = text.encode('utf-8')
	tokens = tokenize_article(text)
	stopped_text = stopword_article(tokens)
	lemmatized_text = lemmatize_article(stopped_text)
	return lemmatized_text
