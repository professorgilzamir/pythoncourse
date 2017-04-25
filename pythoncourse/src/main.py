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
import entities
import os

def main():
    RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"

    if os == "Windows":
        OUTPUT_PATH = os.path.expanduser("~\saida.zip")
        EXTRACTED_PATH = os.path.expanduser("~\\")
    else:
        OUTPUT_PATH = os.path.expanduser("~/saida.zip")
        EXTRACTED_PATH = os.path.expanduser("~/")

    if len(sys.argv) > 1:
        RESOURCE_URL = sys.argv[1] 
    if len(sys.argv) > 2:
        OUTPUT_PATH = sys.argv[2]
    if len(sys.argv) > 3:
        EXTRACTION_PATH = sys.argv[3]
    

    '''
    dt = dw.loadlistfromcsv(RESOURCE_URL, OUTPUT_PATH, EXTRACTION_PATH)
    index = dw.create_index_from(dt, {'nom_stab':4})   

    line = index["POSTO DE SAUDE DE ANTA"]
    '''

    if (os.path.exists(OUTPUT_PATH) == 0):
        response = request.urlopen(RESOURCE_URL)
        out_file = io.FileIO(OUTPUT_PATH, mode="w")
        content_length = response.getheader('Content-Length')
        if content_length:
            length = int(content_length)
            dw.download_length(response, out_file, length)
        else:
            dw.download(response, out_file)

        response.close()
        out_file.close()

    zfile = zipfile.ZipFile(OUTPUT_PATH)
    zfile.extractall(EXTRACTED_PATH)
    filename = [name for name in os.listdir(EXTRACTED_PATH) if '.csv' in name]

    dt = dw.loadlistfromcsv(RESOURCE_URL, OUTPUT_PATH, EXTRACTED_PATH)
    # index = dw.create_cidcnes_index(dt[1:])
    index = dw.create_index_from(dt, {'codCid': 2})

    # ===========================================================================
    # try:
    # dw.validarTelefone("(88)992810740")
    # except NumeroTelefoneInvalido as nti:
    # print(nti._mensagem);
    # else:
    # print("Numero esta no formato correto")
    # ===========================================================================

    print("Finished")

if __name__ == "__main__":
    main()
