import pandas as pd
import matplotlib.pyplot as plt


def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    plt.boxplot(df["Attendance"])
    plt.show()
    
if __name__ =="__main__":
    main()