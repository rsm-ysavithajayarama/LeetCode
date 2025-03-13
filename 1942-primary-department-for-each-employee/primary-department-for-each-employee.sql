with CTE as (
select employee_id, department_id, count(department_id)over(partition by  employee_id) cnt, primary_flag
from Employee
)
select employee_id, department_id
from CTE
where cnt = 1 or (cnt !=1 and primary_flag = 'Y')