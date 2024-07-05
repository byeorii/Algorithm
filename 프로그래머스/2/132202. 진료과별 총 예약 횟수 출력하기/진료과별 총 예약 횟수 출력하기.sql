-- 코드를 입력하세요
SELECT mcdp_cd 진료과코드, count(apnt_no) 5월예약건수
from appointment
where date_format(apnt_ymd, '%Y-%m') = '2022-05'
group by mcdp_cd
order by count (apnt_no), mcdp_cd


