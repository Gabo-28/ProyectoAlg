from datetime import datetime

class Pago:
    def __init__(self, cliente, monto, moneda, tipo_pago, fecha_pago=None):
        self.cliente = cliente  # Cliente que realizó el pago
        self.monto = monto  # Monto del pago
        self.moneda = moneda  # Moneda del pago
        self.tipo_pago = tipo_pago  # Tipo de pago
        self.fecha_pago = fecha_pago if fecha_pago else datetime.now()  # Fecha del pago, por defecto es la fecha actual

    def show(self):
        print("Detalles del pago:")
        print('Cliente:')
        self.cliente.show()
        print(f"Monto del pago: {self.monto} {self.moneda}")
        print(f"Tipo de pago: {self.tipo_pago}")
        print(f"Fecha del pago: {self.fecha_pago.strftime('%Y-%m-%d %H:%M:%S')}")
        
    def dictionary(self):
        return {
            'cliente_id': self.cliente.id,
            'monto': self.monto,
            'es divisa': self.moneda,
            'tipo_pago': self.tipo_pago,
            'fecha_pago': self.fecha_pago.strftime('%Y-%m-%d %H:%M:%S')
        }
