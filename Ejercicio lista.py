'''Tarea (9 de Junio):
📋 Problema: Lista de Compras Simple
Queremos crear un programa que permita al usuario guardar productos en una lista de compras y ver los productos guardados.

✅ Requisitos
El programa debe mostrar un menú con estas opciones:

Agregar producto.

Ver lista de compras.

Salir.

Si el usuario selecciona "Ver lista" y no hay productos, debe mostrar un mensaje.

El programa debe continuar hasta que el usuario elija salir.

Todo se guarda en una lista (no usar archivos, bases de datos ni diccionarios).'''


def lista_de_compras():

    compra=[]
    while True:
        print('1.Agregar producto➕: ')
        print('2.Ver lista de Compras👓')
        print('3.👋')
        opcion=input('Ingrese una opcion: ') 

        if opcion=='1':
            producto=input('➕Agregue un producto: ')
            compra.append(producto)
        
        elif opcion=='2':
            if len(compra)==0:
                print('No hay prodcutos en la lista🚫')
            else:
                print('🛒 Lista de Compras:')
                for item in compra:
                    print(f'- {item}')

        
        elif opcion=='3':
            print('Gracias por usar la lista✅')
            break
        else:
            print('Opcion No valida por favor intente nuevamente')


lista_de_compras()