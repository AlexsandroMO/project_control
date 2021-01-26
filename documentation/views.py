from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import MyProjectForm, SubjectForm, PageTForm, DocTForm, PageformatForm, DocumentStandardForm, EmployeeForm, StatusDocForm, ActionForm, CotationForm
from django.contrib import messages
from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue

import codes as CODE
import trata_cota as LDcreate
import delete_itens
from datetime import datetime
from decimal import Decimal
import sqlite3
import pandas as pd
import numpy as np

def hello(request):
    return HttpResponse('<h1>Hello!</h1>')


def dataTable(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')

    return render(request, 'documentation/datatable.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations})


@login_required
def index(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')
    colab = request.user
    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/index.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations, 'colaborador':colaborador, 'photo_colab':photo_colab})


def projectlist(request):

    MyProj = MyProject.objects.all().order_by('-project_name')

    paginator = Paginator(MyProj, 10)
    page = request.GET.get('page')

    MyProjects = paginator.get_page(page)

    return render(request, 'documentation/projetos.html', {'MyProjects': MyProjects})



def Pagetypelist(request):
    
    pagets = PageT.objects.all()

    return render(request, 'documentation/pages-type.html', {'pagets': pagets})



def Doctypelist(request):
    
    docts = DocT.objects.all()
    #paginator = Paginator(doc, 10)
    #page = request.GET.get('page')

    #docts = paginator.get_page(page)

    return render(request, 'documentation/doc-type.html', {'docts': docts})



@login_required
def docummentypelist(request):
    
    #Document = DocumentStandard.objects.all().order_by('doc_type').filter(user=request.user)
    Document = DocumentStandard.objects.all().order_by('doc_type')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    Employees = Employee.objects.all().order_by('-emp_name')

    len_doc = len(Document)

    #paginator = Paginator(Document, 20)
    #page = request.GET.get('page')
    #DocumentStandards = paginator.get_page(page)

    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo

    return render(request, 'documentation/tipos-documentos.html', {'Document': Document, 'MyProjects': MyProjects, 'Subjects': Subjects, 'Employees':Employees, 'len_doc':len_doc, 'colaborador':colaborador, 'photo_colab':photo_colab})



def Subjectlist(request):
    
    Sub = Subject.objects.all().order_by('-subject_name')
    paginator = Paginator(Sub, 10)
    page = request.GET.get('page')

    Subjects = paginator.get_page(page)

    return render(request, 'documentation/disciplinas.html', {'Subjects': Subjects})



def Actionlist(request):
    
    Actions = Action.objects.all().order_by('-action_type') 

    return render(request, 'documentation/action.html', {'Actions': Actions})



def Statuslist(request):
    
    Status = StatusDoc.objects.all().order_by('-doc_status')

    paginator = Paginator(Status, 10)
    page = request.GET.get('page')

    StatusDocs = paginator.get_page(page)

    return render(request, 'documentation/status-doc.html', {'StatusDocs': StatusDocs})



def Employeelist(request):
    
    Empl = Employee.objects.all().order_by('-emp_name')

    paginator = Paginator(Empl, 10)
    page = request.GET.get('page')

    Employees = paginator.get_page(page)

    cols = ['NOME DO COLABORADOR', 'CARGO', 'REGISTRO']

    return render(request, 'documentation/employee.html', {'Employees': Employees, 'cols':cols})



def Uploadlists(request):
    if request.GET.get('arq'):
        print('entrou')

    Uploads = Upload.objects.all().order_by('-arq')

    return render(request, 'documentation/upload.html', {'Uploads':Uploads})




#---------------------------------------------------------------
def LD_Proj(request):

    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo


    return render(request, 'documentation/LD-projeto.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'colaborador':colaborador, 'photo_colab':photo_colab})







#---------------------------------------------------------------
def Cotationlist(request):

    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocumentStandards = DocumentStandard.objects.all()
    Employees = Employee.objects.all().order_by('-emp_name')

    calc = []
    for i in Cotations:
        print(i.cost_doc)
        calc.append(i.cost_doc)

    total = sum(calc)

    colab = request.user

    colaborador = ''
    photo_colab = ''

    for a in Employees:
        if colab == a.user:
            colaborador = a.emp_name
            photo_colab = a.photo


    return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'total':total, 'colaborador':colaborador, 'photo_colab':photo_colab})



#@login_required
def Cotationlist_filter(request):

    print(request.GET)

    #GET['proj']
    
    Cota = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocumentStandards = DocumentStandard.objects.all()

    Cotations = Cota.objects.all().filter(proj_name='Projeto Porto Novo', subject_name='CFTV')

    for i in Cotations:
        print(i.proj_name, i.subject_name)


    calc = []
    for i in Cotations:
        print(i.cost_doc)
        calc.append(i.cost_doc)

    total = sum(calc)

    print(total)

    return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocumentStandards':DocumentStandards, 'MyProjects':MyProjects, 'Subjects':Subjects, 'total':total})



def EditeCotation(request, id):

    Values = ProjectValue.objects.all()
    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)

    print(Values[0].cost_by_hh, Values[0].cost_by_doc, Values[0].cost_by_A1)
    print(form)
  

    if (request.method == 'POST'):
        form = CotationForm(request.POST, instance=Cotations)
        
        if (form.is_valid()):
            Cotations.cost_doc = 0
            Cotations.save()
            return redirect('cotation-list')
            
        else:
            return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations}) 

    else:
        return render(request, 'documentation/edite-cotation.html', {'form': form, 'Cotations': Cotations})


