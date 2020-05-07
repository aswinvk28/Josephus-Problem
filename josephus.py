def josephus(n, k):
    if(n == 1): 
        return 1

    v = (josephus(n-1, k) + k-1) % n + 1
    return v

def main():
    n = 0
    k = 0
    n = input("Enter the value of number of soldiers..: ")
    n = int(n)
    k = input("Enter the iterations..: ")
    k = int(k)
    print("\n")
    print("Josephus Value: ", josephus(n, k))
    return 0;

if __name__ == "__main__":

    main()