import pandas as pd

student_csv = pd.read_csv('Students.csv',index_col='ID')
print(student_csv)
# sep 为读取格式的分隔符
student_tsv = pd.read_csv('Students.tsv',sep='\t',index_col='ID')
print(student_tsv)

student_txt = pd.read_csv('Students.txt',sep='|',index_col='ID')
print(student_txt)