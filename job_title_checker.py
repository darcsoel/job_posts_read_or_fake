import pandas as pd
from sklearn.model_selection import train_test_split


def read_dataset():
    """
    Data columns = ['job_id', 'title', 'location', 'department', 'salary_range',
       'company_profile', 'description', 'requirements', 'benefits',
       'telecommuting', 'has_company_logo', 'has_questions', 'employment_type',
       'required_experience', 'required_education', 'industry', 'function']

    Result column = fraudulent

    :return: pd.DataFrame
    """

    df = pd.read_csv('fake_job_postings.csv', index_col='job_id')
    return df


def split_result_from_features(dataframe: pd.DataFrame,
                               result: str) -> (pd.DataFrame, pd.Series):
    y = dataframe[result]
    x = dataframe.drop(columns=[result])
    return x, y


if __name__ == '__main__':
    dataset = read_dataset()
    train, test = train_test_split(dataset, test_size=0.2)
    train_x, train_y = split_result_from_features(train, result='fraudulent')
    test_x, test_y = split_result_from_features(test, result='fraudulent')
