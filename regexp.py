import re

#Return a list containing every occurrence of "ai":

txt = "The rain in Spain"
x = re.findall("[\w]+ai[\w]+", txt)
#print(x)

txt = "The rain in Spain"
x = re.search("pai", txt)
print(dir(x))
print("The first white-space character is located in position:", x.start())