
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

def main():
  
  #load the data

  data=pd.read_csv("Advertising.csv",index_col=0)  
  print(data.columns)

  print(data.head())

  #Train data

  X=data.drop("sales",axis=1)
  y=data["sales"]

  print(X.shape,"And",y.shape)

  X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.5,random_state=42)
  model=LinearRegression()
  model.fit(X_train,y_train)

  #get slope and interceot
  slope=model.coef_
  intercept=model.intercept_

  print("Slope:",slope)
  print("Intercept:",intercept)
  
  #Test the data

  y_pred=model.predict(X_test)
  
  for i in range(5):
    print("Actual:",y_test.iloc[i],"Predicted:",round(y_pred[i],2))

  R2=r2_score(y_pred,y_test)

  print("R2 square is:",R2)

if __name__=="__main__":
    main()