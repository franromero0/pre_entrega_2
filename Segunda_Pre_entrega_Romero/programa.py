from clase_cliente import *
from pre_entrega_1 import *

base_datos = leerData()    #Traigo el archivo JSON para poder operar con esto
print("¡Bienvenido a la segunda entrega!")
print("Tienda on-line")
print("• Para comenzar es necesario que se registre.")
print("————————————————————————————————————————————↓↓↓↓↓↓——————————")
nombre,edad,pais,user,pw,email,intereses = registro(db)  #Reuno los datos del cliente en cuestión

db["usuario"] = user       
db["password"] = pw       
db["nombre"] = nombre       
db["edad"] = edad          #Agrego cada atributo del cliente a un diccionario que se almacenará en el .JSON.
db["pais"] = pais
db["e-mail"] = email
db["intereses"] = intereses                          
 
guardar_data(base_datos,db)  #Procedo a guardar los datos  obtenidos (db) en registro en el archivo JSON (base_datos)

print("A continuacion realizará la compra del producto que quieras en la tienda que elijas")
 
print("————————————————————————————————————————————————↓↓↓↓↓↓——————————")
producto = input("Ingrese el producto que desea comprar: ")
print("————————————————————————————————————————————————↓↓↓↓↓↓——————————")
tienda = input("En que tienda desea realizar la compra: ")                             #    Cliente realiza la primer compra de un producto en una tienda especifica

carrito_actual = []
cliente_actual = (Cliente(nombre,edad,pais,intereses,user,email,carrito_actual))     #Creación del objeto de clase Cliente con los datos obtenidos en registro

compra = cliente_actual.comprar(producto,tienda,carrito_actual) # Ejecucion del metodo comprar() de la clase Cliente.



while compra == True:
    
    if compra == True:
 
        prod_tienda = cliente_actual.añadircarrito()   # Ejecucion del metodo añadircarrito() de la clase Cliente.
        carrito_actual.append(prod_tienda)
 
        while True:
            for e in opciones:
                print(e)
            print("———————————————————————————————————————————————————————")
            cont = input("¿Qué acción desea realizar? 1, 2, 3 o 4") #¿Que accion quiere realizar?
            
            if cont == "1":
                prod_tienda = cliente_actual.añadircarrito()     #Ejecucion del metodo añadircarrito() de la clase Cliente.
                carrito_actual.append(prod_tienda)
                print("----------------------------------------")
                
            elif cont == "2":
                cliente_actual.removercarrito(carrito_actual)      #Ejecucion del metodo removercarrito() de la clase Cliente.
                print("----------------------------------------")
            elif cont == "3":
                print("----------------------------------------")
                print(f"Muchas gracias por comprar se ha enviado la factura detallada al e-mail: {cliente_actual.email}")
                print("----------------------------------------")
                compra = False
                break
            elif cont == "4":
                cliente_actual.vercarrito(carrito_actual)    
            else: cont = input("Es necesario que ingrese una de las opciones válidas con número: ")
    else:
        print("———————————————————————————————————————————————————————")
        print(f"Tu compra actual fue: {cliente_actual.vercarrito(carrito_actual)}")
        print("———————————————————————————————————————————————————————")
        print(f"Muchas gracias por comprar se ha enviado la factura al e-mail: {cliente_actual.email}")
        compra = False             




# Creación manual de clientes

cliente2 = Cliente("Francisco",23,"Argentina","PC, Programar, Futbol","franromero0","fran@hotmail.com",[]) #La lista vacía es donde deberían almacenarse los productos y tiendas (carrito_actual)
cliente3 = Cliente("Susana",44,"Argentina","Computación, Trekking", "susidep","susidep@hotmail.com",[])

#Los atributos corresponden a:

#cliente4 = Cliente("Nombre","Edad","Pais","Intereses","Nombre de usuario", "Email", "Productos que compró o carrito" )


