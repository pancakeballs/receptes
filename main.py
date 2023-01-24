def izmaksas_receptei(recepte, cena):
  summa = 0
  for sastavdala, daudzums in recepte.items():
    summa += daudzums * cena[sastavdala]
  return summa

def izmaksas_kopa(abolusvars):
  recepte = {"cukurs": 0.6, "kanelis": 0.08, "aboli": 2.0, "udens": 0.2}
  cenas = {"cukurs": 0.75, "kanelis": 30.0, "aboli": 0.0, "udens": 0.0}
  izmaksaskg = izmaksas_receptei(recepte, cenas) / recepte["aboli"]
  return abolusvars * izmaksaskg

aboli = 2.6
print("Uz {} kg ābolu izmaksas būs {} EUR".format(aboli, izmaksas_kopa(aboli)))