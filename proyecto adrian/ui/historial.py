import funciones.consulta as rt
import funciones.globales as gf
import main


def Menuconsultas(op : int):
    title = """
    ***************************
    * MENU DE MEDICOS    JP  *
    ***************************
    """
    Menumedicosop = "1.agregar \n2.editar \n3.eliminar \n4.salir"
    gf.borrar_pantalla()  
    if (op !=4):
        print(title)
        print(Menumedicosop)
        try:
            op =int(input(":)"))
        except ValueError:
            print("Opcion no tiene formato adecuado ")
            gf.borrar_pantalla
            Menuconsultas(0)
        else:
            match (op):
                case 1:
                    rt.Newconsultas(0)
                case 2:
                    rt.Modifydata(0)
                case 3:
                    pass
                case 4:
                    main.mainmenu(0)
                case _:
                    print("la opcion ingresada no esta disponible en las opciones")
                    gf.pausar_pantalla()