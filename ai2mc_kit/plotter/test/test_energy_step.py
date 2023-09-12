import unittest

# python3 -m ai2mc_kit.plotter.test.test_energy_step
from ...extractor.energy import EnergyExtractor
from ...extractor.utils import ExtractorUtils
from ..energy_step import EnergyStepPlot


mc_folder = "/data/home/liuhanyu/hyliu/aimc_demo/mc_1"
jpg_path = "/data/home/liuhanyu/hyliu/code/ai2mc-kit/test_data/energy_step.jpg"

class EnergyStepPlotTest(unittest.TestCase):
    def test_all(self):
        utils = ExtractorUtils(mc_folder=mc_folder)
        energy_extractor = EnergyExtractor(mc_folder=mc_folder)
        
        steps_lst = utils.get_steps_lst()
        exchanged_steps_lst = utils.get_exchanged_steps_lst()
        energys_lst = energy_extractor.execute(option="all")

        plotter = EnergyStepPlot(
                    steps_lst=steps_lst,
                    exchanged_steps_lst=exchanged_steps_lst,
                    energys_lst=energys_lst)

        plotter.plot(jpg_path=jpg_path)
        
    
    
if __name__ == "__main__":
    unittest.main()