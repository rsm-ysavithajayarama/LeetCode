-- Write your PostgreSQL query statement below

select id 
from (
    select id, recordDate, temperature, lag(temperature) over(order by recordDate) prev_temp, lag(recordDate) over(order by recordDate) prev_date
    from weather
) A
where temperature > prev_temp and recordDate - prev_date = 1
