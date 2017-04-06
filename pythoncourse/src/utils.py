'''
Created on 9 de mar de 2017

Obtém dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
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
    filename = filename.split('.')
    del filename[len(filename) - 1]
    return ".".join(filename)

def loadlistfromcsv(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data

def create_cidcnes_index (fdata):
    data = {}
    for line in fdata:
        key = str(line[2]) + str(line[3])
        data[key] = line
    return data

def create_index_from (source, columns_index, *args):
    for arg in args:
        if (columns_index.get(arg) == None):
            return False;
    size = len(source)
    for column in columns_index:
        if (column < 0 and column >= size):
            return False
    data = {}
    for line in source:
        key = ""
        for arg in args:
            key = key + str(line[columns_index[arg]])
        data[key] = line
    return data

def interpret (line_from_source, columns_index, **kargs):
    size = len(line_from_source)
    for column in columns_index:
        if (column < 0 and column >= size):
            return False;
    for karg in kargs:
        if (kargs[karg] == 'int'):
            line_from_source[columns_index[karg]] = int(line_from_source[columns_index[karg]])
        else:
            line_from_source[columns_index[karg]] = line_from_source[columns_index[karg]] 
    return line_from_source