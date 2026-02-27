import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
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

    Y_pred= model.predict(X_test)
    print("MOdel testing completed")

    
    print("Expected answers: ")
    print(Y_test)

    print("Predicted answers: ")
    print(Y_pred)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is: ",accuracy*100)

    cm = confusion_matrix(Y_test,Y_pred)

    print("Confusion matrix : ")
    print(cm)

    train_pred  = model.predict(X_train)
    Train_acc = accuracy_score(Y_train,train_pred)
    print("The training accuracy is: ",Train_acc*100)

    test_pred  = model.predict(X_test)
    Test_acc = accuracy_score(Y_test,test_pred)
    print("The testing accuracy is: ",Test_acc*100)

    # when we change max_depth into 1,3,None it is showing testing accuracies every time 100%

    


if __name__ == "__main__":
    main()