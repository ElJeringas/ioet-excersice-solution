
import csv;
import pandas as pd
pd.read_csv

with open('c:/Users/Santiago/Desktop/SantiagoSarmiento_Ioet/schedule.txt',newline='') as file:
    csv_reader = csv.DictReader(file, delimiter=',',)
    """ line_count = 0 """
    df = pd.DataFrame(csv_reader) 

    """ mondays = (df.loc[df['monday']!='free',["name","monday"]]) """
    """     print(mondays['monday'].isin(['10:00-12:00']))"""
    df_mon=df["name","monday"]
    data_frame = df_mon.set_index('monday')
    df_monday = data_frame[(data_frame.index > '10:00') & (data_frame.index <= '12:00')]
    print (df_monday)


"""     print('-------------')
    print(df.loc[df['tuesday']!='free',["name","tuesday"]]) 
    print('-------------')
    print(df.loc[df['wednesday']!='free',["name","wednesday"]])
    print('-------------')
    print(df.loc[df['thursday']!='free',["name","thursday"]]) 
    print('-------------')
    print(df.loc[df['friday']!='free',["name","friday"]]) 
    print('-------------')
    print(df.loc[df['saturday']!='free',["name","saturday"]]) 
    print('-------------')
    print(df.loc[df['sunday']!='free',["name","sunday"]]) 
 """
        