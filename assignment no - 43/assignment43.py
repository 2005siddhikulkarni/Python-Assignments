import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def CheckAccuracy(X,Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape: ",X_train.shape)
    print("X_test shape: ",X_test.shape)
    print("Y_train shape: ",Y_train.shape)
    print("Y_test shape: ",Y_test.shape)

    accuracies = []
    K_values = range(1,20)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)
        accuracies.append(accuracy)

    print("Printing accuracies for the values of k from 1 to 20")
    for value in accuracies:
        print(value)


def UserDefinedLogisticRegression(DataPath):
    Border = "-"*40

    #----------------------------------------------------
    # Step 1 : Get Data
    #----------------------------------------------------

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print(df.shape)

    print(df.head())

    #----------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #----------------------------------------------------

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate data")
    print(Border)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'], inplace = True)

    print(df.shape)

    Encoder = LabelEncoder()

    df["Whether"]= Encoder.fit_transform(df["Whether"])

    df["Temperature"]= Encoder.fit_transform(df["Temperature"])

    df["Play"]= Encoder.fit_transform(df["Play"])
    
    print("Encoded dataste: ")
    print("For Whether: ")
    print("0 -> Overcast")
    print("1 -> Rainy")
    print("2 -> Sunny")

    print(Border)
    print("For Temperature: ")
    print("0 -> Cool")
    print("1 -> Hot")
    print("2 -> Mild")

    print(Border)
    print("For label/Play: ")
    print("0 -> No")
    print("1 -> Yes")
    print(Border)

    print(df)

    print(Border)
    print(Border)

    X = df[["Whether", "Temperature"]]
    Y = df["Play"]

    print("Independent Variables/Features: ",X.shape)
    print("Dependent Variables/Labels: ",Y.shape)

    #----------------------------------------------------
    # Step 3 : Train data
    #----------------------------------------------------

    print(Border)
    print("Step 3 : Train data")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)

    #----------------------------------------------------
    # Step 4 : Test data
    #----------------------------------------------------

    print(Border)
    print("Step 4 : Test data")
    print(Border)

    Test_data = {"Whether": int(input("Enter the weather for testing: ")), "Temperature": int(input("Enter the temperature for testing: "))}

    Result = model.predict([[Test_data["Whether"], Test_data["Temperature"]]])

    if Result == 1:
        print("Yes")
    else:
        print("No")

    #----------------------------------------------------
    # Step 5 : Calculate Accuracy
    #----------------------------------------------------

    print(Border)
    print(" Step 5 : Calculate Accuracy")
    print(Border)

    CheckAccuracy(X, Y) 

def main():
    UserDefinedLogisticRegression("PlayPredictor.csv")

if __name__ == "__main__":
    main()