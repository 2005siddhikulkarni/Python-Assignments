import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    X = np.array([
        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 10000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 15000, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ])

    Y = np.array([0,1,1,0,1,1,0,1,0,1])

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    X_train,X_test,Y_train,Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=42)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    model = MLPClassifier(
        hidden_layer_sizes=(7,9,),
        activation="relu",
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train,Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of the testing is : ",Accuracy * 100)

    print("Classification Report : ")
    print(classification_report(Y_test,Y_pred))

    new_applicant = np.array([[55000, 720, 400000, 10000, 1]])
    print("New student for prediction : ",new_applicant)
    
    new_applicant_scaled = scaler.transform(new_applicant)

    prediction = model.predict(new_applicant_scaled)

    if(prediction[0] == 1):
        print("Loan Approved")

    else:
        print("Loan Rejected")

if __name__ == "__main__":
    main()
