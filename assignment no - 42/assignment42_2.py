import numpy as np

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    m = 0.4
    c = 2.4

    n = len(X)

    predicted = []

    print("Actual Y vs Predicted Y")

    for i in range(n):
        y_pred = m * X[i] + c
        predicted.append(y_pred)
        print("X =",X[i],"Actual Y =",Y[i],"Predicted Y =",y_pred)

    error_sum = 0

    for i in range(n):
        error = Y[i] - predicted[i]
        error_sq = error ** 2
        error_sum = error_sum + error_sq

    MSE = error_sum / n

    print("\nMean Squared Error (MSE) =",MSE)

    mean_y = sum(Y)/n

    ss_total = 0
    ss_res = 0

    for i in range(n):

        ss_total += (Y[i] - mean_y)**2
        ss_res += (Y[i] - predicted[i])**2

    R2 = 1 - (ss_res/ss_total)

    print("R2 Score =",R2)

if __name__ == "__main__":
        main()