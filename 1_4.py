a = int(3)
b = 4
c = float(2)
d = 2.0

e = a + c
f = a - c
g = a * c
h = c / d

4//3
# a//b: gives quotient  
4%3
# a%b: gives remainder
4**3
# a**b: a to the exponent of b

# Boolean 
# 1 = true 0 = false

a += 2
print(a)

# String
# Python uses both '' single quotation and "" double quotation
a = 'thank'
b = "you"
c = 'thank' 
# But one single quotation and one double quotation does not work
d = """t
h
a
n
k
s
"""

# Sum of Strings
a+b 
# connects "thank" and "you" without a space
a+" "+b 
# connects "thank", " ", and "you" 

# For variable to be used in string needs .format()
a = "Jiho Lee"
name1 = "{}" .format(a)

name = "Jiho Lee"

email = "jhkin0819@gmail.com"

print("{}'s email address is {}.".format(name,email))


s = "2024-7-16"
result = s.split('-')
print(result)

# upper(): all capital 
# lower(): all lowercase
# capitalize(): first letter caps and other lowercased
email.capitalize()

ex = s.center(50)
ex = s.center(50, '*')
ex = s.center(50, '/')

s.count('2')

s.find('2')

ex.strip(" ")

"asdf123".isalnum()
# isalnum = is there a number
"aaaaaaa".isalpha()
# isalpha = is there an alphabet
"313333".isdecimal()
"3131".isdigit()

"a".isidentifier()
# checks if the string can be a variable
"a31".isidentifier()
"31a".isidentifier()

" ".isspace()
print("")
print(" ")

a = ""
b = " "
len(a) #counts the length of the text
len(b)

#task 1

x = 5.0
y = 3
a = x + y
print('x + y = {}'.format(a))

#task 2
x = 'Than3k'
y = 'yo97u'

print(x.replace("3","") + " " + y.replace("97",""))
