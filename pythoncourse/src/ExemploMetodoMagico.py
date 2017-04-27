class Pessoa:
 def _init_(self):
     self.nome = "Gil"
 def mget(self, prop):
     return self._dict_[prop]
 def mset(self, prop, value):
     self._dict_[prop] = value
     
#import pessoa as mp
# p = mp.Pessoa();
# p.mset("nome","Pedro")
# print(p.mget("nome"))
