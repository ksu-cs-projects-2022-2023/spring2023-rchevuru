import pandas as pd
csvfile = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/Algeria2.csv")

part = sorted(csvfile['Partner'].astype(str).drop_duplicates())

print(part)