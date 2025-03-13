-- Write your PostgreSQL query statement below
with A as(
select event_day, emp_id, out_time - in_time diff
from Employees)
select event_day as day , emp_id, sum(diff) total_time
from A 
group by 1,2