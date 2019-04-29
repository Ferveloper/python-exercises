#-*- coding: utf-8 -*
class Alumno:
    def __init__(self, matricula, nombre, apellido, correo, estatus):
        self.numeroMatricula = matricula
        self.nombre = nombre
        self.apellido = apellido
        self.correoElectronico = correo
        self.estatusInscrito = estatus