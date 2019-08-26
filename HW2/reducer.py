#### ANLY502 Homework2
#### Problem 2

#!/usr/bin/env python3

# Import library
import sys

if __name__ == "__main__":   
    # The output from basic-mapper.py looks like
    # 2012-01	1
    # 2012-01	1
    # 2012-02	1
    # 2012-02	1
    # ....

    current_date = None
    current_count = 0
    date = None
    
    for line in sys.stdin:
    	line = line.strip()
        # Separate date and count
    	date, count = line.split('\t', 1)
        
    	# convert count from string to int 
    	try:
    		count = int(count)
    	except ValueError:
                # Ignore the line having error
    		continue
        
    	if current_date == date:
    		current_count += count
    	else:

    		if current_date:
    		       print('%s\t%s' % (current_date, current_count))
            
    		current_count = count
    		current_date = date
            
    # Output the last date 
    if current_date == date:
    	print('%s\t%s' % (current_date, current_count))
