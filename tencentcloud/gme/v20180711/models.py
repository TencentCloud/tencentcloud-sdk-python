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


class DescribeFilterResultListRequest(AbstractModel):
    """DescribeFilterResultList请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用id
        :type BizId: int
        :param StartDate: 开始时间，格式为 年-月-日，如: 2018-07-11
        :type StartDate: str
        :param EndDate: 结束时间，格式为 年-月-日，如: 2018-07-11
        :type EndDate: str
        :param Offset: 偏移量, 默认0
        :type Offset: int
        :param Limit: 限制数目	, 默认10, 最大100
        :type Limit: int
        """
        self.BizId = None
        self.StartDate = None
        self.EndDate = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.StartDate = params.get("StartDate")
        self.EndDate = params.get("EndDate")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeFilterResultListResponse(AbstractModel):
    """DescribeFilterResultList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 过滤结果总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Data: 当前分页过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilterInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilterInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class VoiceFilter(AbstractModel):
    """过滤结果

    """

    def __init__(self):
        """
        :param Type: 过滤类型，1：政治，2：色情，3：涉毒
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: int
        :param Word: 过滤命中关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Word: str
        """
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Word = params.get("Word")


class VoiceFilterInfo(AbstractModel):
    """语音文件过滤详情

    """

    def __init__(self):
        """
        :param BizId: 应用id
注意：此字段可能返回 null，表示取不到有效值。
        :type BizId: int
        :param FileId: 文件id，表示文件唯一id
注意：此字段可能返回 null，表示取不到有效值。
        :type FileId: str
        :param FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param OpenId: 用户id
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Timestamp: 数据创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Timestamp: str
        :param Data: 过滤结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of VoiceFilter
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.OpenId = None
        self.Timestamp = None
        self.Data = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.OpenId = params.get("OpenId")
        self.Timestamp = params.get("Timestamp")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = VoiceFilter()
                obj._deserialize(item)
                self.Data.append(obj)


class VoiceFilterRequest(AbstractModel):
    """VoiceFilter请求参数结构体

    """

    def __init__(self):
        """
        :param BizId: 应用id
        :type BizId: int
        :param FileId: 文件id，表示文件唯一id
        :type FileId: str
        :param FileName: 文件名
        :type FileName: str
        :param FileUrl: 文件内容url，FileUrl和FileContent二选一
        :type FileUrl: str
        :param FileContent: 文件内容，base64编码，FileUrl和FileContent二选一
        :type FileContent: str
        :param OpenId: 用户id
        :type OpenId: str
        """
        self.BizId = None
        self.FileId = None
        self.FileName = None
        self.FileUrl = None
        self.FileContent = None
        self.OpenId = None


    def _deserialize(self, params):
        self.BizId = params.get("BizId")
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileUrl = params.get("FileUrl")
        self.FileContent = params.get("FileContent")
        self.OpenId = params.get("OpenId")


class VoiceFilterResponse(AbstractModel):
    """VoiceFilter返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")