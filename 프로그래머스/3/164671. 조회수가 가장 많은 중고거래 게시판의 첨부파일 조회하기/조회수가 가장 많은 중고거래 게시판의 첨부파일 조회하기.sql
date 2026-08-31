select concat('/home/grep/src/', board_id, '/', file_id, file_name, file_ext) as file_path
from(
    select a.board_id, b.file_id, file_ext, file_name, rank() over(order by views desc) rank_
    from used_goods_board a
    join used_goods_file b on a.board_id = b.board_id
) a
where rank_ = 1
order by file_id desc