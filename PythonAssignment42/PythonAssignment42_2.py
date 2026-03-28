import math

def main():
    # Dataset
    X = [1, 2, 3, 4, 5]
    y = [3, 4, 2, 4, 5]

    # Calculte X mean and Y mean

    x_mean=float(sum(X)/len(X))
    print("Mean of X is :",x_mean)

    y_mean=float(sum(y)/len(y))
    print("Mean of Y is :",y_mean)

    #Slope(m)

    numerator=sum((X[i]-x_mean)*(y[i]-y_mean) for i in range(len(X)))
    dinominator=sum((X[i]-x_mean)**2 for i in range(len(X)))

    m=numerator/dinominator

    print("The slope of m:",m)

    #Intercept(c)

    c=y_mean-(x_mean*m)
    print("Intercept is:",c)

    #Predicted values 

    y_pred=[m*X[i]+c for i in range(len(X))]
    print("Predicted Y:",y_pred)

    #Mean squared error

    MSE=sum((y[i]-y_pred[i])**2 for i in range(len(X)))
    print("Mean squared error:",MSE)

    #R2 sqaure

    ss_res=sum((y[i]-y_pred[i])**2 for i in range(len(y)))
    ss_tot=sum((y[i]-y_mean)**2 for i in range(len(X)))

    R2=1-(ss_res/ss_tot)

    print("R2 square is:",R2)








    




if __name__=="__main__":
    main()
