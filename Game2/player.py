from items import *
from map import rooms

inventory = [item_id, item_laptop, item_money]
carrying_capacity = (item_id["weight"] + item_laptop["weight"] + item_money["weight"])
# Start game at the reception
                     
current_room = rooms["Reception"]
