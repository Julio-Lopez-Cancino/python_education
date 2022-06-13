import csv
import os


#data to save
movies = [['Top Gun','Risky Business','Minority Report'],
          ['Titanic','The Revenant','Inception'],
          ['Training Day','Man on Fire','Flight']]


#setting the path where the file will be saved
os.chdir(r'C:\PythonFundamentos\python\tstp')


#writing the csv file
with open('movies.csv','w', newline='') as f:
    write = csv.writer(f,delimiter=',')
    for line in movies:
        write.writerow(line)
    
    
