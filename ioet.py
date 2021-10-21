
import csv; #csv library
import pandas as pd #import pandas library for data handle
cont  = 0
with open('c:/Users/Santiago/Desktop/SantiagoSarmiento_Ioet/schedule.txt',newline='') as file:  #open the .txt file going to the directory  and name this variable 'file'
    csv_reader = csv.DictReader(file, delimiter=',',) #convert the .txt in csv format, this will transform the text to table
    df = pd.DataFrame(csv_reader) #return object wiht rows and columns.

    mondays = (df.loc[df['monday']!='free',["name","monday"]]) #separa al dia lunes y muestra los nombres de trabajadores y horario, excepto si esta "free"
    """     print(mondays['monday'].isin(['10:00-12:00']))"""
    data_frame = mondays.set_index('monday') #transforma la cadena de texto string a un conjunto de numeros (formato hora)
    df_monday = data_frame[(data_frame.index > '10:00') & (data_frame.index <= '12:00')] # compara si hay valores dentro del dia que estan dentro de las horas 10:00-12:00 y muestra si es que existen cruces de trabajadores, sino no los muestra
    print (df_monday)
    print('-----------------------')
    tuesday = (df.loc[df['tuesday']!='free',["name","tuesday"]]) #separa al dia lunes y muestra los nombres de trabajadores y horario, excepto si esta "free"
    data_frame_tuesday = tuesday.set_index('tuesday') #transforma la cadena de texto string a un conjunto de numeros (formato hora)
    df_tuesday = data_frame_tuesday[(data_frame_tuesday.index > '10:00') & (data_frame_tuesday.index <= '12:00')] # compara si hay valores dentro del dia que estan dentro de las horas 10:00-12:00 y muestra si es que existen cruces de trabajadores, sino no los muestra
    print (df_tuesday)


        