-- 코드를 작성해주세요
 
with cnt as 
(
select parent_id id2, count(parent_id) child_count
from ecoli_data
group by parent_id)

#select * from cnt

select id, ifnull(child_count,0) as child_count
from ecoli_data
left outer join cnt
on id = id2

order by id 



