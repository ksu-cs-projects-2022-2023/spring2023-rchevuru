import pandas as pd
import numpy as np
import plotly.express as px

PDfilter = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/testing/add.csv")
print(PDfilter.head(5))
PDfilter.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)

PDfilter.drop(["a"], axis=1, inplace=True)
print(PDfilter.head(5))

#PDfilter.sort_values(by='ReporterName',inplace=True)
#print(PDfilter.head(5))
print("")
locAndHover = []
partners = PDfilter['Partner']
threeAbb = PDfilter['3 Wrd Abb']
print(partners)
print(threeAbb)

print(len(partners))
print(len(threeAbb))
    
for i in range(len(partners)):
    locAndHover.append(partners[i])
    locAndHover.append(threeAbb[i])

print(locAndHover)

#print(PDfilter.head(5))

Answer = PDfilter
aws = pd.Series(locAndHover)
#Answer.insert(loc=0, column='loc and hover data', value=aws)
Answer['loc and hover data'] = aws
print(Answer.head(50))

print("")
print("")

partnerPD = PDfilter['Partner']
CountryPD = PDfilter['3 Wrd Abb']

newPD = pd.DataFrame()
newPD["country"] = CountryPD
newPD["Partner"] = partnerPD

print(newPD.head(5))
fig = px.line_geo(data_frame=newPD, 
                   locations=[newPD["country"], newPD["Partner"]], #has to be country name
                   hover_name=[newPD["country"], newPD["Partner"]], 
                  # hover_data={'Partner','ReporterName','ReporterName', 'NomenclatureCode','ProductCount'},
                   #line_dash='ReporterName', 
                   #color='ProductCount', #value needs to be total count instead
                   #color_continuous_scale=px.colors.sequential.Turbo, 
                  # labels={'Partner':'Partner'},
                   projection='orthographic')

fig.show()