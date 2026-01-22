def DisplayGrade(Marks):
    if Marks >= 75 :
        Result = print("Distinction")

    elif Marks >= 60 and Marks <= 75 :
        Result = print("First Class")

    elif Marks >= 50 and Marks <= 60 :
        Result = print("Second Class")

    elif Marks < 50 :
        Result = print("Fail")

    return Result


def main():
    Value = print("Enter the marks: ")
    Value = int(input())

    DisplayGrade(Value)
    
if __name__ == "__main__":
    main()