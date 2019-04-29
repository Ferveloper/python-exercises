#-*- coding: utf-8 -*
class Alumno:
    def __init__(self, matricula, nombre, apellido, correo, estatus):
        self.numero_matricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo
        self.estatus_inscrito = estatus

class AlumnoRemoto(Alumno):
    def __init__(self, matricula, nombre, apellido, correo, estatus, skype, huso_horario):
        Alumno.__init__(self, matricula, nombre, apellido, correo, estatus)
        self.skype = skype
        self.huso_horario = huso_horario

class AlumnoPresencial(Alumno):
    def __init__(self, matricula, nombre, apellido, correo, estatus, numero_asiento):
        Alumno.__init__(self, matricula, nombre, apellido, correo, estatus)
        self.numero_asiento = numero_asiento