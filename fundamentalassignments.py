words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words.replace("day","month")

x = [2,54,-2,7,12,98]
x.min()
x.max()

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[len(x)-1]
newlist= x[1:len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
x1=[x[0:len(x)/2]]
x2=x[len(x)/2:len(x)]
y=x1+x2
