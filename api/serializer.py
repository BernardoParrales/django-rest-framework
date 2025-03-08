from rest_framework import serializers
from .models import *

# fields = ['nombre_materia'] # Serealizar solo los campos que se especifiquen
class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__' # Serealizar todos los campos

class MaestroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maestro
        fields = '__all__'

class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class AlumnoHasCalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoHasCalificacion
        fields = '__all__'

class MaestroHasGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaestroHasGrupo
        fields = '__all__'

class TipoParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoParentesco
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

class AlumnoHasTutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoHasTutor
        fields = '__all__'

class ColegiaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegiatura
        fields = '__all__'

class AlumnoHasColegiaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlumnoHasColegiatura
        fields = '__all__'