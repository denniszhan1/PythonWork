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


Type List

def type(x):
    y=0
    z=""
    for i in x:
        if isinstance(i,int):
            y+=i
        if isinstance(i,str):
            z+=i
    if y==0:
        print "The list you entered is of string type"
        print "String:", z
    elif z==[]:
        print "The list you entered is of integer type"
        print "Sum:", y
    else:
        print "The list you entered is of mixed type"
        print "Sum:", y
        print "String:", z


Compare Lists

def comp(x,y):
    if x==y:
        print "The lists are the same"
    else:
        print "The lists are not the same"


Find Chars

def letter(x,y):
    count=0
    for string in x:
        for letter in string:
            if letter==y:
                count=+1
        if count==0:
            x.remove(string)
        count=0 
    print x


Checkerboard

def checkerboard():
    for i in range(0,4):
        print "* * * *"
        print " * * * *"


Odd/Even

def odd_even():
    for i in range(0,2001):
        if i%2==0:
            print "Number is ", i, ".", "This is an even number,"
        else:
            print "Number is ", i, ".", "This is an odd number,"


Multiply

def multiply(x,y):
    for i in range(0,len(x)):
        x[i]*=y
    return x

    
Hacker Challenge

def layered_multiples(arr):
    new=[]
    for i in arr:
        print i
        i=[1]*i
        print i
        new.append(i)
    return new


def scores():
    print "Scores and Grades"
    arr=[]
    for i in range(0,11):
        i=random.randint(60,100)
        arr.append(i)
    print arr
    for score in arr:
        if  if score >= 60 and score <= 69:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score <= 79:
            print "Score: ", score, "; Your grade is C"
        elif score >= 80 and score <= 89:
            print "Score: ", score, "; Your grade is B"
        elif score >= 90 and score <= 100:
            print "Score: ", score, "; Your grade is A"
        else:
            print "You failed"
    print "End of the program.  Bye!"


