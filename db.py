import requests
import Clientes
r = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/products.json')

productos_api = r.json()
#se crean clientes para realizar pruebas en el programa
cliente_natural1 = Clientes.Cliente_Natural(1,"Juan","Pérez",'12345678',"juan.perez@example.com","Calle Falsa 123, Ciudad","0412-3456789")

cliente_natural2 = Clientes.Cliente_Natural(2,"María","Gómez",'87654321',"maria.gomez@example.com","Avenida Siempre Viva 742, Ciudad","0414-9876543")

cliente_natural3 = Clientes.Cliente_Natural(3,"Carlos","Rodríguez",'11223344',"carlos.rodriguez@example.com","Calle de la Paz 456, Ciudad","0416-1234567")

cliente_juridico1 = Clientes.Cliente_Juridico(4,"Compañía ABC, C.A.",'12345678-9',"contacto@companiaabc.com","Avenida Libertador 1000, Ciudad","0212-3456789","Ana Martínez","0412-3456789","ana.martinez@companiaabc.com")

cliente_juridico2 = Clientes.Cliente_Juridico(5,"Servicios XYZ, S.A.",'98765432-1',"info@serviciosxyz.com","Calle Principal 200, Ciudad","0212-9876543","Luis Fernández","0414-9876543","luis.fernandez@serviciosxyz.com")

clientes_data = {
    "clientes_naturales": [
        {
            "id": 1,
            "nombre": "Juan",
            "apellido": "Pérez",
            "cedula": 12345678,
            "correo": "juan.perez@example.com",
            "direccion": "Calle Falsa 123, Ciudad",
            "telefono": "0412-3456789"
        },
        {
            "id": 2,
            "nombre": "María",
            "apellido": "Gómez",
            "cedula": "87654321",
            "correo": "maria.gomez@example.com",
            "direccion": "Avenida Siempre Viva 742, Ciudad",
            "telefono": "0414-9876543"
        },
        {
            "id": 3,
            "nombre": "Carlos",
            "apellido": "Rodríguez",
            "cedula": "11223344",
            "correo": "carlos.rodriguez@example.com",
            "direccion": "Calle de la Paz 456, Ciudad",
            "telefono": "0416-1234567"
        }
    ],
    "clientes_juridicos": [
        {
            "id": 4,
            "razon_social": "Compañía ABC, C.A.",
            "rif": "12345678-9",
            "correo": "contacto@companiaabc.com",
            "direccion": "Avenida Libertador 1000, Ciudad",
            "telefono": "0212-3456789",
            "nombre_contacto": "Ana Martínez",
            "telefono_contacto": "0412-3456789",
            "correo_contacto": "ana.martinez@companiaabc.com"
        },
        {
            "id": 5,
            "razon_social": "Servicios XYZ, S.A.",
            "rif": "98765432-1",
            "correo": "info@serviciosxyz.com",
            "direccion": "Calle Principal 200, Ciudad",
            "telefono": "0212-9876543",
            "nombre_contacto": "Luis Fernández",
            "telefono_contacto": "0414-9876543",
            "correo_contacto": "luis.fernandez@serviciosxyz.com"
        }]}