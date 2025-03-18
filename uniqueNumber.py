
# Find the unique number in an array where all numbers except one, are present twice.
def main():
    arr = list(map(int,input().split()))
    unique_element  = 0 
    
    # a ^ a = 0 , a ^ 0 = a
    for num in arr:
        unique_element =  unique_element ^ num
        
    return unique_element
    

if __name__=="__main__":
    # main()
    print(main())