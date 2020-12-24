from django.contrib import admin
from . models import MyProject, Subject, DocumentStandard, Action, StatusDoc, Employee, Cotation, Upload, ProjectValue, PageT, DocT, Pageformat


class MyProjectAdmin(admin.ModelAdmin):
    fields = ('project_name','company','comments')
    list_display = ('project_name','company','comments','created_proj','update_proj')
    

class PageTAdmin(admin.ModelAdmin):
    fields = ('name_page',)
    list_display = ('name_page','created_pt','update_pt')


class DocTAdmin(admin.ModelAdmin):
    fields = ('name_doc',)
    list_display = ('name_doc','created_dt','update_dt')


class DocumentStandardAdmin(admin.ModelAdmin):
    fields = ('documment_name', 'doc_type','format_doc','doc_type_page')
    list_display = ('documment_name', 'doc_type','format_doc','doc_type_page','created_doc','update_doc')


class SubjectAdmin(admin.ModelAdmin):
    fields = ('subject_name',)
    list_display = ('subject_name', 'created_sub','update_sub')


class CotationAdmin(admin.ModelAdmin):
    fields = ('proj_name', 'subject_name', 'doc_name_pattern','doc_name', 'cod_doc_type','page_type','format_doc','qt_page', 'qt_hh','cost_doc')
    list_display = ('proj_name', 'subject_name', 'doc_name_pattern','doc_name', 'cod_doc_type','page_type','format_doc','qt_page', 'qt_hh','cost_doc','created_ct','update_ct') 

 
class UploadAdmin(admin.ModelAdmin):
    fields = ('arq',)
    list_display = ('arq', 'update_arq')


class ProjectValueAdmin(admin.ModelAdmin):
    fields = ('cost_by_hh','cost_by_doc','cost_by_A1')
    list_display = ('cost_by_hh','cost_by_doc','cost_by_A1')


class PageformatAdmin(admin.ModelAdmin):
    fields = ('name_format',)
    list_display = ('name_format','created_fm','update_fm')
    


admin.site.register(MyProject, MyProjectAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(DocumentStandard, DocumentStandardAdmin)
admin.site.register(Action)
admin.site.register(StatusDoc)
admin.site.register(Employee)
admin.site.register(Cotation, CotationAdmin)
admin.site.register(Upload)
admin.site.register(ProjectValue, ProjectValueAdmin)
admin.site.register(PageT, PageTAdmin)
admin.site.register(DocT, DocTAdmin)
admin.site.register(Pageformat, PageformatAdmin)
