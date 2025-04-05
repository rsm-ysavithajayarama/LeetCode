# Write your MySQL query statement below
select user_id, round(avg(case when activity_type = 'free_trial' then activity_duration end),2) trial_avg_duration
, round(avg(case when activity_type = 'paid' then activity_duration end),2) paid_avg_duration
from UserActivity
where user_id in (
select user_id 
from UserActivity
where activity_type = 'paid'
group by 1)
group by 1