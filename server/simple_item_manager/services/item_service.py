from simple_item_manager.db import db, MItem
from simple_item_manager.models import Item

def get_item_list(ids=None, user_id=None, include_using=None):  # noqa: E501
  """物品情報一覧取得

  物品情報の一覧を取得します。 # noqa: E501

  :param ids: 物品ID一覧
  :type ids: List[int]
  :param user_id: 使用者ユーザID
  :type user_id: int
  :param include_using: 利用中を含む判定
  :type include_using: bool

  :rtype: List[Item]
  """
  # ひとまず全件取得
  # MItem.queryが入力候補に表示されない
  items = db.session.query(MItem).all
  # MItemからItemにマッピング（ラムダ式より内包表記のほうが早いらしい）
  return [Item(id=item.id) for item in items]

  