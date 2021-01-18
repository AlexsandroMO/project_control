
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
from decimal import *
import time


date_today = datetime.today()


def cria_orc_all(GET, DocumentStandards):

    def cria_cota(proj, sub, id_doc,name_doc,type_id,type_page_id,format_id,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO documentation_cotation(proj_name_id,subject_name_id,doc_name_pattern_id,doc_name,cod_doc_type_id,page_type_id,format_doc_id,qt_page,qt_hh,cost_doc,created_ct,update_ct)
                    VALUES ('{proj}','{sub}','{id_doc}','{name_doc}','{type_id}','{type_page_id}','{format_id}',0,0,0,'{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

    
    for i in DocumentStandards:
        #print('>>>>>>',GET['proj'][0], GET['sub'][0], i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id,date_today)
        cria_cota(int(GET['proj'][0]), int(GET['sub'][0]), i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id,date_today)


def cria_orc_ind(GET):

    def read_sql_doc(id_doc): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM documentation_documentstandard
                    WHERE id = {id_doc};
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db
    
    def cria_cota(proj, sub, id_doc,name_doc,type_id,type_page_id,format_id,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO documentation_cotation(proj_name_id,subject_name_id,doc_name_pattern_id,doc_name,cod_doc_type_id,page_type_id,format_doc_id,qt_page,qt_hh,cost_doc,created_ct,update_ct)
                    VALUES ('{proj}','{sub}','{id_doc}','{name_doc}','{type_id}','{type_page_id}','{format_id}',0,0,0,'{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

    
    for i in range(1,len(GET['action'])):
        readed = read_sql_doc(GET['action'][i])
        print('>>>id>>>', readed['id'])
        #print('>>>doc>>>', readed['documment_name'][0])
        #print('>>>type>>>', readed['doc_type_id'])
        #print('>>>page>>>', readed['doc_type_page_id'])
        #print('>>form>>>>', readed['format_doc_id'])
        #print('>>>>date>>', date_today)

        cria_cota(int(GET['proj'][0]), int(GET['sub'][0]), int(readed['id']),readed['documment_name'][0], int(readed['doc_type_id']),int(readed['doc_type_page_id']),int(readed['format_doc_id']),date_today)



def calc_cota(Cotations):

    for a in Cotations:
        print('::::', a.proj_name, a.doc_name_pattern)

    pass













'''

def cria_orc_all(GET, MyProjects,DocumentStandards,Subjects,Cotation,form_proj,form_dis,form_doc,form_cota,proj, sub):

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


    
    for i in DocumentStandards:
        print('>>>>>>',DocumentStandards[i].id, DocumentStandards[i].documment_name, DocumentStandards[i].doc_type_id,DocumentStandards[i].doc_type_page_id,DocumentStandards[i].format_doc_id, '>>>>',len(DocumentStandards))
        cria_cota(int(GET['proj'][0]), int(GET['sub'][0]), i.id, i.documment_name, i.doc_type_id,i.doc_type_page_id,i.format_doc_id)


def cria_orc_unic(GET, id_proj, documment, doc_type,doc_type_page,format_doc, form_cota):

    def cria_cota(proj, sub, id_proj, documment, doc_type,doc_type_page,format_doc):
        cota = form_cota.save(commit=False)
        cota.proj_name_id = int(proj)
        cota.subject_name_id = int(sub)
        cota.doc_name_pattern_id = int(id_proj)
        cota.doc_name = documment
        cota.cod_doc_type_id = int(doc_type)
        cota.page_type_id = int(doc_type_page)
        cota.format_doc_id = int(format_doc)
        cota.qt_page = 0
        cota.qt_hh = 0
        cota.cost_doc = 0
        cota.save()

    
    cria_cota(GET['proj'][0], GET['sub'][0], id_proj,documment,doc_type,doc_type_page,format_doc)'''