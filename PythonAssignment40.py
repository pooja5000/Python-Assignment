from sklearn.tree import DecisionTreeClassifier,plot_tree
import pandas as pd

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import numpy as np

def main():

    print("-"*70)

    #model=DecisionTreeClassifier(max_depth=1) Accuraccy of model is: 75.0

    #model=DecisionTreeClassifier(max_depth=3) Accuraccy of model is: 80.0

    #Create model
    model=DecisionTreeClassifier(max_depth=None) #Accuraccy of model is: 75.0

    #load the data
    data=pd.read_csv("student_performance_ml.csv")

    print(data.head())

    X=data.drop("FinalResult",axis=1)
    y=data["FinalResult"]

   

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=20,random_state=42)

    model.fit(X_train,y_train)
    print("Data training done")

    y_pred=model.predict(X_test)
    result=pd.DataFrame({
        "Actual values":y_test,
        "Predicted values":y_pred
    })

    print("Actual data vs predicted data")
    print(result)

    
    plt.figure(figsize=(15,10))
    
    plot_tree(model,filled=True,feature_names=X.columns,class_names=[str(cls) for cls in model.classes_],rounded=True)
    plt.show()

    Accuracy_score_all_features=accuracy_score(y_test,y_pred)

    print("Accuraccy of model is:",Accuracy_score_all_features*100)

    cm=confusion_matrix(y_test,y_pred)
    print("Confusion Matrix")
    print(cm)

    Train_Accuraccy=model.score(X_train,y_train)
    print("Training Accuraccy:",Train_Accuraccy*100)

    Test_Accuraccy=model.score(X_test,y_test)
    print("Testing Accuraccy:",Test_Accuraccy*100)

    student_data=pd.DataFrame({
        "StudyHours":[6],
        "Attendance":[85],
        "PreviousScore":[66],
        "AssignmentsCompleted":[7],
        "SleepHours":[7]
    })

    predicted_data=model.predict(student_data)

    print("Final result for student will be:",predicted_data)
    print("-"*70)

    #Display importance score of each feature
    importamce=model.feature_importances_

    feature_importance=pd.DataFrame({
        "Feature":X.columns,
        "Importance":importamce 
    }).sort_values(by="Importance",ascending=False)

    print(feature_importance)

    #Feature that contributes the most

    print("Feature that contributes the most:")
    print(feature_importance.iloc[0])

    #Feature that contributes the least

    print("Feature that contributes the least:")
    print(feature_importance.iloc[-1])

    print("-"*70)

    #Remove the SleepHours column

    X_new=X.drop(columns=["StudyHours"])

    #2. Train the Decision Tree model again

    X_train,X_test,y_train,y_test=train_test_split(X_new,y,test_size=0.2,random_state=42)

    Model_new=DecisionTreeClassifier(random_state=42)

    Model_new.fit(X_train,y_train)

    y_pred_new=Model_new.predict(X_test)

    New_accurcy=accuracy_score(y_test,y_pred_new)
    print("New accurccy:")
    print(New_accurcy*100)

    print("Original all features accuraccy:",Accuracy_score_all_features*100)
    print("New accurccy without Study Hours:",New_accurcy*100)

    print("-"*70)

    #Train the model using only StudyHours and Attendance

    X_Two=X[["StudyHours","Attendance"]]
    X_train,X_test,y_train,y_test=train_test_split(X_Two,y,test_size=0.2,random_state=42)
    Model_Two=DecisionTreeClassifier(random_state=42)

    Model_Two.fit(X_train,y_train)
    y_pred_two=Model_Two.predict(X_test)

    Accurccy_Two=accuracy_score(y_test,y_pred_two)

    print("Accurccy with Two features StudyHours,Attendance: ",Accurccy_Two*100)

    print("Original all features accuraccy:",Accuracy_score_all_features*100)

    print("-"*70)
    
#     # Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their results.
# Display predictions clearly.

    new_student=pd.DataFrame({
    "StudyHours":[6, 4, 8, 5, 7],
        "Attendance":[85, 70, 92, 75, 88],
        "PreviousScore":[66, 55, 81, 60, 72],
        "AssignmentsCompleted":[7, 5, 9, 6, 8],
        "SleepHours":[7, 6, 8, 5, 7]
    })

    new_student_pred=model.predict(new_student)
    #Without using accuracy_score, manually calculate accuracy:
    new_Y=[1,0,1,1,1]

    correct=np.sum(new_student_pred==new_Y)
    accuraccy=correct/len(new_Y)
    print("Accuraccy of new student data is:",accuraccy)
    print(new_student_pred)

    #Identify students where:
# y_test != y_pred
# Display those rows.
# How many students were misclassified?
# What common pattern do you observe?
    missclssified=result[result["Actual values"]!=result["Predicted values"]]
    print("Missclassified records:",missclssified)

#     Train model using:
# random_state = 0
# random_state = 10
# random_state = 42
# Compare testing accuracy.
# Does the result change?

    random_state=[0,10,42]

    for rs in random_state:
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=rs)

        model.fit(X_train,y_train)

        Y_pred=model.predict(X_test)

        accuraccy=accuracy_score(Y_pred,y_test)

        print("Accuraccy of random_state=",rs,":",accuraccy)

        # visualize a trained decision tree

    plt.figure(figsize=(20,10))
    plot_tree(model,filled=True,feature_names=X.columns,class_names=True,rounded=True)
    plt.show()

    # Create new column and train the model
    X["Performance"]=(X["StudyHours"]*2+X["Attendance"])

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    model.fit(X_train,y_train)
    Y_NewColumn_Pred=model.predict(X_test)

    New_accurcy=accuracy_score(Y_NewColumn_Pred,y_test)
    print("New accuraccy after adding new column:",New_accurcy)
    


if __name__=="__main__":
    main()