import unittest

# python3 -m ai2mc_kit.extractor.tests.test_energy
from ..energy import EnergyExtractor


mc_folder = "/data/home/liuhanyu/hyliu/aimc_demo/mc_1"

class EnergyExtractorTest(unittest.TestCase):
    def test_all(self):
        energy_extractor = EnergyExtractor(mc_folder=mc_folder)
        energys_lst = energy_extractor.execute(option="exchanged")
        print(energys_lst)
    
    
    def test_vasp(self):
        energy_extractor = EnergyExtractor(mc_folder=mc_folder, fmt="vasp")
        energys_lst = energy_extractor.execute()
        print(energys_lst)



if __name__ == "__main__":
    unittest.main()