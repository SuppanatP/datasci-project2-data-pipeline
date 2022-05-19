# datasci-project2-data-pipeline
Data pipeline for data science project 2 [auto scrape + insert/query api]

## Pipeline Diagram
![Pipeline](https://github.com/palmpalmpalm/datasci-project2-data-pipeline/blob/dev/public/diagram2.png)


## There are two directories
- backend [fastapi + postgresql]
- airflow

## Follow these setup steps
1. download docker engine<br>
2. cd to those directories <br>
3. rename .env.example to .env and config your own secrets in .env <br>
4. run this command <br>
```
docker-compose up -d
```
checkout airflow server at localhost:8000 <br>
checkout backend server at localhost:8080/docs

