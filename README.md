# Metrics API

## Installation

* Clone Git repository: `https://github.com/ezdookie/metrics-api.git`
* Enter cloned directory and run command `make build` or `docker-compose build` then `docker-compose up -d`.
* Run migrations with command `make migrate` or `docker-compose exec api python manage.py migrate`.
* Seed the database with command `make seeds` or `docker-compose exec api python manage.py loadcsv`.
* App should be running on `http://localhost:8000`

## Common API use-cases
1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.

  `/metrics/?date_to=2017-05-31&groupby=channel,country&ordering=-clicks`

2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.

  `/metrics/?date_from=2017-05-01&date_to=2017-05-31&groupby=date&ordering=date`

3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.

  `/metrics/?date_from=2017-06-01&date_to=2017-06-01&groupby=os&ordering=-revenue`

4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

  `/metrics/?groupby=channel&ordering=-cpi`
