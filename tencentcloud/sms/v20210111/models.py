# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class DescribeSmsTemplateListRequest(AbstractModel):
    """DescribeSmsTemplateList请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateIdSet: 模板 ID 数组。
        :type TemplateIdSet: list of int non-negative
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        """
        self.TemplateIdSet = None
        self.International = None


    def _deserialize(self, params):
        self.TemplateIdSet = params.get("TemplateIdSet")
        self.International = params.get("International")


class DescribeSmsTemplateListResponse(AbstractModel):
    """DescribeSmsTemplateList返回参数结构体

    """

    def __init__(self):
        """
        :param DescribeTemplateStatusSet: 获取短信模板信息响应
        :type DescribeTemplateStatusSet: list of DescribeTemplateListStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DescribeTemplateStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DescribeTemplateStatusSet") is not None:
            self.DescribeTemplateStatusSet = []
            for item in params.get("DescribeTemplateStatusSet"):
                obj = DescribeTemplateListStatus()
                obj._deserialize(item)
                self.DescribeTemplateStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateListStatus(AbstractModel):
    """获取短信模板信息响应

    """

    def __init__(self):
        """
        :param TemplateId: 模板Id
        :type TemplateId: int
        :param International: 是否国际/港澳台短信：
0：表示国内短信。
1：表示国际/港澳台短信。
        :type International: int
        :param StatusCode: 申请签名状态。其中：
0：表示审核通过。
1：表示审核中。
-1：表示审核未通过或审核失败。
        :type StatusCode: int
        :param ReviewReply: 审核回复，审核人员审核后给出的回复，通常是审核未通过的原因。
        :type ReviewReply: str
        :param TemplateName: 模板名称。
        :type TemplateName: str
        :param CreateTime: 提交审核时间，UNIX 时间戳（单位：秒）。
        :type CreateTime: int
        """
        self.TemplateId = None
        self.International = None
        self.StatusCode = None
        self.ReviewReply = None
        self.TemplateName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.International = params.get("International")
        self.StatusCode = params.get("StatusCode")
        self.ReviewReply = params.get("ReviewReply")
        self.TemplateName = params.get("TemplateName")
        self.CreateTime = params.get("CreateTime")