def countwords():
    filename= input("Enter File Name: ")
    f=open(filename,"r")
    count=0
    for i in f:
        words=i.split()
        count=count +len(words)
    print(count)

countwords()
