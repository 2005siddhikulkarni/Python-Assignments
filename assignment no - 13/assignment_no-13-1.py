def AreaOfRect(Value1, Value2):
    Area = Value1 * Value2

    return Area

def main():
    Length = print("Enter the length of rectangle: ")
    Length = float(input())

    Width = print("Enter the width of rectangle: ")
    Width = float(input())

    Ans = AreaOfRect(Length, Width)
    print("Area of rectangle is: ",Ans)

if __name__ == "__main__":
    main()