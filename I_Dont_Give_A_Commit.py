import requests
from collections import defaultdict as ddict
import os
from openpyxl import load_workbook
from alive_progress import alive_bar

DIR = os.path.dirname(os.path.realpath(__file__))
TARGET = fr'{DIR}\\target'
RES = fr'{DIR}\\res'

class IDGAC:
    
    def __init__(self) -> None:
        self.lacking_by_coach = ddict(dict)
        
        
    def __grab_data_from_file(self) -> None:
        """
        This function reads data from an Excel file in the target folder and populates a dictionary with the data.
        """
        target_file = os.listdir(TARGET)[0]
        data = load_workbook(fr'{TARGET}\\{target_file}')
        sheet = data.active
        self.total_seekers = sheet.max_row-1

        with alive_bar(sheet.max_row-1, title="Grabing Data...") as bar:
            for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row):
                curr_row = dict()
                for idx, cell in enumerate(row):
                    
                    data_list = {
                        0: 'seeker',
                        1: 'coach',
                        2: 'status',
                        3: 'solo',
                        4: 'capstone',
                        5: 'group'
                    }
                    
                    val = cell.value
                    if val == ' ' and idx == 1:
                        val = 'Placements' 
                    
                    curr_row[data_list[idx]] = val
                    
                        
                
                for proj in ['status', 'solo', 'capstone', 'group']:
                    self.sites_by_coach[curr_row['coach']][curr_row['seeker']][proj] = curr_row[proj]
                bar()
    
    
    def main(self):
        self.__grab_data_from_file()
    
    
    
if __name__ == '__main__':
    if not os.path.isdir(RES):
        os.mkdir(RES)
        
    idgac = IDGAC()
    idgac.main()