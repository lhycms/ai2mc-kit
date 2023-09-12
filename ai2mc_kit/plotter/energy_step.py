import matplotlib.pyplot as plt
from typing import Union, List



class EnergyStepPlot(object):
    def __init__(self,
                steps_lst:List[int],
                exchanged_steps_lst:List[int],
                energys_lst:List[int]):
        self.steps_lst = steps_lst
        self.exchanged_steps_lst = exchanged_steps_lst
        self.energys_lst = energys_lst
        self.exchanged_energys_lst = [energys_lst[ii] for ii in self.exchanged_steps_lst]
    
    
    def plot(self, jpg_path:str, yrange:Union[List[float], bool]=False):
        ### 0. 全局设置
        # 0.1. 字体设置
        plt.rcParams["font.family"] = "Times New Roman"
        plt.rcParams['mathtext.fontset'] = 'custom'
        plt.rcParams['mathtext.rm'] = 'Times New Roman'
        plt.rcParams['mathtext.it'] = 'Times New Roman:italic'
        plt.rcParams['mathtext.bf'] = 'Times New Roman:bold'
        # 0.2. 刻度线朝内
        plt.rcParams['xtick.direction'] = 'in'
        plt.rcParams['ytick.direction'] = 'in'
        plt.figure(figsize=(10, 8))
        
        # 1. Plot
        plt.scatter(self.steps_lst, self.energys_lst,
                    s=70,
                    color="#FD6D5A",
                    edgecolors="black",
                    label="Rejected")
        plt.plot(self.exchanged_steps_lst, self.exchanged_energys_lst,
                color="steelblue",
                linewidth=3,
                label="Accepted")
    
    
        # 2. xlabel, ylabel
        plt.xlabel("Steps", fontsize=28, fontweight="bold")
        plt.ylabel("Energy (eV)", fontsize=28, fontweight="bold")
        
        # 3. xaxis, yaxis
        plt.xticks(fontsize=20, fontweight="bold")
        plt.yticks(fontsize=20, fontweight="bold")
        
        # 4. y range()
        if (yrange):
            if ((len(yrange) == 2) and (yrange[0] < yrange[1])):
                plt.ylim([yrange[0], yrange[1]])
        
        # 5. 刻度线粗细
        plt.tick_params(
            width=2,        # 刻度线的粗细
            length=5,       # 刻度线的长短
            #labelsize=28   # 刻度线的字体大小
        )
        
        # 5. 设置坐标轴的粗细
        ax = plt.gca()
        ax.spines['bottom'].set_linewidth(1.5);###设置底部坐标轴的粗细
        ax.spines['left'].set_linewidth(1.5);####设置左边坐标轴的粗细
        ax.spines['right'].set_linewidth(1.5);###设置右边坐标轴的粗细
        ax.spines['top'].set_linewidth(1.5);###设置右边坐标轴的粗细
        
        # 6. label字体
        legend_font = {"size" : 23, 
                "weight": "bold"
                }
        plt.legend(loc=(0.6, 0.75),
                prop=legend_font,
                frameon=False)
        
        plt.savefig(jpg_path, dpi=300, bbox_inches="tight")