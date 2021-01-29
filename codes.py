
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
import xlrd
import openpyxl

def financial(var):

  start, middle, middle2, tip, result = '','','','',''

  if len(var[0]) > 9:
    start = var[0][-6::]
    middle = var[0][:len(var[0])-6:]

    if len(middle) > 3:
      middle2 = middle[-3::]
      tip = middle[:len(middle)-7:]

    result = '{}.{}.{}'.format(tip, middle2, start)
      

  elif len(var[0]) <= 9 and len(var[0]) > 6:
    start = var[0][-6::]
    middle = var[0][:len(var[0])-6:]

    result = '{}.{}'.format(middle, start)

  elif len(var[0]) <= 6:
    start = var[0][-6::]
    middle = var[0][:len(var[0])-6:]

    result = '{}'.format(start)

  return result








def cria_tabelas(MyProjects,PageTs,DocTs,DocumentStandards,Subjects,Actions,StatusDocs,Employees,form_proj,form_dis,form_paget,form_doct,form_format,form_doc,form_func,form_st,form_ac):

    def cria_proj(name_proj, name_company, comment):
        proj = form_proj.save(commit=False)
        proj.project_name = name_proj
        proj.company = name_company
        proj.comments = comment
        proj.save()

    def cria_paget(name_page):
        paget = form_paget.save(commit=False)
        paget.name_page = name_page
        paget.save()

    def cria_doct(name_doc):
        doct = form_doct.save(commit=False)
        doct.name_doc = name_doc
        doct.save()

    def cria_form(form_page):
        format = form_format.save(commit=False)
        format.name_format = form_page
        format.save()

    def cria_doc(doc_name, code_doc, format_doc, doc_type):
        doc = form_doc.save(commit=False)
        doc.documment_name = doc_name
        doc.doc_type_id = int(code_doc)
        doc.format_doc_id = int(format_doc)
        doc.doc_type_page_id = int(doc_type)
        doc.save()

    def cria_dis(name_dis):
        dis = form_dis.save(commit=False)
        dis.subject_name = name_dis
        dis.save()

    def cria_st(status):
        st = form_st.save(commit=False)
        st.doc_status = status
        st.save()


    def cria_act(acao):
        ac = form_ac.save(commit=False)
        ac.action_type = acao
        ac.save()

    def cria_func(function, cargo, contr):
        func = form_func.save(commit=False)
        func.emp_name = function
        func.emp_office = cargo
        func.emp_contrato = contr
        func.photo = ''
        func.save()

    df_proj = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PROJECTS')
    df_doct = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DOC_TYPE')
    df_paget = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PAGE_TYPE')
    df_doc = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','MODELO_DOCUMENTO')
    df_dis = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DISCIPLINAS')
    df_st = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','STATUS')
    df_ac = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','ACAO')
    df_emp = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','EMPLOYEES')
    df_form = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','FORMAT_PAGE')
        
    #PROJ---------------------------------------------------------
    for a in range(len(df_proj['NOME_PROJETO'])):
        name_proj = df_proj['NOME_PROJETO'].loc[a]
        name_company = df_proj['EMPRESA'].loc[a]
        comment = df_proj['COMENTARIO'].loc[a]
        cria_proj(name_proj, name_company, comment)

    #Paget---------------------------------------------------------
    for a in range(len(df_paget['TIPO_FOLHA'])):
        name_page = df_paget['TIPO_FOLHA'].loc[a]
        cria_paget(name_page)

    #Doct---------------------------------------------------------
    for a in range(len(df_doct['TIPO_DOC'])):
        name_doc = df_doct['TIPO_DOC'].loc[a]
        cria_doct(name_doc)

    #Dis----------------------------------------------------------
    for a in range(len(df_dis['NOME_DISCIPLINA'])):
        name_dis = df_dis['NOME_DISCIPLINA'].loc[a]
        cria_dis(name_dis)

    #st-----------------------------------------------------------
    for a in range(len(df_st['STATUS'])):
        status = df_st['STATUS'].loc[a]
        cria_st(status)

    #act----------------------------------------------------------
    for a in range(len(df_ac['ACAO'])):
        acao = df_ac['ACAO'].loc[a]
        cria_act(acao)

    #emp----------------------------------------------------------
    for a in range(len(df_emp['FUNCIONARIO'])):
        function = df_emp['FUNCIONARIO'].loc[a]
        cargo = df_emp['CARGO'].loc[a]
        contr = df_emp['CONTRATO'].loc[a]
        cria_func(function, cargo, contr)

    #format--------------------------------------------------------
    for a in range(len(df_form['FORMATO_FOLHA'])):
        form_page = df_form['FORMATO_FOLHA'].loc[a]
        cria_form(form_page)

    #Doc----------------------------------------------------------
    for a in range(len(df_doc['LISTA_DOCUMENTOS'])):
        doc_name = df_doc['LISTA_DOCUMENTOS'].loc[a]
        code_doc = int(df_doc['COD_DOC_TIPO'].loc[a])
        format_doc = df_doc['FORMATO'].loc[a]
        doc_type = int(df_doc['TIPO'].loc[a])
        cria_doc(doc_name, code_doc, format_doc, doc_type)


    return 'feito!'