def DeleteCotation(request, id):
    Cotations = get_object_or_404(Cotation, pk=id)
    Cotations.delete()

    #messages.info(request, 'Documento Deletado com Sucesso!')

    return redirect('/')


#---------------------------------------------------------------



def Create_LD(request):

    DocumentStandards = DocumentStandard.objects.all()

    if len(dict(request.GET)) == 3 and dict(request.GET)['proj'][0] != '0' and dict(request.GET)['sub'][0] != '0':
        
        GET = dict(request.GET)

        if dict(request.GET)['action'][0] == 'All':
            LDcreate.cria_orc_all(GET,DocumentStandards)

            return redirect('cotation-list')

        elif dict(request.GET)['action'][0] != 'All':
            print('>>>>>>>>>>>>>>>>>>>', dict(request.GET))
            LDcreate.cria_orc_ind(GET)

            return redirect('cotation-list')


    else:
        return redirect('documment-type-list')



def Create_Cotation(request):

    cost = ProjectValue.objects.all()

    cost_proj = []
    if cost:
        for a in cost:
            cost_proj.append([a.cost_by_hh,a.cost_by_doc,a.cost_by_A1])

    if request.GET.get('cota-radio'):
        cost_type = request.GET.get('cota-radio')
        if cost_type == 'option1':
            val = cost_proj[0][0]

        elif cost_type == 'option2':
            val = cost_proj[0][1]

        elif cost_type == 'option3':
            val = cost_proj[0][2]

    LDcreate.trata_cotation(str(val), cost_type)

    return redirect('cotation-list')



def Calc_Cota(request):

    Values = ProjectValue.objects.all()
    Cotations = Cotation.objects.all()
    GET = dict(request.GET)

    LDcreate.calc_cota(Cotations, Values, GET)

    return redirect('cotation-list')



def Create_PL(request): #Uso admin /CreatePL

    MyProjects = MyProject.objects.all()
    PageTs = PageT.objects.all()
    DocTs = DocT.objects.all()
    DocumentStandards = DocumentStandard.objects.all()
    Subjects = Subject.objects.all()
    Actions = Action.objects.all().order_by
    StatusDocs = StatusDoc.objects.all().order_by
    Employees = Employee.objects.all().order_by

    form_proj = MyProjectForm()
    form_dis = SubjectForm()
    form_paget = PageTForm()
    form_doct = DocTForm()
    form_format = PageformatForm()
    form_doc = DocumentStandardForm()
    form_func = EmployeeForm()
    form_st = StatusDocForm()
    form_ac = ActionForm()

    execute = CODE.cria_tabelas(MyProjects,PageTs,DocTs,DocumentStandards,Subjects,Actions,StatusDocs,Employees,form_proj,form_dis,form_paget,form_doct,form_format,form_doc,form_func,form_st,form_ac)
    #print(execute)

    return redirect('/')














'''
def Create_LD(request):

    MyProjects = MyProject.objects.all()
    Subjects = Subject.objects.all()
    DocumentStandards = DocumentStandard.objects.all()
    Cotations = Cotation.objects.all()

    form_proj = MyProjectForm()
    form_dis = SubjectForm()
    form_doc = DocumentStandardForm()
    form_cota = CotationForm()
    

    print('======',dict(request.GET))
    print('==LEN ',len(dict(request.GET)), dict(request.GET)['action'][0])

    

    # for i in DocumentStandards:
    #     print('--',i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id, '>>>>',len(DocumentStandards))
    #     #print('>>>>>>',DocumentStandards[i].id, DocumentStandards[i].documment_name, DocumentStandards[i].doc_type_id,DocumentStandards[i].doc_type_page_id,DocumentStandards[i].format_doc_id, '>>>>',len(DocumentStandards))

    #documment_name,doc_type,format_doc,doc_type_page

    if len(dict(request.GET)) == 3 and dict(request.GET)['proj'][0] != '0' and dict(request.GET)['sub'][0] != '0':
        
        GET = dict(request.GET)
        
        if dict(request.GET)['action'][0] == 'All':
            LDcreate.cria_orc_all(GET, MyProjects,DocumentStandards,Subjects,Cotations,form_proj,form_dis,form_doc,form_cota,int(dict(request.GET)['proj'][0]), int(dict(request.GET)['sub'][0]), form_cota)

            return redirect('cotation-list')

        elif dict(request.GET)['action'][0] != 'All':
            for i in GET['action']:
                proj = DocumentStandard.objects.all().filter(id=i)
                for a in proj:
                    print('<-->',a.documment_name, a.doc_type_id, a.format_doc_id, a.doc_type_page_id)
                    #LDcreate.cria_orc_unic(GET, a.id, a.documment_name, a.doc_type_id, a.doc_type_page_id, a.format_doc_id, form_cota)
                    #def cria_cota(proj, sub, id_proj, documment, doc_type,doc_type_page,format_doc):
                    cota = form_cota.save(commit=False)
                    cota.proj_name_id = int(GET['proj'][0])
                    cota.subject_name_id = int(GET['sub'][0])
                    cota.doc_name_pattern_id = int(a.doc_type_id)#int(id_proj)
                    cota.doc_name = a.documment_name #documment
                    cota.cod_doc_type_id = int(a.doc_type_id) #int(doc_type)
                    cota.page_type_id = int(a.doc_type_page_id) #int(doc_type_page)
                    cota.format_doc_id = int(a.format_doc_id) #int(format_doc)
                    cota.qt_page = 0
                    cota.qt_hh = 0
                    cota.cost_doc = 0
                    cota.save()

                    print('----------------Registrado!')

            return redirect('cotation-list')

    return redirect('documment-type-list')
'''