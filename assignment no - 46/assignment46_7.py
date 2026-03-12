
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    Border = "-"*40

    #------------------------------------------------
    # Step 1 : Get Data
    #------------------------------------------------

    print(Border)
    print(" Step 1: Get Data")
    print(Border)

    StudyHours = [[1],[2],[3],[4],[5]]
    Marks = [50,55,60,65,70]

    print("Independent variables/features are : StudyHours")
    print("Dependent variables/features are : StudyHours")

    #------------------------------------------------
    # Step 2 : Split the dataset into X and Y
    #------------------------------------------------

    print(Border)
    print(" Step 2 : Split the dataset into X and Y")
    print(Border)

    X = StudyHours
    Y = Marks
    #------------------------------------------------
    # Step 3 : Split the dataset for training and testing
    #------------------------------------------------

    print(Border)
    print(" Step 3 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    print("training dataste: ",X_train,X_test)
    print("testing dataset: ",X_test)

    #------------------------------------------------
    # Step 4 : Create and train the model
    #------------------------------------------------

    print(Border)
    print(" Step 4 : Create and train the model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    print("Model created and trained successfully...")

    #------------------------------------------------
    # Step 5 : test the model
    #------------------------------------------------

    print(Border)
    print("  Step 5 : test the model")
    print(Border)

    Y_pred = model.predict(X_test)

    print("Predicted values: ")
    print(Y_pred)

    #------------------------------------------------
    # Step 6 : Calculate coefficient and intercept of the model
    #------------------------------------------------

    print(Border)
    print("Step 6 : Calculate coefficient and intercept of the model")
    print(Border)

    print("Coefficient: ",model.coef_)
    print("Intercept: ",model.intercept_)

if __name__ == "__main__":
    main()