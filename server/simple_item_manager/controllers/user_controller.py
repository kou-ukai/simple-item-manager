import connexion
import six

from simple_item_manager.models.inline_object import InlineObject  # noqa: E501
from simple_item_manager.models.user import User  # noqa: E501
from simple_item_manager import util


def get_user_list(ids=None):  # noqa: E501
    """ユーザ情報一覧取得

    ユーザ情報の一覧を取得します。 # noqa: E501

    :param ids: ユーザID一覧
    :type ids: List[int]

    :rtype: List[User]
    """
    return 'do some magic!'


def login(inline_object):  # noqa: E501
    """ログイン

    NFCタグのシリアル番号でログインします。 # noqa: E501

    :param inline_object: 
    :type inline_object: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        inline_object = InlineObject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
