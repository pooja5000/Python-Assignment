from sklearn.preprocessing import LabelEncoder
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
  
  #load the data

  data=pd.read_csv("Marvellous_Infosystem_PlayPredictor.csv",index_col=0)  
  print(data.columns)

  #Encoding the data for preprocessing
  le=LabelEncoder()

  data["Whether"]=le.fit_transform(data["Whether"])
  data["Temperature"]=le.fit_transform(data["Temperature"])
  print(data.head())

  #Train data

  X=data.drop("Play",axis=1)
  y=data["Play"]

  print(X.shape,"And",y.shape)

  model=KNeighborsClassifier(n_neighbors=2)
  model.fit(X,y)
  
  #Test the data

  sample=pd.DataFrame([[1,2]],columns=X.columns)
  y_pred=model.predict(sample)
  print("predicted result:",y_pred)

  #calculate accuraccy by spliting data for testing and traini 50-50
  X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.5,random_state=42)

  model.fit(X_train,y_train)
  y_pred=model.predict(X_test)

  accuraccy=accuracy_score(y_test,y_pred)
  print("Accuraccy is:",accuraccy)







if __name__=="__main__":
    main()