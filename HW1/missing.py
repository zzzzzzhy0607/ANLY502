#### ANLY502 HW1
#### Problem 1

#!/usr/bin/python
# Import library
import sys

def main():
    # Take the two arguments
    N=sys.argv[1]
    List=sys.argv[2]
    arr=[]

    # Test whether the inputs are all integers
    try:
        # Try to convert N into integer
        number = int(N) 
        # Try to convert the List into an integer array
        for x in List.split():
            a=int(x) 
            arr.append(a)

    # If there is an error    
    except ValueError:
        print("Your input contains non-integer.")
    
    # Test whether the length of the array is equal to N-1
    else:
        if len(arr)!=number-1:
       
            # If there is an error    
            print("The number of items in the list does not match N-1.")
        
        # Test whether there are duplicate values in the array
        else:
            if len(arr) != len(set(arr)):
            
                # If there is an error    
                print("There are duplicates in the list.")
         
            # If all the conditions pass, find the missing value
            else:
                test=[False]*(number+1)
                for i in range(0,number-1):
                    b=arr[i]
                    test[b]=True
                
                for i in range(1,number+1):
                    if (test[i]==False):
                        print("The missing number is",i)
            
# Call the main function
if __name__ == '__main__':
    main()
