import unittest

# python3 -m ai2mc_kit.extractor.tests.test_utils
from ..utils import ExtractorUtils


mc_folder = "/data/home/liuhanyu/hyliu/aimc_demo/mc_1"


class ExtractorUtilsTest(unittest.TestCase):
    def test_all(self):
        utils = ExtractorUtils(mc_folder=mc_folder)
        print("Step 1. MC simulation 的所有步数:\n", utils.get_steps_lst())
        
        print("\nStep 2. MC simulation 的最大步数:\t", utils.get_max_step())
        
        print("\nStep 3. MC simulation 的所有接收步数", utils.get_exchanged_steps_lst())
        

if __name__ == "__main__":
    unittest.main()