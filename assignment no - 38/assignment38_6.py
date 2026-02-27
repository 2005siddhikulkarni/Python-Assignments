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

    #The histogram shows that students are distributed across different study hour ranges from 1 to 8 hours. The distribution is fairly balanced without extreme skewness. This indicates variation in study habits among students, which may impact their final results.

if __name__ =="__main__":
    main()