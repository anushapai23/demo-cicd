
def sum(a,b):
    return a+b

if __name__ == "__main__":
    a,b = map(int, input("Enter the value of a,b in integers \n").split(","))
    print(f"Sum is {sum(a,b)}")