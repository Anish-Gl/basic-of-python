#!/usr/bin/env python
# coding: utf-8

# Operators in python
# "*","+","-","%"

# In[1]:


4+4


# In[2]:


4-2


# In[3]:


4*3


# In[4]:


10/2


# In[5]:


10//2     #Floor division "//" it will exclude decimal numbers


# In[6]:


10%2     #Remainder of a division


# In[7]:


10%3


# In[8]:


2**3


# In[9]:


4**2


# Working with variables

# In[10]:


a=10


# In[11]:


a


# In[12]:


b=7


# In[13]:


b


# In[14]:


a+b


# In[15]:


a*b


# In[16]:


a%b


# In[17]:


c=a%b


# In[18]:


c


# In[19]:


print("c=")


# In[20]:


print("c=",c)


# In[21]:


print("the value of c=",c)


# area of rectangle

# In[22]:


length=5
breadth=15

area=length*breadth
print("Area of rectangle=",area)


# In[23]:


#Body mass index=weight/height**2
#Circumference of a circle=2*pi*r


# In[24]:


len("Tesla")


# In[25]:


car="Tesla"


# In[26]:


len("car")


# In[27]:


len(car)


# In[28]:


len("city")


# In[29]:


city="bangalore"


# In[30]:


len(city)


# In[31]:


len("bangalore")


# In[32]:


print("Area of a rectangle with length=",length,"and breadth=",breadth,"=",area)


# In[33]:


country=input("enter country ")


# In[34]:


country


# String concatenation

# In[35]:


"Happy"+" Birthday"


# In[36]:


x=input("the value of x")


# In[37]:


y=input("the value of y")


# In[38]:


x+y    #String concatenation


# In[39]:


x


# In[40]:


y    #string datatype within the qoutes


# Type casting

# In[41]:


float(7)


# In[42]:


int(87.47)


# In[43]:


float(7)


# In[44]:


p="85"


# In[45]:


type(p)


# In[46]:


m=int(p)


# In[47]:


m


# In[48]:


type(m)


# In[49]:


j=int(input("enter the value of j"))


# In[50]:


k=int(input("enter the vlaue of k"))


# In[51]:


l=j+k


# In[52]:


l


# Boolean Operations

# In[53]:


6>3


# In[54]:


6<3


# In[55]:


6==3


# In[56]:


6!=3  #"!=" not equal to


# Slicing and indexing operation

# In[57]:


print("Hello"[0])


# In[58]:


print("Hello"[3])


# In[59]:


print("Hello"[0:2])


# In[60]:


print("Hello"[0:4])


# In[61]:


print("Hello"[0:5])


# In[62]:


print("Hello"[0:6])


# In[63]:


print("Hello"[2:4])


# # python data structures

# *Lists
# *tuples
# *Dictionary

# List

# In[64]:


list1=[1,2,3,4,5]


# In[65]:


list2=[6,7,8,9,0]


# In[66]:


list3=[55,66,77,88]


# In[67]:


list3=[78.9,89.5,63.4,89.3,90.4]


# In[68]:


list5=["a","b","c","d","e"]


# In[69]:


mixedlist=[1,"a",78.5,"india","True"]


# In[70]:


fruitlist=["Apple","Mango","Orange","pineapple","Watermelon"]


# In[71]:


len(fruitlist)


# In[72]:


fruitlist.append("Banana")


# In[73]:


fruitlist


# In[74]:


len(fruitlist)


# In[75]:


fruitlist[0]


# In[76]:


fruitlist[2:5]


# In[77]:


fruitlist[-1:-4]


# In[78]:


fruitlist[-4:-1]


# In[79]:


fruitlist[-1]


# In[80]:


fruitlist[:-1]


# In[81]:


fruitlist[:-4]


# In[82]:


fruitlist.insert(3,"Grapes")


# In[83]:


fruitlist


# In[84]:


fruitlist.pop()


# In[85]:


fruitlist


# In[86]:


fruitlist.remove("Mango")


# In[87]:


fruitlist


# In[88]:


fruitlist.pop(3)


# In[89]:


fruitlist[1]="Kiwi"


# In[90]:


l1=[1,2,3,4]
l1.append([77,88,99,00])
l1


# In[91]:


l1=[1,2,3,4]
l1.extend([77,88,99,00])
l1


# In[92]:


fruitlist.clear()


# In[93]:


fruitlist


