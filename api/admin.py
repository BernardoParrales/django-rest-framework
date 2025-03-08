from django.contrib import admin
from .models import Asignatura, Maestro, Grado, Grupo, Alumno, Calificacion, AlumnoHasCalificacion, MaestroHasGrupo, TipoParentesco, Tutor, AlumnoHasTutor, Colegiatura
# Register your models here.

admin.site.register(Asignatura)
admin.site.register(Maestro)
admin.site.register(Grado)
admin.site.register(Grupo)
admin.site.register(Alumno)
admin.site.register(Calificacion)
admin.site.register(AlumnoHasCalificacion)
admin.site.register(MaestroHasGrupo)
admin.site.register(TipoParentesco)
admin.site.register(Tutor)
admin.site.register(AlumnoHasTutor)
admin.site.register(Colegiatura)