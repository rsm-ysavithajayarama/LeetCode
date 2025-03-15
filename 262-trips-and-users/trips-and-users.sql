-- Write your PostgreSQL query statement below
with CTE as (
select *
from Trips A
left join Users B 
on A.client_id = B.users_id
left join Users C
on A.driver_id = C.users_id
where B.banned = 'No' and C.banned = 'No' and request_at between '2013-10-01' and '2013-10-03'
)
select request_at as Day, 
round(count(case when status != 'completed' then client_id end)*1.0/count(client_id),2) as "Cancellation Rate"
from CTE
group by 1
