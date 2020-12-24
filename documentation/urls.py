from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hello/', views.hello),
    path('', views.index, name='index'),
    path('datatable/', views.dataTable, name='data-table'),
    path('projects/', views.projectlist, name='project-list'),
    path('typeDocuments/', views.docummentypelist, name='documment-type-list'),
    path('Subject/', views.Subjectlist, name='subject-list'),
    path('action/', views.Actionlist, name='action-list'),
    path('status/', views.Statuslist, name='status-list'),
    path('employee/', views.Employeelist, name='employee-list'),
    path('cotation/', views.Cotationlist, name='cotation-list'),
    path('edite_cotation/<int:id>', views.EditeCotation, name='edite-cota'),
    path('CreatePL/', views.Create_PL, name='Create-PL'),
    path('CreateCota/', views.Create_Cotation, name='Create-cota'),
    path('PageT/', views.Pagetypelist, name='page-t'),
    path('DocT/', views.Doctypelist, name='doc-t'),
    path('createLD/', views.Create_LD, name='create-LD'),
    path('upload/', views.Uploadlists, name='upload-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#pip3 install django-crispy-forms