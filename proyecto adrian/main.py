import modules.corefiles as cf
import funciones.globales as fg
import funciones.especialistas as st
import funciones.paciente as fp
import funciones.consulta as fc
import ui.historial as uh
def mainmenu(op):
   fg.borrar_pantalla()
   tittle = """
   ***********************
   ** CENTRO CLINICO  JP**
   ***********************
   """   
   mainmenuop = "1. tipos de especialistas\n2. datos de pacientes\n3. consultas \n4. historial \n5. salir"
   if (op !=5):
      print(tittle)
      print(mainmenuop)
      try:
         opcion = int(input('~ '))
      except ValueError:
         input("Error en la opcion ingresada")  
         fg.pausar_pantalla
         mainmenu(0)
      else:
         match(opcion):
            case 1:
               st.NewSpecialista(0)
            case 2:
               fp.Newpaciente(0)
            case 3:
               fc.Newconsultas(0)
            case 4:
               uh.Menuconsultas(0)
            case 5:
               print("hasta luego")
               fg.pausar_pantalla()
            case _:
               print("opcion no valida")
               fg.pausar_pantalla
               mainmenu(0)
if __name__=='__main__':
   cf.checkfileEspecialistas(fg.CentroMedicoEspecialistas)
   cf.checkfilePacientes(fg.CentroMedicoPacientes)
   cf.checkfileconsulta(fg.CentroMedicoconsulta)
   cf.MY_DATOS_ESPECIALISTAS = 'data/especialistas.json'
   cf.MY_DATOS_PACIENTES = 'data/pacientes.json'
   cf.MY_CONSULTA = 'data/consulta.json'
   mainmenu(0)

