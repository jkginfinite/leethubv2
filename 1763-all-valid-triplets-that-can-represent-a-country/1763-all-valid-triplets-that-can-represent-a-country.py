import pandas as pd

def find_valid_triplets(school_a: pd.DataFrame, school_b: pd.DataFrame, school_c: pd.DataFrame) -> pd.DataFrame:

    school_a.columns = ['student_id_A','member_A']
    A = list(school_a.columns)
    school_b.columns = ['student_id_B','member_B']
    B = list(school_b.columns)
    school_c.columns = ['student_id_C','member_C']
    C = list(school_c.columns)
    
    df = pd.merge(school_a, school_b, how='cross')
    df = pd.merge(df, school_c, how='cross')

    dff = df[(df[A[0]]!=df[B[0]]) & (df[A[1]]!=df[B[1]])  & (df[A[0]]!=df[C[0]]) & (df[A[1]]!=df[C[1]]) & (df[B[0]]!=df[C[0]]) & (df[B[1]]!=df[C[1]])]

    cols = ['member_A','member_B','member_C']
    return dff[cols]
    