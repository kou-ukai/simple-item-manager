import connexion
import six

from simple_item_manager.models.inline_object import InlineObject  # noqa: E501
from simple_item_manager import util


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