# In[94]:


del fruitlist


# In[95]:


l1


# In[96]:


l1[5]=100


# In[97]:


l1


# Tuples

# In[98]:


#tuples are same as lists but u cant change the values in it 


# In[99]:


l1=(1,2,3,4)
l2=(5,6,7,8)


# In[100]:


l3=l1+l2


# In[101]:


l3


# In[102]:


l3[2]


# In[103]:


#tuples cant be changed after creation


# Dictionary

# In[104]:


dict1={"Name":"Zara","Age":7,"Class":"First"}


# In[105]:


dict1


# In[106]:


dict1["Name"]


# In[107]:


print(dict1["Age"])


# In[108]:


print("dict['Name']:",dict1["Name"])


# In[109]:


dict1.keys()


# In[110]:


dict1.values()


# In[111]:


dict1.items()


# In[112]:


dict1.update({"Fee":5000})


# In[113]:


dict1


# In[114]:


dict1["Fee"]=9500


# In[115]:


dict1


# In[116]:


#Dictionary with multiple values


# In[117]:


newdict={1:["Red","Yellow","Orange"],2:["White","Black","Brown"],3:["Green","Purple","Blue"]}


# In[118]:


newdict.keys()


# In[119]:


newdict.values()


# In[120]:


newdict.items()


# Sets

# In[121]:


x={11,22,33,44,55}


# In[122]:


x


# In[123]:


x={11,22,33,44,22,33,55,66,11}    #in sets values wont be repeated


# In[124]:


x


# In[125]:


type(x)


# In[126]:


x.pop() #removes random variables


# # Python loops

# While loops

# In[127]:


#initialization
i=0

#condition
while(i<5):
    print(i)
    i=i+1


# In[128]:


i=0
while(i<5):
    print("i= ",i)
    i=i+1


# In[129]:


i=0
while(i<10):
    print("i= ",i)
    i=i+2


# In[130]:


i=0
while(i<5):
    print(i,end=" ")
    i=i+1                            #prints results horizontal


# In[131]:


i=0
while(i<25):
    print(i,end=" ")
    i=i+1                            #prints results horizontal


# In[132]:


x=int(input("enter the value of x"))

i=0
while(i<x):
    print(i)
    i=i+1                            #prints results horizontal


# For loops

# In[133]:


for i in [1,2,3,4]: 
    print(i)


# In[134]:


for i in [1,2,3,4]: 
    print(i,end=" ")


# In[135]:


for i in ["A","B","C","D"]: 
   print(i,end=" ")


# In[136]:


list=[1,2,3,4,5]

for i in list:
    print(i)


# In[137]:


list=[1,2,3,4,5]

for i in list:
    print(i)

print("\n")
print("loop ends")  #not a part of for loop


# Range function

# In[138]:


range(5)


# In[1]:


list(range(5))


# In[2]:


a=list(range(5))


# In[4]:


type(a)


# In[5]:


for i in a:
    print(i)


# In[6]:


list(range(2,10))


# In[7]:


x=list(range(5,20))


# In[ ]:


x


# In[ ]:


for i in x:
    print(i)
print("Range done")


# In[ ]:


list(range(2,10,2))


# In[ ]:


y=list(range(5,50,5))     #(STart End  Jump)


# In[ ]:


for i in y:
    print(i)


# Iterating through a dictionary

# In[149]:


d={1:"sky",2:"earth",3:"water",4:"forest"}


# In[150]:


d


# In[151]:


for i in d:
    print(i)


# In[152]:


for i in d:
    print(d[i])


# list comprehension

# In[153]:


s=[]

for i in range(2,11,2):
    s.append(i)
    print(s)


# In[154]:


s


# In[155]:


list1=[1,2,3,4,5]
m=[d for d in list1]

print(m)


# # Break and continue statements

# In[156]:


for i in["lemon","apples","oranges","banana"]:
   print(i)


# In[157]:


for i in["lemon","apples","oranges","banana"]:
   if i=="oranges":
       break
   print(i)


# In[158]:


for i in["lemon","apples","oranges","banana"]:
   if i=="oranges":
       continue
   print(i)


# # IF constructs

# In[159]:


marks=90

if marks>80:
    print("Excellent")
else :
    print("Good")
# In[160]:


fact=2
num=12
if num%fact==0:
    print("even")
else:
    print("odd")


# # String functions

# In[161]:


