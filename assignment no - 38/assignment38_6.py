import pandas as pd
import matplotlib.pyplot as plt


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    print("Distribution of study hours")
    plt.hist(df["StudyHours"])
    plt.xlabel("Study Hours")
    plt.ylabel("no of students")
    plt.show()

if __name__ =="__main__":
    main()