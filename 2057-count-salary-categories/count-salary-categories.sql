-- Write your PostgreSQL query statement below
with CTE as(
select account_id, count(case when income < 20000 then 'Low Salary' end) l,
    count(case when income >= 20000 and income <= 50000 then 'Average Salary' end) a
   , count(case when income > 50000 then 'High Salary' end) h
from Accounts
group by 1
)
, B as(
select sum(l) L, sum(a) A, sum(h) H
from CTE
)
select 'Low Salary' as category, l as accounts_count
from B
union 
select 'Average Salary' as category, a as accounts_count
from B
union
select 'High Salary' as category, h as accounts_count
from B