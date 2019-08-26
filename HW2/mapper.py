#### ANLY502 Homework2
#### Problem 2

#!/usr/bin/env python3

# Import library
import re
import sys
import datetime

# Input file s3://bigdatateaching/forensicswiki/2012_logs.txt
# Input line looks like :
# 77.21.0.59 - - [04/Jan/2012:00:35:07 -0800] 'GET /w/index.php?title=-&action=ra$

if __name__ == "__main__":
    
	for line in sys.stdin:
        	line = line.rstrip()
        	# Separate the line into three parts
        	words = line.split('[')
        	# The second part contains the time
        	words = re.split(r' -0800| -0700',words[1])
        	# Get the date
        	date = datetime.datetime.strptime(words[0], "%d/%b/%Y:%H:%M:%S")
        	# Get only year and month
        	year_month = date.strftime('%Y-%m')
        	print(year_month +"\t1")