word="WelCOme To PyThOn"


# In[162]:


word


# In[163]:


word.lower()


# In[164]:


word.upper()


# In[165]:


word.swapcase()


# In[166]:


word.split()


# In[167]:


word.isalpha()


# In[168]:


word2="python"


# In[169]:


word2.isalpha()


# string concatenation

# In[170]:


str1="new"
str2="horizon"
print(str1+str2)
print(str1+ " ",str2)


# # string formats

# In[171]:


#this prints out hello joh
name="John"
print("Hello,%s!"%name)


# In[172]:


#This prints out "John is 23 years old"
name="John"
age=23
print("%s is %d years old."%(name,age))


# In[173]:


x="apples"
y="lemons"
z="I have %s and %s"%(x,y)


# In[174]:


z


# In[175]:


name="John"
age=24
print("His name is {} he is {} years old".format(name,age))


# In[176]:


print("{0} and {1}".format("spam", "eggs"))
print("{1} and {0}".format("spam","eggs"))


# # functions

# Built in function

# In[177]:


help()


# In[178]:


k=[10,78,26,18,90,56]


# In[179]:


min(k)


# In[180]:


max(k)


# User defined function

# In[181]:


#function definition
def function1():
    print("Inside function1")


# In[182]:


#call a function

function1()


# In[183]:


def myfunc():
    a=2
    b=9
    c=a+b
    print("the value of c",c)


# In[184]:


myfunc()


# functions with parameters

# In[185]:


def addfunc(a,b):
    c=a+b
    print("the value of c is",c)


# In[186]:


addfunc(5,12)


# In[187]:


def addfunc(a,b,d):
    c=a+b+d
    print("the value of c is",c)


# In[188]:


addfunc(2,3,7)


# In[189]:


def sqrt():
    p=int(input("Enter the value of p"))
    print("sqrt=", (p**.5))


# In[190]:


sqrt()


# In[191]:


def run():
    for x in range(10):
        print(x)


# In[192]:


run()


# In[193]:


def run():
    for x in range(2,15,3):
        print(x)


# In[194]:


run()


# In[195]:


def run():
    for x in range(10):
        if x==5:
            return
        print("run")


# In[196]:


run()


# In[197]:


#function with return value

def sumfunc(arg1 , arg2):
        #add both the paramteres and return them
        total=arg1 + arg2
        print("Inside the function :",total)
        return(total)


# In[198]:


sumfunc(5,10)


# In[199]:


tot=sumfunc(10,20)
print("total=",tot)


# # Variable number of arguments

# In[200]:


def plus(*args):
    return sum(args)


# In[201]:


#callling the functions
plus(6,10,4)


# In[202]:


def plus(*args):
    return max(args)


# In[203]:


plus(1,45,33,20)


# In[204]:


def plus(*variablename):
    return min(variablename)


# In[205]:


plus(1,45,33,20)


# In[206]:


def sum(*numbers):
    s=0
    for n in numbers:
        s+=n                           # s=s+n   s=+n both are same
    return s


# In[207]:


print(sum(1,2,3))


# # Anonymous function Lamda

# In[208]:


#a lamda function  is a small function containing single expression


# In[209]:


test=lambda x:x*2
test(5)


# In[210]:


test(10)


# In[211]:


test1add=lambda x,y:x+y
test1add(5,6)


# In[212]:


m=lambda x,y,z:x+y+z
m(1,2,3)


# In[213]:


addvar=lambda arg1,agr2:arg1+agr2
print("the value of total :",addvar(5,10))
print("the value of total :",addvar(10,23))


# In[214]:


#converting temperature into fahrenheit
def fahrenheit(T):
    return((float((9)/5*T+32)))


# In[215]:


f=fahrenheit(35)


# In[216]:


f


# In[217]:


#converting temperature into celsius
def celsius(T):
    return((float((5)/9)*(T-32)))


# In[218]:


ce=celsius(52)


# In[219]:


ce


# In[220]:


F=lambda t:(float(9)/5)*t+32
F(38.4)


# # Map in lambda

# In[8]:


mylist=[1,2,3,4]
list(map(lambda x:x*2,mylist))


# In[9]:


C=[35.4,56.3,98.7,51.7,87.6]
F=list(map(lambda x:(float(9)/5)*x+32,C))
print(F)


# In[ ]:


C=list(map(lambda x:(float(5)/9)*(x-32),F))
print(C)


