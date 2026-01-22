import math

def AreaOfCircle(No1):
    Area = math.pi * (No1 ** 2)

    return Area

def main():
    r = print("Enter the radius of circle: ")
    r = float(input())

    Result = AreaOfCircle(r)
    print("Area of circle is: ",Result)

if __name__ == "__main__":
    main()