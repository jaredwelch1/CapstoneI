## **Team Information**

**Team Name:** Squad

**Mission Statement:** Our mission is to gather news articles and then categorize them based upon similarity after processing our data with Natural Language Processing techniques. We will provide visualizations of our results to user via a web application. By doing this we hope to expose trends in the news.

#### Team Members:
- **Zach Bryant:** I am a senior undergraduate of Computer Science here at Mizzou. I am very passionate about the influence of today's modern technology and how it can be used for the betterment of all people. I've been working on campus as an IT Support Specialist ever since my freshman year ended. I enjoy helping people and love getting paid for it. Over this past year, I have become very interested in cryptocurrencies and have made the decision to invest as well. After graduation, I plan to further my education by using my gained capital from cryptos to fund my own self-taught education on software development for cryptocurrencies.
![alt text](pictures/zach.jpg "Zach Bryant")

- **Kurt Bognar:** Starting a job at Sogeti as a Consultant. I've been a researcher for the university aiding in the creation of new tools and algorithms for Association-Rule Mining, worked for VU for the past year, and actively trade cryptocurrencies.  
![alt text](pictures/kurt.jpg "Kurt Bognar")

- **Ali Raza:** I am a senior at the University of Missouri studying Computer Science. I do research at the iDAS Lab where I am currently developing a data mining library.   
![alt text](pictures/ali.jpg "Ali Raza")

- **Jared Welch:** Senior at the University of Missouri. Passionate about improving my skills. Excited for the potential of our application.   
![alt text](pictures/jared.png "Jared Welch")

- **Justin Renneke:** Senior undergraduate of Computer Science at the University of Missouri, graduating December '17.  Interested in machine learning, data analysis, cloud computing, and using Python to conquer the galaxy.      
![alt text](pictures/justin.png "Justin Renneke")

## Introduction

#### Problem Definition
News articles generate massive amounts of data. Following the climactic nature of the 2016 Presidential Election due to the dissemination of false news, it is evident that news articles new to be intensively analyzed. Until recent years, it was not possible to effectively categorize news data due to computational limitations. However, recent advances in High Performance Computing, Data Analytics, and Machine Learning have made it possible to gather, store, and analyze news articles. We propose a model to cluster news articles based upon similarity and then provide data visualizations based upon the generated clusters and analysis done.

#### Problem Resolution

We propose the following software solution:
- Scrape news articles
- Organize, clean, and store data
- Pre-process using NLP and then perform TFIDF.
- Cluster news articles based on the similarity of TFIDF vectors.
- Display visualizations

## Changelog for software

### NewsArticleScraper - Version 1.1

- Initial features:

	- automatically scheduled at time during the night

	- each site runs as an independent process, so any error for a site does not hurt the flow of the scraper itself

	- as articles are scraped from a site, they are pushed into the database, including the text, title, authors, url, and other relevant info

- Version 1.1:

	- add additional sites to list

	- clean up inserts to database

	- add custom logging functionality, including error and information log files

	- more try catch error checking to improve error logs

## **Requirements**

### User Requirements
* User can explore visualizations of statistics and analysis of news data using a graphical interface to navigate.
	* Users can use the website to view clusters of articles by topic via a visualization.
	* Users can use the website to view visualizations depicting trending topics per day for a past time period.
	* Users can use the website to view a word cloud representation of trending topics for the whole year.
* User can submit an article to be analyzed and view the results of the analysis of the article compared to our dataset; the results will be classification data based upon our models.
* **User Requirements Stretch Goals:**
	* User can perform custom searches against the database, yielding search results related to statistics on the news article data
	* User can explore articles pertinent to trending twitter topics.

### Functional Requirements
* Given a list of news websites, scrape every new article on every site and return and store in a database the following data from each article: Article title, author name(s), date published, article body text, and webpage url.
* Perform natural language processing analysis on articles to clean the data and generate features such as named entities, bag of word counts, and term frequency-inverse document frequency metrics.
* Categorize articles into groups based on topic determined by performing machine learning-based cluster analysis using generated features.
* A web application will provide users with visualizations of the clustered topics and their articles.
* The web application will allow a user to provide text of a specific news article, assign the article to a topic category, and inform the user of the result.
* **Functional Requirements Stretch Goals**
	* Allow a user to submit a url to a news article and automatically scrape the page for analysis in lieu of copied article text
	* Allow users to perform custom searches of the article database and return data visualizations based on metrics such as frequency of occurrence, trends of occurrence over time, and relation to other topics.
	* Create a scrolling wordcloud graphic to visualize changes in overarching news trends over time.
	* Perform sentiment analysis on articles and visualize the results.

