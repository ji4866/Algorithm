select item_id, item_name, rarity
from item_info a
where not exists(
    select * from item_tree b
    where a.item_id = b.PARENT_ITEM_ID
)
order by item_id desc