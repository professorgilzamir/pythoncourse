'''
Created on 23 de mar de 2017

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

        
def extract_filename(filename):
    filename = filename.split('.')
    del filename[len(filename) - 1]
    string = ""
    return string.join(filename)

def read_data(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data


