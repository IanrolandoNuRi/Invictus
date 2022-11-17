from nturl2path import url2pathname
from django.urls import path, include
from django.views.generic import TemplateView
from datasheet import views
from datasheet.views import (CreateDataSheet, DeleteDataSheet, ListarFicha)

urlpatterns = [
    path('home/', views.Home, name='home'),
    path('view-datasheet/', views.ViewDataSheet, name='view_datasheet'),
    path('coordinacion-agua/<int:num>/', views.CoordinacionAgua, name='coordinacion_agua'),
    path('coordinacion-agua/nueva-acometida/<int:num>/', views.NuevaAcometida, name='nueva_acometida'),
    path('coordinacion-desechos-solidos/<int:num>/', views.CoordinacionDesechosSolidos, name='coordinacion_desechos_solidos'),
    path('coordinacion-alcantarillado/', views.CoordinacionAlcantarillado, name='coordinacion_alcantarillado'),
    path('create-datasheet/', CreateDataSheet.as_view(), name='create_datasheet'),
    path('edit-datasheet/<int:pk>/', views.EditDataSheet, name='edit_datasheet'),
    path('delete-datasheet/<int:pk>/',DeleteDataSheet.as_view(), name='delete_datasheet'),
    path('list-datasheet/', ListarFicha.as_view(), name='listar_fichas'),
    path('buscar/', views.buscarCampos, name='buscar_fichas'),
    path('start-datasheet/',TemplateView.as_view(
                                template_name='fichas.html'
                            ), name='inicio_fichas'),
]