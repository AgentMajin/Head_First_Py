import csv
import glob


# Create an array for saving all .csv file directory
directory_path = "D:/P.Truong/Master Data/Masterdata/SKU/SKU - Store Update/csv converted/"
filenames = glob.glob(directory_path + '/*.csv')

# Create arrays for categorizing file, a file would be in at least 1 array and can be in more than 1 array
HMP = []
TPCN = []
DD = []
All_3 = []

# Create 3 array to categorizing SKUs:
SKU_HMP = []
SKU_TPCN = []
SKU_DD = []
with open(directory_path + 'SKU_NH-added.csv','r') as input_SKUs:
    reader = csv.DictReader(input_SKUs)
    for skus in reader:
        print(skus)


# Categorizing Files
for filename in filenames:
    if filename.find("HMP") != -1:
        HMP.append(filename)
    if filename.find("TPCN") != -1:
        TPCN.append(filename)
    if filename.find("DD") != -1:
        DD.append(filename)
    if filename not in HMP and filename not in TPCN and filename not in DD:
        All_3.append(filename)





