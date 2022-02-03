import pandas as pd
pd1= pd.read_csv('Property.csv')
#https://www.kaggle.com/claytonb/starter-property-price-register-bfd87ab9-7
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# selecting rows based on condition
rslt_df = pd1[pd1['SALE_PRICE'] <= 10000]
print(rslt_df)




