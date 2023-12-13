
import json
ruta_archivo = "D:\DATOS DE USUARIO SUSI\Desktop\Pre_entrega_2_Romero\Segunda_Pre_entrega_Romero"  ##Cambiar

opciones = ["1. Agregar producto al carrito ",
            "2. Remover producto del carrito ",
            "3. Finalizar compra ",
            "4. Ver carrito actual "]



def registro(diccionario):
  nombre = input("• Ingrese su nombre: ")
  print("———————————————————————————————————————————————————————")
  edad = int(input("• Cual es su edad: "))
  print("———————————————————————————————————————————————————————")
  pais = input("• ¿De que país eres? ") 
  print("———————————————————————————————————————————————————————")           #Pide los datos necesarios para el registro
  email = input("• Ingrese su e-mail: ")
  print("———————————————————————————————————————————————————————")
  intereses = input("• ¿Que le interesaria ver en la página? Detalle: ")
  print("———————————————————————————————————————————————————————")
  print("———————————————————————————————————————————————————————")   
  while True:
    user = input("Por favor ingrese su nombre de usuario: ")
    if user in diccionario:                                        #Busca si el nombre esta en el dict para no repetirlo.
      print("Ese nombre de usuario ya está en uso. Prueba con otro")
    else:
      break
  x = True
  while x:
    print("-------------------------------------------------------")
    print("Es necesario que la contraseña tenga más de 6 carácteres")          #Validacion +6 caracteres.
    print("-------------------------------------------------------")
    pw = input("Ingrese su contraseña: ")
    if len(pw)>=6:
      validacion_pw = input("Confirme su contraseña: ")
      if validacion_pw == pw:
        print("-------------------------------------------------------")
        print("¡Registrado con exito!")
        print("———————————————————————————————————————————————————————")
        print(f"Bienvenido {nombre}")
        x = False
        
        return nombre,edad,pais,user,pw,email,intereses                                            
      elif validacion_pw != pw:
       while validacion_pw != pw:
          print("Las contraseñas no coinciden")
          validacion_pw = input("Confirme su contraseña nuevamente: ")
          if validacion_pw == pw:                                           #Validacion si es que no coinciden
            print("¡Registrado con exito!")
            print("-------------------------------------------------------")
            print(f"Bienvenido {nombre}")
            print("———————————————————————————————————————————————————————")
            
            x = False
    else: print("¡Es muy corta!")
  return nombre,edad,pais,user,pw,email,intereses



def login(diccionario):                                               #Funcion de la primer pre-entrega, no se utiliza en el programa.
  print("       Es necesario que inicie sesión")
  print("———————————————————————————————————————————————————————")
  user = input("Ingrese su usuario: ")
  if user in diccionario:
    while True:
      pw = input("Ingrese su contraseña: ")
      if diccionario.get(user) == pw:
        print("———————————————————————————————————————————————————————")
        print("       ¡Ha iniciado sesión!")
        print("———————————————————————————————————————————————————————")
        print(f"       Bienvenido nuevamente ¡{user}!")
        return True                                  
        break
      else:
        print("Contraseña incorrecta, intentelo de nuevo.")
                                                   
  else:
    print("El usuario no está registrado")
    print("———————————————————————————————————————————————————————")
    print("Por favor, registrese para continuar")
    print("———————————————————————————————————————————————————————")
    print("———————————————————————————————————————————————————————")
    registro(diccionario)                                   #    VER
    
  
    #JSON -- Correcciones de la primera pre-entrega
db = {}
lista_vieja = []

def leerData():
  
  try:
      with open(ruta_archivo+"\segunda_pre_entrega_Romero_Francisco.json","r",encoding='utf-8') as f:   #VER RUTA
        base_datos = json.load(f)
        return base_datos
  except json.decoder.JSONDecodeError:
    print(f"La lista está vacía registrate para dejar tus datos. ¡Debes guardar información primero!")
    base_datos = []
    return base_datos
    
  except FileNotFoundError:
    print("La lista no se encontro o está vacia aún")
    base_datos = []
    return base_datos
    
def guardar_data(base_datos,diccionario):
  with open(ruta_archivo+"\segunda_pre_entrega_Romero_Francisco.json","w",encoding='utf-8') as f:  #VER RUTA
    base_datos.append(diccionario)
    cadena_json = json.dumps(base_datos,indent=2)
    f.write(cadena_json)
    
  