# Round of the decimal values

# In[ ]:


newClist=[round(x,2) for x in C]
newClist


# In[ ]:


newlist=["%.2f" % j for j in C]
newlist


# In[ ]:


def sum1(x,y):
    print("addition = ",x+y)


# In[ ]:


#sum1(7,7)


# In[ ]:


def main():
    sum1(20,4)
    print("this is the main function")


# In[ ]:


main()


# In[ ]:


#calling the main function in python


# In[ ]:


if __name__=="__main__":
    main()


# # Class in python

# In[223]:


class car:
    
    #attributes
    year=2019
    mpg=22
    speed=100
    
    #methods
    def accelerate(self):
        return car.speed+20
    def brake(self):
        return car.speed-50


# In[224]:


car1=car()
car1.accelerate()


# In[225]:


car1.brake()


# In[226]:


print(car1.year)


# In[227]:


print(car1.mpg)


# In[228]:


print(car1.speed)


# In[229]:


class myclass:
    k=123     #attribute member
    d=6.7
    def test(self):    #member function
        print("this is the first class")

def main():
    m=myclass()  #creating object/instances
    #calling attribute with member function
    print(m.k)
    print(m.d)
    m.test()
    
if __name__=="__main__":
    main()


# # Constructor

# init method

# In[ ]:


class student:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        


# In[ ]:


p1=student("Sam",25)
print(p1.name)
print(p1.age)


# In[ ]:


class employee:
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
    
    def display(self):
        print("inside display function")
        print(self.name,self.age,self.id,self.salary)


# In[ ]:


emp1=employee("John",24,10000,234) #creating objects
emp2=employee("Andrew",30,15000,564)
emp1.display()
emp2.display()


# In[ ]:


class company:
    #class variable
    revenue=80000
    
    def __init__(self,name,location,number_of_employees):
        self.name=name
        self.location=location
        self.number_of_employees=number_of_employees


# In[ ]:


c=company("Anish","India",400)
print(c.name)
print(c.location)
print(c.number_of_employees)

#accessing class variables 
company.revenue


# In[ ]:


class car:
    def __init__(self,company,color):
        self.company=company
        self.color=color
    
    def display(self):
        print("this is a ",self.color,self.company)


# In[ ]:


def main():
    c=car("Ferrari","Red")
    c.display()


# In[ ]:


if __name__=="__main__":
    main()


# In[ ]:


class employee:
    
    def __init__(self,name,age):
        print("initialized method called")
        self.name=name
        self.age=age
        
    def getdata(self,name,age):
        print("getdata method called")
        self.name=name
        self.age=age
        
    def displaydata(self):
        print("Hello",self.name,self.age)


# In[ ]:


def main():
    e=employee("Anitha",35)
    e.displaydata()
    
    e.getdata("Lakshmi",52)
    e.displaydata()


# In[ ]:


if __name__=="__main__":
    main()


# # Modules

# In[ ]:


#import modulename


# In[ ]:


import keyword


# In[ ]:


print(keyword.kwlist)


#  Python module search path

# In[ ]:


import sys


# In[ ]:


sys.path


# In[ ]:


#get current working directory


# In[ ]:


import os


# In[ ]:


os.getcwd()


# In[ ]:


#changing working directory
#we will change the current working directory using the chdir() method.
#os.chdir('C:\\Users\\Anish G')
#os.getcwd()


# In[ ]:


#show the list of files and folders in current working directory
os.listdir()


# In[ ]:


os.__dict__.keys()


# In[ ]:


import math


# In[ ]:


math.pi


# In[ ]:


math.sqrt(16)


# In[ ]:


math.pow(2,3)


# In[ ]:


math.__dict__.keys()


# In[ ]:


import math as m


# In[ ]:


m.pi


# In[ ]:


m.pow(2,3)


# In[ ]:


from math import pi


# In[ ]:


pi


# In[ ]:


from math import sqrt


# In[ ]:


sqrt(16)


# In[ ]:


import math

class areacircle:
    def __init__(self,area,radius):
        self.area=area
        self.radius=radius
    
    def calculatearea(self):
        self.area=math.pi*(self.radius**2)
        print("Area of circle =",self.area)
    
    def inputdata(self):
        self.radius=int(input("Enter the value of radius"))
        print("Radius =",self.radius)
        self.calculatearea()
        
def main():
    c1=areacircle(0,0)
    c1.inputdata()
    
