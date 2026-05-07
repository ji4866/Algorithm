select a.emp_no, a.emp_name, 
case when score >= 96 then 'S' -- 등급
        when score >= 90 then 'A'
        when score >= 80 then 'B'
    else 'C' end as grade,
    case when score >= 96 then sal*0.2 -- 성과금
        when score >= 90 then sal*0.15
        when score >= 80 then sal*0.1
    else 0 end as bonus
from hr_employees a
left join(
    select emp_no, avg(score) score from hr_grade
    group by emp_no
) b
on a.emp_no = b.emp_no
order by a.emp_no