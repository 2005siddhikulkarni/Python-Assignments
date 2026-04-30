import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report

def main():
    X = np.array([
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 1500, 5, 6, 10],
        [28, 600, 18, 1, 1],
        [35, 800, 30, 0, 0],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 6, 7]
    ])

    Y = np.array([0,0,1,1,0,0,1,1,0,1])

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
        hidden_layer_sizes=(5,),
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

    new_student = np.array([[46, 1450, 5, 6, 9]])
    print("New student for prediction : ",new_student)

    new_student_scaled = scaler.transform(new_student)

    prediction = model.predict(new_student_scaled)

    if(prediction[0] == 1):
        print("Customer will leave")

    else:
        print("Customer will stay")

if __name__ == "__main__":
    main()
