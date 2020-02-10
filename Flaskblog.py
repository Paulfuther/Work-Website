from flask import Flask, render_template, jsonify, request, send_file, url_for, redirect, flash
from random import sample
from flask_mysqldb import MySQL
from flask_moment import Moment
from datetime import time
import os
from werkzeug.utils import secure_filename
import pandas as pd
import numpy
import openpyxl
import xlrd
import xlwt
import xlsxwriter
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename , asksaveasfile
import datetime
from io import BytesIO
from openpyxl.reader.excel import load_workbook
from os import environ

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(APP_ROOT, 'Files')

#print(UPLOAD_FOLDER)


app = Flask(__name__)

app.config.from_object("config.ProductionConfig")

moment = Moment(app)

app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
mysql= MySQL(app)

chartstore =48314


@app.route("/")
@app.route("/home")
def home():
    return render_template ('home.html')
    #return render_template('home.html',posts=posts)
    
@app.route("/about")
def about():
    return render_template('about.html', title ='About')



@app.route("/applications")
def Applications():
    return render_template('applications.html', title ='Applications')

@app.route("/kpiconvert")
def Kpiconvert():
    return render_template('kpiconvert.html', title ='KPI Converter')

@app.route("/carwashkpiconvert")
def CarwashKPIconvert():
    return render_template('carwashkpiconvert.html', title ='Carwash KPI Converter')

@app.route("/carwashkpiupload" , methods=['POST'])
def carwashkpiupload():
    
    if request.method=="POST":
        
         file = request.files['cwinputFile']
         print(file)
         filename = secure_filename(file.filename)
         
         excel_file = file

         df=pd.read_excel(excel_file, skiprows=9,usecols=(3,4,5))

         columnheaders = (df.columns.tolist())
         current_cwdate=(columnheaders[1])
         x = datetime.datetime.strptime(current_cwdate, "%Y/%b").strftime("%b-%Y")
         previous_cwdate=(columnheaders[2])
         px = datetime.datetime.strptime(previous_cwdate, "%Y/%b").strftime("%b-%Y")


         #get list of sheets
         xls=pd.ExcelFile(excel_file)
         res=len(xls.sheet_names)
         nres=res-1

         #get type for the tab names they are a list
         #print(type(res))

         tabs=(xls.sheet_names)
         #print(type(tabs))
         newtabs=(tabs[0:-1])

         dffinal2=[]

         for line in newtabs:
        
            #first half of spreadsheet
        
            type=line.split("_")[1]
            df=pd.read_excel(excel_file,sheet_name=line, skiprows=9,usecols=(3,4,5))
            df.columns = ['a',x,px]
            df['store']=type
            df['Date']=x
            df1=df.iloc[1:3].copy()
            df1['label']='revenue'
            df2=df.iloc[4:14].copy()
            df2['label']='expense'
            df3=df.iloc[17:26].copy()
            df3['label']='operation performnce'
            df4=df.iloc[30:37].copy()
            df4['label']='sales performance'
            df5=df.iloc[40:45].copy()
            df5['label']='paid units %'
            df6=df.iloc[46:52].copy()
            df6['label']='paid units Instore and Crind'
            df7=df.iloc[54:68].copy()
            df7['label']='total units'
            dfpartone=pd.concat([df1,df2,df3,df4,df5,df6,df7])

            #second half of spreadsheet
            
            dftwo=pd.read_excel(excel_file,sheet_name=line,skiprows=9,usecols=(3,8,9))
            dftwo.columns = ['a',x,px]
            
            dftwo['store']=type
            dftwo['Date']=x

            df8=dftwo.iloc[1:3].copy()
            df8['label']='revenue per car'
            df9=dftwo.iloc[4:14].copy()
            df9['label']='expense per car'
            df10=dftwo.iloc[40:45].copy()
            df10['label']='% fullfillment per car'
            df11=dftwo.iloc[46:52].copy()
            df11['label']='paid fullfillments'
            df12=dftwo.iloc[54:68].copy()
            df12['label']='total fullfillments'
            dfparttwo=pd.concat([df8,df9,df10,df11,df12])
            
            
            dffinal=pd.concat([dfpartone,dfparttwo])
        
            #final table of data
        
            dffinal2.append(dffinal)

         #reorganise columns  
            
         dffinal2=pd.concat(dffinal2)
         dffinal2.columns=['Item','Amount',px,'Store','Date','Classification']

         dffinal2=dffinal2[['Date','Store','Classification','Item','Amount',px]]
         dffinal2['Amount'] = pd.to_numeric(dffinal2['Amount'],errors='coerce')
         dffinal2['Date']=pd.to_datetime(dffinal2['Date'], format='%b-%Y')
         dffinal2['Date']=dffinal2['Date'].dt.date

         #save final spreadsheet

         #outputfilename = asksaveasfilename(filetypes=[("Excel files","*.xlsx")])
         #dffinal2.to_excel(outputfilename + ".xlsx", engine='xlsxwriter')

         #dffinal.to_excel("test.xlsx")

         
         
    output=BytesIO()
    writer=pd.ExcelWriter(output, engine='xlsxwriter')
    dffinal2.to_excel(writer)
    writer.save()
    output.seek(0)
            
    return send_file(output, attachment_filename="cwoutput.xlsx", as_attachment=True)       
         

    return render_template("applications.html")


