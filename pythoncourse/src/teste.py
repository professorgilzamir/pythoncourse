
'''
sétima questão

referencia do calculo da distancia usado na função Dist
http://carlosdelfino.eti.br/cursoarduino/geoprocessamento/calculando-distancias-com-base-em-coordenadas-de-gps/

a função menorDistancia iria retornar uma lista ordenada de distancia

funcionando... pode ser adaptada para retornar o que for preciso, como a LocalizacaoGeografia ou um objeto referente a unidade de saude
'''

def menorDistancia (unit_health_ref, unit_health):
  dist = [];

  for unit in unit_health:
    DLA = abs(unit_health_ref.getLatitude() - unit.getLatitude());
    DLO = abs(unit_health_ref.getLongitude() - unit.getLongitude());
    DT = sqrt((DLA * 1.852)^2 + (DLO * 1.852)^2);
    if (DT > 0):
      dist.append(DT)

  return dist.sort()