Strings and Lists

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


Multiples,Sum,Average

for x in range(0,1001):
    print x

for x in range(0,1000001):
    if x%5==0:
        print x

a = [1, 2, 5, 10, 255, 3]
y=0
for x in a:
    y+=x
print y

average= y/len(a)


Filter by Type

def filter(x):
    if isinstance(x,int):
       if x>=100:
           print "That's a big number!"
       else:
           print "Thats a small number."
    if isinstance(x,str):
        if len(x)>=50:
            print "Long sentence."
        else:
            print "Short sentence."
    if isinstance(x,list):
        if len(x)>=10:
            print "Big list!"
        else:
            print "Short list."
        

