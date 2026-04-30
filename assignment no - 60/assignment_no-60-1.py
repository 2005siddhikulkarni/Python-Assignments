import math
import numpy as np

def sigmoid(z):

    return 1 / (1 + math.exp(-z))

def Single_Neuron(inputs, Weights,bias):

    print("Inputs (X) : ",inputs)
    print("Weights (W) : ",Weights)
    print("Bias (b) : ",bias)

    weighted_sum = np.dot(inputs, Weights) + bias

    print("Weighted Sum (z) : ",weighted_sum)

    output = sigmoid(weighted_sum)

    print("Sigmoid output: ",output)
    
    if(output < 0.5):
        print("Sigmoid output is closer to 0")

    else:
        print("Sigmoid output is closer to 1")

def main():
    inputs = np.array([2, 3])

    Weights = np.array([0.4, 0.6])

    bias = 0.5

    Single_Neuron(inputs, Weights, bias)

if __name__ == "__main__":
    main()

