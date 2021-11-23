# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from simple_item_manager.models.base_model_ import Model
from simple_item_manager.models.footprint import Footprint
from simple_item_manager import util

from simple_item_manager.models.footprint import Footprint  # noqa: E501

class Item(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, item_id=None, name=None, image=None, user_id=None, created_at=None, created_by=None, updated_at=None, updated_by=None):  # noqa: E501
        """Item - a model defined in OpenAPI

        :param item_id: The item_id of this Item.  # noqa: E501
        :type item_id: str
        :param name: The name of this Item.  # noqa: E501
        :type name: str
        :param image: The image of this Item.  # noqa: E501
        :type image: file
        :param user_id: The user_id of this Item.  # noqa: E501
        :type user_id: str
        :param created_at: The created_at of this Item.  # noqa: E501
        :type created_at: datetime
        :param created_by: The created_by of this Item.  # noqa: E501
        :type created_by: str
        :param updated_at: The updated_at of this Item.  # noqa: E501
        :type updated_at: datetime
        :param updated_by: The updated_by of this Item.  # noqa: E501
        :type updated_by: str
        """
        self.openapi_types = {
            'item_id': str,
            'name': str,
            'image': file,
            'user_id': str,
            'created_at': datetime,
            'created_by': str,
            'updated_at': datetime,
            'updated_by': str
        }

        self.attribute_map = {
            'item_id': 'itemId',
            'name': 'name',
            'image': 'image',
            'user_id': 'userId',
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            'updated_at': 'updatedAt',
            'updated_by': 'updatedBy'
        }

        self._item_id = item_id
        self._name = name
        self._image = image
        self._user_id = user_id
        self._created_at = created_at
        self._created_by = created_by
        self._updated_at = updated_at
        self._updated_by = updated_by

    @classmethod
    def from_dict(cls, dikt) -> 'Item':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Item of this Item.  # noqa: E501
        :rtype: Item
        """
        return util.deserialize_model(dikt, cls)

    @property
    def item_id(self):
        """Gets the item_id of this Item.

        物品ID  # noqa: E501

        :return: The item_id of this Item.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this Item.

        物品ID  # noqa: E501

        :param item_id: The item_id of this Item.
        :type item_id: str
        """

        self._item_id = item_id

    @property
    def name(self):
        """Gets the name of this Item.

        物品名  # noqa: E501

        :return: The name of this Item.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Item.

        物品名  # noqa: E501

        :param name: The name of this Item.
        :type name: str
        """

        self._name = name

    @property
    def image(self):
        """Gets the image of this Item.

        物品写真  # noqa: E501

        :return: The image of this Item.
        :rtype: file
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Item.

        物品写真  # noqa: E501

        :param image: The image of this Item.
        :type image: file
        """

        self._image = image

    @property
    def user_id(self):
        """Gets the user_id of this Item.

        利用中のユーザID  # noqa: E501

        :return: The user_id of this Item.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Item.

        利用中のユーザID  # noqa: E501

        :param user_id: The user_id of this Item.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this Item.

        作成日時  # noqa: E501

        :return: The created_at of this Item.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Item.

        作成日時  # noqa: E501

        :param created_at: The created_at of this Item.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Item.

        作成者ID  # noqa: E501

        :return: The created_by of this Item.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Item.

        作成者ID  # noqa: E501

        :param created_by: The created_by of this Item.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Item.

        更新日時  # noqa: E501

        :return: The updated_at of this Item.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Item.

        更新日時  # noqa: E501

        :param updated_at: The updated_at of this Item.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Item.

        更新者ID  # noqa: E501

        :return: The updated_by of this Item.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Item.

        更新者ID  # noqa: E501

        :param updated_by: The updated_by of this Item.
        :type updated_by: str
        """

        self._updated_by = updated_by