if __name__=="__main__":
    main()


# # INPUT/OUTPUT operations

# In[ ]:


savefile=open("C:\\Users\\Anish G\\OneDrive\\Desktop\\New folder\\anish.txt","w")


# In[ ]:


savefile.write("This is the first line.")


# In[ ]:


savefile.close()


# In[ ]:


readme=open("C:\\Users\\Anish G\\OneDrive\\Desktop\\New folder\\anish.txt","r")


# In[ ]:


print(readme.read())


# In[ ]:


readme.close()


# In[ ]:


appendfile=open("C:\\Users\\Anish G\\OneDrive\\Desktop\\New folder\\anish.txt","a")


# In[ ]:


appendfile.write("\n Lets add this is the next line")


# In[ ]:


appendfile.close()


# # Pickle in python : Object Serialization

# In[ ]:


import pickle


# In[ ]:


flower_dict = {1:"Rose",2:"Lilly",3:"Lotus",4:"Tulip"}


# In[ ]:


filename="flower"


# In[ ]:


outfile=open(filename,"wb")


# In[ ]:


#pickling the file
pickle.dump(flower_dict,outfile)
outfile.close()


# In[ ]:


#unpickle the file
infile=open(filename,"rb")


# In[ ]:


new_dict=pickle.load(infile)


# In[ ]:


infile.close()


# In[ ]:


print(new_dict)


# In[ ]:


print(new_dict==flower_dict)


# In[ ]:


print(type(new_dict))


# In[ ]:


#!pip install mysql-connector-python


# In[ ]:


#import mysql.connector


# In[ ]:


import pandas as pd
con=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="*******",
    database="empdb")


# In[ ]:


df=pd.read_sql_query("select * from empdb",con)
df


# In[ ]:


df.head()


# In[ ]:


df.tail()


# In[ ]:


df=pd.read_sql_query("select * from empdb where did=1001",con)


# # Numpy tutorial

# In[ ]:


import numpy


# In[ ]:


a=numpy.array([1,2,3,4,5,6,7,8])


# In[ ]:


a


# In[ ]:


b=numpy.array([44,55,66,77,88,99])


# In[ ]:


b


# In[ ]:


a.shape


# In[ ]:


b.shape


# In[ ]:


import numpy as np


# In[ ]:


c=np.array([11,22,33,44,55])


# In[ ]:


c.shape      #1 dimentional array


# In[ ]:


a=np.array([[1,2],[4,3]])   #2 dimentional array
a


# In[ ]:


a.shape


# In[ ]:


c=np.array ([[1,2],[2,3],[4,5]])


# In[ ]:


c.shape


# In[ ]:


c.reshape(2,3)


# In[ ]:


c.min()


# In[ ]:


c.max()


# In[ ]:


c.size


# In[ ]:


c.itemsize   #how much memory is allocated its 4 byte is used


# In[ ]:


c.dtype


# In[ ]:


c.data   #memory address


# In[ ]:


c=np.array ([[1,2],[2,3],[4,5]],dtype="float64")


# In[ ]:


c


# In[ ]:


c.itemsize


# In[ ]:


x=np.arange(15)
print(x)


# In[ ]:


a=x.reshape(3,5)


# In[ ]:


a


# In[ ]:


a=x.reshape(5,3)


# In[ ]:


a


# In[ ]:


x=np.arange(45).reshape(9,5)


# In[ ]:


x


# In[ ]:


x.ndim     # number of dimension 2 means rows and columns


# In[ ]:


type(x)


# In[ ]:


print(x.ravel())    #conerts 2 dimensional array to one dimension


# In[ ]:


np.zeros((3,4))


# In[ ]:


np.ones((3,4))


# In[ ]:


j=np.ones((2,3,4))


# In[ ]:


j


# In[ ]:


j.shape


# In[ ]:


j.ndim


# In[ ]:


np.empty((5,3))   #junk values


# In[ ]:


b=np.array([[1,2,3,4],[5,6,7,8],[3,4,5,6]])


# In[ ]:


b.shape


# In[ ]:


b.reshape(4,3)


# In[ ]:


np.arange(10,70,5)


# In[ ]:


a=np.array([20,30,40,50])
b=np.arange(4)


# In[ ]:


c=a+b


# In[ ]:


c


# In[ ]:


c**2


# In[ ]:


d=np.random.random((2,3))    #any values


