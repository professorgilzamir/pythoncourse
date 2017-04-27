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
import classes


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
    return '.'.join(filename)

def read_data(path):
	fdata = open(path, 'rt', encoding="utf8")
	data = []
	for linha in fdata:
		item = linha.split(',')
		endereco = Endereco(item[5], item[6], item[7], item[8])
		unidadeDeSaude = UnidadeDeSaude(item[0], item[1], item[2], item[3], item[9], item[10], item[11], endereco)
		data.append(unidadeDeSaude)
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
	db = {}

	for unidadeDeSaude in list:
		cidval = unidadeDeSaude.mget('codCid')
		cnesval = unidadeDeSaude.mget('codCnes')
		db[cidval+cnesval] = unidadeDeSaude

	return db;

def create_index_from(source, col_index):
	db = {}
	for unidadeDeSaude in source:
		index = ""
		for key in col_index:
			index += unidadeDeSaude.mget(key)
		db[index] = unidadeDeSaude
	return db;

def interpret(line_from_source, col_index, **kargs):
    line = []
    for key in kargs:
        idx = col_index[key]
        coltype = kargs[key]
        line.append(coltype(line_from_source[idx]))
    return line

def validarTelefone(telefone):
	t = telefone
	if ((len(t) == 13 or len(t) == 14) and (t[0] == '(' and t[3] == ')'))
		print "Telefone Validado"
	else
		raise NumeroDeTelefoneInvalido(1)



