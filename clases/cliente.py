class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.historial_compras = []

    def actualizar_info(self, direccion = None, telefono = None):
        if direccion:
            self.direccion = direccion
        if telefono:
            self.telefono = telefono
    
    def registrar_compra(self, compra):
        self.historial_compras.append(compra)
    
    def mostrar_info(self):
        return f'Cliente: {self.nombre}, Dirección: {self.direccion}, Telefono: {self.telefono}'

        