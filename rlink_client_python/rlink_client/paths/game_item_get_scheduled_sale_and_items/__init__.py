# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from rlink_client.paths.game_item_get_scheduled_sale_and_items import Api

from rlink_client.paths import PathValues

path = PathValues.GAME_ITEM_GET_SCHEDULED_SALE_AND_ITEMS