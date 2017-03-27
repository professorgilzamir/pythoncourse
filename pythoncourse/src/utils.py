'''
Alterado on 27 de mar de 2017

Obtém dados em arquivos da internet

@author: André Oliveira
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
    string = ""
    return string.join(filename)

def loadlistfromcsv(path):
    fdata = open(path, 'rt', encoding="utf8")
    data = []
    for line in fdata:
        data.append(tuple(line.split(',')))
    fdata.close()
    return data


def create_cidcnes_index (fdata):
    data = {}
    for lin in fdata:
        data[str(lin[2]) + str(lin[3])] = lin
    return data
