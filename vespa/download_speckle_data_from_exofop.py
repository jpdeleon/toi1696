#!/usr/bin/env python
import pandas as pd

url1="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194517"
url2="https://exofop.ipac.caltech.edu/tess/get_file.php?id=194516"
urls = [url1,url2]
bands = ['r','z']

for url,band in zip(urls,bands):
    df=pd.read_csv(url, comment='#', skiprows=30, index_col=0, names=['sep','dmag'], delim_whitespace=True)
    fp=f'Gemini_{band}.cc'
    df2 = df[df.dmag>0].drop_duplicates()
    df2.to_csv(fp, header=False, float_format='%.3f', sep=' ')
    print(df2.head())
    print('Saved: ', fp)
