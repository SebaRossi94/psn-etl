# psn-etl

ETL playground using PSN API

## Setup

- Login into PSN
- Request NPSSO key from [here](https://ca.account.sony.com/api/v1/ssocookie)
- Set the response into .env file under NPSSO key or pass it as a string parameter to the constructor
- Set the DB_URL into .env file, else it will use a sqlite DB by default

```
poetry install

make dbinit

make dbupgrade
```

### refs

- [PSN wrapper](https://github.com/isFakeAccount/psnawp/tree/master)
