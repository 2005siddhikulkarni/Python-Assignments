import numpy as np
import math

def Calc_MSE(Actual, Predicted):
    
    n = len(Actual)
    tot_error = 0

    for i in range(n):
        error = Actual[i] - Predicted[i]
        tot_error += error ** 2

    MSE = tot_error / n
    return MSE

def calc_BinaryCrossEntropy(Actual, Predicted):
    
    n = len(Actual)
    total_loss = 0

    for i in range(n):
        y = Actual[i]
        p = Predicted[i]

        # Avoid log(0)
        p = max(min(p, 0.999), 0.001)

        loss = -(y * math.log(p) + (1 - y) * math.log(1 - p))
        total_loss += loss

    return total_loss / n

def  main():

    Actual = np.array([12,10,18])
    Predicted = np.array([15,7,20])

    print("Actual Values : ",Actual)
    print("Predicted Values : ",Predicted)

    loss_1 = Calc_MSE(Actual,Predicted)
    print("Mean Squared Error (MSE Loss) : ",loss_1)

    loss_2 = calc_BinaryCrossEntropy(Actual,Predicted)
    print("Binary Cross Entropy (Loss) : ",loss_2)

if __name__ == "__main__":
    main()