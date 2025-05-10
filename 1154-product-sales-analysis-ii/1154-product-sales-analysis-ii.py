import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales[['product_id','quantity']].groupby('product_id').sum().reset_index().rename(columns={'quantity':'total_quantity'})
    