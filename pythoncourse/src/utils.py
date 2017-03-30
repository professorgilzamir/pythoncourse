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
    return filename.split('.')
    del filename[len(filename) - 1]
    string = ""
    return string.join(filename)



def loadlistfromcsv(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data


def dicio(lista):
    data = {}
    for line in lista:
        index = (str(line[2]) + str(line[3]))
        data[index] = line
    return data



def create_index_from(source, columns_index, columns):
    t = []
    for i in columns:
        for j in columns_index:
            if i in j:
                t.append(columns_index[i])   #pegando as chaves para saber quais colunas concatenar
                
    
    data = {}
    cont = 1
    for line in source:
        index = ''
        for i in t:
            index = str(index) + str(line[i]) #concatena todas as colunas enviadas
        data[index] = cont
        
        cont = cont + 1
    
    return data
        
    
            
                
    
    
    
    
        
    