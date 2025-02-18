def diviser(a , b):
    try:
        r = a / b
        print(r)
    except ZeroDivisionError:
        print('Erreur : Division par z e r o !')
    
    finally:
        print('Fin de l’ e x c u t i o n .')
diviser(100, 7)
diviser(10, 0)
