-- Write your PostgreSQL query statement below
select contest_id, round(count(user_id)*100.0/(select count(user_id) from Users),2) percentage
from Register
group by contest_id
order by 2 desc, 1