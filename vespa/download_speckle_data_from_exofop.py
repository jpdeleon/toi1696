"""
vespa only accepts certain bands:
https://github.com/timothydmorton/VESPA/blob/0446b54d48009f3655cfd1a3957ceea21d3adcaa/vespa/stars/populations.py#L67

We adopt the following:
Gemini
562nm: r
832nm: z
Palomar
H continuum: H
Br(gamma): K
 
based on this filter info:
https://webarchive.gemini.edu/sciops/instruments/niri/NIRIFilterList.html
"""
#!/usr/bin/env python
import pandas as pd
#Gemini
url1="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194517" #20201203
url2="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194516"
url3="https://exofop.ipac.caltech.edu/tess/get_file.php?id=250798" #20211014
url4="https://exofop.ipac.caltech.edu/tess/get_file.php?id=250799"
#palomar 5m
url5="https://exofop.ipac.caltech.edu/tess/get_file.php?id=230251" #H continuum
url6="https://exofop.ipac.caltech.edu/tess/get_file.php?id=230250" #Br gamma
#SAI
#url7=""
#url8=""

dates = [20201203,20201203,20211014,20211014]
urls = [url1,url2,url3,url4,url5,url6]
bands = ['r','z','r','z','H','K']

n=0
cols = ['sep','dmag']
for url,band in zip(urls,bands):
    if n<4:
        df=pd.read_csv(url, comment='#', skiprows=30, names=['sep','dmag'], delim_whitespace=True)
        date = dates[n]
        fp=f'Gemini_{date}_{band}.cc'
    else:
        df=pd.read_csv(url, skiprows=9, names=['sep','dmag','dmrms'])
        fp=f'Palomar_{band}.cc'
    df2 = df[df.dmag>0].drop_duplicates()[cols]
    df2.to_csv(fp, header=False, float_format='%.3f', sep=' ', index=False)
    print(df2.head())
    print('Saved: ', fp)
    n+=1
