BRANCH_OFFICE_ID="branch_office_id"
BRANCH_OFFICE_NAME="name"
BRANCH_OFFICE_ADRESS="adress"
BRANCH_OFFICE_TABLE_NAME="branch_offices"

class BranchOffice:
    
    def __init__(self,branch_office_id,name,adress):
        self.branch_office_id=branch_office_id
        self.name=name
        self.adress=adress
    
    def print_branch_office(self):
        print(self.branch_office_id + " "+self.name+" "+self.adress)







