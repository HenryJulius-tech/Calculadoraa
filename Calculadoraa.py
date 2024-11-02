#Henry Camargo
#cristian miranda
#diego sanjuan
#marleinis orozco
#Antonio bravo 
#Brayan Amaya
def suma(num1, num2):
    
    return num1 + num2 

def resta(num1, num2):
    
    pass  

def multiplicacion(num1, num2):
    
    return num1 * num2

def division(num1, num2):

    pass  

def potencia(num1, num2):
   
    pass  

def raiz_cuadrada(num1):
    
    pass  

print("Bienvenido a la calculadora")
print("Elija una operación escribiendo su nombre:")
print("suma, resta, multiplicacion, division, potencia, raiz cuadrada")

operacion = input("Ingrese la operación deseada: ").lower()

if operacion in ["suma", "resta", "multiplicacion", "division", "potencia"]:
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    # Operacion suma - Cristian Miranda
    if operacion == "suma":
        resultado = suma(num1, num2)
        print("Resultado de la suma:", resultado)

#Operacion multiplicacion - Marleinis Orozco
    elif operacion == "multiplicacion":
        resultado = multiplicacion(num1, num2)
        print("Resultado de la multiplicacion:", resultado)