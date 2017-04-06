'''
Created on 20 de mar de 2017

@author: thiag
'''

line = ("123", "456", "789")
index = str(line[0]) + str(line[1])
print(index)
data = {}
data[str(line[0]) + str(line[1])] = "thiago"
data[str(line[1]) + str(line[1])] = "thiago"

print(data)