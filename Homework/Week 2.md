## Module 2 Homework

1) Within the execution for `Yellow` Taxi data for the year `2020` and month `12`: what is the uncompressed file size (i.e. the output file `yellow_tripdata_2020-12.csv` of the `extract` task)?
- 128.3 MiB
- 134.5 MiB
- 364.7 MiB
- 692.6 MiB

#### Solution:

```
134.5 MiB
```


2) What is the rendered value of the variable `file` when the inputs `taxi` is set to `green`, `year` is set to `2020`, and `month` is set to `04` during execution?
- `{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv` 
- `green_tripdata_2020-04.csv`
- `green_tripdata_04_2020.csv`
- `green_tripdata_2020.csv`

#### Solution:

```
- `green_tripdata_2020-04.csv`
```
```
{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv
```


3) How many rows are there for the `Yellow` Taxi data for all CSV files in the year 2020?
- 13,537.299
- 24,648,499
- 18,324,219
- 29,430,127

#### Solution:

```
- 24,648,499
```
```
SELECT count(*) FROM `kestra-sandbox-486108.zoomcamp.yellow_tripdata` WHERE filename LIKE '%2020%'
```


4) How many rows are there for the `Green` Taxi data for all CSV files in the year 2020?
- 5,327,301
- 936,199
- 1,734,051
- 1,342,034

#### Solution:

```
- 1,734,051
```


5) How many rows are there for the `Yellow` Taxi data for the March 2021 CSV file?
- 1,428,092
- 706,911
- 1,925,152
- 2,561,031

#### Solution:

```
- 1,925,152
```


6) How would you configure the timezone to New York in a Schedule trigger?
- Add a `timezone` property set to `EST` in the `Schedule` trigger configuration  
- Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
- Add a `timezone` property set to `UTC-5` in the `Schedule` trigger configuration
- Add a `location` property set to `New_York` in the `Schedule` trigger configuration  

#### Solution:

```
- Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
```

## Submitting the solutions

* Form for submitting: https://courses.datatalks.club/de-zoomcamp-2026/homework/hw2
* Check the link above to see the due date

## Solution

Will be added after the due date


## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and).

### Example post for LinkedIn

```
🚀 Week 2 of Data Engineering Zoomcamp by @DataTalksClub and @Will Russell complete!

Just finished Module 2 - Workflow Orchestration with @Kestra. Learned how to:

✅ Orchestrate data pipelines with Kestra flows
✅ Use variables and expressions for dynamic workflows
✅ Implement backfill for historical data
✅ Schedule workflows with timezone support
✅ Process NYC taxi data (Yellow & Green) for 2019-2021

Built ETL pipelines that extract, transform, and load taxi trip data automatically!

Thanks to the @Kestra team for the great orchestration tool!

Here's my homework solution: <LINK>

Following along with this amazing free course - who else is learning data engineering?

You can sign up here: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```

### Example post for Twitter/X

```
Module 2 of DE Zoomcamp by @DataTalksClub @wrussell1999 done!

- @kestra_io workflow orchestration
- ETL pipelines for taxi data
- Backfill & scheduling
- Variables & dynamic flows

My solution: <LINK>

Join me here: https://github.com/DataTalksClub/data-engineering-zoomcamp/
```
