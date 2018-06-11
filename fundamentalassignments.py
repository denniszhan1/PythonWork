#Strings and Lists

words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words.replace("day","month")

x = [2,54,-2,7,12,98]
min(x)
max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[len(x)-1]
newlist= x[1:len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
x1=[x[0:len(x)/2]]
x2=x[len(x)/2:len(x)]
y=x1+x2


#Multiples,Sum,Average

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


#Filter by Type

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


#Type List

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


#Compare Lists

def comp(x,y):
    if x==y:
        print "The lists are the same"
    else:
        print "The lists are not the same"


#Find Chars

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


#Checkerboard

def checkerboard():
    for i in range(0,4):
        print "* * * *"
        print " * * * *"


#Odd/Even

def odd_even():
    for i in range(0,2001):
        if i%2==0:
            print "Number is ", i, ".", "This is an even number,"
        else:
            print "Number is ", i, ".", "This is an odd number,"


#Multiply

def multiply(x,y):
    for i in range(0,len(x)):
        x[i]*=y
    return x

    
#Hacker Challenge

def layered_multiples(arr):
    new=[]
    for i in arr:
        print i
        i=[1]*i
        print i
        new.append(i)
    return new

import random
def scores():
    print "Scores and Grades"
    arr=[]
    for i in range(0,11):
        i=random.randint(60,100)
        arr.append(i)
    print arr
    for score in arr:
        if score >= 60 and score <= 69:
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


#Coin Tosses

def cointoss():
    import random
    hcount=0
    tcount=0
    i=0
    while i<5000:
        flip=round(random.random())
        if flip==0.0:
            tcount+=1
            print "Attempt #",i,": Throwing a coin... It's a tail! ... got ",hcount," head(s) so far and ", tcount," tail(s) so far"
        else:
            hcount+=1
            print "Attempt #",i,": Throwing a coin... It's a tail! ... got ",hcount," head(s) so far and ", tcount," tail(s) so far"
        i+=1


#Stars

def draw_stars(arr):
    for i in arr:
        if isinstance(i,int):
            print "*"*i
        elif isinstance(i,str):
            length=len(i)
            letter=i[0].lower()
            print length*letter


#Dictionary Basics

def dictionary(dict):
    for some_key, some_value in dict.iteritems():
        print "My" + "" + some_key + "" + "is" + "" + str(some_value)


#Names

def name(names):
    for name in names:
        print name["first_name"], name["last_name"]

def allnames(names):
    for role in names:
        counter = 0
        print role
        for person in names[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)


#Making Tuples

def ntup(tup):
    new=[]
    for keys in tup:
       new.append((keys, tup[keys]))
    print new


#Lists to Dict

def make_dict(list1, list2):
    new_dict = {}
    for i in range(0,len(list1)):
        new_dict[list1[i]]=list2[i]
    return new_dict