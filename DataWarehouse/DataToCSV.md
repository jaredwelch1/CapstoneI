- Copy data to a file:
	- Note: The data is currently over a GB so probably want to use a LIMIT on the select query

			COPY( SELECT * FROM articles ) to 'absoluteFilePath' CSV HEADER;
