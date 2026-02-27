import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)
Border = "-"*40
#####################################################################################

# Step 1 : Load the Dataset

#####################################################################################
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "Student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset gets loaded successfully...")
print("Initial entries from dataset :")
print(df.head())

#####################################################################################

# Step 2 : Data Analysis (EDA)

#####################################################################################
print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))

print("Missing Values (Per column): ")
print(df.isnull().sum())

print("Class Distribution (FinalResult count)")
print(df["FinalResult"].value_counts())

print("Statistial Report of Dataset")
print(df.describe())

#####################################################################################

# Step 3 : Decide Independent and Dependent Variables

#####################################################################################
print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

# X : Independent Variables / Features
# Y : Dependent Variables / Labels

feature_calls = [
   "StudyHours", 
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
    ]
X = df[feature_calls]
Y = df["FinalResult"]
print(" X shape : ",X.shape)
print(" Y shape : ",Y.shape)

#####################################################################################

# Step 4 : Visualization of Dataset

#####################################################################################
print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

# Scatter plot
plt.figure(figsize=(7,5))

for FR in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == FR]
    plt.scatter(temp["StudyHours"], temp["Attendance"], label = FR)

plt.title("Student_performance_ml")
plt.xlabel("StudyHours")
plt.ylabel("Attendance")

plt.legend()
plt.grid(True)
plt.show()

#####################################################################################

# Step 5 : Split the Dataset for Training and Testing

#####################################################################################
print(Border)
print("Step 5 : Split the Dataset for Training and Testing")
print(Border)

# Test size = 20%
# Train size = 80%

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size = 0.5,
    random_state = 42
)

print("Data splitting activity done : ")

print("X - Independent : ",X.shape)   # (150,4)
print("Y - Dependent: ",Y.shape)      # (150,)

print("X_train : ",X_train.shape)     # (120,4)
print("X_test : ",X_test.shape)       # (30,4)

print("Y_train : ",Y_train.shape)     # (120,)
print("Y_test: ",Y_test.shape)        # (30,)

#####################################################################################

# Step 6 : Build the Model

#####################################################################################
print(Border)
print("Step 6 : Build the Model")
print(Border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(
    criterion = "gini",
    max_depth = 5,
    random_state = 42

)

print("Model successfully created : ",model)

#####################################################################################

# Step 7 : Train the Model

#####################################################################################
print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train,Y_train)

print("Model training completed")

#####################################################################################

# Step 8 : Test / Evaluate the Model

#####################################################################################
print(Border)
print("Step 8 : Test / Evaluate the Model")
print(Border)

Y_pred = model.predict(X_test)

print("Model evaluation (testing) complete")

print(Y_pred.shape)

print("Expected answers : ")
print(Y_test)

print("Predicted answers : ")
print(Y_pred)

#####################################################################################

# Step 9 : Test / Evaluate the Model performance

#####################################################################################
print(Border)
print("Step 9 : Test / Evaluate the Model performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is: ",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix : ")
print(cm)

print("Classification Report")
print(classification_report(Y_test,Y_pred))

#####################################################################################

# Step 10 : Plot the confusion matrix

#####################################################################################
print(Border)
print("Step 10 : Plot the confusion matrix")
print(Border)

data = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=model.classes_)
data.plot()

plt.title("Confusion matrix of Iris dataset")
plt.show()











