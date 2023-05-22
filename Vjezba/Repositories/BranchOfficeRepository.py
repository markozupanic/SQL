from Models.BranchOffice import BranchOffice,BRANCH_OFFICE_ID,BRANCH_OFFICE_NAME,BRANCH_OFFICE_ADRESS,BRANCH_OFFICE_TABLE_NAME
import pymysql


class BranchOfficeRepository:
    
    connection=pymysql.connect(host="localhost",user="root",passwd="",database="bankdatabase",cursorclass=pymysql.cursors.DictCursor)
    
    def __init__(self):
        pass
    
    def convert_list_dict_to_list_branch_office(self,result):
        object_list=[]
        for row in result:
            object_list.append(BranchOffice(row[BRANCH_OFFICE_ID],row[BRANCH_OFFICE_NAME],row[BRANCH_OFFICE_ADRESS]))
        return object_list
    
    def get_all_branch_offices(self):
        cursor=self.connection.cursor()
        query=f"SELECT * FROM {BRANCH_OFFICE_TABLE_NAME};"
        cursor.execute(query)
        result=cursor.fetchall()
        return self.convert_list_dict_to_list_branch_office(result)
        
        











