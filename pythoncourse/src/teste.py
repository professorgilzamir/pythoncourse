
'''
referencia do calculo da distancia usado na função Dist
http://carlosdelfino.eti.br/cursoarduino/geoprocessamento/calculando-distancias-com-base-em-coordenadas-de-gps/

a função menorDistancia iria retornar uma lista ordenada de distancia

funcionando... pode ser adaptada para retornar o que for preciso, como a LocalizacaoGeografia ou um objeto referente a unidade de saude
'''

def menorDistancia (locationReferencia, locations):
  dist = [];

  for location in locations:
    dist.append(dist(locationReferencia, location))

  return dist.sort()

def dist (location1, location2):

  DLA = abs(location1.magicGet("latitude") - location2.magicGet("latitude"));
  DLO = abs(location1.magicGet("longitude") - location2.magicGet("longitude"));

  return sqrt((DLA * 1.852)^2 + (DLO * 1.852)^2);