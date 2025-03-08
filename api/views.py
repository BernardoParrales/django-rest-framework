from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.
class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class MaestroViewSet(viewsets.ModelViewSet):
    queryset = Maestro.objects.all()
    serializer_class = MaestroSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class AlumnoHasCalificacionViewSet(viewsets.ModelViewSet):
    queryset = AlumnoHasCalificacion.objects.all()
    serializer_class = AlumnoHasCalificacionSerializer

class MaestroHasGrupoViewSet(viewsets.ModelViewSet):
    queryset = MaestroHasGrupo.objects.all()
    serializer_class = MaestroHasGrupoSerializer

class TipoParentescoViewSet(viewsets.ModelViewSet):
    queryset = TipoParentesco.objects.all()
    serializer_class = TipoParentescoSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class AlumnoHasTutorViewSet(viewsets.ModelViewSet):
    queryset = AlumnoHasTutor.objects.all()
    serializer_class = AlumnoHasTutorSerializer

class ColegiaturaViewSet(viewsets.ModelViewSet):
    queryset = Colegiatura.objects.all()
    serializer_class = ColegiaturaSerializer

class AlumnoHasColegiaturaViewSet(viewsets.ModelViewSet):
    queryset = AlumnoHasColegiatura.objects.all()
    serializer_class = AlumnoHasColegiaturaSerializer