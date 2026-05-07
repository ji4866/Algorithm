select cart_id
from(
    select cart_id,
        sum(case when name = 'Milk' then 1 else 0 end) milk,
        sum(case when name = 'Yogurt' then 1 else 0 end) yogurt
    from cart_products
    group by cart_id
) a
where milk > 0 and yogurt > 0
order by cart_id

