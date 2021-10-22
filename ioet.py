
import csv
from datetime import datetime


rows = []
employees=[]
cont = 0
start_date1=""
start_date2=""
end_date1=""
end_date2=""



with open('c:/Users/Santiago/Desktop/SantiagoSarmiento_Ioet/schedule.txt',newline='') as file:  #open the .txt file going to the directory  and name this variable 'file'
    csv_reader = csv.reader(file, delimiter=',') #convert the .txt in csv format, this will transform the text to table
    #header=next(csv_reader)
    for row in csv_reader:
        employe={} #diccionario
        for field in row:
            if("-" in field):
                employe[field[0:2]+'_start'] = datetime.strptime(field.split('-')[0][2:], '%H:%M').strftime('%H:%M:%S')
                employe[field[0:2]+'_end'] = datetime.strptime(field.split('-')[1],'%H:%M').strftime('%H:%M:%S')
            else:
                employe['name']=field
        employees.append(employe)
#print(employees)

for index,employe in enumerate (employees,1):
    #print('pivote'+ employe['name'])
    for other_employees in employees[index:]:
        #print(employe['name'] + '-' + other_employees['name'])
        for key,value in employe.items():
            if(key != 'name'):
                #print(employe['name'] + '-' + other_employees['name'],key,value)
                print('----------------')
            for key2,value2 in other_employees.items():
                if(key2 != 'name'):
                    
                    if(key=='MO_start') and (key2=='MO_start') :
                        print ('entrada' + employe['name'] + '-' + other_employees['name'],value+ '-' + value2)
                        start_date1=value
                        start_date2=value2
                        #(StartDate1 <= EndDate2) and (StartDate2 <= EndDate1)
                    if(key=='MO_end') and (key2=='MO_end') :
                        print ('salida' + employe['name'] + '-' + other_employees['name'],value+ '-' + value2)  
                        end_date1=value                
                        end_date2=value2 
                        #print(end_date1)
                       # print(start_date1)
                       #datetime.strptime(start_date1, '%H:%M').strftime('%I:%M%p')
                        if((datetime.strptime(start_date1, '%H:%M:%S').strftime('%H:%M:%S') <= datetime.strptime(end_date2, '%H:%M:%S').strftime('%H:%M:%S')) and (datetime.strptime(start_date2, '%H:%M:%S').strftime('%H:%M:%S') <= datetime.strptime(end_date1, '%H:%M:%S').strftime('%H:%M:%S'))):
                            cont = cont + 1
                            print (employe['name'] + '-' + other_employees['name'] , cont)   
                            cont=0              
                #print(key2,value2)