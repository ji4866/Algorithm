select id, 
    case
        when PERCENT_RANK() over(order by size_of_colony desc) * 100 <= 25 then 'CRITICAL'
        when PERCENT_RANK() over(order by size_of_colony desc) * 100 <= 50 then 'HIGH'
        when PERCENT_RANK() over(order by size_of_colony desc) * 100 <= 75 then 'MEDIUM'
        when PERCENT_RANK() over(order by size_of_colony desc) * 100 <= 100 then 'LOW'
    end as colony_name
from ecoli_data
order by id