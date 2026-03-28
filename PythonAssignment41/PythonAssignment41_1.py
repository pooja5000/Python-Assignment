from math import sqrt

def main():

    data=[
    (2, 60, 'Fail'),
    (5, 80, 'Pass'),
    (6, 85, 'Pass'),
    (1, 50, 'Fail')
    ]

    new_study=float(input("Enter new study hours:"))
    new_attendance=float(input("Enter new attendance:"))

    #calculate distance

    distance=[]

    for records in data:
        study_hours,attendance,result=records
        dist=sqrt((study_hours-new_study)**2+(attendance-new_attendance)**2)
        distance.append((study_hours,attendance,dist,result))

    #sort the distance

    distance.sort(key=lambda x:x[2])

    #K nearest neighbour

    k=3
    neighbour=distance[:k]

    print("Nearest neighbour:")
    for n in neighbour:
        print(n)

    votes={}

    for n in neighbour:
        result=n[3]

        if result in votes:
            votes[result]+=1
        else:
            votes[result]=1
    
    predicted=max(votes,key=votes.get)
    print("Predicted result:",predicted)



if __name__=="__main__":
    main()