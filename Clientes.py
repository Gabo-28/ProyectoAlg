class Cliente:
    def __init__(self, id, name, identificacion, correo, direccion, telefono):
        self.id = id
        self.name = name
        self.identificacion = identificacion # Cedula o Rif
        self.correo = correo
        self.direccion = direccion
        self.telefono = telefono
        
class Cliente_Juridico(Cliente):
    def __init__(self, id, name, identificacion, correo, direccion, telefono, namecont, telefonocont, emailcont):
        super().__init__(id, name, identificacion, correo, direccion, telefono)
        self.namecont = namecont
        self.telefonocont = telefonocont
        self.emailcont = emailcont
        
    def show(self):
        print(f'Razon Social: {self.name}')
        print(f'Rif: J-{self.identificacion}')
        print(f'Correo electrónico: {self.correo}')
        print(f'Dirección: {self.direccion}')
        print(f'Teléfono: {self.telefono}')
        print('---------------------------------------------------------------------------')
        print('Informacion de persona de contacto: ')
        print(f'Nombre del contacto: {self.namecont}')
        print(f'Teléfono del contacto: {self.telefonocont}')
        print(f'Correo electrónico del contacto: {self.emailcont}')
        
    def dictionary(self):
        return {
            'id': self.id,
            'name': self.name,
            'identificacion': self.identificacion,
            'correo': self.correo,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'namecont': self.namecont,
            'telefonocont': self.telefonocont,
            'emailcont': self.emailcont
        }

class Cliente_Natural(Cliente):
    def __init__(self, id, name, lastname, identificacion, correo, direccion, telefono):
        super().__init__( id, name, identificacion, correo, direccion, telefono)
        self.lastname = lastname
        
    def show(self):
        print(f'Nombre: {self.name}')
        print(f'Apellido: {self.lastname}')
        print(f'Cedula: V-{self.identificacion}')
        print(f'Correo electrónico: {self.correo}')
        print(f'Dirección: {self.direccion}')
        print(f'Teléfono: {self.telefono}')
        
    def dictionary(self):
        return {
            'id': self.id,
            'name': self.name,
            'lastname': self.lastname,
            'identificacion': self.identificacion,
            'correo': self.correo,
            'direccion': self.direccion,
            'telefono': self.telefono
        }
        