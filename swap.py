def swapping():
    file1=input("enter first file name: ")
    file2= input("enter second file name: ")
    a=open(file1,"r")
    data1=a.read()
    b=open(file2,"r")
    data2=b.read()
    c=open(file1,"w")
    c.write(data2)
    d=open(file2,"w")
    d.write(data1)

swapping()