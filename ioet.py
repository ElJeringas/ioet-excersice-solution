"""
IOET excersice solution.
Oct 2021
@author: Santiago

(⌐■_■)

Note: no external or additional library was used for solve this problem. "Only default libraries

"""

# import basic libraries in python,
import csv
from datetime import datetime

#declaration of variables
rows = []
employees=[]
cont = 0
start_date1=""
start_date2=""
end_date1=""
end_date2=""



with open('./schedule.txt',newline='') as file:  #open the .txt file going to the directory  and name this variable 'file'
    csv_reader = csv.reader(file, delimiter=',') #convert the .txt in csv format, this will transform the text to table
    for row in csv_reader: #create rows in file converted
        employe={} #dictionary
        for field in row:
            if("-" in field): # search the character - in the file 
                employe[field[0:2]+'_start'] = datetime.strptime(field.split('-')[0][2:], '%H:%M').strftime('%H:%M:%S') #The split() method splits a string into a list. Then convert the string value to data time, in format (H - M - S)
                employe[field[0:2]+'_end'] = datetime.strptime(field.split('-')[1],'%H:%M').strftime('%H:%M:%S') #convert the string value to data time, in format (H - M - S)
            else:
                employe['name']=field #save the name of the employer in array name
        employees.append(employe)
#print(employees)


for index,employe in enumerate (employees,1): #enumerate a range of schedule starting at 1
    
    #print('pivote'+ employe['name'])
    for other_employees in employees[index:]: #employe contains the first name of the employers list, and other employers contains the following names in the list
        #print(employe['name'] + '-' + other_employees['name'])
        cont=0
        for key,value in employe.items(): #extract the days and hours in the variables key and value for the first employer
            
            for key2,value2 in other_employees.items():#extract the days and hours in the variables key2 and value2 for the 2nd employer to compare
                if(key2 != 'name'):
                    if(key==key2): # compare if the name of the key and key2 is equal, f.e(MO-MO)

                        if("_start" in key and "_start" in key2): # extract the line start in the name of the list (MO_start)
                           # print ('entrada' + employe['name'] + '-' + other_employees['name'],value+ '-' + value2)
                            start_date1=value #save the values in a variable
                            start_date2=value2

                        if("_end" in key and "_end" in key2): # extract the line end in the name of the list (MO_end)
                            #print ('salida' + employe['name'] + '-' + other_employees['name'],value + '-' + value2)  
                            end_date1=value #save the values in a variable          
                            end_date2=value2 

                            #(StartDate1 <= EndDate2) and (StartDate2 <= EndDate1)   ----> condition
                            if((datetime.strptime(start_date1, '%H:%M:%S').strftime('%H:%M:%S') <= datetime.strptime(end_date2, '%H:%M:%S').strftime('%H:%M:%S')) and (datetime.strptime(start_date2, '%H:%M:%S').strftime('%H:%M:%S') <= datetime.strptime(end_date1, '%H:%M:%S').strftime('%H:%M:%S'))):
                                cont=cont+1 # if the condition is true, the counter will raise in one asuming as a match or coincidence of schedules
        print (employe['name'] + '-' + other_employees['name'] , cont)   # the result will show the total of counts for each comparision of employers
