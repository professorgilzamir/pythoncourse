'''
Created on 9 de mar de 2017

Obtém dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8


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
    return '.'.join(filename.split('.')[0:len(filename.split('.'))-1])

def read_data(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data

def dicionario(listaLCSV):
    dic = {}
    for x in listaLCSV:
        dic['' + x[2] + x[3]] = x
    return dic

def pesquisa(str, dic):
    return dic[str]

def create_index_from(source, cl1= '', cl2= ''):
    dic = {}
    
    i1 = i2 = 0
    
    #print(args)
    
    for x in range(0, len(source[0])):
        if(source[0][x] == cl1):
            i1 = x
        if(source[0][x] == cl2):
            i2 = x
        
    if(i1 ==0 | i2 == 0): 
        print ("Colunas não existem")
        return 0
    
    #print(i1, i2)
    columns_index = { cl1:i1, cl2:i2 }
    for x in source:
        dic['' + x[ columns_index[ cl1 ]]  + x[ columns_index[ cl2 ]] ] = x
    return dic