-- Write your PostgreSQL query statement below


with A as(
        select id, recordDate, temperature, lag(temperature) over(order by recordDate) prev_temp, lag(recordDate) over(order by recordDate) prev_date
    from weather
)
select id from A
where temperature > prev_temp and recordDate - prev_date = 1
