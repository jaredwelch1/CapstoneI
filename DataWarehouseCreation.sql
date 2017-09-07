create table autor_dim(
	author_id	SERIAL,
	name	TEXT	
);

create table site_dim(
	site_id SERIAL, 
	domain  text, 
	name	text, 
	supersite_id int	
);

create table article_dim(
	article_id 			SERIAL, 
	title				text, 
	URL					text, 
	published_date		timestamp,
	accessed_date		timestamp, 
	body				text,
	html				text, 
	keywords			text, 
	summary				text
);

create table example_stat_dim1(
	statistic_id	SERIAL,
	NLP_results		JSON
);
create table example_stat_dim2(
	
);

create table fact(
	fact_id SERIAL,
	article_id	int references article_dim(article_id),
	author_id	int references author_dim(author_id),
	site_id	int references site_dim(site_id),
	statistic_id	int references statistic_dim(statistic_id),
);


insert into author_dim
select distinct author 
from scraped;

insert into site_dim
select distinct site as name, url as domain, 
parse(url) as supersite id
from scraped;

insert into article_dim
select title, url, published_date, accessed_date, body, html, keywords, summary
from scraped;

insert into fact 
select article_id, author_id, site_id
from various tables, 
then commit; 

















