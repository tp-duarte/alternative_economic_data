import etl_utils as eu
import pandas as pd 
import psycopg2
import os

connection = psycopg2.connect(
    database="california",
    user="postgres",
    password="0000",
    host="localhost",
    port="5433"
)

cursor = connection.cursor()
