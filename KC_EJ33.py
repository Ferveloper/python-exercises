#-*- coding: utf-8 -*
class Alumno:
    def __init__(self, matricula, nombre, apellido, correo, estatus):
        self.numero_matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo
        self.estatus_inscrito = estatus

class Modulo:
    def __init__(self, fecha_inicio, fecha_fin):
        self.listado_alumnos = [{
                'numero_matricula' : 1,
                'nombre' : 'Fernando',
                'apellido' : 'Merino',
                'correo_electronico' : 'fernando@correo.es',
                'estatus_inscrito' : True
                },
                {
                'numero_matricula' : 2,
                'nombre' : 'Rosa',
                'apellido' : 'Artero',
                'correo_electronico' : 'isabel@correo.es',
                'estatus_inscrito' : True
                },
                {
                'numero_matricula' : 3,
                'nombre' : 'Javier',
                'apellido' : 'Ugarte',
                'correo_electronico' : 'jugarte@correo.es',
                'estatus_inscrito' : True
                },
                {
                'numero_matricula' : 4,
                'nombre' : 'María',
                'apellido' : 'López',
                'correo_electronico' : 'mlopez@correo.es',
                'estatus_inscrito' : True
                },
                {
                'numero_matricula' : 5,
                'nombre' : 'José',
                'apellido' : 'Navarro',
                'correo_electronico' : 'josenav@correo.es',
                'estatus_inscrito' : True
                }
            ]
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def agregar_alumno(self):
        matricula = self.listado_alumnos[len(self.listado_alumnos) - 1]['numero_matricula'] + 1
        nombre = raw_input('Escribe un nombre: ')
        apellido = raw_input('Escribe un apellido: ')
        correo = raw_input('Escribe un e-mail: ')
        alumno = {
            'numero_matricula' : matricula,
            'nombre' : nombre,
            'apellido' : apellido,
            'correo_electronico' : correo,
            'estatus_inscrito' : True
        }
        self.listado_alumnos.append(alumno)

    def buscar_alumno(self, matricula):
       if (any(map(lambda person : person['numero_matricula'] == matricula, self.listado_alumnos))):
           alumno = filter(lambda person : person['numero_matricula'] == matricula, self.listado_alumnos)[0]
           print('Resultado:\nNombre: %s\nApellido: %s\nE-mail: %s' %(alumno['nombre'], alumno['apellido'], alumno['correo_electronico']))
       else:
           print('El alumno no está en el listado')

    def mostrar_inscritos(self):
        list = 'Alumnos inscritos:\n\nNº matrícula, Nombre, Apellido, E-mail\n'
        for person in self.listado_alumnos:
            if (person['estatus_inscrito']):
                list += '%s, %s, %s, %s\n' %(person['numero_matricula'], person['nombre'], person['apellido'], person['correo_electronico'])
        print(list)

prebootcamp = Modulo('05/10/2018', '23/11/2018')

while True:
    option = input('Opciones:\n(1) Agregar un alumno\n(2) Ver todos los alumnos enrolados\n(3) Buscar un alumno por matrícula\n')

    if option == 1:
       prebootcamp.agregar_alumno()
    elif option == 2:
       prebootcamp.mostrar_inscritos()
    elif option == 3:
       matricula = input('Introduce el número de matrícula: ')
       prebootcamp.buscar_alumno(matricula)
    else:
       print('Opción no válida. Prueba de nuevo.')