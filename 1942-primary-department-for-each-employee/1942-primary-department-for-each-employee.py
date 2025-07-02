import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    cols = ['employee_id','department_id']
    filtered_by_flag = employee[employee['primary_flag']=='Y'][cols]
    unique_employees = employee.groupby('employee_id').filter(lambda x: len(x)==1)[cols]
    result = pd.concat([filtered_by_flag,unique_employees]).drop_duplicates().reset_index(drop=True)
    return result
    