#!/usr/bin/env python
# coding: utf-8

# In[14]:


import h2o
from h2o.automl import H2OAutoML
import psycopg2
import pandas as pd


# In[48]:


def query_into_df(query, cursor):
	"""

	Description: This function loads a SQL query into a pandas DataFrame.

	Parameters:

	table_name (str): A string containing the name of the table to be retrieved;
	cursor (database cursor): A cursor to make a connection with the database.

	"""

	cursor.execute(query)
	result = cursor.fetchall()
	column_names = [desc[0] for desc in cursor.description]

	df = pd.DataFrame(result, columns=column_names)

	return df


# In[117]:


def add_suffix_to_duplicates(lst):
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

# Example usage
my_list = ['apple', 'orange', 'banana', 'apple', 'apple', 'banana']
suffix = '_dup'
result_list = add_suffix_to_duplicates(my_list,)
print(result_list)


# In[118]:


def query_into_h2o(query, cursor):
    """

    Description: This function loads a SQL query into a pandas DataFrame.

    Parameters:

    table_name (str): A string containing the name of the table to be retrieved;
    cursor (database cursor): A cursor to make a connection with the database.

    """

    cursor.execute(query)
    result = cursor.fetchall()

    column_names = [desc[0] for desc in cursor.description]
    column_names = add_suffix_to_duplicates(column_names)

    df = h2o.H2OFrame(result, column_names=column_names)

    return df


# In[84]:


try:
    db = psycopg2.connect(
        host="aws-california.caclwjj7hnoo.us-east-2.rds.amazonaws.com",
        database="california",
        user="postgres",
        password="24567811"
    )
    cursor = db.cursor()
    print("Connected to the database!")
    
    # Perform database operations here
    
except psycopg2.Error as e:
    print("Error connecting to the database:", e)


# In[119]:


query_trad_data = "SELECT trad.* "                   "FROM traditional_data AS trad"
                 
query_alt_data = "SELECT alt.*, trad.gdp "                  "FROM traditional_data AS trad "                  "JOIN alternative_data AS alt ON trad.date = alt.date"

query_all_data = "SELECT trad.*, alt.* "                  "FROM traditional_data AS trad "                  "FULL OUTER JOIN alternative_data AS alt "                  "ON trad.date = alt.date"

traditional_data = query_into_h2o(query_trad_data, cursor)
alternative_data = query_into_h2o(query_alt_data, cursor)
all_data = query_into_h2o(query_all_data, cursor)
all_data = all_data.drop("date_dupplicated_1")

db.close() # don't want to kill your finances in aws haha


# In[123]:


# sorting data frames 

traditional_data = traditional_data.sort(by='date')
alternative_data = alternative_data.sort(by='date')
all_data = all_data.sort(by='date')


# 
# <br>
# 
# ### Predicting Expenditure and disposable Income 
# 
# <br>

# Expenditure:
# 
# - Remove GDP and disp_inc
# 
# Disp Income:
# 
# - Remove GDP and expenditure

# In[139]:


traditional_data.t


# In[136]:





# Create train and test data based on split time and columns to drop

# In[ ]:


def data_split(split_time):
    """
    Description:
    """


# In[137]:


## Expenditure 

# Decide on a point where you want to split the data
split_time = pd.to_datetime("2019-01-01")


# Create training and test sets
train = traditional_data[traditional_data["date"] <  split_time]
test = traditional_data[traditional_data["date"] >=  split_time]


# In[138]:


drop_from_expend = ["gdp", "disposable_income", "expenditure"]

features = train.columns
features = [feature_col for feature_col in features if feature_col not in drop_from_expend]

target = "expenditure"


# In[36]:


expendt_model = H2OAutoML(max_runtime_secs=120)


# In[37]:


expendt_model.train(x=features, y=target, training_frame=train)


# In[39]:


predictions = expendt_model.predict(test[features])
predictions


# In[40]:


test["expenditure"]


# In[ ]:


## Disp Income 

# Suppose 'time' is your time column and df is your DataFrame
traditional_data = traditional_data.sort_values('date')

# Decide on a point where you want to split the data
split_time = "01-01-2019"

# Create training and test sets
train = df_sorted[df_sorted['time'] < split_time]
test = df_sorted[df_sorted['time'] >= split_time]

# Get the features X and labels y for both sets
X_train, y_train = train.drop('target', axis=1), train['target']
X_test, y_test = test.drop('target', axis=1), test['target']


# In[ ]:


## Traditional Data

# Suppose 'time' is your time column and df is your DataFrame
traditional_data = traditional_data.sort_values('date')

# Decide on a point where you want to split the data
split_time = "01-01-2019"

# Create training and test sets
train = df_sorted[df_sorted['time'] < split_time]
test = df_sorted[df_sorted['time'] >= split_time]

# Get the features X and labels y for both sets
X_train, y_train = train.drop('target', axis=1), train['target']
X_test, y_test = test.drop('target', axis=1), test['target']


# In[ ]:


## Alternative Data  

# Suppose 'time' is your time column and df is your DataFrame
traditional_data = traditional_data.sort_values('date')

# Decide on a point where you want to split the data
split_time = "01-01-2019"

# Create training and test sets
train = df_sorted[df_sorted['time'] < split_time]
test = df_sorted[df_sorted['time'] >= split_time]

# Get the features X and labels y for both sets
X_train, y_train = train.drop('target', axis=1), train['target']
X_test, y_test = test.drop('target', axis=1), test['target']


# In[ ]:


## All Data  

# Suppose 'time' is your time column and df is your DataFrame
traditional_data = traditional_data.sort_values('date')

# Decide on a point where you want to split the data
split_time = "01-01-2019"

# Create training and test sets
train = df_sorted[df_sorted['time'] < split_time]
test = df_sorted[df_sorted['time'] >= split_time]

# Get the features X and labels y for both sets
X_train, y_train = train.drop('target', axis=1), train['target']
X_test, y_test = test.drop('target', axis=1), test['target']

