
# read_all[0] = MyProject
    # read_all[1] = PageT
    # read_all[2] = DOCT
    # read_all[3] = Subject
    # read_all[4] = DocumentStandard
    # read_all[5] = Employee
    # read_all[6] = StatusDoc
    # read_all[7] = Action

''' read_all = delete_itens.delete_befor()

    if read_all[0]:
        for id in read_all[0]:
            proj = get_object_or_404(MyProject, pk=id)
            proj.delete()
    
    if read_all[1]:
        for id in read_all[1]:
            dot = get_object_or_404(PageT, pk=id)
            dot.delete()

    if read_all[2]:
        for id in read_all[2]:
            dot = get_object_or_404(DocT, pk=id)
            dot.delete()

    if read_all[3]:
        for id in read_all[3]:
            pag = get_object_or_404(Subject, pk=id)
            pag.delete()

    if read_all[4]:
        for id in read_all[4]:
            doc = get_object_or_404(DocumentStandard, pk=id)
            doc.delete()


    if read_all[5]:
        for id in read_all[5]:
            emp = get_object_or_404(Employee, pk=id)
            emp.delete()


    if read_all[6]:
        for id in read_all[6]:
            st = get_object_or_404(StatusDoc, pk=id)
            st.delete()


    if read_all[7]:
        for id in read_all[7]:
            ac = get_object_or_404(Action, pk=id)
            ac.delete()'''

















import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
import xlrd


def delete_befor():
    #------------------------------------------------
    def read_proj():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_myproject;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_pag():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_paget;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    def read_dot():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_doct;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_sub():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_subject;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_doc():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_documentstandard;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_emp():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_employee;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_st():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_statusdoc;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_ac():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_action;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

 
    #------------------------------------------------
    new_proj, new_pag, new_dot, new_sub, new_doc, new_emp, new_st, new_ac = [],[],[],[],[],[],[],[]
    
    #------------------------------------------------
    for i in read_proj()['id']:
        new_proj.append(i)

    for i in read_pag()['id']:
        new_pag.append(i)

    for i in read_dot()['id']:
        new_dot.append(i)

    for i in read_sub()['id']:
        new_sub.append(i)

    for i in read_doc()['id']:
        new_doc.append(i)

    for i in read_emp()['id']:
        new_emp.append(i)

    for i in read_st()['id']:
        new_st.append(i)

    for i in read_ac()['id']:
        new_ac.append(i)

    read_all = [new_proj, new_pag, new_dot, new_sub, new_doc, new_emp, new_st, new_ac]

    return read_all

    

def delete_cotation():
    #------------------------------------------------
    def read_cota():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_cotation;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    new_cota = []

    for i in read_cota()['id']:
        new_cota.append(i)

    read_all = new_cota

    return read_all