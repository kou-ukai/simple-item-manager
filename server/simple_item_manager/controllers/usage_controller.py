import connexion
import six

from simple_item_manager.models.usage import Usage  # noqa: E501
from simple_item_manager import util


def get_usageist(user_id=None):  # noqa: E501
    """使用状況情報一覧取得

    使用状況情報の一覧を取得します。 # noqa: E501

    :param user_id: 使用者ユーザID
    :type user_id: int

    :rtype: List[Usage]
    """
    return 'do some magic!'
