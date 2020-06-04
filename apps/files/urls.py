from django.urls import path, include

from .views import importConsultFile, importExamFile

urlpatterns = [
    path('consulta/importar', importConsultFile, name='files-consult-import'),
    path('exame/importar', importExamFile, name='files-exam-import'),
]
