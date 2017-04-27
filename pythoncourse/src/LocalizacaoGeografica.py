class LocalizacaoGeografica:

  def __init__(self, latitude, longitude):
    self._latidude = latitude
    self._longitude = longitude

  def getLatitude (self):
    return self._latitude

  def getLongitude (self):
    return self._longitude

  def setLatitude (self, value):
    self._latitude = value

  def setLongitude (self, value):
    self._longitude = value