import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

def main():

    #load the data
    data=pd.read_csv("WinePredictor.csv")
    print(data.head())
    print(data.shape)

    X=data.drop("Class",axis=1)
    y=data["Class"]

    X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.8,random_state=42)

    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.fit_transform(X_test)

    #train the model
    lr=LogisticRegression(max_iter=1000)
    lr.fit(X_train_scaled,y_train)

    #test the model
    y_pred=lr.predict(X_test_scaled)

    print("Accuraccy:",accuracy_score(y_test,y_pred))
    print("Confusion matrix:\n",confusion_matrix(y_test,y_pred))
    print("Classification report:\n",classification_report(y_test,y_pred))






    


if __name__=="__main__":
    main()