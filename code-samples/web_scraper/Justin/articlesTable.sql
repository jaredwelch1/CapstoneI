DROP TABLE articles;
CREATE TABLE articles(
	site                varchar(100),
	title               varchar(250),
    author              varchar(100),
    secondary_authors   varchar(100),
    published_on        date,
    accessed_on         timestamp,
    url                 varchar(500),
    body                text,
	html				text,
	newspaper_keywords	varchar(300),
	newspaper_summary	text,
    id                  serial	PRIMARY KEY
);
