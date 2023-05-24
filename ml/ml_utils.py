import h2o
from h2o.automl import H2OAutoML
import psycopg2
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


def add_suffix_to_duplicates(lst):
    """
    Description: This function adds a suffix to duplicated values in a list.
    
    Parameters:
    
        lst (list): A list to be checked.
    
    Returns:
    
        result (list): A resulted list from the checking process.
         
    """
    frequency = {}
    result = []
    
    for item in lst:
    
        if item in frequency:
            frequency[item] += 1
            item_with_suffix = item + "_dupplicated_" + str(frequency[item])
            result.append(item_with_suffix)
    
        else:
            frequency[item] = 0
            result.append(item)
    
    return result


def query_into_h2o(query, cursor):
    """

    Description: This function loads a SQL query into a pandas DataFrame.

    Parameters:

        table_name (str): A string containing the name of the table to be retrieved;
        cursor (database cursor): A cursor to make a connection with the database.
    
    Returns:    

        h2o.H2OFrame: A frame containing the queried dataG.

    """

    cursor.execute(query)
    result = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    column_names = add_suffix_to_duplicates(column_names)

    df = h2o.H2OFrame(result, column_names=column_names)

    return df



def data_split(split_time, df, drop_from_features, target):
    """
    Description: Splits data into training and test considerind a split date.
    
    Parameters:
    
        split_time (str): A string with the split date in Y-m-d format;
        df (h2o.H2OFrame): A h2o frame containing the data to be splitted;
        drop_from_features (list): A list containing the features (and the target) to be dropped out of the training step;
        target (str): The name of the target variable;
    
    Returns:
    
        train (h2o.H2OFrame): The data for train;
        test (h2o.H2OFrame): The data for test;
        features (list): A list of features to predict the target;
        target (str): A string of the target to predicted;
        
    """
    
    split_time = pd.to_datetime(split_time)
    
    train = df[df["date"] <  split_time]
    test = df[df["date"] >=  split_time]
    
    features = train.columns
    features = [feature_col for feature_col in features if feature_col not in drop_from_features]
    
    return train, test, features, target


def calculate_metrics(actual_frame, predicted_frame):
    """
    Description: Calculates RMSE, MAE, and R-squared metrics.

    Parameters:
        actual_frame (H2OFrame): The actual target values;
        predicted_frame (H2OFrame): The predicted target values.

    Returns:
        dict: Dictionary containing the calculated metrics.
        
    """
    actual_values = actual_frame.as_data_frame().values.flatten()
    predicted_values = predicted_frame.as_data_frame().values.flatten()

    rmse = np.sqrt(mean_squared_error(actual_values, predicted_values))
    mae = mean_absolute_error(actual_values, predicted_values)
    r2 = r2_score(actual_values, predicted_values)

    return {"RMSE": rmse, "MAE": mae, "R-squared": r2}


def display_metrics(models, actual_values, predicted_values):
    """
    Description: Display the performance metrics for each model in a DataFrame.

    Parameters:
    
        models (list): A list of model names.
        actual_values (H2OFrame): H2OFrame with the actual target values.
        predicted_values (list): A list of H2OFrames with the predicted target values for each model.

    Returns:
    
        pandas.DataFrame: DataFrame containing the performance metrics for each model.
    
    """
    
    results = {}
    
    actual_values = [actual_values]
    actual_values = len(models) * actual_values
    
    for model_name, actual, predicted in zip(models, actual_values, predicted_values):
        
        metrics = calculate_metrics(actual, predicted)
        results[model_name] = metrics

    df = pd.DataFrame.from_dict(results, orient='index')
    
    return df
