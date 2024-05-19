with cte as 
(select *
from mountain_huts m
join trails t
on m.id = t.hut1
order by altitude desc),

cte2 as
(SELECT c.*, m.name, m.altitude as hut2_alt
from cte c
join mountain_huts m
on c.hut2 = m.id)

select * from cte2
where altitude > hut2_alt


