import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    n = len(X)

    mean_x = sum(X)/n
    mean_y = sum(Y)/n

    num = 0
    den = 0

    for i in range(n):
        num += (X[i]-mean_x)*(Y[i]-mean_y)
        den += (X[i]-mean_x)**2

    m = num/den
    c = mean_y - m*mean_x

    print("Slope:",m)
    print("Intercept:",c)

    predicted = []

    for x in X:
        predicted.append(m*x + c)

    salary6 = m*6 + c
    print("Predicted salary for 6 years:",salary6)

    plt.scatter(X,Y)
    plt.plot(X,predicted)
    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Salary Prediction using Linear Regression")
    plt.show()

if __name__ == "__main__":
    main()