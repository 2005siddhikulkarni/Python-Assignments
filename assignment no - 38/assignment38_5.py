import pandas as pd


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    print(df.groupby("FinalResult")["StudyHours"].mean())
    # students who have failed have the average of study hours like 2.55 hours and the students who have passed have the average of study hours like 6.37 hours . so, in the conclusion if the students study for longer duration,they might have chances of passing the exam. 

    print(df.groupby("FinalResult")["Attendance"].mean())
    # students who have failed have the average of attendance like 67.75% and the students who have passed have the average of attendance like 86.61%. so, in the conclusion if the students attends the classes,they might have chances of passing the exam. 

if __name__ =="__main__":
    main()