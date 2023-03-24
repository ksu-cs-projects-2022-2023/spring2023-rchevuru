import pandas as pd
bigCSV = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties.csv")
print("read \n")
Names = sorted(bigCSV["ReporterName"].drop_duplicates())
ISO_code3 = sorted(bigCSV["3 Wrd Abb"].drop_duplicates())
ISO_code2 = sorted(bigCSV["2 Wrd Abb"].drop_duplicates())
country_Lat = sorted(bigCSV["Lat"].drop_duplicates())
country_Long = sorted(bigCSV["Lng"].drop_duplicates())

df = pd.DataFrame()
df.insert(0,'Country Name', Names)
df.insert(1,'3 word Abbreviation', ISO_code3)
df.insert(2,'2 word Abbreviation', ISO_code2)
df.insert(3,'Latatude', country_Lat)
df.insert(4,'Longitude', country_Long)

print(df.head(10))