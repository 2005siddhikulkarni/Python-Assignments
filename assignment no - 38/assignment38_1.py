import pandas as pd

def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")

    FData = df.head()
    print("The starting data from CSV: ")
    print(FData)

    LData = df.tail()
    print("The ending data from CSV: ")
    print(LData)

    print("The total number of rows and columns are: ",df.shape)

    print("The columns are: ")
    res = list(df.columns)
    print(res)

    print("The datatypes of each column are: ")
    Types = df.dtypes
    print(Types)
    
if __name__ =="__main__":
    main()