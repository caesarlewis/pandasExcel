import pandas as pd

books = pd.read_excel('booksSort.xlsx',index_col='ID')
#排序，ascending true为正序 false为倒叙
# inplace = True 在当前dateframe中排序，不会生成新的
books.sort_values(by='Price',inplace=True,ascending=False)
#多级排序
books.sort_values(by=['worthy','Price'],inplace=True,ascending=[True,False])
print(books)