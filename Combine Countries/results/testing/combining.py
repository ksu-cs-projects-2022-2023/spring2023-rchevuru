import pandas as pd
import random
smallcsv = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties1.csv")
products = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedProducts1.csv")
all_countires = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/All Counties/Countries.csv")

#merged = smallcsv.merge(products, on= ['NomenclatureCode','ProductCode']).fillna(0)
#merged = merged.drop(['Unnamed: 4', 'Unnamed: 5'])
#merged = smallcsv.merge(products, on= ['NomenclatureCode','ProductCode'])#.dropna(how='all', axis='columns')
products['ProductCode']=products['ProductCode'].astype(str)
products['NomenclatureCode']=products['NomenclatureCode'].astype(str)

smallcsv['ProductCode']=smallcsv['ProductCode'].astype(str)
smallcsv['NomenclatureCode']=smallcsv['NomenclatureCode'].astype(str)


#PDmerged = products.merge(smallcsv, on= ['NomenclatureCode','ProductCode'])#.dropna(how='all', axis='columns')
PDmerged = smallcsv.merge(products, how = 'outer', left_on=['NomenclatureCode', 'ProductCode'], right_on=['NomenclatureCode', 'ProductCode']).dropna(how='all', axis='columns')
#PDmerged.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
#PDmerged.drop(["a"], axis=1, inplace=True)
Country_names = all_countires['name']
PDmerged['country names'] = Country_names
#merged.rename({"Unnamed: 5":"a"}, axis="columns", inplace=True)
#merged.drop(["a"], axis=1, inplace=True)

print(PDmerged.head(100))
print("tail")
print(PDmerged.tail(100))
#PDmerged.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/Testb2.csv")
print("done")


partners = []
countries = []
product = []
rist = []

product_dict = products['ProductDescription'].drop_duplicates()
partners_dict = sorted(smallcsv['Partner'].drop_duplicates()) 

rist_full = ['H0','H1','H2','H3','H4','HS']
product_full = [product_dict]
countries_full = ['Afghanistan','Algeria','Australia','Bangladesh']
partners_full = [partners_dict]

rist_part = ['H0','H1','H2']
product_part = [product_dict.sample(n=4)]
countries_part = ['Afghanistan','Algeria']
partners_part = [random.sample(partners_dict, 3)]


PDfilter = PDmerged.query(" ReporterName in @countries_full").dropna(how='all', axis='columns')
print(PDfilter.head(100))
print("filter")

if(len(rist) > 1):
            for restric in rist:
               if restric in PDmerged['NTMNomenclature'].values:
                   print("multiple items in restrictions")
elif(len(rist) == 1):
           if(rist[0] == PDmerged['NTMNomenclature'].values):
                  print("one item in restrictions")
else:
            print("no items")
