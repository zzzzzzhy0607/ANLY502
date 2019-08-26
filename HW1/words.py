#### ANLY502 HW1
#### Problem 2

#!/usr/bin/python
# Import libraries
import sys

def main():

    try:
        # Test whether the user enters a filename 
        filename=sys.argv[1]   

    # If there is no filename, read from stdin    
    except:
    
        print("You don't enter a filename, please enter a sentence.")
        # Read from stdin
        string = sys.stdin.readline()
    
        # Split lines into words
        words = string.strip("\n").split(" ")
        # Get unique words
        unique_words=set(words)
        # Sort the words
        unique_words2=sorted(unique_words)
    
        # Write to stdout
        for word in unique_words2:
            sys.stdout.write(word+'\n')

    # If there is a filename, read from the text file  
    # Download using wget http://www.gutenberg.org/files/11/11-0.txt
    else:
    
        # Store the words
        words=[]
    
        # Open the file 
        with open(filename,'r') as f:
            for line in f:
                for word in line.split():
                    # Get all words
                    words.append(word)
            
            # Get unique words
            unique_words=set(words)
            # Sort the words
            unique_words2=sorted(unique_words)
    
            # Write to stdout
            for word in unique_words2:
                sys.stdout.write(word+'\n')
                
# Call the main function
if __name__ == '__main__':
    main()
