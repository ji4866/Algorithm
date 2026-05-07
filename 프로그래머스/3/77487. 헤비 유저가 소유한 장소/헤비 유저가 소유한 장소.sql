select *
from places
where host_id in (
    select host_id
    from places
    group by host_id
    having count(distinct name) >= 2
)
order by id;