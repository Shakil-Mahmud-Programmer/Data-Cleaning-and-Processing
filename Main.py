import pandas as pd
df=pd.read_csv('Data/data_cleaning_challenge.csv')

df=df.drop(columns=['Unnamed: 9','Unnamed: 10'])
df=df.dropna()

first_name=list()
last_name=list()
Date=list()

iter_Number=list()
Row_type=list()
Power1=list()
Speed1=list()
Speed2=list()
Electricity=list()
Effort=list()
Weight=list()
Torque=list()
iteration=list()

f=0

for i in df.values:
    if i[0]=='Row Type':
        f=f+1
        continue
    else:
        first_name.append('Person')
        last_name.append('Human')
        Date.append('End of Time')
        iteration.append(f)

        Row_type.append(i[0])
        iter_Number.append(i[1])
        Power1.append(i[2])
        Speed1.append(i[3])
        Speed2.append(i[4])
        Electricity.append(i[5])
        Effort.append(6)
        Weight.append(i[7])
        Torque.append(i[8])


data=pd.DataFrame({'First Name':first_name, 'Last Name':last_name,'Date':Date,'Iteration':iteration,'Row Type':Row_type, 'Iter Number':iter_Number, 'Power1': Power1, 'Speed1':Speed1, 'Speed2':Speed2, 'Electricity':Electricity, 'Effort':Effort, 'Weight':Weight, 'Torque':Torque})
data.to_excel('Data/completed.xlsx',index=False)