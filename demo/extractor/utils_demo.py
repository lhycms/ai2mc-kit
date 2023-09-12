from ai2mc_kit.extractor.utils import ExtractorUtils


# 1. Custom parameters
mc_folder = "/data/home/liuhanyu/hyliu/aimc_demo/mc_1"

# 2. 
utils = ExtractorUtils(mc_folder=mc_folder)
print("Step 1. Monte Carlo Summary")
print(utils)


print("Step 2. Total Steps (Only show the first 10):")
print(utils.get_steps_lst()[:10])


print("Step 3. Exchanged Steps (Only show the first 10):")
print(utils.get_exchanged_steps_lst()[:10])