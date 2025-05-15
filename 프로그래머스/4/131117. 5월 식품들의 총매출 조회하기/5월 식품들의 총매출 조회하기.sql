select FOOD_ORDER.PRODUCT_ID, PRODUCT_NAME, SUM(AMOUNT*PRICE) AS TOTAL_SALES
from food_order
JOIN food_product
on food_order.PRODUCT_ID = food_product.PRODUCT_ID
where produce_date like '2022-05%'
GROUP BY food_order.PRODUCT_ID

ORDER BY TOTAL_SALES DESC, FOOD_ORDER.PRODUCT_ID;