import db
import Productos
import Clientes
import Ventas
import Pagos
import json
import Envios
import datetime

class App:
    prod = []
    clients = []
    ventas = []
    pagos = []
    json_data = {}
    envios = []
    def start(self):
        self.init_class()
        while True:
            print()
            o1 = input('''Seleccione una opccion:
        1- Gestion de productos
        2- Gestion de ventas
        3- Gestion de clientes
        4- Gestion de pagos
        5- Gestion de envios
        
        0- Salir 
---> ''')
            try:
                o1 = int(o1)
            except ValueError:
                print('Selecione una opcion valida\n\n')
                continue
            
            if o1 == 1:
                while True:
                    o2 = input('''Seleccione una opccion:
        1- Agregar un producto
        2- Buscar en el inventario
        3- Modificar un producto existente
        4- Eliminar un producto
        
        0- Volver
---> ''')
                    if o2 == '1':
                        self.agregar_productos()
                    elif o2 == '2':
                        self.mostrar_ordenados()
                    elif o2 == '3':
                        self.modificar_productos()
                    elif o2 == '4':
                        self.eliminar_productos()
                    elif o2 == '0':
                        break
                    else:
                        print('Selecione una opcion valida\n\n')
            elif o1 == 2:
                o6 = input('''Seleccione una opccion:
        1- Registrar una venta
        2- Generar factura
        3- Buscar ventas
        
        0- Volver
---> ''')
                if o6 == '1':
                    self.registrar_venta()
                elif o6 == '2':
                    self.generar_factura()
                elif o6 == '3':
                    self.buscar_ventas()
                elif o6 == '0':
                    break
                else:
                    print('Selecione una opcion valida\n\n') 
            elif o1 == 3:
                o7 = input('''Seleccione una opccion
    1- Registrar un cliente
    2- Modificar informacion de un cliente existente
    3- Eliminar un cliente
    4- Buscar clientes
    
    0- Volver
---> ''')
                if o7 == '1':
                    self.registrar_cliente()
                elif o7 == '2':
                    self.modificar_cliente()
                elif o7 == '3':
                    self.eliminar_cliente()
                elif o7 == '4':
                    self.buscar_clientes()
                elif o7 == '0':
                    break
                else:
                    print('Selecione una opcion valida\n\n')  
                    
            elif o1 == 4:
                o8 = input('''Seleccione una opccion:
        1- Registrar un pago
        2- Buscar Pagos 
        
        0- Volver
---> ''')
                try:
                    o8 = int(o8)
                except ValueError:
                    print('Introduzca un numero\n')
                
                if o8 == 1:
                    self.registrar_pagos()
                elif o8 == 2:
                    self.buscar_pagos()
                elif o8 == '0':
                    break
            elif o1 == 5:
                o9 = input('''Seleccione una opccion:
        1- Registrar un envio
        2- Buscar un envio
        
        0- Volver
---> ''')
                try:
                    o9 = int(o9)
                except ValueError:
                    print('Introduzca un numero\n')
                
                if o9 == 1:
                    self.registrar_envio()
                elif o9 == 2:
                    self.buscar_envio()
                elif o9 == '0':
                    break
                else:
                    print('Selecione una opcion valida\n\n')
            elif o1 == 0:
                print('-'*40)
                print('SE HA TERMINADO EL PROGRAMA')
                quit()
                
            
                                
    def mostrar_productos(self):
        for productos in self.prod:
            productos.show()
            print()
    
    def modificar_productos(self):

        self.mostrar_productos()
        
        idmod = input('''Introduzca 0 para volver o
Introduzca el id del producto a modificar: ''')
        
        while True:    
            if not idmod.isnumeric():
                idmod = input('''Introduzca 00 para volver o
Introduzca un id valido: ''')
            else:
                int(idmod)
                break   
            
        idmod = int(idmod)
        for producto in self.prod:
            if idmod == producto.id:
                print('\nProducto a modificar:\n')
                producto.show()
                
                while True:
                    o3 = input('''\nQue desea modificar:
1- nombre
2- descripcion
3- precio
4- categoria
5- inventario
6- carros a los que aplica

0- Volver
---> ''')
                    if o3 == '1':
                        print(f'Nombre actual: {producto.name}')
                        mod = input('\nNuevo nombre: ')
                        producto.name = mod
                        producto.show()
                        self.modificar_jsonprod('productos','name',idmod,mod)
                            
                        
                    elif o3 == '2':
                        print(f'Descripcion actual: {producto.description}')
                        mod = input('\nNueva descripcion: ')
                        producto.description = mod
                        producto.show()
                        self.modificar_jsonprod('productos','description',idmod,mod)
                        
                    elif o3 == '3':
                        print(f'Precio actual: {producto.price}')
                        mod = input('\nNuevo precio: ')
                        while True:
                            if mod.isnumeric():
                                int(mod)
                                producto.price = mod
                                producto.show()
                                break
                            mod = input('\nIngrese un numero: ')
                        self.modificar_jsonprod('productos','price',idmod,mod)
                        
                    elif o3 == '4':
                        print(f'Categoria actual: {producto.category}')
                        mod = input('\nNueva categoria: ')
                        producto.category = mod
                        producto.show()
                        self.modificar_jsonprod('productos','category',idmod,mod)
                        
                    elif o3 == '5':
                        print(f'Inventario actual: {producto.inventory}')
                        mod = input('\nNuevo inventario: ')
                        producto.inventory = mod
                        producto.show()
                        self.modificar_jsonprod('productos','inventory',idmod,mod)
                        
                    elif o3 == '6':
                        if 'compatible_vehicles' in producto:
                            print(f'Carros compatibles actual: {producto.compatible_vehicles}')
                            mod = input('\nNuevos carros compatibles: ')
                            producto.specify = mod
                            producto.show()
                        else:
                            print('Este producto no posee esta caracteristica')
                        self.modificar_jsonprod('productos','compatible_vehicles',idmod,mod)
                        
                    elif o3 == '0':
                        break
                    else:
                        print('Ingrese una opccion valida!')
                    
                break
            
    def agregar_productos(self):
        id = self.prod[-1].id +1
        name = input('Nombre: ')
        description = input('Descripcion: ')
        price = input('Precio: ')
        while  True:
            if price.isnumeric():
                int(price)
                break
            else:
                price = input('Introduzca un numero: ')
        categoria = input('Categoria: ')
        categoria = categoria.lower()
        inventario = input('Inventario: ')
        try:
            inventario = int(inventario)
        except ValueError:
            inventario = input('Introduzca un numero: ')
            
        while True:    
            h = input('''El producto que desea agregar es para un vehiculo/s especifico?
    1- Si
    2- No
---> ''')
            if h == '1':
                especy = []
                while True:
                    aux = input('Para que vehiculos es:')
                    ans = input('Es valido para otro vehiculo?\n\t1- SI\n\t2- NO\n\t---> ')
                    if ans == '2':
                        especy.append(aux)
                        break
                    especy.append(aux)
                
                self.prod.append(Productos.Prod_Especificos(id, name, description, price, categoria, inventario, especy))
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                data['productos'].append({
                'id': id,
                "name": name,
                "description": description,
                "price": price,
                "category": categoria,
                "inventory": inventario,
                "compatible_vehicles": especy
                })
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                
                break
            elif h == '2':
                self.prod.append(Productos.Prod(id, name, description, price, categoria, inventario))
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                data['productos'].append({
                'id': id,
                "name": name,
                "description": description,
                "price": price,
                "category": categoria,
                "inventory": inventario
                })
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)    
                break
            else:
                h = input('Introduca 1 para SI o 2 para NO')    
                                        
    def mostrar_ordenados(self):
        print('Filtros:')
        print('\t1- Categoria')
        print('\t2- Precio')
        print('\t3- Nombre')
        print('\t4- Disponibilidad en el inventario')
        o4 = input('---> ')
        if o4 == '1':
            categorias = []
            
            for i in self.prod:
                if not i.category in categorias:
                    categorias.append(i.category)
            
            a = 1
            for i in categorias:
                print(f'{a}- {i}')
                a += 1
                
            while True: 
                ans = input('---> ')   
                if ans.isnumeric() and int(ans) < a:
                    break
                else:
                   print('Introduzca un numero valido')
            
            for producto in self.prod:
                if producto.category == categorias[int(ans)-1]:
                    print('')
                    producto.show()
                    print('')
        
        if o4 == '2':
            print('\n\tEscriba un rango de precios: ')
            min = input('Precio menor: ')
            max = input('Precio mayor: ')
            for productos in  self.prod:
                if float(min) <= float(productos.price) <= float(max):
                    productos.show()

        if o4 ==  '3':
            name = input('Ingrese el nombre del producto: ')
            name = name.capitalize()
            for producto in self.prod:
                if producto.name == name:
                    print('')
                    producto.show()
        
        if o4 == '4':
            print('\n   Como desea buscar?')
            print('1- Productos sin inventario: ')
            print('2- Productos con poco inventario: ')
            o5 = input('---> ')
            if o5 == '1':
                for producto in self.prod:
                    if producto.inventory == '0':
                        print('')
                        producto.show()
            
            if o5 == '2':
                qtt = input('Quiere buscar productos con menos de cuanto inventario?:')
                a = 0
                while True:
                    if qtt.isnumeric():
                        break
                    else:
                        print('Introduzca un numero')

                for producto in self.prod:
                    if int(producto.inventory) < int(qtt):
                        print('')
                        producto.show()
                        a += 1
                if a == 0:
                    print(f'\n\tNO existen productos con menos de {qtt} de inventario\n')
                            
    def eliminar_productos(self):
        self.mostrar_productos()
        id = input('Introduzca el id del producto a eliminar: ')
        while True:    
            if not id.isnumeric():
                id = input('Introduzca un id valido: ')
            else:
                id = int(id)
                break   
        a = 0
        for producto in self.prod:
            if int(id) == producto.id:
                self.prod.remove(producto)
                print(f'\n\tEL producto con id {producto.id} se ha eliminado correctamente\n')
                a += 1
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                datosgood = []
                for i in data['productos']:
                    if i['id'] != id:
                        datosgood.append(i)     
                data['productos'] = datosgood
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                break
        if a == 0:
            print('El producto no existe')

    def registrar_cliente(self):
        while True:
            noj = input('''    1- Cliente Natural
    2- Cliente Juridico
    
    0- Volver
---> ''')
            if noj == '1':
                nombre = input('Nombre: ')
                apellido = input('Apellido: ')
                cedula = input('Cedula: ')
                while True:
                    if cedula.isnumeric():
                        break
                    else:
                        cedula = input('Introduzca una cedula valida: ')
                
                correo = input('Correo electronico: ')
                correo = self.comprobar_correo(correo)
                direccion = input('Direccion: ')
                telefono = input('Telefono: ')
                while True:
                    if telefono.isnumeric():
                        break
                    else:
                        telefono = input('Introduzca un numero valido: ')
               
                if not self.clients:
                    id = 1
                else:
                    id = self.clients[-1].id + 1
                
                self.clients.append(Clientes.Cliente_Natural(id,nombre, apellido, cedula, correo, direccion, telefono))
                print('\nCliente creado exitosamente\n')
                self.clients[-1].show()
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                data['clientes']['clientes_naturales'].append({
                    'id': self.clients[-1].id,
                    'name': self.clients[-1].name,
                    'apellido': self.clients[-1].apellido,
                    'cedula': self.clients[-1].cedula,
                    'correo': self.clients[-1].correo,
                    'direccion': self.clients[-1].direccion,
                    'telefono': self.clients[-1].telefono
                })
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                break
            
            elif noj == '2':
                
                nombre = input('Razón Social: ')
                rif = input('Rif: ')
                while True:
                    if rif.isnumeric():
                        break
                    else:
                        rif = input('Introduzca un Rif valida: ')
                
                correo = input('Correo electronico de la empresa: ')
                correo = self.comprobar_correo(correo)
                
                direccion = input('Direccion: ')
                
                telefono = input('Telefono de la empresa: ')
                
                while True:
                    if telefono.isnumeric():
                        break
                    else:
                        telefono = input('Introduzca un numero valido: ')
                
                namecont = input('Nombre persona de contacto: ')
                
                telfcont = input('telefono persona de contacto: ')
                while True:
                    if telfcont.isnumeric():
                        break
                    else:
                        telfcont = input('Introduzca un numero valido: ')
                        
                correocont = input('Correo persona de contacto: ')
                correocont = self.comprobar_correo(correocont)
                        
                if not self.clients:
                    id = 1
                else:
                    id = self.clients[-1].id + 1
                
                self.clients.append(Clientes.Cliente_Juridico(id,nombre, rif, correo, direccion, telefono, namecont, telfcont, correocont))
                print('\nCliente creado exitosamente: \n')
                self.clients[-1].show()
                
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                data['clientes']['clientes_juridicos'].append({
                    'id': id,
                    'Razon Social': nombre,
                    'Rif': rif,
                    'Correo electrónico': correo,
                    'Dirección': direccion,
                    'Teléfono': telefono,
                    'Nombre del contacto': namecont,
                    'Teléfono del contacto': telfcont,
                    'Correo electrónico del contacto': correocont
                    })
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                break
            
            elif noj == '0':
                break

    def modificar_cliente(self):
        while True:
            self.mostrar_clientes()
            id = input('Introduzca el id del cliente a modificar: ')
            while True:    
                if not id.isnumeric():
                    id = input('Introduzca un id valido: ')
                else:
                    int(id)
                    break   

            for cliente in self.clients:
                if int(id) == cliente.id:
                    print('\n\tCliente a modificar:')
                    cliente.show()
                    print('\n\tQue desea modificar?')
                    if type(cliente) == Clientes.Cliente_Natural:
                        type = 'cliente_natural'
                        print('1- Nombre')
                        print('2- Apellido')
                        print('3- Cedula')
                        print('4- Correo electronico')
                        print('5- Direccion')
                        print('6- Telefono')
                        o1 = input('---> ')
                        if o1 == '1':
                            nombre = input('Nuevo nombre: ')
                            cliente.name = nombre
                            self.modificar_jsoncli(type,'name', 'cliente', id,nombre)
                        elif o1 == '2':
                            apellido = input('Nuevo apellido: ')
                            cliente.lastname = apellido
                            self.modificar_jsoncli(type, 'lastname', 'cliente', id,apellido)
                        elif o1 == '3':
                            cedula = input('Nueva cedula: ')
                            while True:
                                if not cedula.isnumeric():
                                    cedula = input('Introduzca unicamente numeros: ')
                                else:
                                    break
                            cliente.identificacion = cedula
                            self.modificar_jsoncli(type, 'identificacion', 'cliente', id,cedula)
                        elif o1 == '4':
                            correo = input('Nuevo correo electronico: ')
                            correo = self.comprobar_correo(correo)
                            cliente.correo = correo
                            self.modificar_jsoncli(type, 'correo', 'cliente', id,correo)
                        elif o1 == '5':
                            direccion = input('Nueva direccion: ')
                            cliente.direccion = direccion
                            self.modificar_jsoncli(type, 'direccion', 'cliente', id, direccion)
                        elif o1 == '6':
                            telefono = input('Nuevo telefono: ')
                            while True:
                                if not telefono.isnumeric():
                                    telefono = input('Introduzca un telefono valido: ')
                                    break
                            cliente.telefono = telefono
                            self.modificar_jsoncli(type, 'telefono', 'cliente', id, telefono)
                    elif type(cliente) == Clientes.Cliente_Juridico:
                        type = 'cliente_juridico'
                        print('1- Razon Social')
                        print('2- Rif')
                        print('3- Correo electronico')
                        print('4- Direccion')
                        print('5- Telefono')
                        print('6- Nombre persona de contacto')
                        print('7- Telefono persona de contacto')
                        print('8- Correo persona de contacto')
                        o1 = input('---> ')
                        if o1 == '1':
                            nombre = input('Nueva razon social: ')
                            cliente.name = nombre
                            self.modificar_jsoncli(type,'name', 'cliente', id,nombre)
                        elif o1 == '2':
                            rif = input('Nuevo Rif: ')
                            while True:
                                if not rif.isnumeric():
                                    rif = input('Introduzca unicamente numeros: ')
                                else:
                                    break
                            cliente.identificacion = rif
                            self.modificar_jsoncli(type, 'identificacion', 'cliente', id, rif)
                        elif o1 == '3':
                            correo = input('Nuevo correo electronico: ')
                            correo = self.comprobar_correo(correo)
                            cliente.correo = correo
                            self.modificar_jsoncli(type, 'correo', 'cliente', id, correo)
                        elif o1 == '4':
                            direccion = input('Nueva direccion: ')
                            cliente.direccion = direccion
                            self.modificar_jsoncli(type, 'direccion', 'cliente', id, direccion)
                        elif o1 == '5':
                            telefono = input('Nuevo telefono: ')
                            while True:
                                if not telefono.isnumeric():
                                    telefono = input('Introduzca un telefono valido: ')
                                    break
                            cliente.telefono = telefono
                            self.modificar_jsoncli(type, 'telefono', 'cliente', id, telefono)
                        elif o1 == '6':
                            nombrecont = input('Nueva nombre de persona de contacto: ')
                            cliente.contacto = nombrecont
                            self.modificar_jsoncli(type, 'contacto', 'cliente', id, nombrecont)
                        elif o1 == '7':
                            telefonocont = input('Nuevo telefono de persona de contacto: ')
                            while True:
                                if not telefonocont.isnumeric():
                                    telefonocont = input('Introduzca unicamente numeros: ')
                                    break
                            cliente.contacto_telefono = telefonocont
                            self.modificar_jsoncli(type, 'contacto_telefono', 'cliente', id, telefono)
                        elif o1 == '8':
                            correocont = input('Nuevo correo de persona de contacto: ')
                            correo = self.comprobar_correo(correo) 
                            cliente.contacto_correo = correocont
                            self.modificar_jsoncli(type, 'contacto_correo', 'cliente', id, correo)

    def eliminar_cliente(self):
        self.mostrar_clientes()
        id = input('Introduzca el id del cliente a eliminar: ')
        while True:    
            if not id.isnumeric():
                id = input('Introduzca un id valido: ')
            else:
                id = int(id)
                break
        for cliente in self.clients:
            if cliente.id == id:
                self.clients.remove(cliente)
                if type(cliente) == Clientes.Cliente_Natural:
                    tipo = 'clientes_naturales'
                else:
                    tipo = 'clientes_juridicos'
                print('Cliente eliminado :')
                cliente.show()
                print('\nCliente eliminado exitosamente\n')
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                clientesgoods = [] #lista de clientes que no coiciden con el id del cliente a eliminar
                for cliente1 in data['clientes'][tipo]:
                    if cliente1['id'] != int(id):
                        clientesgoods.append(cliente1)
                        
                data['clientes'][tipo] = clientesgoods
                        
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                break
                
    def buscar_clientes(self):
        while True:
            print('Filtros:')
            print('\t1- Cedula o Rif')
            print('\t2- correo')
            print('\n\t0- salir')
            o = input('---> ')
            if o == '1':
                ident = input('Introduzca la cedula o rif: ')
                for cliente in self.clients:
                    if ident == cliente.identificacion:
                        cliente.show()
  
            elif o == '2':
                correo = input('Introduzca la correo: ')
                correo = self.comprobar_correo(correo)
                for cliente in self.clients:
                    if type(cliente) == Clientes.Cliente_Natural:
                        if correo == cliente.correo:
                            print('')
                            cliente.show()
                    elif type(cliente) == Clientes.Cliente_Juridico:
                        if correo == cliente.correo or correo == cliente.emailcont:
                            print('')
                            cliente.show()
            elif o == '0':
                break
            else:
                print('Opcion invalida')
    
    def mostrar_clientes(self):
        print('\n\tClientes:')
        for cliente in self.clients:
            print(f'ID: {cliente.id}')
            cliente.show()
            print('')

    def comprobar_correo(self, correo):
        while True:
            if '@' in correo and '.' in correo:
                return correo  # Si el correo es válido, lo devuelve
            else:
                correo = input('Introduzca un correo electrónico válido: ')
    
    def registrar_venta(self):
        prodventas = []
        qttventas = []
        while True:
            while True:
                if self.clients:
                    self.mostrar_clientes()
                    id_input = input('Introduzca el id del cliente que realizo la compra (o "exit" para salir): ')

                    if id_input.lower() == "exit":
                        print("Saliendo del programa.")
                        break
                   
                    try:
                        id_input = int(id_input)
                    except ValueError:
                        print('Introduzca un numero valido.')
                        continue  
                    
                    clientecom = next((client for client in self.clients if client.id == id_input), None) 

                    if clientecom:
                        print(f"Cliente encontrado: {clientecom.name}")
                        break
                    else:
                        print('El id del cliente no existe.')  
                else:
                    print('No hay clientes registrados.')  
                    break 
            while True:
                self.mostrar_productos()
                idp = int(input('Introduzca el id del producto que se vendio: '))
                for product in self.prod:
                    if product.id == idp:
                        product.show()
                        while True:
                            qtt = int(input('Introduzca la cantidad de producto que se vendio: '))
                            if qtt < product.inventory:
                                product.inventory -= qtt
                                print(f'Disponible: {product.inventory}')
                                prodventas.append(product)
                                qttventas.append(qtt)
                                break
                            elif qtt == product.inventory:
                                product.inventory -= qtt
                                print(f'Disponible: {product.inventory}')
                                prodventas.append(product)
                                qttventas.append(qtt)
                                for producto in self.prod:
                                    if int(idp) == producto.id:
                                        self.prod.remove(producto)
                                        print(f'\n\tEL producto con id {producto.id} se ha eliminado correctamente debido a que se acabo su inventario\n')
                                        with open('basedatos.json', 'r') as file:
                                            data = json.load(file)
                                        datosgood = []
                                        for i in data['productos']:
                                            if i['id'] != idp:
                                                datosgood.append(i)     
                                        data['productos'] = datosgood
                                        with open('basedatos.json', 'w') as file:
                                            json.dump(data, file, indent=2)
                                        break
                                break
                            else:
                                print('No hay stock disponible')
                o = input('''Se compro otro producto?:
    1- Si 
    2- No
---> ''')
                if o == "1":
                    pass
                else:
                    break
            
            print('Tipo de pago')
            print('\t1- De contado')
            if type(clientecom) == Clientes.Cliente_Juridico:
                print('\t2- A crédito 15 dias')
                print('\t3- A crédito 30 dias')
            o = input('---> ')
            if o == "1":
                tipo_pago = 'contado'
            elif o == "2":
                tipo_pago = 'credito 15 dias'
            elif o == "3":
                tipo_pago = 'credito 30 dias'
            while True:
                o = input('''Se va a pagar en efectivo?:
        1- Si 
        2- No
    ---> ''')
                if o == "1":
                    divisa = True
                    break
                elif o == "2":
                    divisa = False
                    break
                else:
                    print('Opcion invalida')
            while True:    
                o = input('''Metodo de envio:
    1- Zoom
    2- Delivery moto
---> ''')
            
                if o == "1":
                    envio = 'Zoom'
                    break
                elif o == "2":
                    envio = 'Delivery moto'
                    break
                else:
                    print('Opcion invalida')
                
            if not self.ventas:
                id = 1
            else:
                id = self.ventas[-1].id + 1
            fecha = str(datetime.date.today())
            prodventasdict = []
            for i,j in zip(prodventas, qttventas):
                    prodventasdict.append(i.dictionary(j))
                
            self.ventas.append(Ventas.Ventas(id, clientecom, prodventas, qttventas, tipo_pago, envio, fecha, divisa,0))
            self.ventas[-1].show()
            with open ('basedatos.json', 'r') as file:
                data = json.load(file)
            data['ventas'].append({'id': self.ventas[-1].id,
                                    'cliente': clientecom.dictionary(),
                                    'prductos comprados': prodventasdict,
                                    'metodo de pago': tipo_pago,
                                    'divisas': divisa,
                                    'metodo de envio': envio,
                                    'fecha': fecha })
            with open('basedatos.json', 'w') as file:
                json.dump(data, file, indent=2)
            break
        
    def generar_factura(self):
        for venta in self.ventas:
            venta.show()
            
        print('Introduzca el id de la venta para generar la factura')
        id = input('---> ')
        for venta in self.ventas:
            if venta.id == int(id):
                print(f'Factura de {venta.cliente.name}:')
                venta.show()
                namefact = f'Factura_de_{venta.cliente.name}_id_{venta.id}.json'
                print(f'{venta.dictionary()}')
                with open (namefact, 'w') as file:
                    json.dump(venta.dictionary(), file, indent=2)
        
    def buscar_ventas(self):
        while True:
            fechaventas = []
            self.mostrar_ventas()
            o = input('''Filtros: \n\t1- Cliente \n\t2- Fecha de venta''')
            if o == '1':
                self.mostrar_clientes()
                id = input('Introduzca el id del cliente: ')
                for venta in self.ventas:
                    if venta.cliente.id == int(id):
                        venta.mostrar_factura()
                        
            if o == '2':
                for venta in self.ventas:
                    if venta.fecha in fechaventas:
                        fechaventas.append(venta.fecha)
                a = 1
                print('Seleccione una fecha')
                for i in fechaventas:
                    print(f'{a}- {i}')
                    a += 1
                    
    def registrar_pagos(self):
        while True:
            if self.ventas:
                for i in self.ventas:
                    i.show()
                id = input('Introduzca el id de la venta(o exit para salir): ')
                try:
                    id = int(id)
                except ValueError:
                    print('Error, el id debe ser un número')
                if id != 'exit':
                    for venta in self.ventas:
                        if venta.id == id:
                            print(f'Factura de {venta.cliente.name}:')
                            venta.show()
                            montopago = input('Que monto se pago?')
                            try:
                                montopago = float(montopago)
                                if montopago > venta.total:
                                    print('El monto a pagar es mayor que el total de la venta')
                                else:
                                    venta.pagado = True
                                    venta.total_pagado += montopago
                                    print('Pago realizado con éxito')
                                    self.pagos.append(Pagos.Pago(venta.cliente,montopago, venta.es_divisa, venta.metodo_pago))
                                    self.pagos[-1].show()
                                    with open('basedatos.json', 'r') as file:
                                        data = json.load(file)
                                    data['pagos'].append(self.pagos[-1].dictionary())
                                    break
                            except ValueError:
                                print('Error, el monto debe ser un número')
                else:
                    break
            else:
                print('No hay ventas registradas')
                break
                                      
    def buscar_pagos(self):
        while True:
            print('Filtos')
            o = input('''   1- Clientes
    2- Fecha
    3- Tipo de Pago
    4- Moneda de Pago
---> ''')
            try:
                o = int(o)
            except ValueError:
                print('Introduzca un numero')
            
            if o == 1:
                self.mostrar_clientes()
                id = input('Introduzca el id del cliente: ')
                for pago in self.pagos:
                    if pago.cliente.id == int(id):
                        pago.show()
            elif o == 2:
                fechas = []
                for pago in self.pagos:
                    for fecha in pago.fecha_pago:
                        if not fecha in fechas:
                            fechas.append(fecha)
                a = 0 
                for i in fechas:
                    print(f'{a+1}- {i}')
                try:
                    o = input('En que fecha desea buscar: ')
                    int(o)
                except ValueError:
                    print('Introduzca un número')
                for pago in self.pagos:
                    if pago.fecha == fechas[a-1]:
                        pago.show()
            elif o == 3:
                tipos_pagos = []
                for pago in self.pagos:
                    if pago.tipo_pago in tipos_pagos:
                        tipos_pagos.append(pago.tipo_pago)
                a = 0
                for i in tipos_pagos:
                    print(f'{a+1}- {i}')        
                o = input('Introduzca el tipo de pago: ')
                for pago in self.pagos:
                    if pago.tipo_pago == tipos_pagos[o-1]: 
                        pago.show()
            elif o == 4:
                print('1- divisa\n2- bs')
                
                o = input('Introduzca la moneda de pago: ')
                for pago in self.pagos:
                    if pago.moneda == o:
                        pago.show()
            else:
                print('Opción no válida')
                                 
    def modificar_jsonprod(self,modificacion,clas,idmod,mod):
        with open('basedatos.json', 'r') as file:
            data = json.load(file)
        data[clas][idmod-1][modificacion] = mod
        with open('basedatos.json', 'w') as file:
            json.dump(data, file, indent=2)
            
    def modificar_jsoncli(self,type,modificacion,clas,idmod,mod):
        with open('basedatos.json', 'r') as file:
            data = json.load(file)
        data[clas][type][idmod-1][modificacion] = mod
        with open('basedatos.json', 'w') as file:
            json.dump(data, file, indent=2)
    
    def registrar_envio(self):
        paraenviar = []
        for i in self.ventas:
            if i.total_pagado == i.total:
                i.show()
                paraenviar.append(i)
            else:
                print('No se puede registrar el envio porque no se ha pagado la totalidad de la factura')
            
        o = input('Ingrese el id del envio a registrar')
        try:
            o = int(o)
        except ValueError:
            print('Opción no válida')
            
        for i in paraenviar:
            if o == i.id:
                i.show()
                direcion = i.cliente.direccion
                servicio = i.metodo_envio
                if servicio == 'Delivery moto':
                    motorizado = input('Ingrese el nombre del motorizado: ')
                else:
                    motorizado = 'N/A'

                precio = input('Precio del envio: ')
                try:
                    precio = float(precio)
                except ValueError:
                    print('Error, el precio debe ser un número')
                while True:
                    try:
                        fecha = input('Fecha de envío (DD-MM-YYYY): ')
                        fecha = datetime.datetime.strptime(fecha, '%d-%m-%Y')
                        break
                    except ValueError:
                        print('Error, la fecha debe ser en el formato DD-MM-YYYY')
                    
                if not self.envios:
                    id = 1
                else:
                    id = self.envios[-1].id + 1
                
                self.envios.append(Envios.Envio(id, i, servicio, precio, direcion, motorizado))
                
                with open('basedatos.json', 'r') as file:
                    data = json.load(file)
                data['envios'].append(self.envios[-1].dictionary())
                with open('basedatos.json', 'w') as file:
                    json.dump(data, file, indent=2)
                
    def init_class(self):
        for i in db.productos_api:
            if 'compatible_vehicles' in i:
                self.prod.append(Productos.Prod_Especificos(i['id'] ,i['name'] ,i['description'], i['price'], i['category'], i['inventory'], i['compatible_vehicles']))
            else:
                self.prod.append(Productos.Prod(i['id'] ,i['name'] ,i['description'], i['price'], i['category'], i['inventory']))
        
        self.json_data['productos'] = []
        self.json_data['pagos'] = []
        self.json_data['ventas'] = []
        self.json_data['envios'] = []
        
        for producto in self.prod:
            self.json_data["productos"].append({
                'id': producto.id,
                "name": producto.name,
                "description": producto.description,
                "price": producto.price,
                "category": producto.category,
                "inventory": producto.inventory,
                "compatible_vehicles": producto.compatible_vehicles,
            })
        self.clients.append(db.cliente_natural1)
        self.clients.append(db.cliente_natural2)
        self.clients.append(db.cliente_natural3)
        self.clients.append(db.cliente_juridico1)
        self.clients.append(db.cliente_juridico2)
        self.json_data['clientes'] = db.clientes_data
        with open("basedatos.json", 'w') as file:
            json.dump(self.json_data,file, indent=2)
