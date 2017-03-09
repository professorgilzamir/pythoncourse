'''
Created on 9 de mar de 2017

@author: Gilzamir Gomes
'''

# coding: utf-8

import io
import sys
import urllib.request as request
import download as dw


def main():
    RESOURCE_URL = "http://repositorio.dados.gov.br/saude/unidades-saude/unidade-basica-saude/ubs.csv.zip"

    if len(sys.argv) > 1:
       RESOURCE_URL = sys.argv[1] 
    response = request.urlopen(RESOURCE_URL)
    out_file = io.FileIO("saida.zip", mode="w")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        dw.download_length(response, out_file, length)
    else:
        dw.download(response, out_file)
    
if __name__ == "__main__":
    main()