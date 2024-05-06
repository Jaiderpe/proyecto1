import os
import json
import funciones.globales as gf
import modules.corefiles as cf
import ui.historial as uh

def Newconsultas():

    title = """
    **************************
    * REGISTRAR CONSULTAS    *
    **************************
    """
    
    gf.borrar_pantalla()
    print(title)
    id_medico=input("ingresa la id medico : ")
    id_paciente=input("ingrese la id de pacientes : ")
    fecha=input("ingrese la fecha : ")
    diagnostico=input("ingrese el diagnostico : ")
    tratamiento=input("ingrese el tratamiento :")

    consulta = {
        'id_medico': id_medico,
        'id_paciente': id_paciente,
        'fecha': fecha,
        'diagnostico': diagnostico,
        'tratamiento': tratamiento
    }
    cf.AddData('dataconsulta',id_medico,consulta)
    gf.CentroMedicoconsulta.get('dataconsulta')
    if(bool(input('desea ingresar otro consultas s(si) o (no)enter :'))):
        Newconsultas()
    else :
        uh.Menuconsultas(0)
def SearchData():
   criterio = input('ingrese el numero de indentificacion del pasiente :')
   data=gf.CentroMedicoconsulta.get("data").get(criterio)
   return data

def Modifydata():
    dataconsul = SearchData()
    id_medico,id_paciente,fecha,diagnostico,tratamiento=dataconsul.values()
    for key in dataconsul.keys():
        if(key !="identificacion" and key != "tratamiento"):
            if(bool(input(f'desea modificar el {key} s(si) o (no)enter'))):
                dataconsul[key]=input(f"ingresa el nuevo valor para {key} :")
    gf.CentroMedicoconsulta.get('data')
    cf.updatefile(gf.CentroMedicoconsulta)
    uh.Menuconsultas(0)

