import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
import xlrd
import excel


def rotina_carrega_pl():

    #-------------------------------------------------------
    def cria_proj(proj_name, company, comments, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_myproject(project_name,company,comments,created_proj,update_proj)
                    VALUES ('{proj_name}','{company}','{comments}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_doc(doc_name, code_doc, format_doc, doc_type, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_documentstandard(documment_name, doc_type_id, format_doc_id, doc_type_page_id, created_doc, update_doc)
                    VALUES ('{doc_name}','{code_doc}','{format_doc}','{doc_type}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_dis(name_dis, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_subject(subject_name, created_sub, update_sub)
                    VALUES ('{name_dis}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

            

    def cria_st(status, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_statusdoc(doc_status,created_st,update_st)
                    VALUES ('{status}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_act(acao, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_action(action_type, created_st, update_st)
                    VALUES ('{acao}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_func(func, cargo, contr, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_employee(emp_name,emp_office,emp_contrato,created_emp,update_emp)
                    VALUES ('{func}','{cargo}','{contr}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_paget(name_page, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_paget(name_page,created_pt,update_pt)
                    VALUES ('{name_page}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_doct(name_doc, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_doct(name_doc,created_dt,update_dt)
                    VALUES ('{name_doc}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    def cria_form(form, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_pageformat(name_format,created_fm,update_fm)
                    VALUES ('{form}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    date_today = datetime.today()

    
    # df_proj = pd.read_csv('media_files/material_start/PROJETOS.csv', sep=',')
    # df_doct = pd.read_csv('media_files/material_start/DOC_TYPE.csv','DOC_TYPE')
    # df_paget = pd.read_csv('media_files/material_start/PAGE_TYPE.csv','PAGE_TYPE')
    # df_doc = pd.read_csv('media_files/material_start/MODELO_DOCUMENTO.csv','MODELO_DOCUMENTO')
    # df_dis = pd.read_csv('media_files/material_start/DISCIPLINAS.csv','DISCIPLINAS')
    # df_st = pd.read_csv('media_files/material_start/STATUS.csv','STATUS') 
    # df_ac = pd.read_csv('media_files/material_start/ACAO.csv','ACAO')
    # df_emp = pd.read_csv('media_files/material_start/EMPLOYEES.csv','EMPLOYEES')
    # df_form = pd.read_csv('media_files/material_start/FORMAT_PAGE.csv','FORMAT_PAGE')

    # print('\n\n\n\n\n\n\n\n\n')
    # print(df_proj)
    # print('\n\n\n\n\n\n\n\n\n')

    # df_cotation = pd.read_excel('media_files/material_start/COTATION_DOC.csv','COTATION_DOC')
    # df_emission = pd.read_excel('media_files/material_start/EMISSION.csv','EMISSION')
    # df_doc-doc = pd.read_excel('media_files/material_start/DOCUMENTATION.csv','DOCUMENTATION')
    

    df_proj = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PROJECTS')
    df_doct = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DOC_TYPE')
    df_paget = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','PAGE_TYPE')
    df_doc = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','MODELO_DOCUMENTO')
    df_dis = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','DISCIPLINAS')
    df_st = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','STATUS')
    df_ac = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','ACAO')
    df_emp = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','EMPLOYEES')
    df_form = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','FORMAT_PAGE')


    for a in range(len(df_proj['NOME_PROJETO'])):
        proj_name = df_proj['NOME_PROJETO'].loc[a]
        company = df_proj['EMPRESA'].loc[a]
        comments = df_proj['COMENTARIO'].loc[a]

        cria_proj(proj_name, company, comments, date_today)


    for a in range(len(df_paget['TIPO_FOLHA'])):
        name_page = df_paget['TIPO_FOLHA'].loc[a]

        cria_paget(name_page, date_today)


    for a in range(len(df_doct['TIPO_DOC'])):
        name_doc = df_doct['TIPO_DOC'].loc[a]

        cria_doct(name_doc, date_today)


    for a in range(len(df_doc['LISTA_DOCUMENTOS'])):
        doc_name = df_doc['LISTA_DOCUMENTOS'].loc[a]
        code_doc = int(df_doc['COD_DOC_TIPO'].loc[a])
        format_doc = df_doc['FORMATO'].loc[a]
        doc_type = int(df_doc['TIPO'].loc[a])
        #print(doc_name, code_doc, format_doc, doc_type, date_today)

        cria_doc(doc_name, code_doc, format_doc, doc_type, date_today)


    for a in range(len(df_dis['NOME_DISCIPLINA'])):
        name_dis = df_dis['NOME_DISCIPLINA'].loc[a]

        cria_dis(name_dis, date_today)


    for a in range(len(df_st['STATUS'])):
        status = df_st['STATUS'].loc[a]

        cria_st(status, date_today)


    for a in range(len(df_ac['ACAO'])):
        acao = df_ac['ACAO'].loc[a]

        cria_act(acao, date_today)


    for a in range(len(df_emp['FUNCIONARIO'])):
        func = df_emp['FUNCIONARIO'].loc[a]
        cargo = df_emp['CARGO'].loc[a]
        contr = df_emp['CONTRATO'].loc[a]

        cria_func(func, cargo, contr, date_today)


    for a in range(len(df_form['FORMATO_FOLHA'])):
        form = df_form['FORMATO_FOLHA'].loc[a]

        cria_form(form, date_today)


    print('Feito!')


    #######Atualizar cargas!!!!!!!!!

#rotina_carrega_pl()