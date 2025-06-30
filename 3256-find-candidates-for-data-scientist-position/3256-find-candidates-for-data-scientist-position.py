import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    candidates = candidates.groupby("candidate_id").agg(lambda x: set(x))
    candidates.reset_index(inplace=True)
    candidates.columns = ['candidate_id','skills']
    logic1 = candidates['skills'].apply(lambda x: 'Python' in x)
    logic2 = candidates['skills'].apply(lambda x: 'Tableau' in x)
    logic3 = candidates['skills'].apply(lambda x: 'PostgreSQL' in x)
    logic = logic1 & logic2 & logic3
    return candidates[logic][['candidate_id']]