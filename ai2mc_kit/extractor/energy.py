import os
from typing import List

from .base import BaseExtractor
from .utils import ExtractorUtils


class EnergyExtractor(BaseExtractor):
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
    
    
    def execute(self):
        steps_lst:List[int] = self.utils.get_steps_lst()
        for ii in steps_lst:
            energy_txt_path = os.path.join(self.mc_folder, str(ii), "energy.txt")
            with open(energy_txt_path, "r") as tmp_f:
                tmp_energy = tmp_f.read()
                print(tmp_energy)