import csv
with open("C:\PythonFundamentos\python\st.csv","w", newline='') as f:
    write = csv.writer(f,delimiter=",")
    write.writerow(['one','two','three'])
    write.writerow(['four','five','six'])
          
