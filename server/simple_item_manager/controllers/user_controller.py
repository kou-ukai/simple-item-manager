import connexion
import six

from simple_item_manager.models.login_req import LoginReq  # noqa: E501
from simple_item_manager.models.user import User  # noqa: E501
from simple_item_manager import util


def add_user(user):  # noqa: E501
    """ユーザ情報登録

    ユーザ情報を登録します。 # noqa: E501

    :param user: 登録するユーザ情報情報
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = User.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_user_list(ids=None):  # noqa: E501
    """ユーザ情報一覧取得

    ユーザ情報の一覧を取得します。 # noqa: E501

    :param ids: ユーザID一覧
    :type ids: List[int]

    :rtype: List[User]
    """
    return 'do some magic!'


def login(login_req):  # noqa: E501
    """ログイン

    NFCタグのシリアル番号でログインします。 # noqa: E501

    :param login_req: 
    :type login_req: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        login_req = LoginReq.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
