# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from simple_item_manager.models.item import Item  # noqa: E501
from simple_item_manager.test import BaseTestCase


class TestItemController(BaseTestCase):
    """ItemController integration test stubs"""

    def test_add_item(self):
        """Test case for add_item

        物品情報登録
        """
        item = {
  "itemId" : "itemId",
  "image" : "",
  "name" : "name",
  "userId" : "userId"
}
        headers = { 
            'cookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/items',
            method='POST',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_item_list(self):
        """Test case for get_item_list

        物品情報一覧取得
        """
        query_string = [('includeUsing', True)]
        headers = { 
            'cookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/items',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_item(self):
        """Test case for update_item

        物品情報更新
        """
        item = {
  "itemId" : "itemId",
  "image" : "",
  "name" : "name",
  "userId" : "userId"
}
        headers = { 
            'cookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/items'.format(item_id='item_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(item),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
