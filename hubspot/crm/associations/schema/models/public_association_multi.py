# coding: utf-8

"""
    Associations

    Associations define the relationships between objects in HubSpot. These endpoints allow you to create, read, and remove associations.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.crm.associations.schema.configuration import Configuration


class PublicAssociationMulti(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {"_from": "PublicObjectId", "to": "list[AssociatedId]", "paging": "Paging"}

    attribute_map = {"_from": "from", "to": "to", "paging": "paging"}

    def __init__(self, _from=None, to=None, paging=None, local_vars_configuration=None):  # noqa: E501
        """PublicAssociationMulti - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self._paging = None
        self.discriminator = None

        self._from = _from
        self.to = to
        if paging is not None:
            self.paging = paging

    @property
    def _from(self):
        """Gets the _from of this PublicAssociationMulti.  # noqa: E501


        :return: The _from of this PublicAssociationMulti.  # noqa: E501
        :rtype: PublicObjectId
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this PublicAssociationMulti.


        :param _from: The _from of this PublicAssociationMulti.  # noqa: E501
        :type _from: PublicObjectId
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this PublicAssociationMulti.  # noqa: E501

        The IDs of objects that are associated with the object identified by the ID in 'from'.  # noqa: E501

        :return: The to of this PublicAssociationMulti.  # noqa: E501
        :rtype: list[AssociatedId]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this PublicAssociationMulti.

        The IDs of objects that are associated with the object identified by the ID in 'from'.  # noqa: E501

        :param to: The to of this PublicAssociationMulti.  # noqa: E501
        :type to: list[AssociatedId]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def paging(self):
        """Gets the paging of this PublicAssociationMulti.  # noqa: E501


        :return: The paging of this PublicAssociationMulti.  # noqa: E501
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PublicAssociationMulti.


        :param paging: The paging of this PublicAssociationMulti.  # noqa: E501
        :type paging: Paging
        """

        self._paging = paging

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PublicAssociationMulti):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PublicAssociationMulti):
            return True

        return self.to_dict() != other.to_dict()
