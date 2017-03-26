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

