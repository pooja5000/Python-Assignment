
import matplotlib.pyplot as plt

def main():

     # Dataset
    X_experience = [1, 2, 3, 4, 5]
    y_Salary = [20000, 25000, 30000, 35000, 40000]
    n=len(X_experience)

    #X-mean and Y-mean

    x_mean=sum(X_experience)/n
    print("Mean of experience:",X_experience)

    y_mean=sum(y_Salary)/n
    print("Mean of Salary:",y_mean)

    #slope(m)

    numerator=sum((X_experience[i]-x_mean)*(y_Salary[i]-y_mean) for i in range(n))
    dinominator=sum((X_experience[i]-x_mean)**2 for i in range(n))
    m=numerator/dinominator
    print("Slope is:",m)

    #intercept

    c=y_mean-(x_mean*m)
    print("Intercept is :",c)

    #new value predicted

    new_X=6

    new_pred=m*new_X+c

    print("Predicted salary is for 6 years of experience:",new_pred)

    plt.scatter(X_experience,y_Salary,color='blue',label="Actual data")
    plt.plot(X_experience,y_Salary,color='red',label="linear regression")

    plt.xlabel("Experience in years")
    plt.ylabel("Salary")
    plt.title("Linear regression")
    plt.legend()
    plt.grid(True)

    plt.show()


    







    


if __name__=="__main__":
    main()