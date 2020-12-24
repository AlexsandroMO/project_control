from django.db import models


class MyProject(models.Model): #Títulos de projeto

    project_name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    comments = models.TextField()
    created_proj = models.DateTimeField(auto_now_add=True)
    update_proj = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name


class Subject(models.Model): #Disciplinas do Projeto

    subject_name = models.CharField(max_length=255)
    created_sub = models.DateTimeField(auto_now_add=True)
    update_sub = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name



class PageT(models.Model): #Lista de Acões

    name_page = models.CharField(max_length=3)
    created_pt = models.DateTimeField(auto_now_add=True)
    update_pt = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_page


class DocT(models.Model): #Lista de Acões

    name_doc = models.CharField(max_length=3)
    created_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_doc


class Pageformat(models.Model): #Lista de Acões

    name_format = models.CharField(max_length=15)
    created_fm = models.DateTimeField(auto_now_add=True)
    update_fm = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.name_format


class DocumentStandard(models.Model): #Documentos de Projeto

    documment_name = models.CharField(max_length=255)
    doc_type = models.ForeignKey(DocT, on_delete=models.CASCADE)
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE)
    doc_type_page = models.ForeignKey(PageT, on_delete=models.CASCADE)
    created_doc = models.DateTimeField(auto_now_add=True)
    update_doc = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.documment_name


class Employee(models.Model): #Lista de Funcionários

    emp_name = models.CharField(max_length=255)
    emp_office = models.CharField(max_length=255)
    emp_contrato = models.CharField(max_length=20)
    created_emp = models.DateTimeField(auto_now_add=True)
    update_emp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.emp_name


class StatusDoc(models.Model): #Lista de Status do Projeto

    doc_status = models.CharField(max_length=50)
    created_st = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.doc_status


class Action(models.Model): #Lista de Acões

    action_type = models.CharField(max_length=12)
    created_st = models.DateTimeField(auto_now_add=True)
    update_st = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return self.action_type


class Cotation(models.Model): #Lista de Acões DocT
    
    proj_name = models.ForeignKey(MyProject, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    doc_name_pattern = models.ForeignKey(DocumentStandard, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=255, blank=True, null=True)
    cod_doc_type = models.ForeignKey(DocT, on_delete=models.CASCADE)
    page_type = models.ForeignKey(PageT, on_delete=models.CASCADE)
    format_doc = models.ForeignKey(Pageformat, on_delete=models.CASCADE)
    qt_page = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)
    qt_hh = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    cost_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    created_ct = models.DateTimeField(auto_now_add=True)
    update_ct = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return str(self.proj_name)


class Upload(models.Model): #Upload de arquivos
    arq = models.FileField(upload_to='uploads/')
    update_arq = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.arq)



class ProjectValue(models.Model): #Upload de arquivos
    cost_by_hh = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cost_by_doc = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    cost_by_A1 = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.cost_by_hh)

