import pandas as pd
pd1= pd.read_csv('Property.csv')
#https://www.kaggle.com/claytonb/starter-property-price-register-bfd87ab9-7

# selecting rows based on condition
rslt_df = pd1[pd1['SALE_PRICE'] <= 10000]



