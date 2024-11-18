from datetime import datetime

class Envio:
    def __init__(self, id, venta, servicio_envio, costo,direccion, motorizado=None):

        self.id = id
        self.venta = venta
        self.servicio_envio = servicio_envio
        self.costo = costo
        self.direccion = direccion 
        self.motorizado = motorizado
        self.fecha = str(datetime.now())

    def show(self):
        """Muestra los detalles del envío de forma estructurada."""
        if self.motorizado:
            motorizado_info = self.motorizado
        else:
            motorizado_info = 'Zoom'
            
        motorizado_info = self.motorizado if self.motorizado else "No asignado"
        print(f"Orden de Compra: {self.orden_compra}\n")
        print(f"Servicio de Envío: {self.servicio_envio}\n")
        print(f"Costo: ${self.costo:.2f}\n")
        print(f"Motorizado: {motorizado_info}\n")
        print(f"Fecha: {self.fecha.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
    def dictionary(self):
        return {
            'id': self.id,
            'venta': self.venta.dictionary(),
            'servicio_envio': self.servicio_envio,
            'costo': self.costo,
            'direccion': self.direccion,
            'motorizado': self.motorizado,
            'fecha': self.fecha
        }

