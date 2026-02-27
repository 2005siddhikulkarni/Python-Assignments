import pandas as pd
import matplotlib.pyplot as plt


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    passed = df[df["FinalResult"] == 1]
    failed = df[df["FinalResult"] == 0]

    plt.scatter(passed["StudyHours"], passed["PreviousScore"], label="Pass")
    plt.scatter(failed["StudyHours"], failed["PreviousScore"], label="Fail")

    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")
    plt.title("StudyHours vs PreviousScore")
    plt.legend()
    plt.show()
if __name__ =="__main__":
    main()