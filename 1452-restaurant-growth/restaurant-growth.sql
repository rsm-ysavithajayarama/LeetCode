-- Write your PostgreSQL query statement below
with CTE as (
    select visited_on, sum(amount) amt
    from Customer
    group by 1
)
, CTE2 as (
select visited_on, sum(amt)over(order by visited_on rows between 6 preceding and current row) amount
, round(avg(amt)over(order by visited_on rows between 6 preceding and current row),2) average_amount
from CTE
)
select visited_on, amount, average_amount
from CTE2
offset 6