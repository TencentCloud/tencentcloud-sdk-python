# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class BatchContent(AbstractModel):
    """批量消息

    """

    def __init__(self):
        r"""
        :param _Body: 消息体
        :type Body: str
        :param _Key: 消息的键名
        :type Key: str
        """
        self._Body = None
        self._Key = None

    @property
    def Body(self):
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Body = params.get("Body")
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageRequest(AbstractModel):
    """SendMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DataHubId: 接入资源ID
        :type DataHubId: str
        :param _Message: 批量消息
        :type Message: list of BatchContent
        """
        self._DataHubId = None
        self._Message = None

    @property
    def DataHubId(self):
        return self._DataHubId

    @DataHubId.setter
    def DataHubId(self, DataHubId):
        self._DataHubId = DataHubId

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._DataHubId = params.get("DataHubId")
        if params.get("Message") is not None:
            self._Message = []
            for item in params.get("Message"):
                obj = BatchContent()
                obj._deserialize(item)
                self._Message.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendMessageResponse(AbstractModel):
    """SendMessage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MessageId: 消息ID
        :type MessageId: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MessageId = None
        self._RequestId = None

    @property
    def MessageId(self):
        return self._MessageId

    @MessageId.setter
    def MessageId(self, MessageId):
        self._MessageId = MessageId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._MessageId = params.get("MessageId")
        self._RequestId = params.get("RequestId")