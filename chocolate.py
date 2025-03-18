#A chocolate factory is packing chocolates into the packets. The chocolate packets here represent an array  of N number of integer values. 
# The task is to find the empty packets(0) of chocolate and push it to the end of the conveyor belt(array).

# N=8 and arr = [4,5,0,1,9,0,5,0].
# Output: [4,5,1,9,5,0,0,0]

def push_zeroes_to_end(arr,n):
    res = []

    for i in range(n):
        if arr[i] != 0:
            res.append(arr[i])

    for i in range(n):
        if arr[i] == 0:
            res.append(arr[i])

    return res

def push_zeroes_to_end_2(arr,n):
    nonZeroIndex = 0 
    
    for i in range(n):
        if arr[i] !=0:
            #swap
            arr[nonZeroIndex],arr[i] = arr[i],arr[nonZeroIndex]
            nonZeroIndex += 1

    return arr

def main():
    n = int(input("Enter the number of elements in the array: "))
    arr = [4,5,0,1,9,0,5,0]
    res = push_zeroes_to_end(arr,n)
    res2 = push_zeroes_to_end_2(arr,n)
    print(res)
    print(res2)

if __name__ == "__main__":
    main()
