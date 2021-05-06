import pandas as pd
pd.set_option('display.max_columns', 500)
 
 
def read_in_rates():
    data = pd.read_csv("rates.csv", names=["PPTNO","CONDITION","EVENT_TYPE","COUNT","DURATION_(SEC)","RATE_(HGs/MIN)"], header=0)
    data = data.pivot(index='PPTNO', columns=['CONDITION', 'EVENT_TYPE'], values='RATE_(HGs/MIN)')
    data.columns = data.columns.map('_'.join)
    print(data)
    data.to_csv("rates_wide.csv", index=True)
