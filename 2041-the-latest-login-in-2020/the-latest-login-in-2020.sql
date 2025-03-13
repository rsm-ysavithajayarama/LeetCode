-- Write your PostgreSQL query statement below

select user_id, max(time_stamp) last_stamp
from Logins
where extract(year from time_stamp) = '2020'
group by 1

