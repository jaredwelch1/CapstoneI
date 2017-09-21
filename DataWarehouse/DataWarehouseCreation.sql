create table author_dim(
    author_id SERIAL,
    name TEXT,
    PRIMARY KEY(author_id)
);

create table site_dim(
    site_id SERIAL, 
    domain text, 
    url text, 
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
