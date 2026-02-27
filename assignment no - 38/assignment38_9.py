import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    sns.boxplot(x=df["AssignmentsCompleted"],y=df["FinalResult"])
    plt.show()
if __name__ =="__main__":
    main()