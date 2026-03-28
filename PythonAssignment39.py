from sklearn.tree import DecisionTreeClassifier,plot_tree
import pandas as pd

from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

def main():

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

    Accuracy_score=accuracy_score(y_test,y_pred)

    print("Accuraccy of model is:",Accuracy_score*100)

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
    

    

if __name__=="__main__":
    main()