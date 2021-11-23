# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from simple_item_manager.models.inline_object import InlineObject  # noqa: E501
from simple_item_manager.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_login(self):
        """Test case for login

        ログイン
        """
        inline_object = simple_item_manager.InlineObject()
        headers = { 
        }
        response = self.client.open(
            '/api/v1/users/token',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
