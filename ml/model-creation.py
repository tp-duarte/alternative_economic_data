'''
Objective:

This python file trains Automated Machine Learning models based on alternative and traditional economic 
data.

The file proceeds as following:
    1 - Gathers data from AWS Relational DataBase Service (RDS);
    2 - Trains three main Automated ML Models from the gathered data;
    3 - Exports the models predictions and metrics (RMSE, MAE, R2) to a specified path.


The predictions and metrics are then consumed and displayed in Power BI .  

'''


import h2o
from h2o.automl import H2OAutoML
import psycopg2
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import ml_utils as mu

SEED = 4875

h2o.init(max_mem_size = "4g")

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


query_trad_data = "SELECT trad.* " \
                  "FROM traditional_data AS trad"
                 
query_alt_data = "SELECT alt.*, trad.gdp " \
                 "FROM traditional_data AS trad " \
                 "JOIN alternative_data AS alt ON trad.date = alt.date"

query_all_data = "SELECT trad.*, alt.* " \
                 "FROM traditional_data AS trad " \
                 "FULL OUTER JOIN alternative_data AS alt " \
                 "ON trad.date = alt.date"
                 
                 
traditional_data = mu.query_into_h2o(query_trad_data, cursor)
alternative_data = mu.query_into_h2o(query_alt_data, cursor)
all_data = mu.query_into_h2o(query_all_data, cursor)
all_data = all_data.drop("date_dupplicated_1")

db.close() 

# sorting data frames 

traditional_data = traditional_data.sort(by='date')
alternative_data = alternative_data.sort(by='date')
all_data = all_data.sort(by='date')

 
#### Predicting Expenditure and disposable Income ####


## Expenditure data ###

split_date = "2019-01-01"
drop_from_expend = ["gdp", "disposable_income", "expenditure"]

train_expend, test_expend, features_expend, expend = mu.data_split(split_date, traditional_data, drop_from_expend, "expenditure")

# Initializing and training model 

expendt_model = H2OAutoML(max_runtime_secs=3600, seed=SEED)
expendt_model.train(x=features_expend, y=expend, training_frame=train_expend)

# Predictions  

predictions_expend = expendt_model.predict(test_expend[features_expend])
del expendt_model


## Disposable Income  ##

drop_from_disp = ["gdp", "disposable_income", "expenditure"]

train_disp, test_disp, features_disp, disp = mu.data_split(split_date, traditional_data, drop_from_disp, "disposable_income")

# Initializing and training model 

disp_model = H2OAutoML(max_runtime_secs=3600, seed=SEED)
disp_model.train(x=features_disp, y=disp, training_frame=train_disp)

# Predictions  

predictions_disp = disp_model.predict(test_disp[features_disp])
del disp_model

#### Traditional Data ####


drop_from_trad = ["gdp"]

train_trad, test_trad, features_trad, gdp = mu.data_split(split_date, traditional_data, drop_from_trad, "gdp")

# replacing expenditure and disposable income data in the test 

test_trad["expenditure"] = predictions_expend
test_trad["disposable_income"] = predictions_disp

# Initializing and training model 

trad_model = H2OAutoML(max_runtime_secs=3600, seed=SEED)
trad_model.train(x=features_trad, y=gdp, training_frame=train_trad)

# Predictions  

predictions_trad = trad_model.predict(test_trad[features_trad])
del trad_model


#### Alternative Data ####


drop_from_alt = ["gdp"]

train_alt, test_alt, features_alt, gdp = mu.data_split(split_date, alternative_data, drop_from_alt, "gdp")


# Initializing and training model 

alt_model = H2OAutoML(max_runtime_secs=3600, seed=SEED)
alt_model.train(x=features_alt, y=gdp, training_frame=train_alt)

# Predictions  

predictions_alt = alt_model.predict(test_alt[features_alt])
del alt_model

#### All Data ####

drop_from_all = ["gdp"]

train_all, test_all, features_all, gdp = mu.data_split(split_date, all_data, drop_from_all, "gdp")

# replacing expenditure and disposable income data in the test 

test_all["expenditure"] = predictions_expend
test_all["disposable_income"] = predictions_disp

# Initializing and training model 

all_model = H2OAutoML(max_runtime_secs=3600, seed=SEED)
all_model.train(x=features_all, y=gdp, training_frame=train_all)

# Predictions  

predictions_all = all_model.predict(test_all[features_all])
del all_model

#### EXPORTING RESULTS ####  
  

models = ["trad_model", "alt_model", "all_model"]
predictions = [predictions_trad, predictions_alt, predictions_all]
actual_gdp = test_all["gdp"]

models_metrics = mu.display_metrics(models, actual_gdp, predictions)


flattened_dict = {
    "date": mu.generate_quarterly_series(split_date, "2022-10-01"),        
    "real_gdp": test_all["gdp"].as_data_frame(),
    "trad_predictions": predictions_trad.as_data_frame(),
    "alt_predictions": predictions_alt.as_data_frame(),
    "all_predictions": predictions_all.as_data_frame()
}

prediction_results = pd.concat(flattened_dict.values(), axis=1, keys=flattened_dict.keys())
prediction_results.columns = prediction_results .columns.get_level_values(0)


prediction_file = "..\data\ml_data\predictions.csv"
metrics_file = "..\data\ml_data\models_metrics.csv"

prediction_results.to_csv(prediction_file, index=False)
models_metrics.to_csv(metrics_file)