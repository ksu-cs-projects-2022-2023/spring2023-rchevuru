import os
import glob
import pandas as pd
print("start")
#csv_files = glob.glob('*.{}'.format('csv'))
csv_files = glob.glob("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/small csv/" + '*.{}'.format('csv'))
print(csv_files)
combined = pd.DataFrame()
for file in csv_files:
    tempRead = pd.read_csv(file,encoding="utf-8") 
    print(file)
    combined = combined.append(tempRead, ignore_index=True)
combined.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties.csv")
print("Done")