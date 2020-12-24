
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
from decimal import *


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


def cria_orc(result_itens):

    def read_sql_doc(id): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_DocumentStandard
                    WHERE id = {id};
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def cria_cotation(proj_name,subj_name,doc_pattern,doc_name,doc_type,page_type,format_doc,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_cotation(proj_name_id,subject_name_id,doc_name_pattern_id,doc_name,cod_doc_type_id,page_type_id,format_doc_id,created_ct,update_ct)
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



