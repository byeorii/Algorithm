
# SELECT O.PRODUCT_ID, P.PRODUCT_NAME, SUM(P.PRICE*O.AMOUNT) TOTAL_SALES

# FROM FOOD_PRODUCT P JOIN FOOD_ORDER O
# ON P.PRODUCT_ID = O.PRODUCT_ID
# WHERE O.PRODUCE_DATE LIKE '2022-05%'
# GROUP BY P.PRODUCT_ID

# ORDER BY TOTAL_SALES DESC, O.PRODUCT_ID ASC









select product_id, product_name, sum(price*amount) total_price
from food_product
join food_order
using (product_id)
where produce_date like '2022-05%'
group by product_id
order by total_price desc, product_id 





