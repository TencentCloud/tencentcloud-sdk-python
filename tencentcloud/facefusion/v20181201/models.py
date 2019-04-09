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


class FaceFusionRequest(AbstractModel):
    """FaceFusion请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param Image: 图片 base64 数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理；请勿在 base64 数据中包含头部，如“data:image/jpeg;base64,”。
        :type Image: str
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。当前仅支持 url 方式，base64 方式后期开放。
        :type RspImgType: str
        :param PornDetect: 0表示不需要鉴黄，1表示需要鉴黄。2018年12月1号以前创建的活动默认值为0，其他情况默认值为1.
        :type PornDetect: int
        :param CelebrityIdentify: 0表示不需要鉴政，1表示需要鉴政。2018年12月1号以前创建的活动默认值为0，其他情况默认值为1。鉴政接口同时会对名人明星进行识别，您可以根据实际需要过滤。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.Image = None
        self.RspImgType = None
        self.PornDetect = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.Image = params.get("Image")
        self.RspImgType = params.get("RspImgType")
        self.PornDetect = params.get("PornDetect")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FaceFusionResponse(AbstractModel):
    """FaceFusion返回参数结构体

    """

    def __init__(self):
        """
        :param Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。当前仅支持 url 方式，base64 方式后期开放。
        :type Image: str
        :param ReviewResultSet: 鉴黄鉴政结果
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Image = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        if params.get("ReviewResultSet") is not None:
            self.ReviewResultSet = []
            for item in params.get("ReviewResultSet"):
                obj = FuseFaceReviewResult()
                obj._deserialize(item)
                self.ReviewResultSet.append(obj)
        self.RequestId = params.get("RequestId")


class FuseFaceReviewDetail(AbstractModel):
    """人脸融合鉴黄鉴政人脸信息

    """

    def __init__(self):
        """
        :param Field: 鉴政使用字段, 为职业属性,其他审核结果对应上一级category
        :type Field: str
        :param Label: 人员名称
        :type Label: str
        :param Confidence: 对应识别label的置信度
        :type Confidence: float
        :param Suggestion: 此字段为保留字段，目前统一返回pass。
        :type Suggestion: str
        """
        self.Field = None
        self.Label = None
        self.Confidence = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.Field = params.get("Field")
        self.Label = params.get("Label")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")


class FuseFaceReviewResult(AbstractModel):
    """人脸融合鉴黄鉴政返回参数item

    """

    def __init__(self):
        """
        :param Category: 对应的类别名称 porn, politics, terror
        :type Category: str
        :param Code: 对应子类别状态码
        :type Code: str
        :param CodeDescription: 对应子类别状态码信息描述
        :type CodeDescription: str
        :param Confidence: 对应识别种类的置信度
        :type Confidence: float
        :param Suggestion: 此字段为保留字段，目前统一返回pass。
        :type Suggestion: str
        :param DetailSet: 审核详细内容
        :type DetailSet: list of FuseFaceReviewDetail
        """
        self.Category = None
        self.Code = None
        self.CodeDescription = None
        self.Confidence = None
        self.Suggestion = None
        self.DetailSet = None


    def _deserialize(self, params):
        self.Category = params.get("Category")
        self.Code = params.get("Code")
        self.CodeDescription = params.get("CodeDescription")
        self.Confidence = params.get("Confidence")
        self.Suggestion = params.get("Suggestion")
        if params.get("DetailSet") is not None:
            self.DetailSet = []
            for item in params.get("DetailSet"):
                obj = FuseFaceReviewDetail()
                obj._deserialize(item)
                self.DetailSet.append(obj)