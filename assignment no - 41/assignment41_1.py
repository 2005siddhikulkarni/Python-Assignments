import numpy as np
import math

def User_EuclideanDistance(P1,P2):
    Result = math.sqrt(((P1["X"] - P2["X"])**2) + ((P1["Y"] - P2["Y"])**2))
    return Result

def User_KNN():
    data = [{"Point" : "A" , "X" : 1 , "Y" : 2 , "label" : "Red"},
            {"Point" : "B" , "X" : 2 , "Y" : 3 , "label" : "Red"},
            {"Point" : "C" , "X" : 3 , "Y" : 1 , "label" : "Blue"},
            {"Point" : "D" , "X" : 6 , "Y" : 5 , "label" : "Blue"}
    ]

    for i in data :
        print(i)

    New_pnt = {"X" : int(input("Enter X coordinate: ")),"Y" : int(input("Enter Y coordinate : "))} 
    print(New_pnt)

    for d in data:
        d["distance"] = User_EuclideanDistance(d,New_pnt)

    for d in data:
        print(d)

    sorted_data = sorted(data, key = lambda item : item ["distance"])

    k = 3
    nearest = sorted_data[:k]

    print("Nearest elements are: ")
    for i in nearest:
        print(i)

    votes = {}
    for neighbour in nearest:
        label = neighbour["label"]
        votes[label] = votes.get(label,0)+1

    for d in votes:
        print("Name:",d,"No of votes: ",votes[d])

    predicted_class = max(votes, key = votes.get)
    print("Predicted class: ",predicted_class)

def main():
    User_KNN()

if __name__ == "__main__":
    main()