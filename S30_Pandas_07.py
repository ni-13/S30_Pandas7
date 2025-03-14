# Pandas_07

# 1173. Immediate Food Delivery I_Solution_Q1

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    cnt=0
    for i in range(len(delivery)):
        o_date= delivery['order_date'][i]
        c_date= delivery['customer_pref_delivery_date'][i]
        if o_date ==c_date:
            cnt= cnt+1
    return pd.DataFrame([round(cnt/len(delivery) *100, 2)], columns =['immediate_percentage'])

#Alternative1

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    immediate_order_series= delivery['order_date']== delivery['customer_pref_delivery_date']
    immediateCount= immediate_order_series.sum()
    return pd.DataFrame([round(immediateCount/len(delivery) * 100, 2)], columns = ['immediate_percentage'])

______________________________________________________________________________________________________________________________________

# 1907. Count Salary Categories_Solution_Q2

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low= 0
    avg=0
    high=0 
    
    for i in range(len(accounts)):
        income= accounts['income'][i]
        if income < 20000:
            low= low+1
        elif income>=20000 and income <=50000:
            avg= avg+1
        else:
            high= high+1

    return pd.DataFrame([['Low Salary', low], ['Average Salary', avg], ['High Salary', high]], columns= ['category', 'accounts_count'])


#Alternative1

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowdf= accounts[accounts['income']<20000]
    avgdf= accounts[(accounts['income']>=200000)& (accounts['income']<=50000)]
    highdf= accounts[accounts['income']>50000]

    return pd.DataFrame([['Low Salary', len(lowdf)], ['Average Salary', len(avgdf)], ['High Salary', len(highdf)]], columns= ['category', 'accounts_count'])

#Alternative2

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    lowseries= accounts['income']<20000
    avgseries=(accounts['income']>=20000) & (accounts['income']<=50000)
    highseries= accounts['income']>50000

    lowCount= lowseries.sum()
    avgCount= avgseries.sum()
    highCount= highseries.sum()
    
    return pd.DataFrame([['Low Salary', lowCount], ['Average Salary', avgCount], ['High Salary', highCount]], columns= ['category', 'accounts_count'])


