import time

t = time.localtime(time.time())
localtime = time.asctime(t)
str = "La date et l'heure actuelle du cameroun est : " + time.asctime(t)

print(str)