from enum import unique
from itertools import product
from msilib.schema import tables
from turtle import title
from app import app
from flask import render_template,request, redirect
import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np


smallcsv = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/SmallCombinedCounties.csv")
products = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedProducts1.csv")
all_countires = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/All Counties/Countries.csv")
   

@app.route('/')
def index():
         return render_template("public/index.html")
@app.route('/about', methods=["GET", "POST"])
def Project():
   
    nodup_countries = sorted(smallcsv["ReporterName"].drop_duplicates())
    nodup_products =  sorted(products['ProductDescription'].drop_duplicates())
    nodup_partners=  sorted(smallcsv['Partner'].drop_duplicates())
    nodup_clatureCode = sorted(smallcsv['NomenclatureCode'].drop_duplicates())

    products['ProductCode']=products['ProductCode'].astype(str)
    products['NomenclatureCode']=products['NomenclatureCode'].astype(str)

    smallcsv['ProductCode']=smallcsv['ProductCode'].astype(str)
    smallcsv['NomenclatureCode']=smallcsv['NomenclatureCode'].astype(str)

    PDmerged = smallcsv.merge(products, how = 'outer', left_on=['NomenclatureCode', 'ProductCode'], right_on=['NomenclatureCode', 'ProductCode']).dropna(how='all', axis='columns')
    PDmerged.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
    PDmerged.drop(["a"], axis=1, inplace=True)
    Country_names = all_countires['name']
    PDmerged['country names'] = Country_names

    if(request.method == 'POST'):
        req = request.form
        User_partners = req.getlist('Partners')
        User_countries = req.getlist('countries')
        User_products = req.getlist('Products')
        User_clatureCode = req.getlist('ClatureCode')
        
        
        PDfilter = PDmerged
      
     
        
        print(User_partners)
        if(len(User_partners) > 0):
             PDfilter = PDfilter.query("Partner in @User_partners").dropna(how='all', axis='columns')
             print(PDfilter.head(100))
        
        print(User_countries)
        if(len(User_countries) > 0):
             PDfilter = PDfilter.query("ReporterName in @User_countries").dropna(how='all', axis='columns')
             print(PDfilter.head(100))

        print(User_products)
        
        if(len(User_products) > 0):
             PDfilter = PDfilter.query("ProductDescription in @User_products & ProductDescription.notnull()").dropna(how='all', axis='columns')
             print(PDfilter.head(100))
        

        print(User_clatureCode)
        if(len(User_clatureCode) > 0):
             PDfilter = PDfilter.query("NomenclatureCode in @User_clatureCode").dropna(how='all', axis='columns')
             print(PDfilter.head(100))

       

        return redirect(request.url)
    df = px.data.gapminder().query("year==2007")
    #print(df.head(10))
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

    graph1JSON = json.dumps(fig, cls= plotly.utils.PlotlyJSONEncoder)

    return render_template("public/project.html", graph1JSON = graph1JSON,nodup_countries = nodup_countries, 
                           nodup_partners = nodup_partners,nodup_products = nodup_products,
                           nodup_clatureCode = nodup_clatureCode)

@app.route('/test')
def testDisplay():
    
    nodup_countries = sorted(smallcsv["ReporterName"].drop_duplicates())
    nodup_products =  products['Product Description'].drop_duplicates()
    nodup_partners=  sorted(smallcsv['Partner'].drop_duplicates())
   
    merged = pd.concat([smallcsv,products], join ='outer')
    
    print(merged)

    #merged = pd.merge(nodup_countries, nodup_countries, left_on='Partner'], right_on=['3 Wrd Abb'])

    return render_template('Testing/test.html')
                           