'''
Created on 9 de mar de 2017

Obtém dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8

import urllib.request as request
import zipfile
import io
import os


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

def loadlistfromcsv(filename):
    filename = filename.split('.')
    del filename[len(filename) - 1]
    return '.'.join(filename)

def read_data(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        linedata = line.split(',')
        data.append(tuple(linedata))
    fdata.close()
    return data

def loadlistfromcsv(URL, OUTPUT_PATH="./dt.zip", EXTRACTION_PATH="./"):
    response = request.urlopen(URL)
    content_length = response.getheader('Content-Length')
    out_file = io.FileIO(OUTPUT_PATH, mode="w")    

    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    zfile = zipfile.ZipFile(OUTPUT_PATH)
    zfile.extractall(EXTRACTION_PATH)
    filename = [name for name in os.listdir(EXTRACTION_PATH) if '.csv' in name]
    dt =  read_data(EXTRACTION_PATH+filename[0])
    response.close()
    out_file.close()
    return dt

def create_cidcnes_index(list):
    cididx = 2
    cnesidx = 3
    db = {}
    for line in list:
        cidval = line[cididx]
        cnesval = line[cnesidx]
        db[cidval+cnesval] = line
    return db;

def create_index_from(source, col_index):
    db = {}
    for line in source:
        index = ""
        for  col in col_index:
            index += line[col_index[col]]
        db[index] = line
    return db;

def interpret(line_from_source, col_index, **kargs):
    line = []
    for key in kargs:
        idx = col_index[key]
        coltype = kargs[key]
        line.append(coltype(line_from_source[idx]))
    return line


