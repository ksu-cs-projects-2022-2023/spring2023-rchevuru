import pandas as pd
print('reading small db')
df =pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties.csv")

print(df.head(10))

print('reading add csv')
df2 = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/small csv/CoteDIVoire2.csv",engine='python')

print('combining')
df3 = pd.concat([df,df2])

df3.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties2.csv")
print('done')