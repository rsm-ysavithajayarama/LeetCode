-- Write your PostgreSQL query statement below
with buy as ( 
select stock_name, sum(price) buy
from stocks
where operation = 'Buy'
group by 1
)
, sell as (
select stock_name, sum(price) sell
from stocks
where operation = 'Sell'
group by 1
)
select A.stock_name, sell - buy capital_gain_loss
from buy A
join sell B
on A.stock_name = B.stock_name