# In[ ]:


d


# # universal functions

# In[ ]:


e=np.arange(3)


# In[ ]:


e


# In[ ]:


np.exp(e)


# In[ ]:


np.sqrt(e)


# # indexing,slicing and iterating

# In[ ]:


a=np.arange(10)


# In[ ]:


a


# In[ ]:


a[2]


# ##### 

# In[ ]:


a[2:5]


# In[ ]:


a[-1]


# In[ ]:


a[:4]


# In[ ]:


a[5:]


# In[ ]:


d=np.arange(20)


# In[ ]:


s=slice(2,20,2)


# In[ ]:


s


# In[ ]:


print(d[s])


# In[ ]:


d[5:]


# In[ ]:


d=np.array([np.nan,1,2,3,np.nan,6,7,8])


# In[ ]:


d


# In[ ]:


print(d[~np.isnan(d)])


# In[ ]:


np.random.rand(2,2)   #we will get random "+ve" values


# In[ ]:


np.random.randn(2,2)   #we will get random "+ve" and "-ve" values


# # Pandas

# # Series

# In[ ]:


import pandas as pd


# In[ ]:


a=pd.Series([1,2,3,4,5,6,7,8])
a


# In[ ]:


b=pd.Series([8,7,6,5,4,3,2,1],index=[11,12,13,14,15,16,17,18])


# In[ ]:


b


# In[ ]:


data=np.array([1,1,2,3,4])
m=pd.Series(data)
m


# In[ ]:


dict={"name":"anitha","AGe":40}
s1=pd.Series(dict)


# In[ ]:


s1


# # Dataframe

# In[ ]:


data=[1,2,3,4]
df=pd.DataFrame(data)
df


# In[ ]:


data=[["Anitha",50],["Anish",18],["Clarke",13]]
df=pd.DataFrame(data)
df


# In[ ]:


data=[["Anitha",50],["Anish",18],["Clarke",13]]
df=pd.DataFrame(data,columns=["NAme","Age"])
df


# In[ ]:


data=[["Anitha",50],["Anish",18],["Clarke",13]]
df=pd.DataFrame(data,columns=["NAme","Age"],dtype=float)
df


# In[ ]:


data={"NAme":["Anish","Anitha","Lakshmi"],"Age":[60,18,50]}
df=pd.DataFrame(data)
df


# In[ ]:


data=[{"a":1,"b":2},{"a":5,"b":6,"c":7}]
df=pd.DataFrame(data,index=["First","Second"],dtype=float)
df


# In[ ]:


data=[{"a":1,"b":2},{"a":5,"b":6,"c":7}]


df=pd.DataFrame(data,index=["First","Second"],columns=["a","b"])

df1=pd.DataFrame(data,index=["First","Second"],columns=["a","b1"])


print(df)
print("\n")
print(df1)


# In[ ]:


df1=pd.DataFrame([[1,2],[3,4]],columns=["a","b"])
df2=pd.DataFrame([[5,6],[7,8]],columns=["a","b"])

df3=df1.append(df2)
df3


# # .loc & .iloc

# In[10]:


df=pd.DataFrame(np.random.randn(8,4),columns=["A","B","C","D"]) 
df


# In[ ]:


print(df.loc[:,"A"])


# In[ ]:


print(df.loc[:,["C","D"]])


# In[ ]:


print(df.iloc[:4,:])


# In[ ]:


print(df.iloc[:,:3])


# In[ ]:


print(df.iloc[2:4,1:2])


# In[ ]:


print(df.iloc[:4,:-1])


# In[ ]:


print(df.iloc[:-4,:-1])


# # Pandas Visualization

# In[ ]:


df=pd.DataFrame(np.random.randn(8,4),columns=["a","b","c","d"])
print(df)
df.plot.bar()


# In[ ]:


df.plot.bar(stacked=True)


# In[ ]:


df.plot.barh(stacked=True)


# In[ ]:


df.plot.hist(bins=20)   #bins means interval between the data


# In[ ]:


df.plot.box()


# In[ ]:


df=pd.DataFrame(np.random.rand(8,4),columns=["a","b","c","d"])
print(df)
df.plot.area()


# In[ ]:


df.plot.scatter(x="a",y="b")


# # Merge,concatenation,Join and Append

# # concat

# In[ ]:


data={
    "Subject":["1","2","3","4","5"],
    "First name":["a","b","c","d","e"],
    "Last name":["f","g","h","i","j"]}
