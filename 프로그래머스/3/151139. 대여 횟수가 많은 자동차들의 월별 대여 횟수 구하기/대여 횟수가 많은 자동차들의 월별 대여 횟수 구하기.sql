select month(start_date) month, car_id, count(*) records
from car_rental_company_rental_history
where car_id in (
    -- 대여 횟수가 5회 이상인 자동차들
    select car_id
    from car_rental_company_rental_history
    where start_date between '20220801' and '20221031'
    group by car_id
    having count(*) >= 5
    )
    and start_date between '20220801' and '20221031'
group by month(start_date), car_id
having count(*) > 0
order by month, car_id desc;
