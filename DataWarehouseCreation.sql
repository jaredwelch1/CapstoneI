create table author_dim(
    author_id SERIAL,
    name TEXT,
    PRIMARY KEY(author_id)
);

create table site_dim(
    site_id SERIAL, 
    domain text, 
    name text, 
    supersite_id int,
    PRIMARY KEY(site_id)
);

create table article_dim(
    article_id SERIAL, 
    title text, 
    URL text, 
    published_date timestamp,
    accessed_date timestamp, 
    body text,
    html text, 
    keywords text, 
    summary text,
    PRIMARY KEY(article_id)
);

create table statistic_dim(
    statistic_id SERIAL,
    NLP_results JSON,
    PRIMARY KEY(statistic_id)
);

create table fact(
    fact_id SERIAL,
    article_id int,
    author_id int,
    site_id int,
    statistic_id int,
    FOREIGN KEY (article_id) REFERENCES article_dim(article_id),
    FOREIGN KEY (author_id) REFERENCES author_dim(author_id),
    FOREIGN KEY (site_id) REFERENCES site_dim(site_id),
    FOREIGN KEY (statistic_id) REFERENCES statistic_dim(statistic_id)
);

insert into author_dim (name)
select distinct author 
from articles;


-- Need to define parse function
-- insert into site_dim (name, domain, supersite_id)
-- select distinct site as name, url as domain, 
-- parse(url) as supersite_id
-- from articles;

-- Date timestamp messing things
-- insert into article_dim (title, URL,published_date, accessed_date, body, html, keywords, summary)
-- select title, url, published_date, accessed_date, body, html, keywords, summary
-- from articles;

-- Waiting on previous tables before we run this
-- insert into fact (article_id, author_id, site_id)
-- select article_id, author_id, site_id
-- from various tables, 
-- then commit; 