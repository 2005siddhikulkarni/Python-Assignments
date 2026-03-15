from sklearn.metrics import classification_report

def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    Report = classification_report(actual,predicted)

    print("\n The classification report is: ")
    print(Report) 

if __name__ == "__main__":
    main()