### Non Functional Requirements
* The server is expected to have a 99% availability.
* Each layer of the system should be backed-up weekly
* The software will be written using modular OOP practices to allow for easy addition of new features.
* The web application will be designed to be compatible on mobile and tablet devices.
* The system will be hosted within Amazon Web Services to provide the ability to scale as needed.
* **Non Functional Requirements Stretch Goal**
	* Response Time: Real time article classification

### System Requirements
* The project will be hosted on Amazon AWS instances.
* A relational database will be used in order to be able to accurately model the data and perform advanced queries.
	* The database should be large enough to store a massive dataset.
	* The database should be indexed so efficient queries can be performed.
* The computational processing power must be sufficient enough to not bottleneck the clustering, analysis, and data visualization process.
* The Random-Access-Memory must be high enough to minimize reading from disk during computationally intensive tasks.

## **Design**

### Phase I: System Design
The project will be deployed within Amazon Web Services. There are two architecture proposals: one for the prototyping phase (which will be the entire extent of the capstone project) and one for a business model deployment (in case the project is to deploy for real world use).

Decoupling and auto-scaling lie at the heart of the scalable design. A decoupled web scraping instance will allow the web scraper to continue to run uninterrupted in an automated environment. Auto Scaling groups of larger EC2 instances will allow the design to scale up for processing intensive data analysis and faster response to user queries when under load, while conserving resources by scaling down when the system is idle. To achieve this, the database must be decoupled as well.
#### AWS Prototyping Deployment
![alt text](pictures/CapstoneV2.png "Prototyping Architecture")
Features:
* Auto Scaling combined Web Servers/Data Processing
	* Single small EC2 instance used for the low-load tasks of serving the web page and scraping and storing news articles
	* A second, high performance EC2 instance was activated for data processing
	* Saves money by reducing resource consumption since the system will not need to handle many users in a prototyping environment and the system can afford to sacrifice some responsiveness for the sake of cost

#### AWS Business Model Deployment
![alt text](pictures/DataDrivenWebApp-Big.png "Business Architecture")
Features:
* Elastic load balancing will redirect work and balance load at two levels: User access of web servers on the front end and data processing and data queries on the back end.
* Multiple auto scaling groups will provide high performance and redundancy across AWS availability zones for a larger business environment deployment
	* SSD-based M3 web server auto scaling group will provide a high performance cluster for front-end processing
	* AWS Elastic block store-based M4 data processing auto scaling group will provide high processing capacity for data analysis and queries
	* Decoupled RDS database scaling group with a Master RDS database feeding RDS Read Replicas will allow us to easily scale manually to provide high database throughput for intense data queries
* Decoupled web scraper will continue to run its relatively undemanding task undisturbed

#### High Level Logical System Flow
![alt text](pictures/SystemFlow.png "System Flow")  

#### Technologies Used
This is a list of the technologies that will be used for reference. These are discussed in more detail at various places throughout this document.  
* ##### Amazon Web Services  
* ##### PostgreSQL  
* ##### Python Back-End
	* ##### Important libraries:
		* Web scraping: Newspaper
		* Natural language processing: NLTK and Stanford OpenNLP
		* Machine learning: skLearn
		* Data manipulation: Pandas, Psycopg2, SQLAlchemy
	* ##### Flask (web framework)   
* ##### HTML/Javascript Front-End


### Phase II: Web Scraping and Data Design

This project required a large database of news articles and their associated metadata. A web scraper has been built to scrape articles from news sites. We created a data warehouse to organize and store the articles and their metadata. We have collected over 160,000 articles for data processing as 11/14/2017.

#### Web scraper
##### Overview
* Parses a list of multiple news sites. This list is provided by a JSON file containing entries with a site name and URL.
* Carefully designed to avoid website's banning our IP
  * The parser is run automatically every day at a random time between 2 AM and 6 AM by using the apscheduler Python library.
  * A random wait is added between page scrapes
  * Runs with threading on each site, but limited to 2 threads to avoid stressing site's resources
