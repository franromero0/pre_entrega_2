class Persona: 
    def __init__(self,nombre,edad,pais,intereses):   # Crear clase para los datos basicos 
        self.nombre = nombre
        self.edad = edad
        self.pais = pais
        self.intereses = intereses
        
class Cliente(Persona): 
    def __init__(self,nombre,edad,pais,intereses,usuario,email,carrito):
        super().__init__(nombre,edad,pais,intereses)
        self.usuario = usuario
        self.email = email
        self.carrito = carrito
        
    def __str__(self):
        return f"¡Se ha creado el cliente '{self.nombre}' con éxito!"
    
    def verdatos(self):
        cldata = [
                f"Nombre: {self.nombre}",
                f"Nombre de Usuario: {self.usuario}",
                f"Correo electronico: {self.email}",
                f"Edad: {self.edad}",
                f"País: {self.pais}",
                f"Intereses: {self.intereses}"
               ]
        for d in cldata:
             print(d) 
        return cldata
        
    def comprar(self,producto,tienda,lista): # comprar un producto en especifico y los guarda en la lista brindada en este caso carrito_actual.
        self.producto = producto
        self.tienda = tienda
        self.lista = lista
        self.tupla = (self.producto,self.tienda)
        print("———————————————————————————————————————————————————————")
        print(f"El cliente {self.nombre} ha realizado la compra de {self.producto} en {self.tienda}")
        print("———————————————————————————————————————————————————————")
        self.lista.append(self.tupla)
        print("----------------------------------------")
        d1 = input("¿Desea realizar otra compra? Si / No   ")
        print("----------------------------------------")
    
        while True:
            if d1.lower() == "si":
                return True
                break
            elif d1.lower() == "no":
                return False
                break
            else: d1 = input("Es necesario que conteste por SI o NO")
            
    
    def añadircarrito(self): # añadir mas de un producto especifico al carrito
        print("----------------------------------------")
        producto = input("¿Que producto desea añadir al carrito? ")
        print("----------------------------------------")
        tienda = input("¿En que tienda desea realizar la compra? ")
        tupla = (producto,tienda)
        print("----------------------------------------")
        print(f"Haz añadido al carrito de {tienda} el producto: {producto}")
        print("----------------------------------------")
        return tupla #Devuelve una tupla producto,tienda para agregar al carrito de la sesion
    
    def removercarrito(self,lista): # metodo donde argumentos son el producto y la tienda ya en una lista son eliminados de la misma.
        self.lista = lista
        prod_remover = input("¿Que producto desea remover? ")
        tienda = input("Ingrese tienda donde compro: ")
        carro = (prod_remover,tienda)
        if (carro) in self.lista:
            self.lista = self.lista.remove(carro)    
            print("----------------------------------------")
            print(f"El producto {prod_remover} ha sido eliminado del carrito")
            print("----------------------------------------")
        else: 
            print("----------------------------------------")
            print("¡El producto no se encontró en el carrito!")
            print("----------------------------------------")
        
    def vercarrito(self,carrito):
        self.carrito = carrito
        print("----------------------------------------")
        for tupla in self.carrito:
            print(f"Compró {tupla[0]} en {tupla[1]} ")
            print("----------------------------------------")
        return self.carrito
        #print(f"Su compra hasta ahora es: {self.carrito}")
        #print("----------------------------------------")
        print("———————————————————————————————————————————————————————")
        
 

            
    