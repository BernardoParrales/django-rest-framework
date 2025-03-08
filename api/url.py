from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'asignatura', views.AsignaturaViewSet)
router.register(r'maestro', views.MaestroViewSet)
router.register(r'grado', views.GradoViewSet)
router.register(r'grupo', views.GrupoViewSet)
router.register(r'alumno', views.AlumnoViewSet)
router.register(r'calificacion', views.CalificacionViewSet)
router.register(r'alumno_has_calificacion', views.AlumnoHasCalificacionViewSet)
router.register(r'maestro_has_grupo', views.MaestroHasGrupoViewSet)
router.register(r'tipo_parentesco', views.TipoParentescoViewSet)
router.register(r'tutor', views.TutorViewSet)
router.register(r'alumno_has_tutor', views.AlumnoHasTutorViewSet)
router.register(r'colegiatura', views.ColegiaturaViewSet)
router.register(r'alumno_has_colegiatura', views.AlumnoHasColegiaturaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]