@app.route("/upload" , methods=['POST'])
def upload():
    
    if request.method=="POST":
            
            file = request.files['inputFile']
            print(file)
            filename = secure_filename(file.filename)
            
            #this will save file to folder in root named Files
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            def convert_amount(val):
                """
                Convert the string number value to a float
                - Remove $
                - Remove commas
                - Convert to float type
                """
                new_val = val.replace(',','').replace('%','').replace('/0','')
                return pd.to_numeric(new_val)

            excel_file = file
            df = pd.read_excel(excel_file,header=3)

            #print (df)

            xls=pd.ExcelFile(excel_file)
            res=len(xls.sheet_names)
            tabs=(xls.sheet_names)
            newtabs=(tabs)
            columnheaders = (df.columns.tolist())
            #print (columnheaders)
            kpidate=(columnheaders[2])
           
            current_kpidate = datetime.datetime.strptime(kpidate, "%Y-%m").strftime("%b-%Y")
            #print (current_kpidate)
            newkpi=[]
            finalkpi=[]

            for x in newtabs:
                    type=x[:5]
                    #print(type)
                    data = pd.read_excel(excel_file, sheet_name=x, skiprows=3, usecols =range(8))
                    data['store']=type
                    data['Date']=current_kpidate
                    finalkpi.append(data)

            finalkpi=pd.concat(finalkpi)

            #print(finalkpi)

            #name columns
            
            finalkpi.columns = ['Category1','Category2',kpidate,'Value2','value3','value4','value5','Rolling','Store','Date']
            #reorder columns
            
            finalkpi=finalkpi[['Date','Store','Category1','Category2',kpidate,'Value2','value3','value4','value5','Rolling']]

            """combine two columns
            """
            finalkpi['Category']=finalkpi.Category2.combine_first(finalkpi.Category1)

            finalkpi=finalkpi[['Date','Store','Category',kpidate,'Value2','value3','value4','value5','Rolling']]

            finalkpi['Date']=pd.to_datetime((finalkpi['Date']), format='%b-%Y')
            
            finalkpi[kpidate]=finalkpi[kpidate].apply(convert_amount)
            finalkpi['Value2']=finalkpi['Value2'].apply(convert_amount)
            finalkpi['value3']=finalkpi['value3'].apply(convert_amount)
            finalkpi['value4']=finalkpi['value4'].apply(convert_amount)
            finalkpi['value5']=finalkpi['value5'].apply(convert_amount)
            finalkpi['Rolling']=finalkpi['Rolling'].apply(convert_amount)


            #create output stream
            
            output=BytesIO()
            writer=pd.ExcelWriter(output, engine='xlsxwriter')
            finalkpi.to_excel(writer)
            writer.save()
            output.seek(0)
            
            return send_file(output, attachment_filename="output.xlsx", as_attachment=True)
            
            print(finalkpi)
            
            
            
            return render_template("applications.html")





@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('index.html', title='Register', form=form)




@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login unsuccessfull. Please check username and password', 'danger')

    return render_template('index.html', title='Login', form=form)




@app.route("/cstoresales")
def data():
    cur = mysql.connection.cursor()
    query = """SELECT Date, Amount 
         FROM growthkpi
         WHERE category = 'Total C-Store Margin ($)'
         and store = %s
         AND date BETWEEN '2019-01-1' and (SELECT max(Date) FROM growthkpi) 
         """ % (chartstore)
    cur.execute(query)  
    rv = cur.fetchall() 
    
    newdata = []
    content= {}
    for result in rv:
       content = {'date': result[0], 'margin': result[1]}
       newdata.append(content)
       content = {}
    return jsonify(newdata)

@app.route("/data")
def seconddata():
    cur2 = mysql.connection.cursor()
    query2 = """SELECT Date, Amount
         FROM growthkpi
         WHERE category = 'Total Fuel Volume'
         and store = %s
         AND date BETWEEN '2019-01-1' and (SELECT max(Date) FROM growthkpi) 
    
         """ % (chartstore)
    cur2.execute(query2)    
    rv2 = cur2.fetchall()     
         
         
    cur3 = mysql.connection.cursor()
    query3 = """SELECT Date, Amount
         FROM growthkpi
         WHERE category = 'Total Fuel Volume'
         and store = %s
         AND date BETWEEN '2018-01-1' and (SELECT max(Date) FROM growthkpi) 
    
         """ % (chartstore)       
         
    cur3.execute(query3)    
    rv3 = cur3.fetchall() 

    print(rv2)
    print('hey here it comes')
    print(rv3)
    
    newdata2 = []
    content2 = {}
    for result in rv2:
       content2 = {'date': result[0], 'volume': result[1]}
       newdata2.append(content2)
       content2 = {}
    return jsonify(newdata2)    
    
    
    
    


    

    



@app.route("/charts")
def charts():
    return render_template('charts.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')



    #print(cur.description)

    #print()

        #month = [];
        #amount = [];

    #for row in cur:
         #   month.push
     #   print(row)

  
    
    #return jsonify({'results' : sample(range(1,10) , 5)})


    
    

if __name__=='__main__':
    app.run(debug=True)
