nombres = input("Entez des nombres en separant par des espaces svp : ")
nombres = [int(nombre) for nombre in nombres.split()]
maximum = max(nombres)
print("par comparason, on peut en deduire que le maximum des nombres saisis est :", maximum)
