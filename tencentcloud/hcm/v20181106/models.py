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


class EvaluationRequest(AbstractModel):
    """Evaluation请求参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 图片唯一标识，一张图片一个SessionId；
        :type SessionId: str
        :param Image: 图片数据，需要使用base64对图片的二进制数据进行编码；
        :type Image: str
        """
        self.SessionId = None
        self.Image = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Image = params.get("Image")


class EvaluationResponse(AbstractModel):
    """Evaluation返回参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 图片唯一标识，一张图片一个SessionId；
        :type SessionId: str
        :param Items: 识别出的算式信息；
        :type Items: list of Item
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class Item(AbstractModel):
    """识别出的算术式信息及评估结果

    """

    def __init__(self):
        """
        :param Item: 识别的算式是否正确
        :type Item: str
        :param ItemString: 识别的算式
        :type ItemString: str
        :param ItemCoord: 识别的算式在图片上的位置信息
        :type ItemCoord: :class:`tencentcloud.hcm.v20181106.models.ItemCoord`
        """
        self.Item = None
        self.ItemString = None
        self.ItemCoord = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.ItemString = params.get("ItemString")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))


class ItemCoord(AbstractModel):
    """目标算式在图片上的坐标信息

    """

    def __init__(self):
        """
        :param Height: 算式高度
        :type Height: int
        :param Width: 算式宽度
        :type Width: int
        :param X: 算式图的左上角横坐标
        :type X: int
        :param Y: 算式图的左上角纵坐标
        :type Y: int
        """
        self.Height = None
        self.Width = None
        self.X = None
        self.Y = None


    def _deserialize(self, params):
        self.Height = params.get("Height")
        self.Width = params.get("Width")
        self.X = params.get("X")
        self.Y = params.get("Y")