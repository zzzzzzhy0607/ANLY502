#### ANLY502 HW1
#### Problem 3

#!/usr/bin/python

# Import libraries
import sys
import re

    
# Function to extract year from a file
def extract_year(filename):
    
    with open(filename, 'r') as f:
        # Search for year
        year = re.search(r'(<h3 align="center">)(Popularity in )(\d\d\d\d)', f.read())
        # If we can find the year
        if year != None:
            # Read the 3rd group as date
            date=year.group(3)
            # Print and return the result
            #print(date)
            return(date)
        # If we do not find the year
        else:
            return('Not found')


# Function to extract name and its rank from a file  
def extract_name_rank(filename):
    
    with open(filename, 'r') as f:
        # Create a dictionary
        name_rank={}       
        # Search for name and rank
        info = re.findall(r'(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)(</td>)', f.read())
        
        # Separate rank and names
        for pieces in info:
            rank=pieces[1]
            name1=pieces[3]
            name2=pieces[5]
            
            name_rank[name1]=rank
            name_rank[name2]=rank
        
        # Sort the names 
        name_rank_sorted = sorted(name_rank.items())
        # Print and return the results
        #print(name_rank_sorted)
        return name_rank_sorted                        
    
    
# Function to return something like ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
def extract_names(filename):
    
    # Create a list to store information
    alist = []
    
    # Get year
    year = extract_year(filename)
    alist.append(year)
    # Get name and rank
    name_rank = extract_name_rank(filename)
   
    # Add names and ranks into the list
    for data in name_rank:
        alist.append(data[0] + ' ' + data[1])
        
    # Print and return the results
    #print(alist)
    return(alist)


# Call extract_names function and take arguments as the filename
def main(): 

  # Omitting the [0] element, which is the script itself
  if len(sys.argv) == 2:
    arg = sys.argv[1]   
  else:
    print("usage: ", sys.argv[0], "filename")
    sys.exit(1)  
  
  # For each filename, get the names, then print the text output
  # for file in sys.argv[1:]:
  # Get the list
  mylist=extract_names(arg)
      
  # Print the list
  text = '\n'.join(mylist) + '\n'
  print(text)
  print('Yes, you are running the script correctly!')

# Call the main function
if __name__ == '__main__':
    main()
