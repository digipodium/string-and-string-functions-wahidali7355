#ques 01
string="THIS IS MY  STRING"
print(string)

#ques 02
str_input=input("Please enter the string=>>> ")
size=len(str_input)
print("The size of entered string is: ",size)

#ques 03 Print the last word of the string Python is great using slices.
string_python="Python is great"
print(string_python[::-1])

#ques 04 Print the each word in different line of string python is everywhere.
word="python is everywhere"
print(*word.split(),sep='\n')

#ques 05 Print the string Hello World! in reverse.
revr="Hello World!"
print(revr[::-1])

#ques 06 Convert the string How are you? in uppercase.
how="How are you?"
u_how=how.upper()
print(u_how)

#ques 07 Convert the string How Is It Going? in lowercase.
low="How Is It Going?"
u_lower=low.lower()
print(u_lower)

#ques 08 Join the following list by spaces( ) and print the result.
#words = ['Python', 'is', 'easy', 'to', 'learn']

words = ['Python', 'is', 'easy', 'to', 'learn']
print(' '.join(words))

#ques 09 Print a multiline string using a single print
mul_str= '''
this
is multiline 
string and i'm
printing it using 
single print'''
print(mul_str)

#ques 10 Print this string to move to newline '\n' is used. (results should look exactly like the provided string)
new_str="to move to newline '\n' is used."
print(repr(new_str))