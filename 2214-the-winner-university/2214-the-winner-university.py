import pandas as pd

def find_winner(new_york: pd.DataFrame, california: pd.DataFrame) -> pd.DataFrame:
    ny = len(new_york[new_york['score']>=90])
    ca = len(california[california['score']>=90])
    winner = np.where(ny==ca,'No Winner',np.where(ny>ca, 'New York University', 'California University'))
    return pd.DataFrame([winner], columns=['winner'])
    