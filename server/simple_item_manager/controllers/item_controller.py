import connexion
import six

from simple_item_manager.models.item import Item  # noqa: E501
from simple_item_manager import util


def add_item(item):  # noqa: E501
    """物品情報登録

    物品情報を登録します。 # noqa: E501

    :param item: 登録するコース配達状況情報情報
    :type item: dict | bytes

    :rtype: Item
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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
    return 'do some magic!'


def update_item(item_id, item):  # noqa: E501
    """物品情報更新

    物品情報を更新します。 # noqa: E501

    :param item_id: 物品ID
    :type item_id: str
    :param item: 更新する物品情報
    :type item: dict | bytes

    :rtype: Item
    """
    if connexion.request.is_json:
        item = Item.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
