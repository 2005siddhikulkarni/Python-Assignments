from sklearn.preprocessing import StandardScaler

def main():
    Data =[
        [25,20000],
        [30,40000],
        [35,80000]
    ]
    print("The original dataset is: ")
    print(Data)

    scaler = StandardScaler()
    Scaled_data = scaler.fit_transform(Data)

    print("The scaled dataset is: ")
    print(Scaled_data)

if __name__ == "__main__":
    main()