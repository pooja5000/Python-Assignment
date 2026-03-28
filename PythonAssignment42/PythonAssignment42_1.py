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




    




if __name__=="__main__":
    main()
