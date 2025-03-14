with orders_2019 as (
select * 
from orders 
where extract( 'year' from order_date ) = '2019'
)
select user_id buyer_id, join_date, count(buyer_id) orders_in_2019
from Users A
left join orders_2019 B
on A.user_id = B.buyer_id
group by 1,2
