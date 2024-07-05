-- 코드를 작성해주세요

-- 연도별 최대 대장균 크기 계산
with t1 as
(
select 
max(size_of_colony) as maxc, 
year(differentiation_date) as year1
from ecoli_data 
group by year1
)

select year(differentiation_date) as year, abs(size_of_colony - t1.maxc) as year_dev, id 
from ecoli_data
join t1 
on year(ecoli_data.differentiation_date) = T1.year1
order by year, year_dev asc;
