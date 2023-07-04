# ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.

# **Given**:

# s1 = "Ault"
# s2 = "Kelly"

# Expected Output:
# AuKellylt

s1 = "Ault"
s2 = "Kelly"

c1=len(s1)/2
c2=0

str=""

for i in s1:
    if c2<c1:
        str+=i;
        c2+=1
    else:
        str=str+s2
        break;

c3=0
for y in s1:
    if c3<c1:
        c3+=1
    else: 
        str=str+y


print(str)