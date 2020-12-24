from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import CotationForm
from django.contrib import messages
from .models import MyProject, PageT, DocT, DocumentStandard, Subject, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue


from decimal import Decimal
import sqlite3
import pandas as pd
import codes
import trata_cota
import delete_itens

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



def index(request):

    MyProjects = MyProject.objects.all().order_by('project_name')
    DocumentStandards = DocumentStandard.objects.all().order_by('doc_type') 
    Actions = Action.objects.all().order_by('-action_type')
    StatusDocs = StatusDoc.objects.all().order_by('-doc_status')
    Employees = Employee.objects.all().order_by('-emp_name')
    Cotations = Cotation.objects.all().order_by('-proj_name')

    return render(request, 'documentation/index.html', {'MyProjects': MyProjects, 'DocumentStandards': DocumentStandards, 'Actions': Actions, 'StatusDocs':StatusDocs, 'Employees':Employees, 'Cotations':Cotations})


def projectlist(request):

    MyProj = MyProject.objects.all().order_by('-project_name')

    paginator = Paginator(MyProj, 10)
    page = request.GET.get('page')

    MyProjects = paginator.get_page(page)

    cols = ['NOME DO PROJETO', 'NOME DA EMPRESA','COMENTÁRIOS']

    return render(request, 'documentation/projetos.html', {'MyProjects': MyProjects, 'cols':cols})



def Pagetypelist(request):
    
    pagets = PageT.objects.all()

    return render(request, 'documentation/pages-type.html', {'pagets': pagets})



def Doctypelist(request):
    
    doc = DocT.objects.all()
    paginator = Paginator(doc, 10)
    page = request.GET.get('page')

    docts = paginator.get_page(page)

    return render(request, 'documentation/doc-type.html', {'docts': docts})



def docummentypelist(request):
    
    Document = DocumentStandard.objects.all().order_by('doc_type')
    MyProjects = MyProject.objects.all().order_by('project_name') 
    Subjects = Subject.objects.all().order_by('subject_name') 

    paginator = Paginator(Document, 10)
    page = request.GET.get('page')

    DocumentStandards = paginator.get_page(page)

    cols = ['NOME DO DOCUMENTO', 'SIGLA DOC','FORMATO', 'TIPO FOLHA']

    return render(request, 'documentation/tipos-documentos.html', {'DocumentStandards': DocumentStandards, 'cols': cols, 'MyProjects': MyProjects, 'Subjects': Subjects})



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
def Cotationlist(request):

    Cotations = Cotation.objects.all().order_by('subject_name').order_by('doc_name').order_by('proj_name')
    MyProjects = MyProject.objects.all().order_by('project_name')
    Subjects = Subject.objects.all().order_by('subject_name')
    DocStandards = DocumentStandard.objects.all()

    '''paginator = Paginator(Cota, 10)
    page = request.GET.get('page')

    Cotations = paginator.get_page(page)'''

    print('>>>>>>', request.GET)

    if request.GET:
        proj_filter = 0
        sub_filter = 0

        if request.GET.get('proj'):
            for a in request.GET.get('proj'):
                proj_filter = a

        if request.GET.get('sub'):
            for a in request.GET.get('sub'):
                sub_filter = a

        cost = ProjectValue.objects.all()

        cost_proj = []
        if cost:
            for a in cost:
                cost_proj.append([a.cost_by_hh,a.cost_by_doc,a.cost_by_A1])


        if request.GET.get('cota'):
            cost_type = request.GET.get('cota')
            if cost_type == 'option1':
                val = cost_proj[0][0]

            elif cost_type == 'option2':
                val = cost_proj[0][1]

            elif cost_type == 'option3':
                val = cost_proj[0][2]

            trata_cota.trata_cotation(str(val), cost_type)


        if proj_filter != 0 and sub_filter == 0:
 
            Cotations = Cotation.objects.all().filter(proj_name=proj_filter).order_by('cod_doc_type')

            cols = ['NOME DO PROJETO', 'DISCIPLINA', 'TIPO DOC.', 'NOME DOC','COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. HH','CUSTO DOC.']

            #return redirect('cotation-list', Cotations='Cotations')
            return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'MyProjects':MyProjects})
	    
        if proj_filter != 0 and sub_filter != 0:

            Cotations = Cotation.objects.all().filter(proj_name=proj_filter, subject_name=sub_filter).order_by('cod_doc_type')

            cols = ['NOME DO PROJETO', 'DISCIPLINA', 'TIPO DOC.', 'NOME DOC','COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. HH','CUSTO DOC.']

            return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'MyProjects':MyProjects})
	
        
        return redirect('cotation-list' )


    cols = ['NOME DO PROJETO', 'DISCIPLINA', 'TIPO DOC.', 'NOME DOC','COD. DOC.', 'TIPO FOLHA','EXT. DOC','QD. FOLHAS', 'QT. HH','CUSTO DOC.']

    return render(request, 'documentation/cotation.html', {'Cotations':Cotations, 'DocStandards':DocStandards,'cols':cols, 'MyProjects':MyProjects, 'Subjects':Subjects})
	

def EditeCotation(request, id):
    Cotations = get_object_or_404(Cotation, pk=id)
    form = CotationForm(instance=Cotations)

    if (request.method == 'POST'):
        form = CotationForm(request.POST, instance=Cotations)
        print('>>>>>>>>>>>>>>>>',request.POST)

        if (form.is_valid()):
            #Cotations = form.save()
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

    trata_cota.trata_cotation(str(val), cost_type)

    return redirect('cotation-list')


def Create_PL(request): #Uso admin /CreatePL

    codes.rotina_carrega_pl()

    return redirect('/')




def Create_LD(request):
    #----------------------------------------------------------
    url = str(request)
    list_get = url.split('&')

    itens = [] 
    for a in range(len(list_get)):
        if list_get[a][:4] == 'acti':
            itens.append(list_get[a][7:])

        elif list_get[a][:4] == 'proj':
            itens.append(list_get[a][5:])

        elif list_get[a][:4] == 'sub=':
            itens.append(list_get[a][4:])

        elif list_get[a][:4] == '_sel':
            itens.append(list_get[a][10:])

    #------------------------------------------------
    if len(itens[len(itens)-1]) == 3:
        itens[len(itens)-1] = itens[len(itens)-1][:1]

    elif len(itens[len(itens)-1]) == 4:
        itens[len(itens)-1] = itens[len(itens)-1][:2]
    #------------------------------------------------
    
    if itens[1] == 'All':
        list_id = itens[4:]
    else:
        list_id = itens[3:]


    result_itens = [itens[:3],list_id]

    print('>>>>>>=====', result_itens)

    if itens[0] == 'create_budget' and len(itens) > 3:
        #result = trata_cota.cria_orc(result_itens)
        #trata_cota.cria_orc(result_itens)
        print('ok')
        return redirect('cotation-list')
        

    #---------------------------------------------------------- Sei que tem como fazer isso de forma muito mais simples, mas por hora foi o que consegui fazer. (Estudar como fazer isso com recursos django...)

    return redirect('documment-type-list')
    #