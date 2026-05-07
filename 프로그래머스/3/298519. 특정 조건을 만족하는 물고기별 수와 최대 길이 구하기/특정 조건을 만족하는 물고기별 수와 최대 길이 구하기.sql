select fish_count, max_length, fish_type
from(
    select fish_type, avg(length) length_avg, count(*) fish_count, max(length) max_length
    from(
        select id, fish_type, if(length <= 10 or length is null, 10, length) length, time
        from fish_info
    ) a
    group by fish_type
) a
where length_avg >= 33
order by fish_type