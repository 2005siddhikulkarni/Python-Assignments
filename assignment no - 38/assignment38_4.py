import pandas as pd


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    Res = df["FinalResult"].value_counts()
    
    Pass_Stud = Res[1] / len(df) * 100
    print("The passed students are: ",Pass_Stud)

    Fail_stud = Res[0] / len(df) * 100
    print("The failed students are : ",Fail_stud)

if __name__ =="__main__":
    main()