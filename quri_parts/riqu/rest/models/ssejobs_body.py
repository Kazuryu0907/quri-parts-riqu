# coding: utf-8
"""Riqu (Rest Interface for QUantum computing)

the cloud server with riqu interface.  # noqa: E501

OpenAPI spec version: 1.1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class SsejobsBody(object):
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
    swagger_types = {"up_file": "str", "remark": "str", "job_type": "str"}

    attribute_map = {"up_file": "up_file", "remark": "remark", "job_type": "job_type"}

    def __init__(self, up_file=None, remark=None, job_type=None):  # noqa: E501
        """SsejobsBody - a model defined in Swagger"""  # noqa: E501
        self._up_file = None
        self._remark = None
        self._job_type = None
        self.discriminator = None
        if up_file is not None:
            self.up_file = up_file
        if remark is not None:
            self.remark = remark
        if job_type is not None:
            self.job_type = job_type

    @property
    def up_file(self):
        """Gets the up_file of this SsejobsBody.  # noqa: E501.

        The file to upload.  # noqa: E501

        :return: The up_file of this SsejobsBody.  # noqa: E501
        :rtype: str
        """
        return self._up_file

    @up_file.setter
    def up_file(self, up_file):
        """Sets the up_file of this SsejobsBody.

        The file to upload.  # noqa: E501

        :param up_file: The up_file of this SsejobsBody.  # noqa: E501
        :type: str
        """

        self._up_file = up_file

    @property
    def remark(self):
        """Gets the remark of this SsejobsBody.  # noqa: E501.

        The remark for ssejob.  # noqa: E501

        :return: The remark of this SsejobsBody.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this SsejobsBody.

        The remark for ssejob.  # noqa: E501

        :param remark: The remark of this SsejobsBody.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def job_type(self):
        """Gets the job_type of this SsejobsBody.  # noqa: E501.

        The remark for ssejob.  # noqa: E501

        :return: The job_type of this SsejobsBody.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this SsejobsBody.

        The remark for ssejob.  # noqa: E501

        :param job_type: The job_type of this SsejobsBody.  # noqa: E501
        :type: str
        """

        self._job_type = job_type

    def to_dict(self):
        """Returns the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(SsejobsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal."""
        if not isinstance(other, SsejobsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal."""
        return not self == other
