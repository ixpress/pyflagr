# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import flagr
from flagr.api.constraint_api import ConstraintApi  # noqa: E501
from flagr.rest import ApiException


class TestConstraintApi(unittest.TestCase):
    """ConstraintApi unit test stubs"""

    def setUp(self):
        self.api = flagr.api.constraint_api.ConstraintApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_constraint(self):
        """Test case for create_constraint

        """
        pass

    def test_delete_constraint(self):
        """Test case for delete_constraint

        """
        pass

    def test_find_constraints(self):
        """Test case for find_constraints

        """
        pass

    def test_put_constraint(self):
        """Test case for put_constraint

        """
        pass


if __name__ == '__main__':
    unittest.main()