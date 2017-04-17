# Capstone 2017 Documentation

## Team info

Mission Statement: Our mission is to analyze news articles and determine whether they are positive or negative and research the effects that they have on the world.

Agenda: Get Amazon Webserver
	Create a database to store articles.
	Create a Python Webscrapper to get and store those articles in the afformentioned database.
	Start webscrapper.
	Brain storm machine learning techniques. 
	Appy machine learning techniques. 
	Create visualizations.
	
	

Thoughts: (insert Step Brothers reference) Fake news is a growing concern today and we want to do something about it?????????????????

Beliefs: The Earth is NOT flat. The sky is not the limit, the mind is.???????????????????????????

Team Name: Squad

#### Team Members:
- Zach Bryant: Nickname = Zen Master Zach. I work on campus as an IT Support Specialist. Yes, I save lives. Really though, I am in charge of keeping all the printers in the computer labs filled with paper. I can get you swipe access to the labs for after hour access ;) I am a senior in Computer Science and will graduate December 2017.
![alt text](pictures/zach.jpg "Zach Bryant")

- Kurt Bognar: Senior at MU Majoring in Computer Science with a Minor in Math. I'm a research for the university aiding in the creation of new tools and algorithms for Association-Rule Mining.
![alt text](pictures/kurt.jpg "Kurt Bognar")

- Ali Raza: I am a senior at the University of Missouri studying Computer Science. I do research at the iDAS Lab where I am currently developing a data mining library.   
![alt text](pictures/ali.jpg "Ali Raza")

- Jared Welch

	- Senior at the Univeristy of Missouri. Passionate about improving my skills. Excited for the potential of our application. 

![alt text](pictures/jared.png "Jared Welch")

- Justin Renneke: Senior undergraduate of Computer Science at the University of Missouri, graduating December '17.  Interested in machine learning, data analysis, cloud computing, and using Python to conquer the galaxy.      
![alt text](pictures/justin.png "Justin Renneke")

## introduction
Team name: Squad
Teams mission: To create a model that classifies the bias of a news article.

This election season has been particularly harsh in America. Republicans
and Democrats alike made false claims against the media and both were
unfairly attacked as well. Being an informed citizen these days is hard
enough without news outlets taking sides and obfuscating this bias from
the public. For this reason, Squad has decided to fix this problem by
creating a model that could be added as an extension so when you are
on a web page, you know that it is bias for or against a certain topic
based on the overall text in the article, allowing you to seek out sources
for the opposing viewpoint and make up your own mind.

## Problem statement and solution

### Problem Definition

Today, the average consumer of media content is very susceptible to unknown bias in the sources that they use. Because all media sources
most likely have some bias, in order for consumers to be most informed, they need a reliable way to measure bias and account for it in
their research/consumtion of media information. If users could know what bias and relevant information about the statistical history for
a particular news establishment, it would increase consumer ability to gather and trust information from media.
Similarly, currently, it is very difficult to document and discuss media bias in a way that is provable and measureable. There needs to be
a standard to use, or a metric to measure by, in order to determine how much of a report is motivated by bias and how much seems to be motivated purely by facts.

### Problem Solution

We propose the following software solution:

Using published text from media sources, and computer analysis, we propse a software system that uses these published works and
the resulting data to provide means to measure how that media source reports on certain topics. This would fix both issues above.
For the first problem, having this data will allow users to have an objective source analyze the data and output information that they can
then use to judge the media source. All the data will be relative to the source, and all source data should be analyzed in the same
way to prevent harming the integrity of the data. Having a metric that is gathered in the same way for all sources allows consumers to
compare data for one source, to the same measurement for a different source, allowing them to make better judgements about bias regarding
sources they use.
The problem of documenting media bias also is solved, as this data could be used as evidence for or against these sources to use as
a basis for research and reports, which is an objective metric, rather than the opinions of the reporting person or eye witness
interview.

## Requirements
### User
* Any person who is interested in obtaining a better understanding of media bias can expect to use this software to explore measureable indicators of bias which will be presented in the form of data analysis and visualizations.
* The software will provide an interactive user experience based on menus and UI elements that will allow the user to explore the data presented.
* The user will be presented with both static and dynamic options for data presentation, including the option to input article text and receive back information regarding analysis of its content.

### Hardware  
* This will require more detail and discussion about the direction of our project

### Functional
* Given a list of news websites, scrape every new article on every site and return and store in a database the following data from each article: Article title, author name(s), date published, article body text, raw html, and webpage url.
* Perform natural language processing analysis on articles to clean the data and generate features such as named entities, bag of word counts, and term frequency-inverse document frequency metrics.
* Categorize articles into groups based on topic determined by performing machine learning-based cluster analysis using generated features.
* A web application will provide users with visualizations of the clustered topics and their articles.
* The web application will allow a user to provide the url of a specific news article, scrape the webpage, assign the article to a topic category, and inform the user of the result.  
#### Functional Stretch Goals
* Allow users to perform custom searches of the article database and return data visualizations based on metrics such as frequency of occurrence, trends of occurrence over time, and relation to other topics.
* Create a scrolling wordcloud graphic to visualize changes in overarching news trends over time.
* Perform sentiment analysis on articles and visualize the results.


## Prezi
* http://prezi.com/ybpo3byyhwaw/?utm_campaign=share&utm_medium=copy

### Non Functional Requirments
* Availibility: 99% server availibility.
* Backup: Bi-weekly backups of server, database, and news articles. 
* HTTPs encryption with a valid SSL certificate.
* Extensibility: Modular software design using OOP practices to allow for easy addition of new features.
* Licensing: MIT License 
* Performance: Analyze users article in less than one minute
* Portability: Designed to be compatible with mobile and tablet user interfaces.
* Scalability: Decoupling an RDS cloud database from computational resources so that we can scale vertically when more computation is required.

#### Non Functional Strech Goal
* Response Time: Real time article classification
