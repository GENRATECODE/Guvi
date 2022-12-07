'''                                                          string manipulation


In a school there are voting to choose the monitor of class.
#Your task is to tell which candidate is winner and if there is a tie print the name of candidate whose come first in lexicographical order.

Input Description:-
You are given with the space separated names.

Output Description:-
Print the winner’s name and the votes he earned.

Sample Input :
john johnny jackie johnny john jackie jamie jamie john johnny jamie johnny john
Sample Output :
john 4.'''
from collections import defaultdict
mylist = list(input().split())
mydict = defaultdict(int)
for i in mylist:
    if i not in mylist:
        mydict[i] = 1
    else:
        mydict[i] = mydict[i] + 1
        anslist = []
for i in mydict:
    anslist.append(mydict[i])
    max_num = max(anslist)
    numlist = []
for i in mydict:
    if mydict[i]==max_num:
        numlist.append(i)
        numlist = sorted(numlist)
print(numlist[0],max_num)
'''
You are given a string ‘s’.Print all the duplicate characters of string.

Input Description:-
String ‘s; is given

Output Description:-
Print only duplicate character and -1 if no character is duplicate.

Sample Input :
abcddee
Sample Output :
d e '''

s = input()
L1, L2 = [], []
for c in s[:] : # loop for  string 
    if c in L1 :  # check string are already on string or not 
        L2.append(c) # if yes then append c in l2
    else :  # else part add on l1
        L1.append(c)
if L2[::] :#simply print out
    print(*L2,end='')
else :
    print(-1,end='')
  
'''You are given some words all in lower case letters your task is to print them in sorted order.

Input Description:-
You are given a string ‘s’

Output Description:-
Print the string in sorted order

Sample Input :
virat kohli
Sample Output :
kohli virat'''
n=list(input().split())
t=sorted(n)
print(*t)

'''
Write a Program to Check if a Date is Valid and Print the Incremented Date Otherwise Invalid

Input Description:-
A single line input contains a three integer separated by space

Output Description:-
Print the incremented date.

Sample Input :
16 1 2020
Sample Output :
17 1 2020'''
date=input()
dd,mm,yy=map(int,date.split(' '))
dd=int(dd)
yy=int(yy)
if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
    max1=31
elif(mm==4 or mm==6 or mm==9 or mm==11):
    max1=30
elif(yy%4==0 or yy%400==0):
    max1=29
else:
    max1=28
#increment of date 
#last month to new year 
print(max1)
if( dd==31 and mm==12 ):
    dd=1
    mm=1
    yy=yy+1
    print(dd,mm,yy)

elif(mm<1 or mm>12):
    print("Invalid")
elif(dd<1 or dd>max1):
    print("Invalid")
elif dd>1 and dd!=max1 or dd<max1 and max1!=dd:
    dd=dd+1
    print(dd,mm,yy)
elif dd==max1:
    dd=1
    mm=mm+1
    print(dd,mm,yy)
