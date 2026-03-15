def main():
    actual = [1,1,1,1,0,0,0,0]
    predicted = [1,1,0,1,0,1,0,0]

    TP=TN=FP=FN=0

    for i in range(len(actual)):

        if actual[i]==1 and predicted[i]==1:
            TP+=1

        elif actual[i]==0 and predicted[i]==0:
            TN+=1

        elif actual[i]==0 and predicted[i]==1:
            FP+=1

        elif actual[i]==1 and predicted[i]==0:
            FN+=1

    print("True Positive:",TP)
    print("True Negative:",TN)
    print("False Positive:",FP)
    print("False Negative:",FN)

if __name__ == "__main__":
    main()