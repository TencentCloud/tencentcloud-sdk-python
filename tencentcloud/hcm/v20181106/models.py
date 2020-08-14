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
        :param Image: 图片数据，需要使用base64对图片的二进制数据进行编码，与url参数二者填一即可；
        :type Image: str
        :param HcmAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 HcmAppid 可以在[控制台](https://console.cloud.tencent.com/hcm)【应用管理】下新建。
        :type HcmAppid: str
        :param Url: 图片url，与Image参数二者填一即可；
        :type Url: str
        :param SupportHorizontalImage: 横屏拍摄开关，若开启则支持传输横屏拍摄的图片；
        :type SupportHorizontalImage: bool
        :param RejectNonArithmeticImage: 拒绝非速算图（如风景图、人物图）开关，若开启，则遇到非速算图会快速返回拒绝的结果，但极端情况下可能会影响评估结果（比如算式截图贴到风景画里可能被判为非速算图直接返回了）。
        :type RejectNonArithmeticImage: bool
        :param IsAsync: 异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :type IsAsync: int
        :param EnableDispRelatedVertical: 是否展开耦合算式中的竖式计算
        :type EnableDispRelatedVertical: bool
        :param EnableDispMidresult: 是否展示竖式算式的中间结果和格式控制字符
        :type EnableDispMidresult: bool
        :param EnablePdfRecognize: 是否开启pdf识别，默认开启
        :type EnablePdfRecognize: bool
        :param PdfPageIndex: pdf页码，从0开始，默认为0
        :type PdfPageIndex: int
        :param LaTex: 是否返回LaTex，默认为0返回普通格式，设置成1返回LaTex格式
        :type LaTex: int
        """
        self.SessionId = None
        self.Image = None
        self.HcmAppid = None
        self.Url = None
        self.SupportHorizontalImage = None
        self.RejectNonArithmeticImage = None
        self.IsAsync = None
        self.EnableDispRelatedVertical = None
        self.EnableDispMidresult = None
        self.EnablePdfRecognize = None
        self.PdfPageIndex = None
        self.LaTex = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Image = params.get("Image")
        self.HcmAppid = params.get("HcmAppid")
        self.Url = params.get("Url")
        self.SupportHorizontalImage = params.get("SupportHorizontalImage")
        self.RejectNonArithmeticImage = params.get("RejectNonArithmeticImage")
        self.IsAsync = params.get("IsAsync")
        self.EnableDispRelatedVertical = params.get("EnableDispRelatedVertical")
        self.EnableDispMidresult = params.get("EnableDispMidresult")
        self.EnablePdfRecognize = params.get("EnablePdfRecognize")
        self.PdfPageIndex = params.get("PdfPageIndex")
        self.LaTex = params.get("LaTex")


class EvaluationResponse(AbstractModel):
    """Evaluation返回参数结构体

    """

    def __init__(self):
        """
        :param SessionId: 图片唯一标识，一张图片一个SessionId；
        :type SessionId: str
        :param Items: 识别出的算式信息；
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param TaskId: 任务 id，用于查询接口
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.Items = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self.Items.append(obj)
        self.TaskId = params.get("TaskId")
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
        :param Answer: 推荐的答案，暂不支持多个关系运算符、无关系运算符、单位换算错题的推荐答案返回。
        :type Answer: str
        :param ExpressionType: 算式题型编号，如加减乘除四则题型，具体题型及编号如下：1 加减乘除四则 2 加减乘除已知结果求运算因子3 判断大小 4 约等于估算 5 带余数除法 6 分数四则运算 7 单位换算 8 竖式加减法 9 竖式乘除法 10 脱式计算 11 解方程
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        :param ItemConf: 文本行置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemConf: float
        """
        self.Item = None
        self.ItemString = None
        self.ItemCoord = None
        self.Answer = None
        self.ExpressionType = None
        self.ItemConf = None


    def _deserialize(self, params):
        self.Item = params.get("Item")
        self.ItemString = params.get("ItemString")
        if params.get("ItemCoord") is not None:
            self.ItemCoord = ItemCoord()
            self.ItemCoord._deserialize(params.get("ItemCoord"))
        self.Answer = params.get("Answer")
        self.ExpressionType = params.get("ExpressionType")
        self.ItemConf = params.get("ItemConf")


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