'''
Created on 05 de abr de 2017
Obtém dados em arquivos da internet
@author: Gilzamir (gilzamir@outlook.com)
modificado por Luis Costa
'''

#coding: utf-8

import string

BUFF_SIZE = 1024

def download_length(response, output, length):
    times = length/BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times = times + 1
    for time in range(int(times)):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d " % (((time * BUFF_SIZE)/100.0) * 100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))

        
def extract_filename(filename):
    arquivo = filename.split('.') 
    s = ""
    for x in range(0, len(arquivo) - 1):
        if (x == 0):
            s += arquivo[x]
        else :
            s += "." + arquivo[x]
    return s

		
def load_data(arquivo):
		dados = open(path, 'rt', encoding="utf8")
		
		
def loadlistfromcsv (path):
	  arquivo = open(path, 'rt', encoding="utf8")
		data = []
		
		for x in arquivo:
			linedata = x.split(',')
			data.append(tuple(linedata))
			
		arquivo.close()
		return data
		
def create_cidcnes_index (data):
	dic = {}
	for linha in data:
		dic[linha[2] + linha[3]] = linha
		
	return dic
""" questao 1 lista 3"""
def create_index_from(source, columns_index, columns):
	dic = {}	
	
	for i in source:
		s = ""
		for j in columns:
			s += i[column_index[j]]
		dic[s] = i

	return dic		
""" fim questao 1 lista 3"""


""" questao 3 lista 3"""
def interpret(line_from_source, columns_index, **kargs):
	for i, j in kargs:
		if j == "int":
			line_from_source[columns_index[i]] = int(line_from_source[columns_index[i]])

	return line_from_source
""" fim questao 3 lista 3"""
