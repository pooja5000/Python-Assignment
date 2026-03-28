from math import sqrt
def main():
    data=[
        ('A', 1, 2, 'Red'),
        ('B', 2, 3, 'Red'),
        ('C', 3, 1, 'Blue'),
        ('D', 6, 5, 'Blue')
    ]

    #Take new point

    x_new=float(input("Enter new X point:"))
    y_new=float(input("Enter new Y point:"))

    #Calculate the euclidean distance
    Distance=[]

    for point in data:
        name,x,y,label=point
        dist=sqrt((x-x_new)**2+(y-y_new)**2)
        Distance.append((name,dist,label))

    #Sort the distance

    Distance.sort(key=lambda X:X[1])

    #K nearest neighbours

    k=3
    neighbour=Distance[:k]

    print("Nearest neighbours:\n")

    for n in neighbour:
        print(n)

    #MAjority vaotings

    Votes={}

    for n in neighbour:
        label=n[2]

        if label in Votes:
            Votes[label]+=1
        else:
            Votes[label]=1

    #find predicted class
    predicted=max(Votes,key=Votes.get)

    print("predicted class :\n",predicted)

    #k=1

    k=1
    neighbour=Distance[:k]
    print("Neighbours using K=1: \n")
    for n in neighbour:
        print(n)

    Votes={}

    for n in neighbour:
        label=n[2]

        if label in Votes:
            Votes[label]+=1
        else:
            Votes[label]=1
    predicted=max(Votes,key=Votes.get)
    print("Predicted class using K=1:\n",predicted)

    #k=5

    k=5
    neighbour=Distance[:k]

    print("Neighbours using K=5: \n")
    for n in neighbour:
        print(n)

    Votes={}

    for n in neighbour:
        label=n[2]
        if label in Votes:
            Votes[label]+=1
        else:
            Votes[label]=1
    predicted=max(Votes,key=Votes.get)

    print("predicted class using k=5:\n",predicted)


if __name__=="__main__":
    main()