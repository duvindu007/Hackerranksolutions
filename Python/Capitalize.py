#You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
#For example, alison heck should be capitalised correctly as Alison Heck.
#Spaces also should reamin same 
# in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.
 

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s
    