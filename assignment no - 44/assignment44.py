import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

def MarvellousAdvertise(DataPath):
    Border = "-"*40
    #----------------------------------------------------------------
    # Step 1 : Get Data
    #----------------------------------------------------------------

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Few records from the dataset: ",df.head())

    #----------------------------------------------------------------
    # Step 2 : Clean, Prepare and Manipulate data
    #----------------------------------------------------------------

    print(Border)
    print("Step 2 :  Clean, Prepare and Manipulate data")
    print(Border)

    print("Shape of dataset before removal: ",df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace =True)

    print("Shape of dataset after  removal: ",df.shape)

    print(Border)
    print("Clean dataset is: ")
    print(Border)

    print(df.head())

    print("Missing values count: \n",df.isnull().sum())

    X = df[['TV','radio','newspaper']]
    Y = df['sales']

    print("Shape of Independent variables: ",X.shape)
    print("Shape of Dependent variables: ",Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X_train shape: ",X_train.shape)
    print("X_test shape: ",X_test.shape)
    print("Y_train shape: ",Y_train.shape)
    print("Y_test shape: ",Y_test.shape)

    #----------------------------------------------------------------
    # Step 3 : Train Data
    #----------------------------------------------------------------

    print(Border)
    print("Step 3 : Train Data")
    print(Border)

    model = LinearRegression()

    model.fit(X_train, Y_train)

    #----------------------------------------------------------------
    # Step 4 : Test the data
    #----------------------------------------------------------------

    print(Border)
    print("Step 4 : Test the data")
    print(Border)

    Y_pred = model.predict(X_test)

    #----------------------------------------------------------------
    # Step 5 : Display the actual and predicted values
    #----------------------------------------------------------------

    print(Border)
    print("Step 5 : Display the actual and predicted values")
    print(Border)

    Result = pd.DataFrame({
        'Actual sale' : Y_test.values,
        'predicted sale' : Y_pred
        })
    
    print(Result.head())













def main():
    MarvellousAdvertise("Advertising.csv")
    

if __name__ == "__main__":
    main()