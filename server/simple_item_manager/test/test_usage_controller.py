# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from simple_item_manager.models.usage import Usage  # noqa: E501
from simple_item_manager.test import BaseTestCase


class TestUsageController(BaseTestCase):
    """UsageController integration test stubs"""

    def test_get_usageist(self):
        """Test case for get_usageist

        使用状況情報一覧取得
        """
        query_string = [('userId', 56)]
        headers = { 
            'cookieAuth': 'special-key',
        }
        response = self.client.open(
            '/api/v1/usages',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
