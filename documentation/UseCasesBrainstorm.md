# Use Cases

**this is only a draft of possible use cases, not an exhaustive list of what to include. Many things on this list will not make
the scope of our project.**

## Machine Learning Applications

- Analyze given articles, based upon user specified criteria (i. e., user chooses to analyze "Political Bias" and
"Positive or negative" if they desire to view predictions of those categories), and display predicted values for where
the article falls on the scale based upon our model.

- create model of bias and news sources from training data, then using the model, analyze bias over time
  
  - the model would need to be based upon training data, maybe chosen at random to reduce selection bias, from all time periods
  (or depending, from each year), This model should give us classifiers that are modeled based on data from all times sampled.
  
  - Then, comparing inidividual samples from each 'bucket' (here meaning years, decades, whatever we use to separate them) we could 
  say "in year X, the average leaning was here, and year Y, it moved to here"

## Data visualizations pulled from News articles

(note: many of the machine learning applications will also probably require data visualizations, but these use cases should 
only be related to those visualizations that do not require machine learning modeling, e.g., "What percentage of Fox reporting 
is about guns?" Since this is a raw statistic (number about guns/ total) that can be quickly calculated, we can use the same data
and simple queries to accomplish these use cases as the machine learning ones, but they are much smaller in work load than 
the more complex use cases above.)

- Simple polling about the percentages of various topics
  
  - for instance: "What percentage of analyzed articles relate to women's rights or feminist movements?" 
  
- Given a topic/event, return a list of news sources that have reported on it 

  - "Event: Google CEO resigns, return: Fox, CBS, CNBC, ..., 
