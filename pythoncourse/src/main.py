'''
Created on 9 de mar de 2017
Alterado em 16 de mar de 2017
@author: Gilzamir Gomes
'''

# coding: utf-8

import io
import sys
import urllib.request as request
import zipfile
import utils as dw
import os

def main():
    RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"
    OUTPUT_PATH = "./dt.zip";
    EXTRACTION_PATH = "./"

    if len(sys.argv) > 1:
        RESOURCE_URL = sys.argv[1] 
    if len(sys.argv) > 2:
        OUTPUT_PATH = sys.argv[2]
    if len(sys.argv) > 3:
        EXTRACTION_PATH = sys.argv[3]
    
    dt = dw.loadlistfromcsv(RESOURCE_URL, OUTPUT_PATH, EXTRACTION_PATH)
    index = dw.create_index_from(dt, {'nom_stab':4})   

    line = index["POSTO DE SAUDE DE ANTA"];
    
    print(line)
    print("Finished")

if __name__ == "__main__":
    main()
