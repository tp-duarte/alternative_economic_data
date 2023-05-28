
![image](https://github.com/tp-duarte/alternative_economic_data/assets/69936708/5efb3190-9fb4-4a97-8d9b-75de74a7a56d)


### Description 🏖️

<br>

Hi! This project creates predictions of California - USA Gross Domestic Product (GDP) using traditional and alternative data. The main goal is to test out if alternative data sources could be something to turn to. 

In the scientific literature we see [CITE REFERENCES] that alternative data might be a way to make a walkthrough economic crisis. And in hands with that, we can also see that machine leanrning techniques could serve as a way to make macroeconomical forecasting. 

Knowing that, this project gathered traditional data that contains:

-
-
-
-

And alternative data that contains:

-
-
-
-

After loading data to a PostgreSQL database in AWS RDS, the Machine Learning Models were trained with h2o AutoML
that considering:

- Only Traditional data sources;
- Alternative data sources;
- All data sources.

The results are displayed as you can see above. One of the problems with the project is that with the use of AutoML that 
are constraints with models reproducibility that weren't tackled here. 

But Nonetheless, the results might be a clue that you need to have a wide range of alternative sources to compare with traditional ones, when training models. And that might also not be an out of the box sollution since we aren't necessarily talking about governamental institutions.  

....
