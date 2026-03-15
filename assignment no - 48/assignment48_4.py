from sklearn.preprocessing import StandardScaler
import math

def main():
    point1 = [30,40]
    point2 = [25,45]

    print("Euclidean distance before scaling")

    Euc_dis1 = math.sqrt(((point2[0] - point1[0])**2)+ ((point2[1] - point1[1])**2))
    print("Euclidean distance before scaling is: ",Euc_dis1)

    print("Euclidean distance after scaling")

    Data = [
        [30,40],
        [25,45]
    ]

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(Data)
    print("The dataset after scaling is: ")
    print(scaled_data)

    scaled_pnt1 = scaled_data[0]
    scaled_pnt2 = scaled_data[1]

    Euc_dis2 = math.sqrt(((scaled_pnt2[0] - scaled_pnt1[0])**2) + (scaled_pnt2[1] - scaled_pnt1[1])**2)
    print("Eucidean distance after scaling is: ",Euc_dis2)

if __name__ == "__main__":
    main()