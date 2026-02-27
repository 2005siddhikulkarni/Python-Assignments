import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Path = "student_performance_ml.csv"
    df = pd.read_csv(Path)
    print("The CSV file loaded successfully....")
    
    sns.boxplot(x=df["FinalResult"],y=df["SleepHours"])
    plt.show()

    #The boxplot shows that passed students generally sleep more (around 7–8 hours) compared to failed students (around 5–6 hours). This suggests that adequate sleep may positively influence academic performance.
if __name__ =="__main__":
    main()