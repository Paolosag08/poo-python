from clases.cliente import Cliente
from clases.inventario import Inventario
from clases.mascota import Gato, Perro
from clases.producto import Producto
from clases.venta import Venta


def registrar_mascota():
    tipo = input('Ingrese el tipo de mascota (Gato/Perro): ').strip().lower()
    nombre = input('Ingrese el niombre de la mascota: ')
    edad = int(input('Ingrese la edad de la mascota: '))
    salud = input('Estado de salud de la mascota: ')
    precio = float(input('Precio de la mascota: '))

    if tipo == 'perro':
        raza = input('Ingrese la raza del perro: ')
        nivel_de_energia = input('Nivel de energia del perro: ')
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)
    elif tipo == 'gato':
        raza = input('Ingrese la raza del gato: ')
        independencia = input('Nivel de independencia del gato: ')
        mascota = Gato(nombre, edad, salud, precio, raza, independencia)
    else:
        print('Tipo de mascota no reconocido')
        return
    return mascota

def registrar_cliente():
    nombre = input('Ingrese el nombre del cliente: ')
    direccion = input('Ingrese la direccion del cliente: ')
    telefono = input('Ingrese el telefono del cliente: ')
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input('Ingrese el nombre del producto: ')
    categoria = input('Ingrese la categoria del producto: ')
    precio = float(input('Ingrese el precio del producto: '))
    cantidad = int(input('Ingrese la cantidad del producto: '))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto


def registrar_venta(clientes, inventario):
    nombre_cliente = input('Ingrese el nombre del cliente: ')
    cliente = next((c for c in clientes if c.nombre == nombre_cliente), None)
    if not cliente:
        print('Cliente no encontrado')
        return
    
    productos = []

    while True:
        nombre_producto = input('Ingrese el nombre del producto (deje vacio para finalizar): ')
        if not nombre_producto:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_producto), None)
        if producto:
            productos.append(producto)
        else:
            print('Producto no encontrado')
        
    if productos:
        venta = Venta(cliente, productos)
        venta.registrar_venta()
        print('La venta ha sido registrada con exito')
    else:
        print('No se han registrado los productos para la venta')

def mostrar_menu():
    print('\n --- Menú de gestion de Patas Felices ---')
    print('1. Registrar Mascota')
    print('2. Registrar Cliente')
    print('3. Registrar Producto')
    print('4. Registrar Venta')
    print('5. Mostrar informacion de la Mascota')
    print('6. Mostrar informacion del Cliente')
    print('7. Mostrar informacion de los Productos')
    print('8. Generar alaerta de inventario')
    print('9. Salir')

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            mascota = registrar_mascota()
            if mascota:
                mascotas.append(mascota)
                print('Mascota registrada con éxito')
        elif opcion == '2':
            cliente = registrar_cliente()
            if cliente:
                clientes.append(cliente)
                print('Cliente registrado con éxito')
        elif opcion == '3':
            producto = registrar_producto()
            if producto:
                inventario.agregar_producto(producto)
                print('Producto registrado con éxito')
        elif opcion == '4':
            registrar_venta(clientes, inventario)
        elif opcion == '5':
            for mascota in mascotas:
                print(mascota.mostrar_info())
                if isinstance(mascota, Perro) or isinstance(mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == '6':
            for cliente in clientes:
                print(cliente.mostrar_info())
        elif opcion == '7':
            for producto in inventario.lista_de_productos:
                print(producto.mostrar_info())
        elif opcion == '8':
            umbral_minimo = int(input('Ingrese el umbral minimo del inventario: '))
            print(inventario.generar_alerta(umbral_minimo))
        elif opcion == '9':
            print('Saliendo del sistema ¡Gracias por usar Patas Felices APP!')
            break
        else:
            print('Opción no válida, intente nuevamente')

if __name__ == '__main__':
    main()



