import pandas as pd


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    rows , columns = df.shape
    print(f"rows : {rows} , columns : {columns}")
    print("The total number of students in dataset are: ",rows)

    print("Students passed: ",len(df[df["FinalResult"] == 1]))
    
    print("Students failed: ",len(df[df["FinalResult"] == 0]))


if __name__ =="__main__":
    main()