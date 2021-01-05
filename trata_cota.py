
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
from decimal import *
import time

def cria_orc_all(MyProjects,DocumentStandards,Subjects,Cotation,form_proj,form_dis,form_doc,form_cota,proj, sub):

    def cria_cota(proj, sub, id_proj, documment, doc_type,doc_type_page,format_doc):
        cota = form_cota.save(commit=False)
        cota.proj_name_id = proj
        cota.subject_name_id = sub
        cota.doc_name_pattern_id = int(id_proj)
        cota.doc_name = documment
        cota.cod_doc_type_id = int(doc_type)
        cota.page_type_id = int(doc_type_page)
        cota.format_doc_id = int(format_doc)
        cota.qt_page = 0
        cota.qt_hh = 0
        cota.cost_doc = 0
        cota.save()

    #for i in range(len(DocumentStandards)):
    for i in DocumentStandards:
        #print('>>>>>>',i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id, '>>>>',len(DocumentStandards))
        #print('>>>>>>',DocumentStandards[i].id, DocumentStandards[i].documment_name, DocumentStandards[i].doc_type_id,DocumentStandards[i].doc_type_page_id,DocumentStandards[i].format_doc_id, '>>>>',len(DocumentStandards))
        #cria_cota(int(proj), int(sub), DocumentStandards[i].id, DocumentStandards[i].documment_name, DocumentStandards[i].doc_type_id,DocumentStandards[i].doc_type_page_id,DocumentStandards[i].format_doc_id)
        cria_cota(int(proj), int(sub), i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id)

 








'''
#-----------------------------------
def trata_cotation(val, cost_type):

    def read_sql_cota():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_cotation
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    def cria_cota(custo,date_today,id):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    UPDATE taskproject_cotation
                    SET cost_doc = {custo}, update_ct = '{date_today}'
                    WHERE id = {id};
                    """

        c.execute(qsl_datas)
        conn.commit()
        conn.close()

    date_today = datetime.today()
    cota = read_sql_cota()


    for a in range(len(cota)):
        if cost_type == 'option1':
            if str(cota['qt_hh'].loc[a]) != 'nan':
                custo = Decimal(cota['qt_hh'].loc[a]) * Decimal(val)
                cria_cota(custo, date_today, cota['id'].loc[a])
            else:
                print('É necessário que o campo QT_HH estejam preenchidos')

        elif cost_type == 'option2':
            if str(cota['qt_page'].loc[a]) != 'nan' and str(cota['qt_hh'].loc[a]) != 'nan':
                custo = Decimal(val)
                cria_cota(custo, date_today, cota['id'].loc[a])
            else:
                print('É necessário que o campo QT_PAGE estejam preenchidos') 

        elif cost_type == 'option3':
            if str(cota['qt_page'].loc[a]) != 'nan':
                if cota['page_type_id'].loc[a] == 0:
                    custo = (Decimal(val) * 2) * Decimal(cota['qt_page'].loc[a])
                    cria_cota(custo, date_today, cota['id'].loc[a])

                elif cota['page_type_id'].loc[a] == 1:
                    custo = Decimal(val) * Decimal(cota['qt_page'].loc[a])
                    cria_cota(custo, date_today, cota['id'].loc[a])

                elif cota['page_type_id'].loc[a] == 2:
                    custo = (Decimal(val) / 2) * Decimal(cota['qt_page'].loc[a])
                    cria_cota(custo, date_today, cota['id'].loc[a])

                elif cota['page_type_id'].loc[a] == 3:
                    custo = (Decimal(val) / 4) * Decimal(cota['qt_page'].loc[a])
                    cria_cota(custo, date_today, cota['id'].loc[a])

                elif cota['page_type_id'].loc[a] == 4:
                    custo = (Decimal(val) / 8) * Decimal(cota['qt_page'].loc[a])
                    cria_cota(custo, date_today, cota['id'].loc[a])

            else:
                print('É necessário que o campo QT_PAGE estejam preenchidos')     
   
    return 'Feito!'


def cria_orcxx(result_itens):

    def read_sql_doc(id): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM documentation_documentstandard
                    WHERE id = {id};
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def cria_cotation(proj_name,subj_name,doc_pattern,doc_name,doc_type,page_type,format_doc,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO documentation_cotation(proj_name_id,subject_name_id,doc_name_pattern_id,doc_name,cod_doc_type_id,page_type_id,format_doc_id,created_ct,update_ct)
                    VALUES ('{proj_name}','{subj_name}','{doc_pattern}','{doc_name}','{doc_type}','{page_type}','{format_doc}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    date_today = datetime.today()
    print('\n-----------------------------')
    
    for i in range(len(result_itens[1])):
        doc = read_sql_doc(int(result_itens[1][i]))
        name = doc['documment_name'].loc[0]

        cria_cotation(int(result_itens[0][1]), int(result_itens[0][2]), doc['id'].loc[0], name, doc['doc_type_id'].loc[0],doc['doc_type_page_id'].loc[0],doc['format_doc_id'].loc[0], date_today)

 
    return 'feito!'




















def cria_orc_all(proj, sub):

    def read_sql_doc():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM documentation_documentstandard
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def cria_cotation(proj_name,subj_name,doc_pattern,doc_name,doc_type,page_type,format_doc,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO documentation_cotation(proj_name_id,subject_name_id,doc_name_pattern_id,doc_name,cod_doc_type_id,page_type_id,format_doc_id,created_ct,update_ct)
                    VALUES ('{proj_name}','{subj_name}','{doc_pattern}','{doc_name}','{doc_type}','{page_type}','{format_doc}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    date_today = datetime.today()
    doc = read_sql_doc()

    for i in range(len(doc['id'])):
        print('>>>>>>',i)
        #doc['documment_name'].loc[i]
        #name = doc['documment_name'].loc[0]

        cria_cotation(int(proj), int(sub), doc['id'].loc[i], doc['documment_name'].loc[i], doc['doc_type_id'].loc[i],doc['doc_type_page_id'].loc[i],doc['format_doc_id'].loc[i], date_today)


    return 'feito!'''