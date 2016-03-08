import pandas as pd

def make_submission(data, filename = None):
    # Don't want to modify data, so take copy
    d = data.copy()
    d['Year'] = d['Year'].astype(str)
    d['team_id1'] = d['team_id1'].astype(str)
    d['team_id2'] = d['team_id2'].astype(str)
    submission = pd.DataFrame(d['Year'] + '_' + d['team_id1'] + '_' + d['team_id2'])
    submission['Pred'] = d['Pred']
    submission.columns = ['Id', 'Pred']
    if filename is not None:
        submission.to_csv('NCAA Submissions/' + filename, index = False)
    return(submission)
