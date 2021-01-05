
from django import forms

from .models import  MyProject, Subject, PageT, DocT, Pageformat, DocumentStandard, Employee, StatusDoc, Action, Cotation


class MyProjectForm(forms.ModelForm):

    class Meta:
        model = MyProject
        fields = ('project_name', 'company', 'comments')


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_name',)


class PageTForm(forms.ModelForm):

    class Meta:
        model = PageT
        fields = ('name_page',)


class DocTForm(forms.ModelForm):

    class Meta:
        model = DocT
        fields = ('name_doc',)


class PageformatForm(forms.ModelForm):

    class Meta:
        model = Pageformat
        fields = ('name_format',)


class DocumentStandardForm(forms.ModelForm):

    class Meta:
        model = DocumentStandard
        fields = ('documment_name', 'doc_type', 'format_doc','doc_type_page')


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_name', 'emp_office', 'emp_contrato','photo')


class StatusDocForm(forms.ModelForm):

    class Meta:
        model = StatusDoc
        fields = ('doc_status',)


class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ('action_type',)


class CotationForm(forms.ModelForm):

    class Meta:
        model = Cotation
        fields = ('proj_name', 'subject_name', 'doc_name_pattern','doc_name', 'cod_doc_type','page_type','format_doc','qt_page', 'qt_hh','cost_doc')
