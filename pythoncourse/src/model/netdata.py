'''
Created on 9 de mar de 2017

Obtem dados em arquivos da internet

@author: Gilzamir (gilzamir@outlook.com)
'''

#coding: utf-8

import urllib.request as request
import zipfile
import io
import os
import re
import model
import sys

BUFF_SIZE = 1024

class NetDataModel():
    def download_length(self, response, output, length):
        times = length/BUFF_SIZE
        if length % BUFF_SIZE > 0:
            times = times + 1
        for time in range(int(times)):
            output.write(response.read(BUFF_SIZE))
            print("Downloaded %d " % (((time * BUFF_SIZE)/100.0) * 100))

    def download(self, response, output):
        total_downloaded = 0
        while True:
            data = response.read(BUFF_SIZE)
            total_downloaded += len(data)
            if not data:
                break
            output.write(data)
            print('Downloaded {bytes}'.format(bytes=total_downloaded))

    def extract_filename(self, filename):
        filename = filename.split('.')
        del filename[len(filename) - 1]
        return '.'.join(filename)

    def read_data(self, path):
        fdata = open(path, 'rt', encoding="utf8")
        data = []
        for line in fdata:
            ld = line.split(',')
            
            ender = model.Endereco(ld[5], ld[6], ld[7], ld[8])
            unit_health = model.UnidadeDeSaude(ld[0], ld[1], ld[2], ld[3], ld[4], ender, ld[9], ld[10], ld[11], ld[12])
            
            data.append(unit_health)
        fdata.close()
        return data

    def validarTelefone(self, telefone):
        if not re.match('\(\d{2}\)\d{8,9}$', telefone):
            raise model.NumeroTelefoneInvalido(telefone, "Telefone Inválido")

    def loadlistfromcsv(self, URL, OUTPUT_PATH="dt.zip", EXTRACTION_PATH="./"):
        response = request.urlopen(URL)
        content_length = response.getheader('Content-Length')
        out_file = io.FileIO(OUTPUT_PATH, mode="w")    

        if content_length:
            length = int(content_length)
            self.download_length(response, out_file, length)
        else:
            self.download(response, out_file)
        zfile = zipfile.ZipFile(OUTPUT_PATH)
        zfile.extractall(EXTRACTION_PATH)
        filename = [name for name in os.listdir(EXTRACTION_PATH) if '.csv' in name]
        dt = self.read_data(EXTRACTION_PATH+filename[0])
        response.close()
        out_file.close()
        return dt

    def create_cidcnes_index(self, list):
        db = {}
        for obj in list:
            cidval = obj.magicGet('codCid')
            cnesval = obj.magicGet('codCnes')
            print(type(obj))
            db[cidval+cnesval] = obj
        return db;

    def create_index_from(self, source, col_index):
        db = {}
        for obj in source:
            index = ""
            for key in col_index:
                index += obj.magicGet(key)
            db[index] = obj
        return db;

    def interpret(self, line_from_source, col_index, **kargs):
        line = []
        for key in kargs:
            idx = col_index[key]
            coltype = kargs[key]
            line.append(coltype(line_from_source[idx]))
        return line

    def syncdata(self):
        RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"
        
        if os == "Windows":
            OUTPUT_PATH = os.path.expanduser("saida.zip")
            EXTRACTED_PATH = os.path.expanduser("~\\")
        else:
            OUTPUT_PATH = os.path.expanduser("saida.zip")
            EXTRACTED_PATH = os.path.expanduser("~/")

        if len(sys.argv) > 1:
            RESOURCE_URL = sys.argv[1] 
        if len(sys.argv) > 2:
            OUTPUT_PATH = sys.argv[2]
        if len(sys.argv) > 3:
            EXTRACTION_PATH = sys.argv[3]
        self.repository = self.loadlistfromcsv(RESOURCE_URL, OUTPUT_PATH, EXTRACTED_PATH)

    def searchNearUnitHealth(self, longitude, latitude):
        print("Ainda não implementado")
        pass

    def searchAllUnitHealth(self):
        print("Ainda não implementado")
        pass

    def __init__(self):
        self.repository = []