df1=pd.DataFrame(data,columns=["Subject","First name","Last name"])
df1


# In[ ]:


data={
    "Subject":["4","5","6","7","8"],
    "First name":["k","l","m","n","o"],
    "Last name":["p","q","r","s","t"]}
df2=pd.DataFrame(data,columns=["Subject","First name","Last name"])
df2


# In[ ]:


data={
    "Subject":["1","2","3","4","5","4","5","6","7","8"],
    "TestID":[51,52,53,54,55,56,57,58,59,60]}
df3=pd.DataFrame(data,columns=["Subject","TestID"])
df3


# In[ ]:


df_new=pd.concat([df1,df2])
df_new


# In[ ]:


df_new=pd.concat([df1,df2],ignore_index=True)   #indexing is done in order
df_new


# In[ ]:


df_new=pd.concat([df1,df2],axis=1)   # data will added along the column 
df_new


# # merge

# In[ ]:


pd.merge(df_new,df3)


# In[ ]:


pd.merge(df_new,df3,on="Subject")


# In[ ]:


pd.merge(df_new,df3,on="Subject",how="outer")


# In[ ]:


pd.merge(df_new,df3,on="Subject",how="inner")


# # Append

# In[ ]:


df1.append(df2)


# In[ ]:


df1.append(df2,ignore_index=True)


# # join

# In[ ]:


j=df1.join(df2)
j


# # Set Index

# # change the index

# In[ ]:


data=pd.DataFrame({
    "Subject":["1","2","3","4","5"],
    "First name":["a","b","c","d","e"],
    "Last name":["f","g","h","i","j"]})
 
data


# In[ ]:


df1=data.set_index("Subject")
df1


# In[ ]:


df1=data.set_index("Subject",inplace=True)    # inplace means will make changes to original data
df1


# In[ ]:


df=data.rename(columns={"First name":"1st name"})
df


# # data analysis in python

# In[ ]:


df_new.head()


# In[ ]:


df_new.head(3)


# In[ ]:


df_new.tail()


# In[ ]:


df_new.tail(3)


# In[ ]:


df_new.sample()


# In[ ]:


df_new.sample(3)


# # Pandas IO-input/output tools

# In[ ]:


df=pd.read_csv("Baseball.csv")
df.head()


# In[ ]:


print(type(df["W"][0]))


# In[ ]:


# writing csv files with pandas
df.head()
df.to_csv("Baseball_csv")


# In[ ]:


df=pd.read_csv("Baseball.csv",index_col=["Serial no"])
df.head()


# In[ ]:


df=pd.read_csv("Baseball.csv",dtype={"W":np.float64})
print(df.dtypes)
df.head()


# In[ ]:


df.count()


# In[ ]:


df["W"].unique()


# In[ ]:


df["W"].nunique() #count of unique values


# In[ ]:


print(df["W"].describe())


# In[ ]:


df.describe() # descrine only numeric data


# In[ ]:


df.describe(include="all")   # describes all datas


# # Droping

# In[ ]:


df1=df.drop([14,15,16,17])
df1


# In[ ]:


df2=df.drop(["W"],axis=1)
df2


# # data munging

# In[ ]:


df=pd.read_csv("Baseball.csv",index_col=0)

df.to_html("base.html")


# # Replacing NaN values with zeros

# In[ ]:


df.replace(np.Nan,0)    #replacing NaN vlaue with zero


# # Replacing 0 with NaN values

# In[ ]:


df.replace(0,np.Nan)    #replacing zero value with NaN


# # Droping NaN values

# In[ ]:


df.dropna()


# In[ ]:


df.dropna(axis=1)   #columns


# In[ ]:


df.fillna(0)


# In[ ]:


