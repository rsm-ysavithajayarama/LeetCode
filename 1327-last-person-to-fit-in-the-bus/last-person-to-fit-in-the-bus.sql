-- Write your PostgreSQL query statement below
with A as(
select turn, person_name, weight, sum(weight) over(order by turn) sm
from Queue

)
select person_name 
from A
where sm <=1000
order by turn desc
limit 1

