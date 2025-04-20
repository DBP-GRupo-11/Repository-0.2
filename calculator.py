def division(a,b):
    if b != 0:
        return a/b


calc = int(input("Bienvenido a la calculadora por favor ingrese la operación que desee:" \
"1: Suma" \
"2:Resta" 
"3:Multiplicacion"
"4:Division"))

if calc == 1:
    primer_t = int(input("Ingrese el primer termino"))
    segundo_t = int(input("Ingrese el segundo termino"))


elif calc == 4:
    primer_t = int(input("Ingrese el primer termino"))
    segundo_t = int(input("Ingrese el segundo termino"))
    print(division(primer_t,segundo_t))
    


