# 2. Write a program to:
# Display total number of students in the dataset
# Count how many students Passed (FinalResult = 1)
# Count how many students Failed (FinalResult = 0)

import pandas as pd
import numpy as np

def main():
    border="-"*40

    #load the data from csv
    data=pd.read_csv("student_performance_ml.csv")

    print(border)

    #Display the first 5 records
    print(data.head())

    print(border)
    #Display the last 5 records
    print(data.tail())
    print(border)

    # Total number of rows and columns
    print("No of columns and rows in dataset",data.shape)
    print(border)

    # List of column names
    print("List of columns:",list(data.columns))
    print(border)

    # Data types of each column
    
    for column in list(data.columns):
        print("Data types of ",column,":",data[column].dtype)
    print(border)

    # Display total number of students in the dataset
    print("Total no of student:",data.shape[0])
    print(border)

    # Count how many students Passed (FinalResult = 1)
    pass_student=(data['FinalResult']==1).sum()
    print("No of passed student:",pass_student)

    # Count how many students Failed (FinalResult = 0)
    failed_student=(data['FinalResult']==0).sum()
    print("No of passed student:",failed_student)

    

if __name__=="__main__":
    main()