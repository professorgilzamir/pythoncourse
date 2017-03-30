'''
Created on 9 de mar de 2017

ALTERADO EM 15 DE MAR DE 2017!


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
    OUTPUT_PATH = "C:/eclipse/saida.zip"
    EXTRACTED_PATH = "C:/eclipse/" 
    if len(sys.argv) > 1:
       RESOURCE_URL = sys.argv[1] 
    if len(sys.argv) > 2:
        OUTPUT_PATH = sys.argv[2]
    if len(sys.argv) > 3:
        EXTRACTED_PATH = sys.argv[3]
    response = request.urlopen(RESOURCE_URL)
    out_file = io.FileIO(OUTPUT_PATH, mode="w")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        dw.download_length(response, out_file, length)
    else:
        dw.download(response, out_file)
    zfile = zipfile.ZipFile(OUTPUT_PATH)
    zfile.extractall(EXTRACTED_PATH)
    
    filename = [name for name in os.listdir(EXTRACTED_PATH) if '.csv' in name]
    
    
    dt = dw.loadlistfromcsv(EXTRACTED_PATH+filename[0])
    
    for t in dt:
        print(t) 
    
    print("Finished")
    
    #dic = dw.dicio(dt)
    
    columns_index = {'cod_munic': 2, 'cod_cnes': 3, 'nome_estab': 4, 'desc_endereco': 5}
    index = ('cod_munic', 'cod_cnes')
    
    dict = dw.create_index_from(dt, columns_index, index)
    
    for t in dict:
        print("{0} : {1} ".format(t, dict[t])) 
    
    response.close()
    out_file.close()
    print("Finished")

if __name__ == "__main__":
    main()
