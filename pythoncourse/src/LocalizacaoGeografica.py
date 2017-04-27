class LocalizacaoGeografica:

  def __init__(self, latitude, longitude):
    self._latidude = latitude
    self._longitude = longitude

  def magicGet(self, atrib):
    if atrib == 'latitude':
      return self._latidude
    elif atrib == 'longitude':
      return self._longitude
    else:
      return None

  def magicSet(self, atrib, value):
    if atrib == 'latitude':
      self._latitude = value
    elif atrib == 'longitude':
      self._longitude = value
