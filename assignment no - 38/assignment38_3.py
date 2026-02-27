import pandas as pd

def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    Avg1 = df["StudyHours"].mean()
    print("Average of StudyHours is: ",Avg1)

    Avg2 = df["Attendance"].mean()
    print("Average of attendance is: ",Avg2)

    Max = df["PreviousScore"].max()
    print("Maximum value of PreviousScore is: ",Max)

    Min = df["SleepHours"].min()
    print("Minimum value of SleepHours is: ",Min)

if __name__ =="__main__":
    main()