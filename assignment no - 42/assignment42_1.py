

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    n = len(X)

    mean_x = sum(X)/n
    mean_y = sum(Y)/n

    print("Mean of X:",mean_x)
    print("Mean of Y:",mean_y)

    num = 0
    den = 0

    for i in range(n):
        num += (X[i]-mean_x)*(Y[i]-mean_y)
        den += (X[i]-mean_x)**2

    m = num/den
    c = mean_y - m*mean_x

    print("Slope (m):",m)
    print("Intercept (c):",c)

    print("Regression Equation: Y =",m,"X +",c)

    x = 6
    y_pred = m*x + c

    print("Predicted Y for X=6:",y_pred)

if __name__ == "__main__":
    main()