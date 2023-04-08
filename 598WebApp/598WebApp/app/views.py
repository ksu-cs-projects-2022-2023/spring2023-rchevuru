from enum import unique
from itertools import product
from msilib.schema import tables
from turtle import title
from xml.etree.ElementInclude import include
from app import app
from flask import render_template,request, redirect
import pandas as pd
import json
import plotly
import plotly.express as px
import numpy as np


Countrycsv = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedCounties2.csv")
products = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedProducts1.csv")
all_countires = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/All Counties/Countries.csv")
   
#Countrycsv.rename(columns ={'NomenCode': 'NomenclatureCode'})

@app.route('/')
def index():
         return render_template("public/index.html")
@app.route('/about', methods=["GET", "POST"])
def Project():
   
    nodup_countries = sorted(Countrycsv["ReporterName"].drop_duplicates())
    nodup_products =  sorted(products['ProductDescription'].drop_duplicates())
    nodup_partners=  sorted(Countrycsv['Partner'].drop_duplicates())
    nodup_clatureCode = sorted(Countrycsv['NomenclatureCode'].drop_duplicates())

    products['ProductCode']=products['ProductCode'].astype(str)
    products['NomenclatureCode']=products['NomenclatureCode'].astype(str)

    Countrycsv['ProductCode']=Countrycsv['ProductCode'].astype(str)
    Countrycsv['NomenclatureCode']=Countrycsv['NomenclatureCode'].astype(str)

    PDmerged = Countrycsv.merge(products, how = 'outer', left_on=['NomenclatureCode', 'ProductCode'], right_on=['NomenclatureCode', 'ProductCode']).dropna(how='all', axis='columns')
    #PDmerged.rename({"Unnamed: 0":"a"}, axis="columns", inplace=True)
   # PDmerged.drop(["a"], axis=1, inplace=True)
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
            #if User_partners contains WLD get all partners except WLD 
            
            if('WLD' not in User_partners):
                PDfilter = PDfilter.query("Partner in @User_partners").dropna(how='all', axis='columns')
               
        print(PDfilter.head(100))
        
       # PDfilter.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/testing/PD.csv")

        
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
             # maybe perform an additional check here


        partner_count = PDfilter.groupby('Partner').count().reset_index()
        product_count = PDfilter.groupby(['Partner','ReporterName','NomenclatureCode'])['ProductDescription'].count().reset_index(name = 'ProductCount')
        #product_count = PDfilter.groupby(['Partner','ProductDescription','ReporterName','NomenclatureCode']).transform('count')
        #PDfilter['product_count'] = product_count
        #PDfilter.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/testing/PD.csv")
        #product_count.to_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/testing/add.csv")

        fig = px.line_geo(data_frame=product_count,locations = 'Partner', locationmode= 'ISO-3',
                           hover_name=product_count['Partner'], 
                           hover_data= { 'ReporterName','ProductCount'},
                           line_dash = 'ProductCount', 
                           color= 'ReporterName', #value needs to be total count instead
                           #color_continuous_scale=px.colors.sequential.Turbo, 
                           #labels = {'Partner':'Partner'},
                           projection='orthographic'
                           )
        #fig.update_traces(line=dict(color="Black", width=3))

        print('fig')
        

        fig.update_layout(coloraxis_colorbar=dict(
            ticktext=PDfilter["Partner"]
            ))
        grahJSON = json.dumps(fig, cls= plotly.utils.PlotlyJSONEncoder)
        #PDfilter.drop('info')
        #fix error here
        return render_template("public/project.html", grahJSON = grahJSON,nodup_countries = nodup_countries, 
                           nodup_partners = nodup_partners,nodup_products = nodup_products,
                           nodup_clatureCode = nodup_clatureCode)
    """
    df = px.data.gapminder().query("year==2007")
    #print(df.head(10))
    
    fig = px.choropleth(df, locations="iso_alpha",
                    color="lifeExp", # lifeExp is a column of gapminder
                    hover_name="country", # column to add to hover information
                    color_continuous_scale=px.colors.sequential.Plasma)

    graph1JSON = json.dumps(fig, cls= plotly.utils.PlotlyJSONEncoder)
    """
    return render_template("public/project.html",nodup_countries = nodup_countries, 
                           nodup_partners = nodup_partners,nodup_products = nodup_products,
                           nodup_clatureCode = nodup_clatureCode)

@app.route('/included')
def includedCountries():

    df = pd.read_csv("C:/Users/nonAdmin/Documents/Classes/Cs/598(new)/seperate python scripts_Coloab doesn't like_/combine/results/CombinedCountiesNOTImportant.csv")
    #pd.set_option('display.max_colwidth', 100)
    return render_template('public/info.html', tables = [df.to_html(col_space=100,justify='left', float_format='{:10.2f}'.format)],titles = [''])

@app.route('/country_info')
def countryInfo():
    nodup_countries = sorted(Countrycsv["ReporterName"].drop_duplicates())

    products['ProductCode']=products['ProductCode'].astype(str)
    products['NomenclatureCode']=products['NomenclatureCode'].astype(str)

    Countrycsv['ProductCode']=Countrycsv['ProductCode'].astype(str)
    Countrycsv['NomenclatureCode']=Countrycsv['NomenclatureCode'].astype(str)

    PDmerged = Countrycsv.merge(products, how = 'outer', left_on=['NomenclatureCode', 'ProductCode'], right_on=['NomenclatureCode', 'ProductCode']).dropna(how='all', axis='columns')

    if(request.method == 'POST'):
        req = request.form
        User_countries = req.getlist('country_info')


    return render_template("public/country_info.html",nodup_countries = nodup_countries
                          )
@app.route('/test')
def testDisplay():
    
    nodup_countries = sorted(Countrycsv["ReporterName"].drop_duplicates())
    nodup_products =  products['Product Description'].drop_duplicates()
    nodup_partners=  sorted(Countrycsv['Partner'].drop_duplicates())
   
    merged = pd.concat([Countrycsv,products], join ='outer')
    
    print(merged)

    #merged = pd.merge(nodup_countries, nodup_countries, left_on='Partner'], right_on=['3 Wrd Abb'])

    return render_template('Testing/test.html')
                           