import pandas as pd
# 构建序列
d = {'x':100,'y':200,'z':300}
t1 = pd.Series(d)
print(t1.index)
print(t1.keys())
print(t1.values)

s1 = ['a','b','c']
s2 = [100,200,300]
t2 = pd.Series(s2,index=s1)
print(t2)

ss1 = pd.Series([1,2,3],index=[1,2,3],name='A')
ss2 = pd.Series([10,20,30],index=[1,2,3],name='B')
ss3 = pd.Series([100,200,300],index=[1,2,3],name='C')
# 标准输入方式，以map形式添加，以index为行以name为列
df = pd.DataFrame({ss1.name:ss1,ss2.name:ss2,ss3.name:ss3})
print(df)
# 使用list形式添加，以name为行，以index为列
df1 = pd.DataFrame([ss1,ss2,ss3])
print(df1)
# 错行情况，没有找到对应填充的值使用NAN代替
ss1 = pd.Series([1,2,3],index=[1,2,3],name='A')
ss2 = pd.Series([10,20,30],index=[1,2,3],name='B')
ss3 = pd.Series([100,200,300],index=[2,3,4],name='C')
df = pd.DataFrame({ss1.name:ss1,ss2.name:ss2,ss3.name:ss3})
print(df)