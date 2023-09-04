import os
from typing import List


class ExtractorUtils(object):
    def __init__(self, mc_folder:str):
        self.mc_folder = mc_folder
    
    def get_steps_lst(self):
        '''
        Description
        -----------
            1. 得到 ai2mc 计算的所有步数 (从小到大排序)
        '''
        steps_lst:List[int] = \
            [
                int(tmp_fname) for tmp_fname in os.listdir(self.mc_folder) \
                if os.path.isdir(os.path.join(self.mc_folder, tmp_fname)) and \
                any(tmp_c.isdigit() for tmp_c in tmp_fname)
            ]
            
        return sorted(steps_lst)
            
            
    def get_max_step(self):
        '''
        Description
        -----------
            1. 得到 ai2mc 模拟的最大步数
        '''
        steps_lst:List[int] = self.get_steps_lst()
        return max(steps_lst)
    
    
    def get_exchanged_steps_lst(self):
        '''
        Description
        -----------
            1. 得到 mc 模拟中的接收步数
        '''
        exchanged_steps_lst:List[int] = []
        for ii in self.get_steps_lst():
            if os.path.exists(os.path.join(self.mc_folder, str(ii), "exchanged.txt")):
                exchanged_steps_lst.append(ii)
        return exchanged_steps_lst