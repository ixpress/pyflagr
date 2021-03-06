# coding: utf-8

"""
    Flagr

    Flagr is a feature flagging, A/B testing and dynamic configuration microservice  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EvalContext(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_id': 'str',
        'entity_type': 'str',
        'entity_context': 'object',
        'enable_debug': 'bool',
        'flag_id': 'int'
    }

    attribute_map = {
        'entity_id': 'entityID',
        'entity_type': 'entityType',
        'entity_context': 'entityContext',
        'enable_debug': 'enableDebug',
        'flag_id': 'flagID'
    }

    def __init__(self, entity_id=None, entity_type=None, entity_context=None, enable_debug=None, flag_id=None):  # noqa: E501
        """EvalContext - a model defined in Swagger"""  # noqa: E501

        self._entity_id = None
        self._entity_type = None
        self._entity_context = None
        self._enable_debug = None
        self._flag_id = None
        self.discriminator = None

        self.entity_id = entity_id
        self.entity_type = entity_type
        if entity_context is not None:
            self.entity_context = entity_context
        if enable_debug is not None:
            self.enable_debug = enable_debug
        self.flag_id = flag_id

    @property
    def entity_id(self):
        """Gets the entity_id of this EvalContext.  # noqa: E501


        :return: The entity_id of this EvalContext.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EvalContext.


        :param entity_id: The entity_id of this EvalContext.  # noqa: E501
        :type: str
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501
        if entity_id is not None and len(entity_id) < 1:
            raise ValueError("Invalid value for `entity_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this EvalContext.  # noqa: E501


        :return: The entity_type of this EvalContext.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EvalContext.


        :param entity_type: The entity_type of this EvalContext.  # noqa: E501
        :type: str
        """
        if entity_type is None:
            raise ValueError("Invalid value for `entity_type`, must not be `None`")  # noqa: E501
        if entity_type is not None and len(entity_type) < 1:
            raise ValueError("Invalid value for `entity_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._entity_type = entity_type

    @property
    def entity_context(self):
        """Gets the entity_context of this EvalContext.  # noqa: E501


        :return: The entity_context of this EvalContext.  # noqa: E501
        :rtype: object
        """
        return self._entity_context

    @entity_context.setter
    def entity_context(self, entity_context):
        """Sets the entity_context of this EvalContext.


        :param entity_context: The entity_context of this EvalContext.  # noqa: E501
        :type: object
        """

        self._entity_context = entity_context

    @property
    def enable_debug(self):
        """Gets the enable_debug of this EvalContext.  # noqa: E501


        :return: The enable_debug of this EvalContext.  # noqa: E501
        :rtype: bool
        """
        return self._enable_debug

    @enable_debug.setter
    def enable_debug(self, enable_debug):
        """Sets the enable_debug of this EvalContext.


        :param enable_debug: The enable_debug of this EvalContext.  # noqa: E501
        :type: bool
        """

        self._enable_debug = enable_debug

    @property
    def flag_id(self):
        """Gets the flag_id of this EvalContext.  # noqa: E501


        :return: The flag_id of this EvalContext.  # noqa: E501
        :rtype: int
        """
        return self._flag_id

    @flag_id.setter
    def flag_id(self, flag_id):
        """Sets the flag_id of this EvalContext.


        :param flag_id: The flag_id of this EvalContext.  # noqa: E501
        :type: int
        """
        if flag_id is None:
            raise ValueError("Invalid value for `flag_id`, must not be `None`")  # noqa: E501
        if flag_id is not None and flag_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `flag_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._flag_id = flag_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EvalContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
