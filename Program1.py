import pandas as pd
pd1= pd.read_csv('Property.csv')
#https://www.kaggle.com/claytonb/starter-property-price-register-bfd87ab9-7

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


print(pd1.head(10))
print(pd1.columns.tolist())

# selecting rows based on condition
rslt_df = pd1[pd1['SALE_PRICE'] <= 9000]

print('\nResult dataframe :\n', rslt_df['ADDRESS']+rslt_df['SALE_DATE']+str(rslt_df['SALE_PRICE']))

print(str(rslt_df['SALE_PRICE']))