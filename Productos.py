class Prod():
    
    def __init__(self, id, name, description, price, category, inventory):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.inventory = inventory
    
    def show(self):
        print(f'id: {self.id}')
        print(f'nombre: {self.name}')
        print(f'descripcion: {self.description}')
        print(f'precio: {self.price}')
        print(f'categoría: {self.category}')
        print(f'inventario: {self.inventory}')
    
    def dictionary(self, prod_vend):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': prod_vend,
            'inventory': self.inventory
        }
        


class Prod_Especificos(Prod):
    def __init__(self, id, name, description, price, category, inventory, compatible_vehicles):
        super().__init__(id, name, description, price, category, inventory)
        self.compatible_vehicles = compatible_vehicles
        
    def show(self):
        super().show()
        for i in range(len(self.compatible_vehicles)):
            print(f'Aplica para: {self.compatible_vehicles[i]}')
    def dictionary(self, prod_vend):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category,
            'productos comprados': prod_vend,
            'compatible_vehicles': self.compatible_vehicles
        }
        
    
        
            