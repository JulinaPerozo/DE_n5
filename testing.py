select top 10 *
from openrowset(
    bulk 'C:/Users/Lili/Downloads/country_wise_latest.parquet',
    format = 'parquet') as rows