import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    Border = "-"*40

    #--------------------------------------------------
    # Step 1 : Load the dataset from CSV file
    #--------------------------------------------------

    print(Border)
    print(" Step 1 : Load the dataset from CSV file")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Some entries from dataset")
    print(df.head())
    print(Border)

    #--------------------------------------------------
    # Step 2 : Clean the dataset by removing empty rows
    #--------------------------------------------------

    print(Border)
    print(" Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace = True)
    print("Total records: ",df.shape[0])
    print("Total columns: ",df.shape[1])
    print(Border)

    #--------------------------------------------------
    # Step 3 : Separate Independent and Dependent variables
    #--------------------------------------------------

    print(Border)
    print(" Step 3 : Separate Independent and Dependent variables")
    print(Border)

    X = df.drop(columns=['Class'])
    Y= df['Class']

    print("Shape of X: ",X.shape)
    print("Shape of Y: ",Y.shape)

    print(Border)
    print("Input columns: ",X.columns.tolist())
    print("Output column : Class")

    #--------------------------------------------------
    # Step 4 : Split the dataset for training and testing
    #--------------------------------------------------

    print(Border)
    print(" Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)

    print(Border)
    print("Information of training and testing data")
    print("X_train shape: ",X_train.shape)
    print("X_test shape: ",X_test.shape)
    print("Y_train shape: ",Y_train.shape)
    print("Y_test shape: ",Y_test.shape)

    #--------------------------------------------------
    # Step 5 : Feature Scaling
    #--------------------------------------------------

    print(Border)
    print(" Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()
    
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)
    
    print("Feature scaling is done")

    #--------------------------------------------------
    # Step 6 : Explore the multiple values of k
    #--------------------------------------------------

    print(Border)
    print(" Step 6 : Explore the multiple values of k")
    print(Border)

    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train_scaled, Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test, Y_pred)
        accuracy_scores.append(accuracy)

    print(Border)
    print("Accuracy report of all k values from 1 to 20")
    for value in accuracy_scores:
        print(value)

    print(Border)

    #--------------------------------------------------
    # Step 7 : Find best value of K
    #--------------------------------------------------

    print(Border)
    print(" Step 7 : Find best value of K")
    print(Border)

    best_k = list(K_values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is: ",best_k)

    #--------------------------------------------------
    # Step 8 : Build final model using best value of k
    #--------------------------------------------------

    print(Border)
    print(" Step 8 : Build final model using best value of k")
    print(Border)

    final_model = KNeighborsClassifier(n_neighbors=best_k)
    final_model.fit(X_train_scaled, Y_train)
    Y_pred = final_model.predict(X_test_scaled)

    #--------------------------------------------------
    # Step 9 : Calculate final accuracy
    #--------------------------------------------------

    print(Border)
    print(" Step 9 : Calculate final accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of model is: ",accuracy*100)

def main():
    Border = "-"*40
    print(Border)
    print("Wine Classifier Using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()