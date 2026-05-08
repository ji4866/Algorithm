select id, fish_name, length
from(
    select *, row_number() over(partition by fish_type order by if(length <= 10, NULL, length) desc) rnum
    from fish_info
) a
left join(
    select * from fish_name_info
) b
on a.fish_type = b.fish_type
where rnum = 1
order by id
