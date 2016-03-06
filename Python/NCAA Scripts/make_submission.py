import pandas as pd

def make_submission(data, filename = None):
    submission = pd.DataFrame(data['Year'] + '_' + data['team_id1'] + '_' + data['team_id2'])
    submission['Pred'] = data['Pred']
    submission.columns = ['Id', 'Pred']
    if filename is not None:
        submission.to_csv('NCAA Submissions/' + filename, index = False)
    return(submission)