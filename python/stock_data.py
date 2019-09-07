import tushare as ts


df = ts.get_hist_data('sh')

#save directly
df.to_excel('e:/source/python/stock_data/sh.xlsx')

#set data position (3th row , sixth column)
#df.to_excel('e:/source/python/stock_data/sh.xlsx', startrow=2,startcol=5)