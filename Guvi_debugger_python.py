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
  
