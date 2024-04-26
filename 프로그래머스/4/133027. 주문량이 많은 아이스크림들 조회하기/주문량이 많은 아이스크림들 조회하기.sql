-- 코드를 입력하세요
# SELECT A.FLAVOR
# FROM (
#     SELECT * FROM FIRST_HALF
#     UNION ALL # 중복제거 하지 않고 다 보여줌
#     SELECT * FROM JULY
#     ) AS A
# GROUP BY A.FLAVOR 
# ORDER BY SUM(A.TOTAL_ORDER) DESC
# LIMIT 3


# 출하 번호 다르다고 문제에 써있었음, 고유 키가 뭔지 파악하기
# 문제 끝까지 제대로 읽고 어떤 것을 의미하는지 파악하기

# SELECT F.FLAVOR FROM FIRST_HALF F
# JOIN JULY AS J
# ON F.FLAVOR = J.FLAVOR
# GROUP BY F.FLAVOR
# ORDER BY F.TOTAL_ORDER + SUM(J.TOTAL_ORDER) DESC 
# LIMIT 3

# f테이블에서는 중복이 없으니까 sum 안해도 됨.
# j는 두 공장에서 출하 진행할수도 있다 했으니 sum으로 집계








SELECT F.FLAVOR FROM FIRST_HALF F
JOIN JULY AS J
ON F.FLAVOR = J.FLAVOR
group by flavor
order by f.total_order + sum(j.total_order) desc
limit 3