* Implements logging to help with troubleshooting an otherwise fully automated program
* Every individual site crawl and scrape is forked out as a separate process to improve performance and avoid memory issues
##### Python's Newspaper Library  

[Link to Newspaper library Homepage](http://newspaper.readthedocs.io/en/latest/)

The Newspaper library is specifically designed to scrape articles from news websites. Newspaper itself is based on Python's popular BeautifulSoup and Goose parsing libraries. This library provides the ability to cleanly scrape news articles from a wide variety of websites - a challenge that would otherwise be incredibly time consuming. The library accomplishes this by: querying a website's home page, crawling through all the links associated with the website, building a tree structure to represent it, then scraping and parsing every previously unseen article in the tree.

Using this library, it is possible to collect the following data from every article:
* Title
* Primary author (if exists)
* Secondary authors (if exists)
* Date published (if exists)
* URL
* Body text
* Raw html

The library also has a memoization capability that is being used. This allows the scraper to scrape only new articles for every subsequent scrape of a site.

**Scraper Code/Pseudocode**
```
# Open database connection
# Read in site list JSON

# Enter core scraping code
for site in site_list:
		child_id = os.fork()

		if child_id == 0:			
			name = site['name']
			url = site['url']
			# if a site should throw an exception for any reason (maybe bad url), catch it, pass, and move to next site
			try:
				paper = newspaper.build(url,
						keep_article_html=True,
						fetch_images=False,
						memoize_articles=True,	# track the articles we have already scraped from session to session
						MIN_WORD_COUNT=200,		# this doesn't seem to be having any affect
						number_threads=2,
						request_timeout=12,
						thread_timeout=3)
				total = paper.size()
				numScraped = total
				authors = []
				secondAuth = ''

				for x in range(0,numScraped):
					sleep(randint(3,6))
					if paper.articles[x] != None:
						paper.articles[x].download()
						if paper.articles[x].is_downloaded:
							if paper.articles[x].html != None:
								paper.articles[x].parse()
								# Ensure article is long enough to be valid
								if len(nltk.word_tokenize(paper.articles[x].text)) > 200:
									html = paper.articles[x].article_html.replace('\n', ' ')
									title = (paper.articles[x].title)
									url = paper.articles[x].url
									published_date = paper.articles[x].publish_date
									authors = paper.articles[x].authors
									text = paper.articles[x].text.replace('\n', ' ')
			except Exception as e:
				logging.error("::Exception:Scrapping error for site: " + name + "::")
				logging.error("::Exception: " + str(e) + "::")
				pass
			os._exit(0)									
# Clean author strings
# Insert into database
# Log any other errors
```
#### Data Design
![alt text](pictures/ERD.png "ERD")  
* ERD Diagram  
		The database has 2 schemas. The reason for this is that there are three different access points. There are reporting mechanisms that would use the data warehouse in schema 2. In schema 1 only the data warehouse and the scraper will have access to this transactional table which is a flow of articles. The reason for creating the data warehouse is because it allows you to create data marts that will join together all of the information you use easier for reporting. Each visualization will have a data mart if we made them real time.
* RDBMS: PostgreSQL is the database system to be used for a variety of reasons:
	- It is a relational database; this is needed because the data being gathered by our scraper has many complex relationships.
	- PostgreSQL supports advanced data-types such as JSON while also providing object features which will allow for easy object-relational mapping if needed.
* ETL Pipeline:
	* Extraction: The articles are extracted by a webscraper. The scraper places all the data collected into a single database table. This table is what is used to feed the reporting data warehouse
	* Transformation: The data is pulled into memory via a Python script and it is at this stage that foreign language articles are removed. 
	* Loading: We followed a star-schema methodology when designing the data warehouse so the data is seperated into logical groupings and placed in the dimensions tables. 

### Phase III: Data Analysis

#### Pre-Processing and Feature Extraction

* ##### Natural Language Processing
 	Various NLP methods will play a key role in cleaning our data and extracting features for use in machine learning analysis.
	* ###### **Removal of Stopwords**  
		Stopwords are the very common words in the English language such as 'the', 'there', 'from', etc that provide little to no information on their own. The project will use NLP to remove these words before performing further analysis. Python's NLTK library offers predefined lists of stopwords and functions to easily accomplish this.

		Example code:
		```
		from nltk.corpus import stopwords
		stopwords.words('english')
		# For every article in the database, filter out the stopwords and return the filtered text using a list comprehension
		for article in article_database:
			filtered_article = [word for word in word_list if word not in stopwords.words('english')]
		```
	* ###### **Lemmatization**  
		Lemmatization attempts to find the root of a word from amongst its many forms to reduce data dimensionality. Lemmatization uses a comprehensive approach that takes into account the parts of speech surrounding the word in question. For example: lemmatization would derive 'stem' from 'stemming,' 'stemmer,' and 'stemmed' or 'be' from 'am', 'are', and 'is.' NLTK offers lemmatization via the WordNetLemmatizer.
		```
		from nltk.stem import WordNetLemmatizer
		sent = "cats running ran cactus cactuses cacti community communities"

		wnl = WordNetLemmatizer()
		" ".join([wnl.lemmatize(i) for i in sent.split()])
		# outputs 'cat running ran cactus cactus cactus community community'
		```
	* ###### **Named Entity Extraction**  
		Named entity extraction attempts to find all named entities within a text document and categorize them as a person, location, organization, etc. The Stanford NLP library is recognized as being the best at this and Python offers access to this Java library with a wrapper. Example:
		```
		from nltk.tag import StanfordNERTagger
		from nltk.tokenize import word_tokenize

		text = "The President of the United States is named Donald Trump and he has several children including Donald Trump Jr., Invanka Trump, and a son-in-law: Jared Kushner. He also has a wife named Melania. President Trump is the defacto head of the Republican Party, even though he identified as a Democrat for most of his life. The Republicans have been slow to embrace Mr. Trump."

		# Tokenize the text
		tokenized_text = word_tokenize(text)
		# Run the text through the tagger
		categorized_text = st.tag(tokenized_text)
		# This will return labeled tuples and, after further manipulation, we will get a list of tagged entity tuples:
		[('United States', 'LOCATION'), ('Donald Trump', 'PERSON'), ('Donald Trump Jr.', 'PERSON'), ('Invanka Trump', 'PERSON'), ('Jared Kushner', 'PERSON'), ('Trump', 'PERSON'), ('Melania', 'PERSON'), ('Trump', 'PERSON'), ('Republican Party', 'ORGANIZATION'), ('Trump', 'PERSON')]
		```
	* ###### **Frequency Distribution**  
		A frequency distribution counts the number of times every word appears in a text. NLTK offers this functionality with the FreqDist() function.
		```
		import nltk

		sentence = 'How much wood would a wood chuck chuck if a wood chuck could chuck wood?'

		tokens = nltk.word_tokenize(sentence)
		fdist = nltk.FreqDist(w.lower() for w in tokens)

		# returns: 'wood': 4, 'chuck': 4, 'a': 2, 'would': 1, 'could': 1, 'how': 1, 'much': 1, 'if': 1
		```
	* ###### **Term Frequency - Inverse Document Frequency (TF-IDF)**  
		TF-IDF is a way to score the importance of words (or "terms") in a document based on how frequently they appear across multiple documents. If a word appears frequently in a document, it's important. Give the word a high score. But if a word appears in many documents, it's not a unique identifier. Give the word a low score. Python's scikit learn toolkit provides the sklearn library with this functionality.
		```
		from sklearn.feature_extraction.text import TfidfVectorizer

		# create a TfidfVectorizer object
		tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
		# give the vectorizor a dictionary of documents containing document:content pairs to vectorize
		tfs = tfidf.fit_transform(token_dict.values())
		```
		The code snippet seen above, if run on a corpus containing the works of Shakespeare, will return a matrix containing the following values for the selected words:  
	unseen  -  0.309281094362  
	lord  -  0.156737043549  
	king  -  0.164996828044  
	juliet  -  0.544613034225  
* #### NLP Workflows
	* Flowchart for NLP-based processing pipeline.

	![alt text](pictures/flow_chart.png "Data Processing")

#### Machine Learning Analysis

This section will briefly outline the machine learning techniques we intend to use within this project.

* ##### Unsupervised Learning
	* **Clustering**

		At a high level, clustering is simply a process of letting data group together by placing points near those other data points that
	are more similar; of course more different data points would be farther away from each other. This allows the data to create clusters,
	simply meaning groups of similar data points. In our case, we will use K-means clustering, a technique more thoroughly discussed in the
	research paper about this topic. The most important aspect is that the data clusters are based purely on the similarity of their keywords,
	and at a later step the clusters will be characterized using training data.  

		Another important thing to mention is that articles can overlap with their topics, so it is important not to try to over distinguish
	clusters from each other, as overlap is expected with this type of dataset. K-means clustering might need some modifications in order to
	ensure the overlap is not lost (if it is significant).

	![alt text](pictures/clustering.png)


* ##### Supervised Learning
	- **K-nearest Neighbors and Distinguishing Clusters**

		We will be employing the classic KNN technique within our project in a unique way. Once we have created clusters from the data, we
	will supply training data, and based upon that training data and its nearest neighbors, we can hopefully somewhat classify our clusters
	based on the training data and its placements within. KNN will be the way we calculate the proportion of our training points within clusters. For further details about KNN check the research paper related to clustering.  

		Further, once we have chosen a fixed set of so-called 'topic clusters', we can grow these clusters as we add more datasets, hopefully
	creating more diverse and accurate classification of new articles as the model improves through laws of big numbers in statistics.

	* **Sentiment Analysis**  
	Sentiment analysis is a supervised learning process of classifying text as having either a neutral, positive, or negative sentiment. The classic example analyzes movie reviews. A sentiment analysis classifier is trained on a subset of data from a dataset containing reviews of movies that have already been rated as being good movies or bad movies by viewers with the goal of being able to classify new, uncategorized reviews as being positive or negative. The classifier is then tested on the remaining subset of the data to check for correctness of predictions.

	Unfortunately, we were unable to find sentiment labeled data for a dataset similar enough to our news articles to be able to use supervised learning-based sentiment analysis. Instead, due to time and resource constraints, we chose to use a general purpose sentiment classifier known as VaderSentiment. This classifier is trained on a wide range of labeled data types, making it a good general purpose sentiment analyzer, even if less accurate for new articles than a classifier specifically trained on labeled news article data. As this classifier works at the sentence level, we processed every sentence in our article with this classifier one at a time and summed the totals then divided by the number of sentences in the article to calculate an average sentiment score for the entire article.

#### Formal Procedure for Taking Text to Valid Topic Clusters

- (1) From the entire dataset, word frequencies will be calculated. Stop words will be removed from this list of words, either through
pre-processing of the text or by removing them from the list of word frequencies.

- (2) Keywords will be selected by choosing a subset k of the most frequent words; these selected keywords will be used for TF-IDF analysis
on each article. This will represent the article as a vector of keywords.

- (3) Using cosine similarity or Euclidean distance, similarity will be measure between articles. Those more similar will be grouped closer, less similar further.

- (4) Once the entire set of articles is measured and positioned relative to other articles, areas of highest density should naturally occur,
indicating similar articles in that area. Using KNN-like measurement, and training datasets pre-determined for some topic, the clusters will
be classified and identified as representative of those pre-determined topics.

- (5) Using this model, repeated training can be supplied to improve it, and as users submit articles, their submitted articles can be classified and described, then utilized back into the model to improve it as well.

- (6) Once a similarity classification system is in place, we can attempt to extract meaningful sentiment classification at many different levels including by article, by topic cluster, by news outlet, etc.



### Phase IV: Web Application
* #### Web framework  
	* ##### Flask
		* Allows communication between our Python-based back-end and our front-end web application.
		* Flask is a micro framework which means that it has a simple yet extensible core. This is important for a computationally intensive project because any overhead incurred by functionality not being used would be detrimental.
		* One of the easier to learn and use frameworks with a low amount of organizational overhead compared to many other frameworks, allowing for rapid integration and expansion.
* #### Languages
	* ##### HTML
	* ##### Flask (Python)
	* ##### JavaScript
* #### Data Visualizations
	* ##### Clustering Visualization/Explanation

		In order to provide meaningful information to end users, and for purposes of measurement and accuracy and interacting with the
		clusters of data, creating a visualization tool for this clustering could serve both of these purposes. This graphic could show
		density of clusters, count of articles within, boundaries of clusters, and/or any information that is determined to be useful
		in relation to the grouping of the articles by similarities.
		![alt text](pictures/ClusterViz.png "ClusteringViz")
		In this example, node size represents confidence, cluster represents rule part groupings, color represents something else and transparency could be another stat if it's not overwhelming.
	* ##### Examples of Statistics-based Visualizations/Explanations  
		![alt text](pictures/CalendarPieChart.png "CalendarPieChart")

		By day we can show the amounts of the pie graph based on topics, or based on sentiment towards certain topics.  

		![alt text](pictures/RelationalViz.png "RelationalViz")
		This could use news sites around the and the relations could be be cross site topics.  

		[More information](https://csaladenes.com/2015/06/21/a-visual-exploratory-of-refugee-flows-over-the-world-using-dynamic-chord-diagrams/)
	* ##### Wordcloud example/Explanation
		![alt text](pictures/WordCloud.png "WordCloud")
		Size will be representative of the word count, color will indicate sentiment and orientation will represent something else.

		[Link to Potential Python Library](https://www.jasondavies.com/wordcloud/)

* #### User Interface Diagrams
	##### Site Flow
	![alt text](pictures/SiteFlow.png "Site Flow")
	##### Homepage
	![alt text](pictures/index.png "Homepage")
	##### About
	![alt text](pictures/about.png "About")
	##### Request Disclosure
	![alt text](pictures/disclosure.png "Request Disclosure")
	##### Request Disclosure Error
	![alt text](pictures/disclosureError.png "Request Disclosure Error")
	##### Disclosure Result
	![alt text](pictures/disclosureResult.png "Disclosure Result")
	##### Visuals
	![alt text](pictures/visuals.png "Visuals")
	![alt text](pictures/visualsData.png "VisualsData")

## Research

![alt text](pictures/research-1.png)
![alt text](pictures/research-2.png)
![alt text](pictures/research-3.png)
![alt text](pictures/research-4.png)
![alt text](pictures/research-5.png)
![alt text](pictures/research-6.png)
![alt text](pictures/research-7.png)
![alt text](pictures/research-8.png)
![alt text](pictures/research-9.png)
![alt text](pictures/research-10.png)
![alt text](pictures/research-11.png)
![alt text](pictures/research-12.png)
![alt text](pictures/research-13.png)
![alt text](pictures/research-14.png)
![alt text](pictures/research-15.png)
![alt text](pictures/research-16.png)
![alt text](pictures/research-17.png)
![alt text](pictures/research-18.png)
![alt text](pictures/research-19.png)
![alt text](pictures/research-20.png)
![alt text](pictures/research-21.png)
![alt text](pictures/research-22.png)
![alt text](pictures/research-23.png)
![alt text](pictures/research-24.png)
![alt text](pictures/research-25.png)
![alt text](pictures/research-26.png)
![alt text](pictures/research-27.png)
![alt text](pictures/research-28.png)
![alt text](pictures/research-29.png)
![alt text](pictures/research-30.png)
![alt text](pictures/research-31.png)
![alt text](pictures/research-32.png)
![alt text](pictures/research-33.png)
![alt text](pictures/research-34.png)
![alt text](pictures/research-35.png)
![alt text](pictures/research-36.png)
![alt text](pictures/research-37.png)
![alt text](pictures/research-38.png)
![alt text](pictures/research-39.png)
![alt text](pictures/research-40.png)
![alt text](pictures/research-41.png)

# Development Plan

## Development Method
Waterfall methodology follows the following steps:
First capture all of the requirements of a software system, which has been done via this documentation. Next, start analyzing the scraped data using the NLP and machine learning python libraries and creation of the data warehouse. Design will be next so the layout of the website can be solidified and work will begin on the visualization. Coding will be done throughout all of these steps, along with testing; however a testing suite will be implemented last. And finally the software will be  deployed from DEV to PROD, ending Capstone II and 2017 Seniors at Mizzou. Any further support, migration or maintenance will come through all members of the team for review and verification.
The main reason waterfall is best for this project is because many of the methodologies that could potentially be used to attempt a task may fail, but that developer should still succeed at their task. Research is often done this way since it is difficult to partition out the different smaller goals. For example, having someone do the clustering piece or be in charge of it is better than doing it in smaller chunks. This is because they could while researching and prototyping discover some new way to do clustering that invalidates their work on that problem up to this point. They should continue chugging away at this new idea. If agile was used for this project someone would have a week to implement X clustering algorithm. If it works awesome, if not, they've failed and now the timeline is wrong, since time is not built into this agile development for failure and research since its done at such a granular approach.
![alt text](pictures/waterfall.png)
## Timeline
![alt text](pictures/Timeline-1.png)
![alt text](pictures/timeline2.png)

## Work Delegation
* Kurt: Data-warehousing/ data visualization
	* Data warehouse development to create data marts that ease reporting analytics
	* Create visualization based upon categorization and statistics done via analysis using Javascript (D3)
* Ali: Backend web development
	* Develop a normalized transactional database using PostgreSQL
	* Backend web development using Python (Flask)
* Justin: Natural Language Processing
	* Natural language processing for cleaning data and extracting features for use in machine learning analysis
	* Development of web scraper
	* Design of AWS deployment prototype
* Jared: Machine Learning Analysis
	* Categorization of articles using both unsupervised and supervised learning techniques
	* Web server deployment
* Zach: Front End Development
	* UI design using HTML, CSS, and JavaScript
	* System administration

## Possible Troubles
* In general, this is a big, challenging project for undergraduates who will be required to learn many new techniques to bring it to the finish line.  
* Using AWS offers great potential for decoupled, scalable data processing but this could be limited by running up against financial constraints.  
* It might be difficult to get a high degree of accuracy in this application of unsupervised clustering due to the nature of news articles and their tendency to contain overlapping topics.
* It might prove difficult to draw accurate conclusions with sentiment analysis due to the typically neutral language used in most news articles.
* If any of the data needs to be labeled by hand, this could prove to be incredibly time consuming and, due to the small size of the development team, would be vulnerable to bias.

## Alternative Strategies
* If AWS proves to be unfeasible for the large amount of data processing required due to financial constraints, the team has access to the university research cluster computer to process data locally, outside of the cloud and its associated costs.
* If unsupervised clustering proves inadequate for topic classification, we can fall back on supervised learning using K nearest neighbors or other supervised learning algorithms on labeled data.

## Testing

We plan on testing using unit testing, creating testing suites with each new version release of the software. As new features are added,
unit testing will allow us to continuously ensure old functionality while introducing new features. There remains research to be done in this area as far as testing software to use. However, a general plan for testing will resemble the following:

- As new features are written, verify their functionality with unit tests, ensuring all tests are passing before a feature is finished.
Alternatively, development may sometimes begin with a test first style of development, writing code to match the tests perceived to
be important to that feature.

- Tests will be consolidated in one testing suite, which will allow old tests to be run along with new features to test that the new
features do not hurt existing functionality.

- A stretch goal for this project will be to implement testing hooks and build automation so that all live code complies with testing
before being put into a live environment. This ensures highly stable code releases, and prevents bad code from being released.

 - Database Integration Testing
Since our data is what drives this projects, we need to be aware of its status. To do this, I will create a bar chart that gives a count of all null fields in each column of the database and check it by weekly. If it seems like the count is getting too high we will need to check our scraper to confirm it is passing its unit tests and that it’s passing information to the database the way we intended it too

Below is a general outline of what we think will need to be tested as we develop.

| Feature | How we will need to test |
|--|--|
| TF-IDF keyword values | For this we can test our TF-IDF by giving articles with known TF-IDF values and testing the accuracy of our TF-IDF methods |
| Clustering | We will need to verify the accuracy of grouped clusters. We will do this by comparing word frequency of articles pulled from a cluster and see if those articles actually share keywords|
| Topic Classification | We will test this by sampling a few random articles from each topic cluster after we train it and verify the articles relate to that topic |
| Sentiment Analysis | To test this, we will need to compare sentiment analysis results with the actual content of the article and judge whether the sentiment is expressed accurately |
| Database stored procedure testing | In the general case, we should have test data to run stored procedures on and test the results to verify they work as intended |
| Stop word Removal | Similar to TF-IDF, we will need to verify our stop words are being removed by giving sample articles and checking the output for remaining stop words |
| Stemming/Lemmatization | Given sample words, test the expected stem output with process |
| Data warehouse from current database | We will need to verify when we create our data warehouse that the data accurately reflects the database data; this can be done by comparing queries and their output from the database vs the data warehouse |
| Flask/Front End testing | The best way to test front in features seems to be with integration tests and workflow procedures to verify that the old workflows work as new features are added. This does not yield itself well to unit testing |
| Web scraper | We can test the scraper is working by checking for recently posted articles at sites we expect to scrape properly and verifying those articles are contained in the database as expected |
| Visualizations | Testing visualizations should be relatively simple using dummy data to visualize and verifying it is displayed accurately |



## Prezi
* http://prezi.com/ybpo3byyhwaw/?utm_campaign=share&utm_medium=copy
