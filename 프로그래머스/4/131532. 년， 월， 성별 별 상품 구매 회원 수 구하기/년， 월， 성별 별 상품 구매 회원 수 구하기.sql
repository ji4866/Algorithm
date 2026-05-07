select sales_year, sales_month, b.gender, count(distinct a.user_id) user_id_cnt
from(
    select user_id, year(sales_date) sales_year, month(sales_date) sales_month
    from online_sale
) a
left join(
    select distinct user_id, gender
    from user_info
) b
on a.user_id = b.user_id
where gender is not null
group by sales_year, sales_month, gender
order by sales_year, sales_month, gender