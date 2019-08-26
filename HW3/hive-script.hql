CREATE EXTERNAL TABLE data (gram string,year int,occurrences int,books int)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LOCATION '/user/hadoop/hw03hive';

LOAD DATA INPATH 'r-bigrams/googlebooks-eng-us-all-2gram-20120701-r?' OVERWRITE INTO TABLE data;

INSERT OVERWRITE DIRECTORY 'results'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT gram,SUM(occurrences) AS total_occur,SUM(books) AS total_books,CAST(SUM(occurrences)AS float)/SUM(books) AS avg_occur,MIN(year) AS first_year,MAX(year) AS last_year,COUNT(year) as total_year
FROM data
GROUP BY gram
HAVING first_year==1950 AND total_year==60
ORDER BY avg_occur DESC
LIMIT 50;
