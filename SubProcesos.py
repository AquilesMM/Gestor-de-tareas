from Gestor_de_tareas import *
class CRUD():

    def ver_tareas(self, tarea):
        for llave, valor in self.tarea.items():
            print(valor)

    def ver_llave_tarea(self, tarea):
        for llave, valor in self.tarea.items():
            print(llave, valor)
    def eliminar_tarea(self, tarea):
        print(CRUD.ver_llave_tarea(self.tarea))
        opcion = int(input('Elija la tarea que quiere eliminar:'))
        opcion2 = int(input(f'Seguro de eliminar: {tarea.get(opcion)}'
              f'\n 1.si'
              f'\n 2.no'))
        
    def crear_tarea(self, tarea):
        dia= input("Ingrese la fecha de la tarea: ")
        nombre= input("Ingrese el nombre de la tarea a crear: ")
        tarea ={ "tarea 1":{"dia": dia,
                "tarea": nombre}}
        print("Su tarea fue creada con exito")
        
            