# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class EvaluationRequest(AbstractModel):
    r"""Evaluation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 图片唯一标识，一张图片一个SessionId；
        :type SessionId: str
        :param _Image: 图片数据，需要使用base64对图片的二进制数据进行编码，与url参数二者填一即可；
        :type Image: str
        :param _HcmAppid: 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 HcmAppid 可以在[控制台](https://console.cloud.tencent.com/hcm)【应用管理】下新建。
        :type HcmAppid: str
        :param _Url: 图片url，与Image参数二者填一即可；
        :type Url: str
        :param _SupportHorizontalImage: 横屏拍摄开关，若开启则支持传输横屏拍摄的图片；
        :type SupportHorizontalImage: bool
        :param _RejectNonArithmeticImage: 拒绝非速算图（如风景图、人物图）开关，若开启，则遇到非速算图会快速返回拒绝的结果，但极端情况下可能会影响评估结果（比如算式截图贴到风景画里可能被判为非速算图直接返回了）。
        :type RejectNonArithmeticImage: bool
        :param _IsAsync: 异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :type IsAsync: int
        :param _EnableDispRelatedVertical: 是否展开耦合算式中的竖式计算
        :type EnableDispRelatedVertical: bool
        :param _EnableDispMidresult: 是否展示竖式算式的中间结果和格式控制字符
        :type EnableDispMidresult: bool
        :param _EnablePdfRecognize: 是否开启pdf识别，默认开启
        :type EnablePdfRecognize: bool
        :param _PdfPageIndex: pdf页码，从0开始，默认为0
        :type PdfPageIndex: int
        :param _LaTex: 是否返回LaTex，默认为0返回普通格式，设置成1返回LaTex格式
        :type LaTex: int
        :param _RejectVagueArithmetic: 用于选择是否拒绝模糊题 目。打开则丢弃模糊题目， 不进行后续的判题返回结 果。
        :type RejectVagueArithmetic: bool
        """
        self._SessionId = None
        self._Image = None
        self._HcmAppid = None
        self._Url = None
        self._SupportHorizontalImage = None
        self._RejectNonArithmeticImage = None
        self._IsAsync = None
        self._EnableDispRelatedVertical = None
        self._EnableDispMidresult = None
        self._EnablePdfRecognize = None
        self._PdfPageIndex = None
        self._LaTex = None
        self._RejectVagueArithmetic = None

    @property
    def SessionId(self):
        r"""图片唯一标识，一张图片一个SessionId；
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Image(self):
        r"""图片数据，需要使用base64对图片的二进制数据进行编码，与url参数二者填一即可；
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def HcmAppid(self):
        r"""业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 HcmAppid 可以在[控制台](https://console.cloud.tencent.com/hcm)【应用管理】下新建。
        :rtype: str
        """
        return self._HcmAppid

    @HcmAppid.setter
    def HcmAppid(self, HcmAppid):
        self._HcmAppid = HcmAppid

    @property
    def Url(self):
        r"""图片url，与Image参数二者填一即可；
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def SupportHorizontalImage(self):
        r"""横屏拍摄开关，若开启则支持传输横屏拍摄的图片；
        :rtype: bool
        """
        return self._SupportHorizontalImage

    @SupportHorizontalImage.setter
    def SupportHorizontalImage(self, SupportHorizontalImage):
        self._SupportHorizontalImage = SupportHorizontalImage

    @property
    def RejectNonArithmeticImage(self):
        r"""拒绝非速算图（如风景图、人物图）开关，若开启，则遇到非速算图会快速返回拒绝的结果，但极端情况下可能会影响评估结果（比如算式截图贴到风景画里可能被判为非速算图直接返回了）。
        :rtype: bool
        """
        return self._RejectNonArithmeticImage

    @RejectNonArithmeticImage.setter
    def RejectNonArithmeticImage(self, RejectNonArithmeticImage):
        self._RejectNonArithmeticImage = RejectNonArithmeticImage

    @property
    def IsAsync(self):
        warnings.warn("parameter `IsAsync` is deprecated", DeprecationWarning) 

        r"""异步模式标识，0：同步模式，1：异步模式。默认为同步模式
        :rtype: int
        """
        return self._IsAsync

    @IsAsync.setter
    def IsAsync(self, IsAsync):
        warnings.warn("parameter `IsAsync` is deprecated", DeprecationWarning) 

        self._IsAsync = IsAsync

    @property
    def EnableDispRelatedVertical(self):
        r"""是否展开耦合算式中的竖式计算
        :rtype: bool
        """
        return self._EnableDispRelatedVertical

    @EnableDispRelatedVertical.setter
    def EnableDispRelatedVertical(self, EnableDispRelatedVertical):
        self._EnableDispRelatedVertical = EnableDispRelatedVertical

    @property
    def EnableDispMidresult(self):
        r"""是否展示竖式算式的中间结果和格式控制字符
        :rtype: bool
        """
        return self._EnableDispMidresult

    @EnableDispMidresult.setter
    def EnableDispMidresult(self, EnableDispMidresult):
        self._EnableDispMidresult = EnableDispMidresult

    @property
    def EnablePdfRecognize(self):
        r"""是否开启pdf识别，默认开启
        :rtype: bool
        """
        return self._EnablePdfRecognize

    @EnablePdfRecognize.setter
    def EnablePdfRecognize(self, EnablePdfRecognize):
        self._EnablePdfRecognize = EnablePdfRecognize

    @property
    def PdfPageIndex(self):
        r"""pdf页码，从0开始，默认为0
        :rtype: int
        """
        return self._PdfPageIndex

    @PdfPageIndex.setter
    def PdfPageIndex(self, PdfPageIndex):
        self._PdfPageIndex = PdfPageIndex

    @property
    def LaTex(self):
        r"""是否返回LaTex，默认为0返回普通格式，设置成1返回LaTex格式
        :rtype: int
        """
        return self._LaTex

    @LaTex.setter
    def LaTex(self, LaTex):
        self._LaTex = LaTex

    @property
    def RejectVagueArithmetic(self):
        r"""用于选择是否拒绝模糊题 目。打开则丢弃模糊题目， 不进行后续的判题返回结 果。
        :rtype: bool
        """
        return self._RejectVagueArithmetic

    @RejectVagueArithmetic.setter
    def RejectVagueArithmetic(self, RejectVagueArithmetic):
        self._RejectVagueArithmetic = RejectVagueArithmetic


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Image = params.get("Image")
        self._HcmAppid = params.get("HcmAppid")
        self._Url = params.get("Url")
        self._SupportHorizontalImage = params.get("SupportHorizontalImage")
        self._RejectNonArithmeticImage = params.get("RejectNonArithmeticImage")
        self._IsAsync = params.get("IsAsync")
        self._EnableDispRelatedVertical = params.get("EnableDispRelatedVertical")
        self._EnableDispMidresult = params.get("EnableDispMidresult")
        self._EnablePdfRecognize = params.get("EnablePdfRecognize")
        self._PdfPageIndex = params.get("PdfPageIndex")
        self._LaTex = params.get("LaTex")
        self._RejectVagueArithmetic = params.get("RejectVagueArithmetic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluationResponse(AbstractModel):
    r"""Evaluation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 图片唯一标识，一张图片一个SessionId；
        :type SessionId: str
        :param _Items: 识别出的算式信息；
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of Item
        :param _TaskId: 任务 id，用于查询接口
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionId = None
        self._Items = None
        self._TaskId = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""图片唯一标识，一张图片一个SessionId；
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Items(self):
        r"""识别出的算式信息；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Item
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TaskId(self):
        warnings.warn("parameter `TaskId` is deprecated", DeprecationWarning) 

        r"""任务 id，用于查询接口
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        warnings.warn("parameter `TaskId` is deprecated", DeprecationWarning) 

        self._TaskId = TaskId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = Item()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Item(AbstractModel):
    r"""识别出的算术式信息及评估结果

    """

    def __init__(self):
        r"""
        :param _Item: 识别的算式是否正确，算式运算结果:
‘YES’:正确 
‘NO’: 错误 
‘NA’: 非法参数
‘EMPTY’: 未作答
        :type Item: str
        :param _ItemString: 识别出的算式，识别出的文本行字符串
        :type ItemString: str
        :param _ItemCoord: 识别的算式在图片上的位置信息，文本行在旋转纠正之后的图像中的像素坐 标，表示为(左上角 x, 左上角 y，宽 width， 高 height)
        :type ItemCoord: :class:`tencentcloud.hcm.v20181106.models.ItemCoord`
        :param _Answer: 错题推荐答案，算式运算结果正确返回为 ""，算式运算结果错误返回推荐答案 (注:暂不支持多个关系运算符(如 1<10<7)、 无关系运算符(如 frac(1,2)+frac(2,3))、单 位换算(如 1 元=100 角)错题的推荐答案 返回)
(注:使用@@标记答案填写区域)
        :type Answer: str
        :param _ExpressionType: 算式题型编号，如加减乘除四则题型，具体题型及编号如下：1 加减乘除四则 2 加减乘除已知结果求运算因子3 判断大小 4 约等于估算 5 带余数除法 6 分数四则运算 7 单位换算 8 竖式加减法 9 竖式乘除法 10 脱式计算 11 解方程
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpressionType: str
        :param _ItemConf: 文本行置信度
注意：此字段可能返回 null，表示取不到有效值。
        :type ItemConf: float
        :param _QuestionId: 用于标识题目 id，如果有若干算式属于同一 题，则其对应的 id 相同。
注意：此字段可能返回 null，表示取不到有效值。
        :type QuestionId: str
        """
        self._Item = None
        self._ItemString = None
        self._ItemCoord = None
        self._Answer = None
        self._ExpressionType = None
        self._ItemConf = None
        self._QuestionId = None

    @property
    def Item(self):
        r"""识别的算式是否正确，算式运算结果:
‘YES’:正确 
‘NO’: 错误 
‘NA’: 非法参数
‘EMPTY’: 未作答
        :rtype: str
        """
        return self._Item

    @Item.setter
    def Item(self, Item):
        self._Item = Item

    @property
    def ItemString(self):
        r"""识别出的算式，识别出的文本行字符串
        :rtype: str
        """
        return self._ItemString

    @ItemString.setter
    def ItemString(self, ItemString):
        self._ItemString = ItemString

    @property
    def ItemCoord(self):
        r"""识别的算式在图片上的位置信息，文本行在旋转纠正之后的图像中的像素坐 标，表示为(左上角 x, 左上角 y，宽 width， 高 height)
        :rtype: :class:`tencentcloud.hcm.v20181106.models.ItemCoord`
        """
        return self._ItemCoord

    @ItemCoord.setter
    def ItemCoord(self, ItemCoord):
        self._ItemCoord = ItemCoord

    @property
    def Answer(self):
        r"""错题推荐答案，算式运算结果正确返回为 ""，算式运算结果错误返回推荐答案 (注:暂不支持多个关系运算符(如 1<10<7)、 无关系运算符(如 frac(1,2)+frac(2,3))、单 位换算(如 1 元=100 角)错题的推荐答案 返回)
(注:使用@@标记答案填写区域)
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def ExpressionType(self):
        r"""算式题型编号，如加减乘除四则题型，具体题型及编号如下：1 加减乘除四则 2 加减乘除已知结果求运算因子3 判断大小 4 约等于估算 5 带余数除法 6 分数四则运算 7 单位换算 8 竖式加减法 9 竖式乘除法 10 脱式计算 11 解方程
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpressionType

    @ExpressionType.setter
    def ExpressionType(self, ExpressionType):
        self._ExpressionType = ExpressionType

    @property
    def ItemConf(self):
        r"""文本行置信度
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._ItemConf

    @ItemConf.setter
    def ItemConf(self, ItemConf):
        self._ItemConf = ItemConf

    @property
    def QuestionId(self):
        r"""用于标识题目 id，如果有若干算式属于同一 题，则其对应的 id 相同。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QuestionId

    @QuestionId.setter
    def QuestionId(self, QuestionId):
        self._QuestionId = QuestionId


    def _deserialize(self, params):
        self._Item = params.get("Item")
        self._ItemString = params.get("ItemString")
        if params.get("ItemCoord") is not None:
            self._ItemCoord = ItemCoord()
            self._ItemCoord._deserialize(params.get("ItemCoord"))
        self._Answer = params.get("Answer")
        self._ExpressionType = params.get("ExpressionType")
        self._ItemConf = params.get("ItemConf")
        self._QuestionId = params.get("QuestionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemCoord(AbstractModel):
    r"""目标算式在图片上的坐标信息

    """

    def __init__(self):
        r"""
        :param _Height: 算式高度
        :type Height: int
        :param _Width: 算式宽度
        :type Width: int
        :param _X: 算式图的左上角横坐标
        :type X: int
        :param _Y: 算式图的左上角纵坐标
        :type Y: int
        """
        self._Height = None
        self._Width = None
        self._X = None
        self._Y = None

    @property
    def Height(self):
        r"""算式高度
        :rtype: int
        """
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height

    @property
    def Width(self):
        r"""算式宽度
        :rtype: int
        """
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def X(self):
        r"""算式图的左上角横坐标
        :rtype: int
        """
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        r"""算式图的左上角纵坐标
        :rtype: int
        """
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y


    def _deserialize(self, params):
        self._Height = params.get("Height")
        self._Width = params.get("Width")
        self._X = params.get("X")
        self._Y = params.get("Y")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        