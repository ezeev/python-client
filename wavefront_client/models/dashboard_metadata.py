# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class DashboardMetadata(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        DashboardMetadata - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'customer_tags_with_counts': 'dict(str, int)',
            'days_in_trash': 'int',
            'description': 'str',
            'display_description': 'bool',
            'display_query_parameters': 'bool',
            'display_section_table_of_contents': 'bool',
            'is_favorite': 'bool',
            'last_update_time': 'int',
            'name': 'str',
            'num_charts': 'int',
            'num_favorites': 'int',
            'trash': 'bool',
            'url': 'str',
            'user_tags_with_counts': 'dict(str, int)'
        }

        self.attribute_map = {
            'customer_tags_with_counts': 'customerTagsWithCounts',
            'days_in_trash': 'daysInTrash',
            'description': 'description',
            'display_description': 'displayDescription',
            'display_query_parameters': 'displayQueryParameters',
            'display_section_table_of_contents': 'displaySectionTableOfContents',
            'is_favorite': 'isFavorite',
            'last_update_time': 'lastUpdateTime',
            'name': 'name',
            'num_charts': 'numCharts',
            'num_favorites': 'numFavorites',
            'trash': 'trash',
            'url': 'url',
            'user_tags_with_counts': 'userTagsWithCounts'
        }

        self._customer_tags_with_counts = None
        self._days_in_trash = None
        self._description = None
        self._display_description = False
        self._display_query_parameters = False
        self._display_section_table_of_contents = False
        self._is_favorite = False
        self._last_update_time = None
        self._name = None
        self._num_charts = None
        self._num_favorites = None
        self._trash = False
        self._url = None
        self._user_tags_with_counts = None

    @property
    def customer_tags_with_counts(self):
        """
        Gets the customer_tags_with_counts of this DashboardMetadata.


        :return: The customer_tags_with_counts of this DashboardMetadata.
        :rtype: dict(str, int)
        """
        return self._customer_tags_with_counts

    @customer_tags_with_counts.setter
    def customer_tags_with_counts(self, customer_tags_with_counts):
        """
        Sets the customer_tags_with_counts of this DashboardMetadata.


        :param customer_tags_with_counts: The customer_tags_with_counts of this DashboardMetadata.
        :type: dict(str, int)
        """
        self._customer_tags_with_counts = customer_tags_with_counts

    @property
    def days_in_trash(self):
        """
        Gets the days_in_trash of this DashboardMetadata.


        :return: The days_in_trash of this DashboardMetadata.
        :rtype: int
        """
        return self._days_in_trash

    @days_in_trash.setter
    def days_in_trash(self, days_in_trash):
        """
        Sets the days_in_trash of this DashboardMetadata.


        :param days_in_trash: The days_in_trash of this DashboardMetadata.
        :type: int
        """
        self._days_in_trash = days_in_trash

    @property
    def description(self):
        """
        Gets the description of this DashboardMetadata.


        :return: The description of this DashboardMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DashboardMetadata.


        :param description: The description of this DashboardMetadata.
        :type: str
        """
        self._description = description

    @property
    def display_description(self):
        """
        Gets the display_description of this DashboardMetadata.


        :return: The display_description of this DashboardMetadata.
        :rtype: bool
        """
        return self._display_description

    @display_description.setter
    def display_description(self, display_description):
        """
        Sets the display_description of this DashboardMetadata.


        :param display_description: The display_description of this DashboardMetadata.
        :type: bool
        """
        self._display_description = display_description

    @property
    def display_query_parameters(self):
        """
        Gets the display_query_parameters of this DashboardMetadata.


        :return: The display_query_parameters of this DashboardMetadata.
        :rtype: bool
        """
        return self._display_query_parameters

    @display_query_parameters.setter
    def display_query_parameters(self, display_query_parameters):
        """
        Sets the display_query_parameters of this DashboardMetadata.


        :param display_query_parameters: The display_query_parameters of this DashboardMetadata.
        :type: bool
        """
        self._display_query_parameters = display_query_parameters

    @property
    def display_section_table_of_contents(self):
        """
        Gets the display_section_table_of_contents of this DashboardMetadata.


        :return: The display_section_table_of_contents of this DashboardMetadata.
        :rtype: bool
        """
        return self._display_section_table_of_contents

    @display_section_table_of_contents.setter
    def display_section_table_of_contents(self, display_section_table_of_contents):
        """
        Sets the display_section_table_of_contents of this DashboardMetadata.


        :param display_section_table_of_contents: The display_section_table_of_contents of this DashboardMetadata.
        :type: bool
        """
        self._display_section_table_of_contents = display_section_table_of_contents

    @property
    def is_favorite(self):
        """
        Gets the is_favorite of this DashboardMetadata.


        :return: The is_favorite of this DashboardMetadata.
        :rtype: bool
        """
        return self._is_favorite

    @is_favorite.setter
    def is_favorite(self, is_favorite):
        """
        Sets the is_favorite of this DashboardMetadata.


        :param is_favorite: The is_favorite of this DashboardMetadata.
        :type: bool
        """
        self._is_favorite = is_favorite

    @property
    def last_update_time(self):
        """
        Gets the last_update_time of this DashboardMetadata.


        :return: The last_update_time of this DashboardMetadata.
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """
        Sets the last_update_time of this DashboardMetadata.


        :param last_update_time: The last_update_time of this DashboardMetadata.
        :type: int
        """
        self._last_update_time = last_update_time

    @property
    def name(self):
        """
        Gets the name of this DashboardMetadata.


        :return: The name of this DashboardMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DashboardMetadata.


        :param name: The name of this DashboardMetadata.
        :type: str
        """
        self._name = name

    @property
    def num_charts(self):
        """
        Gets the num_charts of this DashboardMetadata.


        :return: The num_charts of this DashboardMetadata.
        :rtype: int
        """
        return self._num_charts

    @num_charts.setter
    def num_charts(self, num_charts):
        """
        Sets the num_charts of this DashboardMetadata.


        :param num_charts: The num_charts of this DashboardMetadata.
        :type: int
        """
        self._num_charts = num_charts

    @property
    def num_favorites(self):
        """
        Gets the num_favorites of this DashboardMetadata.


        :return: The num_favorites of this DashboardMetadata.
        :rtype: int
        """
        return self._num_favorites

    @num_favorites.setter
    def num_favorites(self, num_favorites):
        """
        Sets the num_favorites of this DashboardMetadata.


        :param num_favorites: The num_favorites of this DashboardMetadata.
        :type: int
        """
        self._num_favorites = num_favorites

    @property
    def trash(self):
        """
        Gets the trash of this DashboardMetadata.


        :return: The trash of this DashboardMetadata.
        :rtype: bool
        """
        return self._trash

    @trash.setter
    def trash(self, trash):
        """
        Sets the trash of this DashboardMetadata.


        :param trash: The trash of this DashboardMetadata.
        :type: bool
        """
        self._trash = trash

    @property
    def url(self):
        """
        Gets the url of this DashboardMetadata.


        :return: The url of this DashboardMetadata.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this DashboardMetadata.


        :param url: The url of this DashboardMetadata.
        :type: str
        """
        self._url = url

    @property
    def user_tags_with_counts(self):
        """
        Gets the user_tags_with_counts of this DashboardMetadata.


        :return: The user_tags_with_counts of this DashboardMetadata.
        :rtype: dict(str, int)
        """
        return self._user_tags_with_counts

    @user_tags_with_counts.setter
    def user_tags_with_counts(self, user_tags_with_counts):
        """
        Sets the user_tags_with_counts of this DashboardMetadata.


        :param user_tags_with_counts: The user_tags_with_counts of this DashboardMetadata.
        :type: dict(str, int)
        """
        self._user_tags_with_counts = user_tags_with_counts

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

