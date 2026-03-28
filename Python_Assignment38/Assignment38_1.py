#1. Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
# First 5 records
# Last 5 records
# Total number of rows and columns
# List of column names
# Data types of each column

import pandas as pd

def main():

    #load the data from csv
    data=pd.read_csv("student_performance_ml.csv")

    #Display the first 5 records
    print(data.head())

    #Display the last 5 records
    print(data.tail())

    # Total number of rows and columns
    print("No of columns and rows in dataset",data.shape)

    # List of column names
    print("List of columns:",list(data.columns))

    # Data types of each column
    
    for column in list(data.columns):
        print("Data types of ",column,":",data[column].dtype)

    

if __name__=="__main__":
    main()