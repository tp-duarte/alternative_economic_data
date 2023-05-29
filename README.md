
<img src="https://github.com/tp-duarte/alternative_economic_data/assets/69936708/74ac7f56-e725-42c0-b2d8-b9d6ea3b66dc" alt="image" width="600">


### Description 🏖️

<br>

Hi! This project creates predictions of California - USA Gross Domestic Product (GDP) in the pandemic period using traditional and alternative data. The main goal is to test out if alternative data sources could be something to turn to make better GDP predictions. 

Knowing that, this project gathered traditional data that contains:

- GDP
- Employment
- Expenditure
- Exports and Imports
- Minimum Wage
- Personal and Disposable Income

And alternative data that contains:

- Google Trends Queries
- Mobility Reports
- Consumer Sentiment Index


After loading data to a PostgreSQL database in AWS RDS, three Machine Learning Models were trained with h2o AutoML
that considered:

- Traditional data sources;
- Alternative data sources;
- All data sources.

The results are displayed as you can see above. One of the problems with the project is that, with the use of AutoML there
are constraints with models reproducibility that weren't tackled. 

But Nonetheless, the results might be a clue that you need to have a wide range of alternative sources to compare with traditional ones when training ML models. And that might also not be an out of the box sollution since we aren't necessarily talking about governamental institutions.  

For a more detailed commentary of the project you can access it's Medium article **here**. And the results in [**PowerBI**](https://app.powerbi.com/view?r=eyJrIjoiZGQwMzJmYjgtOGJjNC00OGE1LTlkY2UtMzllNTFkNGZlODNkIiwidCI6ImZlODc4N2JjLWM5MTQtNDY2NS04NTQ3LTI2OGUxNWNiMGQ5YSJ9&embedImagePlaceholder=true)
