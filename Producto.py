
def lista_de_productos():

    compra=[]
    precio=[]
    while True:
        print('1.Agregar producto ➕: ')
        print('2.Ver lista de productos👓')
        print('3. Salir...👋')
        opcion=input('Ingrese una opcion: ') 

        if opcion=='1':
            producto=input('➕Agregue un producto: ')
            compra.append(producto)
            costo=input('➕ingrese un precio al producto: ')
            precio.append(costo)
        elif opcion=='2':
            if len(compra)==0:
                print('No hay productos en la lista🚫')
            elif len(precio)<=0:
                print('ERROR por favor verifique que el valor sea correcto🚫')
            else:
                print('🛒 Lista de Compras:')
                for item, valor in zip(compra, precio):
                    print(f'- {item},{valor}')

        
        elif opcion=='3':
            print('Gracias por usar la lista✅')
            break
        else:
            print('Opcion No valida por favor intente nuevamente')


lista_de_productos()