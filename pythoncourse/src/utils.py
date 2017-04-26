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
import entities
import re

from src.Endereco import Endereco
from src.UnidadeDeSaude import UnidadeDeSaude
from src.NumeroTelefoneInvalido import NumeroTelefoneInvalido

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
    atrib = line.split(',')
    address = Endereco(atrib[5], atrib[6], atrib[7], atrib[8])
    unit_health = UnidadeDeSaude(atrib[0], atrib[1], atrib[2], atrib[3], atrib[9], atrib[10], atrib[11], address)
    data.append(unit_health)

  fdata.close()
  return data

def loadlistfromcsv(URL, OUTPUT_PATH, EXTRACTION_PATH):
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
    dt = read_data(EXTRACTION_PATH+filename[0])
    response.close()
    out_file.close()
    return dt

def create_cidcnes_index(list):
    db = {}

    for obj in list:
        cidval = obj.getCodCid()
        cnesval = obj.gtCodCnes()
        db[cidval+cnesval] = obj
    return db

def create_index_from(source, col_index):
    db = {}

    for obj in source:
        index = ""
<<<<<<< HEAD
        for atrib in col_index:
          if atrib == 'latitude':
            index += obj.getLatitude()
          elif atrib == 'longitude':
            index += obj.getLongitude()
          elif atrib == 'codCid':
            index += obj.getCodCid()
          elif atrib == 'codCnes':
            index += obj.getCodCnes()
          elif atrib == 'dscEstFisAmb':
            index += obj.getDscEstFisAmb()
          elif atrib == 'dscAdapFisldo':
            index += obj.getDscAdapFisldo()
          elif atrib == 'sitEquipamentos':
            index += obj.getSitEquipamentos()
          elif atrib == 'endereco':
            index += obj.getEndereco()

        db[index] = obj
    return db

def interpret(line_from_source, col_index, **kargs):
    line = []
    for key in kargs:
        idx = col_index[key]
        coltype = kargs[key]
        line.append(coltype(line_from_source[idx]))
    return line

def validarTelefone(phone):
  if not re.match('\(\d{2}\)\d{8,9}$', phone):
    raise NumeroTelefoneInvalido(1)

def menorDistancia (unit_health_ref, unit_health):
  dist = [];

  for unit in unit_health:
    DLA = abs(unit_health_ref.getLatitude() - unit.getLatitude());
    DLO = abs(unit_health_ref.getLongitude() - unit.getLongitude());
    DT = sqrt((DLA * 1.852)^2 + (DLO * 1.852)^2);
    if (DT > 0):
      dist.append(DT)

  return dist.sort()
