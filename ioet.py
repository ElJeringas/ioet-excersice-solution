
import csv
from datetime import datetime


rows = []
employees=[]



with open('c:/Users/Santiago/Desktop/SantiagoSarmiento_Ioet/schedule.txt',newline='') as file:  #open the .txt file going to the directory  and name this variable 'file'
    csv_reader = csv.reader(file, delimiter=',') #convert the .txt in csv format, this will transform the text to table
    #header=next(csv_reader)
    for row in csv_reader:
        employe={} #diccionario
        for field in row:
            if("-" in field):
                employe[field[0:2]+'_start'] = datetime.strptime(field.split('-')[0][2:], '%H:%M').strftime('%I:%M%p')
                employe[field[0:2]+'_end'] = datetime.strptime(field.split('-')[1],'%H:%M').strftime('%I:%M%p')
            else:
                employe['name']=field
        employees.append(employe)
#print(employees)

for index,employe in enumerate (employees,1):
    #print('pivote'+ employe['name'])
    for other_employees in employees[index:]:
        print(employe['name'] + '-' + other_employees['name'])
        for key,value in employe.items():
            if(key != 'name'):
                if(employe[key] >= other_employees[key]) and (employe[key] <= other_employees[]):