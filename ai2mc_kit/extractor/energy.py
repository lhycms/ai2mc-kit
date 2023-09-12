import os
from typing import List, Union

from .base import BaseExtractor
from .utils import ExtractorUtils


class EnergyExtractor(object):
    '''
    Description
    -----------
        1. AI2MC 会将 VASP/PWmat/mlff 的能量存储到 energy.txt 文件中
            $ vim energy.txt
            -760.33556 eV
    '''
    def __init__(self, mc_folder:str):
        self.mc_folder = mc_folder
        self.utils = ExtractorUtils(mc_folder=self.mc_folder)
        #self.steps_lst = self.utils.get_steps_lst()
        #self.exchanged_steps_lst = self.utils.get_exchanged_steps_lst()
    
    
    def execute(self, option:str="all"):
        if option.lower() == "all":
            steps_lst = self.utils.get_steps_lst()
        elif option.lower() == "exchanged":
            steps_lst = self.utils.get_exchanged_steps_lst()
        
        energys_lst:List[float] = []
        for ii in steps_lst:
            energy_txt_path = os.path.join(self.mc_folder, str(ii), "energy.txt")
            with open(energy_txt_path, "r") as tmp_f:
                tmp_energy = tmp_f.read()
                energys_lst.append(float(tmp_energy.split()[0].strip()))
        
        return energys_lst