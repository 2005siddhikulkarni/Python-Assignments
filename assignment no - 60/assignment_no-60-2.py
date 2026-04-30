import numpy as np
import matplotlib.pyplot as plt

def ReLU(X):
    return np.maximum(0,X)

def Sigmoid(X):

    return 1 / (1 + np.exp(-X))

def Tanh(X):

    return np.tanh(X)

def main():
    inputs = np.linspace(-10,10,100)

    output_ReLU = ReLU(inputs)
    output_Sigmoid = Sigmoid(inputs)
    output_Tanh = Tanh(inputs)

    plt.plot(inputs,output_ReLU,label = "ReLU") 
    plt.plot(inputs,output_Sigmoid,label = "Sigmoid") 
    plt.plot(inputs,output_Tanh,label = "Tanh")

    plt.title("Activation Functions")
    plt.xlabel("Inputs")
    plt.ylabel("Outputs") 
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()