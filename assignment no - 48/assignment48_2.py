import numpy as np

def main():
    Data = [6,7,8,9,10,11,12]
    print("The dataset is: ",Data)

    Result1 = np.var(Data)
    print("Variance of dataset is: ",Result1)

    Result2 = np.std(Data)
    print("The standard deviation of dataset is: ",Result2)


if __name__ == "__main__":
    main()