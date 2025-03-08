from django.db import models

# Create your models here.
class Asignatura(models.Model):
    nombre_materia = models.CharField(max_length=45)

class Maestro(models.Model):
    nombre_completo = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo_e = models.CharField(max_length=45)
    curp = models.CharField(max_length=45)
    rfc = models.IntegerField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

class Grado(models.Model):
    grado = models.CharField(max_length=45)

class Grupo(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)

class Alumno(models.Model):
    nombre_completo = models.CharField(max_length=45)
    genero = models.CharField(max_length=45)
    curp = models.CharField(max_length=45)
    fecha_nac = models.DateField()
    direccion = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class Calificacion(models.Model):
    bimestre = models.PositiveSmallIntegerField()
    calificacion = models.CharField(max_length=45)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

class AlumnoHasCalificacion(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    calificacion = models.ForeignKey(Calificacion, on_delete=models.CASCADE)

class MaestroHasGrupo(models.Model):
    maestro = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

class TipoParentesco(models.Model):
    descripcion = models.CharField(max_length=45)

class Tutor(models.Model):
    nombre = models.CharField(max_length=45)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    tipo_parentesco = models.ForeignKey(TipoParentesco, on_delete=models.CASCADE)

class AlumnoHasTutor(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

class Colegiatura(models.Model):
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    mes = models.DateField()
    pagado = models.CharField(max_length=1, choices=[('S', 'Sí'), ('N', 'No')])

class AlumnoHasColegiatura(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    colegiatura = models.ForeignKey(Colegiatura, on_delete=models.CASCADE)