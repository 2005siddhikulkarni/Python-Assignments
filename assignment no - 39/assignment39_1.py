import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():

    DatasetPath = "Student_performance_ml.csv"
    df = pd.read_csv(DatasetPath)
    print("CSV gets loaded successfully...")

    print("The shape of the dataset is: ",df.shape)
    print("The column names are : ",list(df.columns))

    print("Missing values (per cloumns) are: ")
    print(df.isnull().sum())

    print("Class distribution (final result count): ")
    print(df["FinalResult"].value_counts())

    print("The statistical report is : ")
    print(df.describe())

    feature_calls = [
    "StudyHours", 
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "FinalResult"
    ]
    X = df[feature_calls]
    Y = df["FinalResult"]

    print(" X shape : ",X.shape)
    print(" Y shape : ",Y.shape)

    X_train, X_test , Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size = 0.2,
        random_state = 42
    )

    print("We are going to use DecisionTreeClassifier")
    model = DecisionTreeClassifier(
        criterion = "gini",
        max_depth = 3,
        random_state = 42
    )

    print("Model created successfully",model)

    model.fit(X_train,Y_train)
    print("Model training completed")

if __name__ == "__main__":
    main()