import pandas as pd
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag=[90,40,80,98]

dict={'name':nme,'site':st,'age':ag}

df=pd.DataFrame(dict)

df.to_csv('site.csv')