# Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve unit assignment problems before the lecture. 
# Today he got one tricky question. The problem statement is “A positive integer has been given as an input. Convert decimal value to binary representation. 
# Toggle all bits of it after the most significant bit including the most significant bit. Print the positive integer value after toggling all bits”.


# convert decimal to binary
# toggle all bits after the most significant bit including the most significant bit 0-->1 and 1-->0
# print the positive integer value after toggling all bits


def toggle_bits(n):
    if n == 0:
        return 1
    
    # most significant bit
    msb =  n.bit_length()
    print("Most significant bit: ",msb)

    
    # create a mask with all bits set to 1 after the most significant bit ,Example: If n=13 (1101), mask=1111
    mask = ( 1 << msb) -1
    print("Mask: ",mask)
    
    # toggle using XOR
    result = n ^ mask
    
    return result


def main():
    n = int(input("Enter a positive integer: "))
    result = toggle_bits(n)
    print("Result: ",result)
    
    

if __name__ == "__main__":
    main()
    
    

