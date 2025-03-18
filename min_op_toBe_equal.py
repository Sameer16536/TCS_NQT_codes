def min_operations(p,q,r):
    
    if p==q==r:
        return 0
    
    if (p+q+r) % 3 != 0:
        return -1
    maxValue = max(p,q,r)
    current_Total = p+q+r
    required_Total = 3*maxValue
    
    num_operations = (required_Total - current_Total)//2
    
    return num_operations

def main():
    
    
    n = int(input("Enter the number of test cases: "))
    for _ in range(n):
        line = input("Enter the numbers p q r : ") 
        p,q,r = map(int,line.split())
        print(min_operations(p,q,r))
    
    
    
if __name__ =="__main__":
    print(main())