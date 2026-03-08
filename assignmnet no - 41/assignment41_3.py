import numpy as np
import math

def User_EuclideanDistance(P1,P2):
    Result = math.sqrt(((P1["StudyHours"] - P2["StudyHours"])**2) + ((P1["Attendance"] - P2["Attendance"])**2))
    return Result

def User_KNN():
    data = [{"Point" : "A" , "StudyHours" : 2 , "Attendance" : 60 , "Result" : "Fail"},
            {"Point" : "B" , "StudyHours" : 5 , "Attendance" : 80 , "Result" : "Pass"},
            {"Point" : "C" , "StudyHours" : 6 , "Attendance" : 85 , "Result" : "Pass"},
            {"Point" : "D" , "StudyHours" : 1 , "Attendance" : 50 , "Result" : "Fail"}
    ]

    for i in data :
        print(i)

    New_pnt = {"StudyHours" : int(input("Enter Study Hours : ")),"Attendance" : int(input("Enter Attendance : "))} 
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
        Result = neighbour["Result"]
        votes[Result] = votes.get(Result,0)+1

    for d in votes:
        print("Name:",d,"No of votes: ",votes[d])

    predicted_class = max(votes, key = votes.get)
    print("Predicted class: ",predicted_class)

def main():
    User_KNN()

if __name__ == "__main__":
    main()