
def suma (a, b):
    return a + b

def resta (a, b):
    return a - b

def multiplicacion (a, b):
    return a * b

def division (a, b):
    return a / b


    
while True:
    try:
        a = int (input ("ingrese un numero: "))
        b = int (input ("ingrese otro numero: "))
        print (suma (a, b))    
        print (resta (a, b)) 
        print (multiplicacion (a, b))
        print (division(a, b)) 
    except ValueError:
        print ("Los datos ingresados solo pueden ser numeros")
    except Exception: 
        b == 0
        print ("No se puede dividir por 0")
