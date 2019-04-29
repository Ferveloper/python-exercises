class Alumno:
    def __init__(self, matricula, nombre, apellido, correo, estatus):
        self.numero_matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo
        self.estatus_inscrito = estatus

class Modulo:
    def __init__(self, fecha_inicio, fecha_fin):
        self.listado_alumnos = []
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