df["column name"].fillna(df["Column name".mean())

df["column name"].fillna(df["Column name".median())     #mean and median is only for numeric data


# In[ ]:


df["column name"].fillna(df["Column name".mode())    #is used nly for string values


# # Data visualization using Matplotlib

# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


a=np.array([1,2,3,4,5,6,7])
b=np.array([1,2,3,4,5,6,7])


# In[ ]:


plt.title("Liner Line")
plt.xlabel("a")
plt.ylabel("b")
plt.plot(a,b)
plt.show()


# In[ ]:


plt.plot(a,b,"--g")   #--g means dotted line with green color
plt.show()


# In[ ]:


plt.title("Bar")
plt.xlabel("a")
plt.ylabel("b")
plt.bar(a,b)
plt.show()


# In[ ]:


a=np.array([15,20,23,24,56,78,92,98,89,90])
plt.hist(a,bins=[0,20,40,60,80,100])   #bins means intervals
plt.title("Histogram")
plt.show()


# In[ ]:


plt.violinplot(df["Column name"])


# In[ ]:


plt.title("scatter")
plt.xlabel("a")
plt.ylabel("b")
plt.scatter(a,b)
plt.show()


# In[ ]:


plt.bar? # shows bar plot description


# # Seaborn visualization library

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[ ]:


x=["sun","mon","tue","wed","thu","fri","sat"]
y=[5,5.5,7,8,9,10,12]


# In[ ]:


a=sns.stripplot(x,y)
a.set(xlabel="Days",ylabel="Amount spent")
plt.title("My first graph")
plt.show()


# In[ ]:


get_ipython().run_line_magic('pinfo', 'sns.violinplot')


# In[ ]:


sns.violinplot(x="column name",data=df)


# In[ ]:


df=pd.read_csv("Baseball.csv")
print(df.head())
sns.set(style="whitegrid")
x=sns.stripplot(x="W",y="R",data=df)
plt.title("Graph")
plt.show()


# In[ ]:


x=sns.swarmplot(x="W",y="R",data=df)
plt.title("Graph")
plt.show()


# In[ ]:


sns.get_dataset_names()     #inbuilt dataset


# In[ ]:


flights=sns.load_dataset("flights")
flights.head()


# In[ ]:


flights.passengers.hist(bins=5)


# In[ ]:


flights.passengers.hist(bins=20)


# In[ ]:


flights.passengers.describe()


# In[ ]:


sns.boxplot(x=flights.passengers)


# In[ ]:


titanicdf=sns.load_dataset("titanic")
print(titanicdf)


# In[ ]:


titanicdf.columns


# In[ ]:


titanicdf["class"]


# In[ ]:


titanicdf["class"].value_counts()


# In[ ]:


#Category plot
g=sns.catplot(x="class",y="survived",hue="sex",data=titanicdf,kind="bar")
plt.show()


# In[ ]:


#Category plot
g=sns.catplot(x="class",y="survived",hue="sex",data=titanicdf,kind="violin")
plt.show()


# In[ ]:


tipsdf=sns.load_dataset("tips")
print(tipsdf)


# In[ ]:


sns.distplot(tipsdf["tip"],bins=20)


# In[ ]:


sns.distplot(tipsdf["tip"],bins=20,kde=False)


# In[ ]:


sns.scatterplot(data=tipsdf,x="tip",y="smoker")


# In[ ]:


sns.jointplot(data=tipsdf,x="tip",y="smoker")


# In[ ]:


sns.jointplot(data=tipsdf,x="sex",y="smoker",kind="hex")


# In[ ]:


sns.jointplot(data=tipsdf,x="sex",y="smoker",kind="kde")


# In[ ]:


sns.stripplot(data=tipsdf,x="tip",y="smoker")


# In[276]:


sns.catplot(data=tipsdf,x="tip",y="smoker")


# In[277]:


sns.catplot(data=tipsdf,x="tip",y="smoker",kind="box")


# In[279]:


sns.pairplot(tipsdf)


# In[ ]:


x=sns.heatmap(flights)
x


# In[284]:


import numpy
print("Numpy ::",numpy.__version__)
import pandas
print("Pandas ::",pandas.__version__)
import numpy as np


# In[286]:


a=np.arange(4).reshape((2,2))
a


# In[287]:


np.amin(a)


# In[288]:


np.amin(a,axis=0)   #column wise


# In[289]:


np.amin(a,axis=1)   #row wise


# In[292]:


a=np.array([[3,7,5],[8,4,6],[2,7,9]])
print("our array is :",a)

print(a)
print("\n")

print(np.amin(a,1))
print("\n")

print(np.amin(a,0))
print("\n")

print(np.amax(a))
print("\n")

print(np.amax(a,1))
print("\n")


print(np.amax(a,0))
print("\n")


# In[293]:


print(np.ptp(a))


# In[295]:


print(np.ptp(a,axis=0))


# In[296]:


print(np.ptp(a,axis=1))


# In[297]:


np.ptp


# In[ ]:




