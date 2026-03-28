# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
#  Is the dataset balanced? Justify your answer.

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
    print(border)

    # Count how many students Failed (FinalResult = 0)
    failed_student=(data['FinalResult']==0).sum()
    print("No of failed student:",failed_student)
    print(border)

    # Average StudyHours
    AvgStudyHrs=(data['StudyHours']).mean()
    print("Average study hours of student:",AvgStudyHrs)
    print(border)

    # Average Attendance
    AvgAttendence=(data['Attendance']).mean()
    print("Average attendance of student:",AvgAttendence)
    print(border)

    # Maximum Previous Score
    MaxPreviousScore=(data['PreviousScore']).max()
    print("Maximum previous score is:",MaxPreviousScore)
    print(border)

    # Minimum Sleep Hours
    MinSleepHours=(data['SleepHours']).min()
    print("Minimum sleep hours:",MinSleepHours)
    print(border)

    #Use value_counts() to analyze the distribution of FinalResult.
    result_count=data["FinalResult"].value_counts()
    print("Distribution of result",result_count)
    print(border)

    # Calculate the percentage of Pass and Fail students.
    pecPassedStudent=(pass_student/data.shape[0])*100
    print("Percentage of passed student:",pecPassedStudent)
    print(border)

    pecFailedStudent=(failed_student/data.shape[0])*100
    print("Percentage of failed student:",pecFailedStudent)
    print(border)
    

if __name__=="__main__":
    main()