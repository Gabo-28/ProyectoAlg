import Clientes
import Productos

class Ventas:
    def __init__(self, id,  cliente, productos, cantidades, metodo_pago, metodo_envio, fecha, es_divisa=False,total_pagado= 0):
        self.id = id
        self.cliente = cliente  # Cliente que realizó la compra
        self.productos = productos  # Lista de productos comprados
        self.cantidades = cantidades  # Lista de cantidades correspondientes a cada producto
        self.metodo_pago = metodo_pago  # Método de pago (contado, credito (15 o 30) dias)
        self.metodo_envio = metodo_envio  # Método de envío
        self.es_divisa = es_divisa  # Indica si el pago es en divisas
        self.fecha = fecha  # Fecha de la compra
        self.subtotal = self.calcular_subtotal()  # Calcular el subtotal
        self.iva = self.calcular_iva()  # Calcular IVA
        self.igtf = self.calcular_igtf()  # Calcular IGTF
        self.descuento = self.calcular_descuento()  # Calcular descuentos
        self.total = self.calcular_total()  # Calcular total
        self.total_pagado = 0  # Total pagado por el cliente

    def calcular_subtotal(self):
        subtotal = 0.0
        for producto, cantidad in zip(self.productos, self.cantidades):
            subtotal += producto.price * cantidad
        return subtotal

    def calcular_iva(self):
        return self.subtotal * 0.16  # 16% de IVA

    def calcular_igtf(self):
        return self.subtotal * 0.03 if self.es_divisa else 0  # 3% IGTF si es en divisas

    def calcular_descuento(self):
        if isinstance(self.cliente, Clientes.Cliente_Juridico) and self.metodo_pago in ['credito 15 dias', 'credito 30 dias']:
            return self.subtotal * 0.05  # 5% de descuento
        return 0.0

    def calcular_total(self):
        tot = self.subtotal + self.iva + self.igtf - self.descuento
        tot = round(tot,2)
        return tot

    def show(self):
        print(f'ID: {self.id}')
        print(f'Cliente: {self.cliente.name}')
        print('Productos comprados:')
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f' - {producto.name}: {cantidad} x ${producto.price} = ${producto.price * cantidad}')
        print('Forma de pago:', self.metodo_pago)
        print(f'Subtotal: ${self.subtotal}')
        print(f'IVA (16%): ${self.iva}')
        print(f'IGTF (3%): ${self.igtf}')
        print(f'Descuento: - ${self.descuento}')
        print(f'Total: ${self.total}')
        print(f'Pagado: ${self.total_pagado}')
        print(f'Deuda: ${self.total - self.total_pagado}')


    def mostrar_facturas(self):
        print(f'Factura de {self.cliente.name}:')
        for producto, cantidad in zip(self.productos, self.cantidades):
            print(f' - {producto.name}: {cantidad} x ${producto.price} = ${producto.price * cantidad} | {(producto.price*cantidad)*0.16}')
        print(f'IGTF (3%): ${self.igtf}')
        print(f'Descuento: - ${self.descuento}')
        print(f'Total: ${self.total}')
    
    def dictionary(self):
        return {
            'id': self.id,
            'cliente': self.cliente.name,
            'productos': [{'name': p.name, 'price': p.price, 'quantity': q} for p, q in zip(self.productos, self.cantidades)],
            'metodo_pago': self.metodo_pago,
            'metodo_envio': self.metodo_envio,
            'es_divisa': self.es_divisa,
            'fecha': self.fecha,
            'subtotal': self.subtotal,
            'iva': self.iva,
            'igtf': self.igtf,
            'descuento': self.descuento,
            'total': self.total,
            'total_pagado': self.total_pagado,
            'deuda': self.total - self.total_pagado
        }