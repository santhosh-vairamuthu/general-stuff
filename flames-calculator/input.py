"""
FLAMES calculator made using python. Common letters are cleared and final lenth is found in input.py
The desired condition is found using flames.py as a module.
The input and output are handled in input.py
The input you enter are hidden
Made just for fun 😀


Created on Fri Mar 18 2022
purpose : IO
@author: Santhosh
"""

import flames
from getpass import getpass

fname=str(getpass("Enter your name : "))
a=list(map(str,fname.strip()))
A=a.copy()
for i in a:
    if i.isalpha() or i==" ":
        pass
    else:
        print("Only alphabets")
        break

sname=str(getpass("Enter your partners name : "))
b=list(map(str,sname.strip()))
for i in b:
    if i.isalpha() or i==" ":
        pass
    else:
        print("Only alphabets")
        break

c=[]
for i in A:
    if i in b:
        c.append(i)
        b.remove(i)
for i in c:
    if i in a:
        a.remove(i)
d=a+b 
num=0
for i in d:
    if i.isalpha():
        num+=1
#print(num)

result=flames.result(num)
fname=len(fname)*'#'
sname=len(sname)*'#'
print()
print()
if result=="F":
    print(f'''The relationship between {fname} and {sname} is FRIENDSHIP 💛''')
elif result=="L":
    print(f'''The relationship between {fname} and {sname} is LOVE 💘''')
elif result=="A":
    print(f'''The relationship between {fname} and {sname} is AFFECTION 🥰''')
elif result=="M":
    print(f'''The relationship between {fname} and {sname} is MARRIAGE 🤵💍👰''')
elif result=="E":
    print(f'''The relationship between {fname} and {sname} is ENEMIES 🙅''')
elif result=="S": 
    print(f'''The relationship between {fname} and {sname} is  SIBLINGS 💙💜.''')  
print()
print()
print("Thank you 🙏")

'''End of program'''
