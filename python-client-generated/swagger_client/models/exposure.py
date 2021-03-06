# coding: utf-8

"""
    Environmental Exposures API

    API for environmental exposure models for NIH Data Translator program

    OpenAPI spec version: 1.0.0
    Contact: stealey@renci.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Exposure(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, exposure_type=None, start_time=None, end_time=None, value=None, units=None, latitude=None, longitude=None):
        """
        Exposure - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'exposure_type': 'str',
            'start_time': 'datetime',
            'end_time': 'datetime',
            'value': 'str',
            'units': 'str',
            'latitude': 'str',
            'longitude': 'str'
        }

        self.attribute_map = {
            'exposure_type': 'exposure_type',
            'start_time': 'start_time',
            'end_time': 'end_time',
            'value': 'value',
            'units': 'units',
            'latitude': 'latitude',
            'longitude': 'longitude'
        }

        self._exposure_type = exposure_type
        self._start_time = start_time
        self._end_time = end_time
        self._value = value
        self._units = units
        self._latitude = latitude
        self._longitude = longitude


    @property
    def exposure_type(self):
        """
        Gets the exposure_type of this Exposure.


        :return: The exposure_type of this Exposure.
        :rtype: str
        """
        return self._exposure_type

    @exposure_type.setter
    def exposure_type(self, exposure_type):
        """
        Sets the exposure_type of this Exposure.


        :param exposure_type: The exposure_type of this Exposure.
        :type: str
        """
        if exposure_type is None:
            raise ValueError("Invalid value for `exposure_type`, must not be `None`")

        self._exposure_type = exposure_type

    @property
    def start_time(self):
        """
        Gets the start_time of this Exposure.


        :return: The start_time of this Exposure.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this Exposure.


        :param start_time: The start_time of this Exposure.
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """
        Gets the end_time of this Exposure.


        :return: The end_time of this Exposure.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """
        Sets the end_time of this Exposure.


        :param end_time: The end_time of this Exposure.
        :type: datetime
        """

        self._end_time = end_time

    @property
    def value(self):
        """
        Gets the value of this Exposure.


        :return: The value of this Exposure.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this Exposure.


        :param value: The value of this Exposure.
        :type: str
        """

        self._value = value

    @property
    def units(self):
        """
        Gets the units of this Exposure.


        :return: The units of this Exposure.
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """
        Sets the units of this Exposure.


        :param units: The units of this Exposure.
        :type: str
        """

        self._units = units

    @property
    def latitude(self):
        """
        Gets the latitude of this Exposure.


        :return: The latitude of this Exposure.
        :rtype: str
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Exposure.


        :param latitude: The latitude of this Exposure.
        :type: str
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this Exposure.


        :return: The longitude of this Exposure.
        :rtype: str
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Exposure.


        :param longitude: The longitude of this Exposure.
        :type: str
        """

        self._longitude = longitude

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
