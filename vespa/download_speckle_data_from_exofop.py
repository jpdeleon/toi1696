#!/usr/bin/env python
import pandas as pd

url1="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194517" #20201203
url2="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194516"
url3="https://exofop.ipac.caltech.edu/tess/get_file.php?id=250798" #20211014
url4="https://exofop.ipac.caltech.edu/tess/get_file.php?id=250799"
urls = [url1,url2,url3,url4]
dates = [20201203,20201203,20211014,20211014]
bands = ['r','z','r','z']

for url,date,band in zip(urls,dates,bands):
    df=pd.read_csv(url, comment='#', skiprows=30, index_col=0, names=['sep','dmag'], delim_whitespace=True)
    fp=f'Gemini_{date}_{band}.cc'
    df2 = df[df.dmag>0].drop_duplicates()
    df2.to_csv(fp, header=False, float_format='%.3f', sep=' ')
    print(df2.head())
    print('Saved: ', fp)
