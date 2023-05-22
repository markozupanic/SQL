import PySimpleGUI as sg
from Repositories.BranchOfficeRepository import BranchOfficeRepository

branch_office_repository=BranchOfficeRepository()
all_branch_offices=branch_office_repository.get_all_branch_offices()

branch_office_rows=[]

for branch_office in all_branch_offices:
    row_text=str(branch_office.branch_office_id) + " " +branch_office.name
    branch_office_rows.append([sg.Text(row_text)])

sg.theme('DarkAmber')  
layout = [  [sg.Text('Branch offices')],
            branch_office_rows]

def asd():
  window = sg.Window('Window Title', layout)

  while True:
     event, values = window.read()
     if event == sg.WIN_CLOSED or event == 'Cancel':
         break

  window.close()
  
  
  class Controller:
      def __init__(self):
         pass
  
  
  
  
  
  
  
  
  
  