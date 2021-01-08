
# # Remove Outliers form CSV dataset (IQR Method)

import matplotlib.pyplot as plt
import pandas
import sys

def loadDataFrameFromCsvFile(url,names):
    data = pandas.read_csv(url, usecols=names)
    return data

def RemoveOutlierIQR(rawData,columnNames,groupLabel):
    df_all_clean = pandas.DataFrame(columns = columnNames) 
    for name, group in rawData.groupby(['ObjectClass']):
        Q1 = group.quantile(0.25)
        Q3 = group.quantile(0.75)
        IQR = Q3 - Q1

        data_clean = group[~((group < (Q1 - 1.5 * IQR)) |(group > (Q3 + 1.5 * IQR))).any(axis=1)]
        df_all_clean = pandas.concat([df_all_clean,data_clean])
    return df_all_clean

# ==================================================
# --- MAIN -----------------------------------------
def main(argv):
    if len(argv)!= 3:
        print("usage: remove-outliers.py <sourceDataset Path/URL> <datasetName> <labelColumn>")
        sys.exit(2)

    sourceDataset = argv[0]
    datasetName = argv[1]
    labelColumn = argv[2]

    names = ['HCSR04_001', 'HCSR04_002', 'HCSR04_003', 'HCSR04_004', 'HCSR04_005', 'HCSR04_006', 'HCSR04_007','ObjectClass']

    data= loadDataFrameFromCsvFile(sourceDataset,names)
    data_outliers_removed=RemoveOutlierIQR(data,names,labelColumn)
    data_outliers_removed.to_csv(datasetName+"_outliers_removed.csv")


if __name__ == "__main__":
   main(sys.argv[1:])