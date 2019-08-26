data = LOAD 'i-bigrams/googlebooks-eng-us-all-2gram-20120701-i?' USING PigStorage('\t') AS (gram:chararray, year:int, occur:int, books:int);

Bigram = GROUP data BY gram;

Aggregated = FOREACH Bigram {
	TotalOccurrences = SUM(data.occur);
	TotalBooks = SUM(data.books);
	GENERATE $0 AS word:chararray, TotalOccurrences, TotalBooks, 
        (float)((float)TotalOccurrences / (float)TotalBooks) AS avg, 
        MIN(data.year) AS firstyear, 
        MAX(data.year) AS lastyear, 
        COUNT(data.year) as records;
        }

Filtered = FILTER Aggregated BY (firstyear == 1950) AND (records == 60);

Ordered = ORDER Filtered BY avg DESC;

Top50 = LIMIT Ordered 50;

STORE Top50 INTO 'results-pig1' USING PigStorage(',');
