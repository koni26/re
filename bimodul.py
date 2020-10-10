""" in this module I am gonna do some practise with 
imported python module called as re. some exapmles
to search given text within a specific text will follow"""


#lets begin with importing module to use its features
import re


#firstly defining text variable to search within
text= "Python is a programming language \t that is \n object-oriented."

#here defining variable to look for as an object
#we ll check for some of whitespaces    
lookws= re.compile(r"\s")

#iteration goes to result variable that we can check every occurence in a loop
result_ws= lookws.finditer(text)

#here is dictionary for some of whitespace chars that are involved in main text
whitespacechars={" ": "space","\t":"tab","\n":"line"}


#this loop is printing corresponding value in dictionary of found wspace value
#and also mention its location
for i in result_ws:
    print("'" + whitespacechars[i.group(0)] + "' --> found at start point: " + str(i.start()) + " and end point: " + str(i.end()))

#lets have a look another great feature
#naming the grouped matches and calling them
#we are gonna look for first and second alphanumerics

firstsecond=re.compile(r"(?P<first>\w+) (?P<second>\w+)")
result_fs=firstsecond.match(text)
dic=result_fs.groupdict()
# #now lets call first item from dictionary
print(dic["first"])
print(dic["second"])

#printing a word start with P and end with n
specificword=re.compile(r"\bP.*n\b")
result_sw=specificword.search(text)
print(result_sw.group())

#lets split text with matched strings
splitword=re.compile(r"\s+ *\s*")
result_spw=splitword.split(text)
print(result_spw)

#and this counts user-typed occurences in text
typed=input("Type text you wanna search: ")
typed_text=re.compile(typed)
result_tt=typed_text.findall(text)
print(result_tt)
print("No of occurence of " + typed + " is " + str(len(result_tt)))


#you can see these also on github below link;
#   https://github.com/koni26/re
