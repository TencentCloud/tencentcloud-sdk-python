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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.ocr.v20181119 import models


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.tencentcloudapi.com'


    def ArithmeticOCR(self, request):
        """本接口支持作业算式题目的自动识别，目前覆盖 K12 学力范围内的 14 种题型，包括加减乘除四则运算、分数四则运算、竖式四则运算、脱式计算等。

        :param request: Request instance for ArithmeticOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ArithmeticOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ArithmeticOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ArithmeticOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ArithmeticOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BankCardOCR(self, request):
        """本接口支持对中国大陆主流银行卡的卡号、银行信息、有效期等关键字段的检测与识别。

        :param request: Request instance for BankCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BankCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BankCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BankCardOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BizLicenseOCR(self, request):
        """本接口支持快速精准识别营业执照上的字段，包括注册号、公司名称、经营场所、主体类型、法定代表人、注册资金、组成形式、成立日期、营业期限和经营范围等字段。

        :param request: Request instance for BizLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BizLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BizLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BizLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BizLicenseOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BusInvoiceOCR(self, request):
        """本接口支持识别公路汽车客票的发票代码、发票号码、日期、姓名、票价等字段。

        :param request: Request instance for BusInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BusInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BusInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BusInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BusInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BusinessCardOCR(self, request):
        """本接口支持名片各字段的自动定位与识别，包含姓名、电话、手机号、邮箱、公司、部门、职位、网址、地址、QQ、微信、MSN等。

        :param request: Request instance for BusinessCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.BusinessCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.BusinessCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BusinessCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BusinessCardOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CarInvoiceOCR(self, request):
        """本接口支持机动车销售统一发票和二手车销售统一发票的识别，包括发票号码、发票代码、合计金额、合计税额等二十多个字段。

        :param request: Request instance for CarInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.CarInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.CarInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CarInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CarInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DriverLicenseOCR(self, request):
        """本接口支持驾驶证主页和副页所有字段的自动定位与识别，重点字段的识别准确度达到99%以上。

        驾驶证主页：包括证号、姓名、性别、国籍、住址、出生日期、初次领证日期、准驾车型、有效期限。

        驾驶证副页：包括证号、姓名、档案编号、记录。

        另外，本接口还支持复印件、翻拍和PS告警功能。

        :param request: Request instance for DriverLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.DriverLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.DriverLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DriverLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DriverLicenseOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DutyPaidProofOCR(self, request):
        """本接口支持对完税证明的税号、纳税人识别号、纳税人名称、金额合计大写、金额合计小写、填发日期、税务机关、填票人等关键字段的识别。

        :param request: Request instance for DutyPaidProofOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.DutyPaidProofOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.DutyPaidProofOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DutyPaidProofOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DutyPaidProofOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EduPaperOCR(self, request):
        """本接口支持数学试题内容的识别和结构化输出，包括通用文本解析和小学/初中/高中数学公式解析能力（包括91种题型，180种符号）。

        :param request: Request instance for EduPaperOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EduPaperOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EduPaperOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EduPaperOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EduPaperOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnglishOCR(self, request):
        """本接口支持图像英文文字的检测和识别，返回文字框位置与文字内容。支持多场景、任意版面下的英文、字母、数字和常见字符的识别，同时覆盖英文印刷体和英文手写体识别。

        :param request: Request instance for EnglishOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EnglishOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EnglishOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnglishOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnglishOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnterpriseLicenseOCR(self, request):
        """本接口支持智能化识别各类企业登记证书、许可证书、企业执照、三证合一类证书，结构化输出统一社会信用代码、公司名称、法定代表人、公司地址、注册资金、企业类型、经营范围等关键字段。

        :param request: Request instance for EnterpriseLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EnterpriseLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EnterpriseLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnterpriseLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnterpriseLicenseOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EstateCertOCR(self, request):
        """本接口支持不动产权证关键字段的识别，包括使用期限、面积、用途、权利性质、权利类型、坐落、共有情况、权利人、权利其他状况等。



        :param request: Request instance for EstateCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.EstateCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.EstateCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EstateCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EstateCertOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FinanBillOCR(self, request):
        """本接口支持常见银行票据的自动分类和识别。整单识别包括支票（含现金支票、普通支票、转账支票），承兑汇票（含银行承兑汇票、商业承兑汇票）以及进账单等，适用于中国人民银行印发的 2010 版银行票据凭证版式（银发[2010]299 号）。

        :param request: Request instance for FinanBillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FinanBillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FinanBillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FinanBillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FinanBillOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FinanBillSliceOCR(self, request):
        """本接口支持常见银行票据的自动分类和识别。切片识别包括金融行业常见票据的重要切片字段识别，包括金额、账号、日期、凭证号码等。（金融票据切片：金融票据中待识别字段及其周围局部区域的裁剪图像。）

        :param request: Request instance for FinanBillSliceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FinanBillSliceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FinanBillSliceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FinanBillSliceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FinanBillSliceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FlightInvoiceOCR(self, request):
        """本接口支持机票行程单关键字段的识别，包括姓名、身份证件号码、航班号、票价 、合计、电子客票号码、填开日期等。

        :param request: Request instance for FlightInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FlightInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FlightInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FlightInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FlightInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FormulaOCR(self, request):
        """本接口支持识别主流初高中数学符号和公式，返回公式的 Latex 格式文本。

        :param request: Request instance for FormulaOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.FormulaOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.FormulaOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("FormulaOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FormulaOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GeneralAccurateOCR(self, request):
        """本接口支持图像整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，高精度版在英文、数字、小字、模糊字、倾斜文本行等困难场景下，准确率和召回率更高。

        :param request: Request instance for GeneralAccurateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralAccurateOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralAccurateOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralAccurateOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GeneralBasicOCR(self, request):
        """本接口支持多场景、任意版面下整图文字的识别。支持自动识别语言类型，同时支持自选语言种类（推荐），除中英文外，支持日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语等多种语言。应用场景包括：印刷文档识别、网络图片识别、广告图文字识别、街景店招识别、菜单识别、视频标题识别、头像文字识别等。

        :param request: Request instance for GeneralBasicOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralBasicOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralBasicOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralBasicOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GeneralEfficientOCR(self, request):
        """本接口支持多场景、任意版面下整图文字的识别。相较于“通用印刷体识别”接口，精简版接口在准召率有一定损失的情况下，耗时更短。适用于对接口耗时较为敏感的客户。

        :param request: Request instance for GeneralEfficientOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralEfficientOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralEfficientOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralEfficientOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralEfficientOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GeneralFastOCR(self, request):
        """本接口支持图片中整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，识别速度更快、支持的 QPS 更高。

        :param request: Request instance for GeneralFastOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralFastOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralFastOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralFastOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralFastOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GeneralHandwritingOCR(self, request):
        """本接口支持图片内手写体文字的检测和识别，针对手写字体无规则、字迹潦草、模糊等特点进行了识别能力的增强。

        :param request: Request instance for GeneralHandwritingOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.GeneralHandwritingOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.GeneralHandwritingOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GeneralHandwritingOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GeneralHandwritingOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HmtResidentPermitOCR(self, request):
        """港澳台居住证OCR支持港澳台居住证正反面全字段内容检测识别功能，包括姓名、性别、出生日期、地址、身份证ID、签发机关、有效期限、签发次数、通行证号码关键字段识别。可以应用于港澳台居住证信息有效性校验场景，例如银行开户、用户注册等场景。

        :param request: Request instance for HmtResidentPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.HmtResidentPermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HmtResidentPermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HmtResidentPermitOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IDCardOCR(self, request):
        """本接口支持中国大陆居民二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限，识别准确度达到99%以上。

        另外，本接口还支持多种增值能力，满足不同场景的需求。如身份证照片、人像照片的裁剪功能，同时具备9种告警功能，如下表所示。

        <table style="width:650px">
              <thead>
                <tr>
               <th width="150">增值能力</th>
                  <th width="500">能力项</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td rowspan="2">裁剪功能</td>
                  <td>身份证照片裁剪（去掉证件外多余的边缘、自动矫正拍摄角度）</td>
                </tr>
                <tr>
                  <td>人像照片裁剪（自动抠取身份证头像区域）</td>
                </tr>
                <tr>
                  <td rowspan="9">告警功能</td>
                  <td>身份证有效日期不合法告警</td>
                </tr>
                <tr>
                  <td>身份证边框不完整告警</td>
                </tr>
                <tr>
                  <td>身份证复印件告警</td>
                </tr>
                <tr>
                  <td>身份证翻拍告警</td>
                </tr>
                  <tr>
                  <td>身份证框内遮挡告警</td>
                </tr>
                 <tr>
                  <td>临时身份证告警</td>
                </tr>
                  <tr>
                  <td>身份证 PS 告警</td>
                </tr>
                  <tr>
                  <td>图片模糊告警</td>
                </tr>
              </tbody>
            </table>

        :param request: Request instance for IDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.IDCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IDCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IDCardOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InstitutionOCR(self, request):
        """本接口支持事业单位法人证书关键字段识别，包括注册号、有效期、住所、名称、法定代表人等。

        :param request: Request instance for InstitutionOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InstitutionOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InstitutionOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InstitutionOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstitutionOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InsuranceBillOCR(self, request):
        """本接口支持病案首页、费用清单、结算单、医疗发票四种保险理赔单据的文本识别和结构化输出。

        :param request: Request instance for InsuranceBillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InsuranceBillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InsuranceBillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InsuranceBillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InsuranceBillOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InvoiceGeneralOCR(self, request):
        """本接口支持对通用机打发票的发票代码、发票号码、日期、购买方识别号、销售方识别号、校验码、小写金额等关键字段的识别。

        :param request: Request instance for InvoiceGeneralOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.InvoiceGeneralOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.InvoiceGeneralOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InvoiceGeneralOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvoiceGeneralOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LicensePlateOCR(self, request):
        """本接口支持对中国大陆机动车车牌的自动定位和识别，返回地域编号和车牌号信息。

        :param request: Request instance for LicensePlateOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.LicensePlateOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LicensePlateOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LicensePlateOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MLIDCardOCR(self, request):
        """本接口支持马来西亚身份证识别，识别字段包括身份证号、姓名、性别、地址；具备身份证人像照片的裁剪功能和翻拍、复印件告警功能。
        本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)

        :param request: Request instance for MLIDCardOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDCardOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MLIDCardOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MLIDCardOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MLIDPassportOCR(self, request):
        """本接口支持中国港澳台地区以及其他国家、地区的护照。识别字段包括护照ID、姓名、出生日期、性别、有效期、发行国、国籍；具备护照人像照片的裁剪功能和翻拍、复印件告警功能。
        本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)

        :param request: Request instance for MLIDPassportOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MLIDPassportOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MLIDPassportOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MLIDPassportOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MainlandPermitOCR(self, request):
        """智能识别并结构化港澳台居民来往内地通行证正面全部字段，包含中文姓名、英文姓名、性别、出生日期、签发机关、有效期限、证件号、签发地点、签发次数、证件类别。

        :param request: Request instance for MainlandPermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MainlandPermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MainlandPermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MainlandPermitOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MixedInvoiceDetect(self, request):
        """本接口支持多张、多类型票据的混合检测和自动分类，返回对应票据类型。目前已支持增值税发票、增值税发票（卷票）、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票、酒店账单、客运限额发票、购物小票、完税证明共15种票据。

        :param request: Request instance for MixedInvoiceDetect.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceDetectRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MixedInvoiceDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MixedInvoiceDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MixedInvoiceOCR(self, request):
        """本接口支持多张、多类型票据的混合识别，系统自动实现分割、分类和识别，同时支持自选需要识别的票据类型。目前已支持增值税发票、增值税发票（卷票）、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票共11种票据。

        :param request: Request instance for MixedInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.MixedInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MixedInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MixedInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OrgCodeCertOCR(self, request):
        """本接口支持组织机构代码证关键字段的识别，包括代码、有效期、地址、机构名称等。

        :param request: Request instance for OrgCodeCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.OrgCodeCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.OrgCodeCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OrgCodeCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OrgCodeCertOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PassportOCR(self, request):
        """本接口支持中国大陆地区护照个人资料页多个字段的检测与识别。已支持字段包括英文姓名、中文姓名、国家码、护照号、出生地、出生日期、国籍英文、性别英文、有效期、签发地点英文、签发日期、持证人签名、护照机读码（MRZ码）等。

        :param request: Request instance for PassportOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PassportOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PassportOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PassportOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PassportOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PermitOCR(self, request):
        """本接口支持对卡式港澳台通行证的识别，包括签发地点、签发机关、有效期限、性别、出生日期、英文姓名、姓名、证件号等字段。

        :param request: Request instance for PermitOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PermitOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PermitOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PermitOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PermitOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PropOwnerCertOCR(self, request):
        """本接口支持房产证关键字段的识别，包括房地产权利人、共有情况、登记时间、规划用途、房屋性质、房屋坐落等。

        :param request: Request instance for PropOwnerCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.PropOwnerCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.PropOwnerCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PropOwnerCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PropOwnerCertOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QrcodeOCR(self, request):
        """本接口支持条形码和二维码的识别（包括 DataMatrix 和 PDF417）。
        本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)

        :param request: Request instance for QrcodeOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.QrcodeOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.QrcodeOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QrcodeOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QrcodeOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QuotaInvoiceOCR(self, request):
        """本接口支持定额发票的发票号码、发票代码、金额(大小写)、发票消费类型、地区及是否有公司印章等关键字段的识别。

        :param request: Request instance for QuotaInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.QuotaInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QuotaInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QuotaInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResidenceBookletOCR(self, request):
        """本接口支持居民户口簿户主页及成员页关键字段的识别，包括姓名、户别、地址、籍贯、身份证号码等。

        :param request: Request instance for ResidenceBookletOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ResidenceBookletOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ResidenceBookletOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResidenceBookletOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResidenceBookletOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ShipInvoiceOCR(self, request):
        """本接口支持识别轮船票的发票代码、发票号码、日期、姓名、票价等字段。

        :param request: Request instance for ShipInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.ShipInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.ShipInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShipInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShipInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TableOCR(self, request):
        """本接口支持图片内表格文档的检测和识别，返回每个单元格的文字内容，支持将识别结果保存为 Excel 格式。

        :param request: Request instance for TableOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TableOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TableOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TableOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TableOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TaxiInvoiceOCR(self, request):
        """本接口支持出租车发票关键字段的识别，包括发票号码、发票代码、金额、日期、上下车时间、里程、车牌号、发票类型及所属地区等字段。

        :param request: Request instance for TaxiInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TaxiInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TaxiInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TaxiInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TaxiInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TextDetect(self, request):
        """本接口通过检测图片中的文字信息特征，快速判断图片中有无文字并返回判断结果，帮助用户过滤无文字的图片。

        :param request: Request instance for TextDetect.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TextDetectRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TextDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TollInvoiceOCR(self, request):
        """本接口支持对过路过桥费发票的发票代码、发票号码、日期、小写金额等关键字段的识别。

        :param request: Request instance for TollInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TollInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TollInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TollInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TollInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TrainTicketOCR(self, request):
        """本接口支持火车票全字段的识别，包括编号、票价、姓名、座位号、出发时间、出发站、到达站、车次、席别、发票类型及序列号等。

        :param request: Request instance for TrainTicketOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.TrainTicketOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.TrainTicketOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TrainTicketOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TrainTicketOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VatInvoiceOCR(self, request):
        """本接口支持增值税专用发票、增值税普通发票、增值税电子发票全字段的内容检测和识别，包括发票代码、发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方识别号、复核、销售方识别号、开票人、密码区1、密码区2、密码区3、密码区4、发票名称、购买方名称、销售方名称、服务名称、备注、规格型号、数量、单价、金额、税额、收款人等字段。

        :param request: Request instance for VatInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VatInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VatInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VatInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VatRollInvoiceOCR(self, request):
        """本接口支持对增值税发票（卷票）的发票代码、发票号码、日期、校验码、合计金额（小写）等关键字段的识别。

        :param request: Request instance for VatRollInvoiceOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VatRollInvoiceOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VatRollInvoiceOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VatRollInvoiceOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VatRollInvoiceOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VehicleLicenseOCR(self, request):
        """本接口支持行驶证主页和副页所有字段的自动定位与识别。

        行驶证主页：车牌号码、车辆类型、所有人、住址、使用性质、品牌型号、识别代码、发动机号、注册日期、发证日期、发证单位。

        行驶证副页：号牌号码、档案编号、核定载人数、总质量、整备质量、核定载质量、外廓尺寸、准牵引总质量、备注、检验记录。

        另外，本接口还支持复印件、翻拍和PS告警功能。

        :param request: Request instance for VehicleLicenseOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VehicleLicenseOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VehicleLicenseOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VehicleLicenseOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VehicleLicenseOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VehicleRegCertOCR(self, request):
        """本接口支持国内机动车登记证书主要字段的结构化识别，包括机动车所有人、身份证明名称、号码、车辆型号、车辆识别代号、发动机号、制造厂名称等。

        :param request: Request instance for VehicleRegCertOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VehicleRegCertOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VehicleRegCertOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VehicleRegCertOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VehicleRegCertOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VinOCR(self, request):
        """本接口支持图片内车辆识别代号（VIN）的检测和识别。

        :param request: Request instance for VinOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.VinOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.VinOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VinOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VinOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WaybillOCR(self, request):
        """本接口支持市面上主流版式电子运单的识别，包括收件人和寄件人的姓名、电话、地址以及运单号等字段。

        :param request: Request instance for WaybillOCR.
        :type request: :class:`tencentcloud.ocr.v20181119.models.WaybillOCRRequest`
        :rtype: :class:`tencentcloud.ocr.v20181119.models.WaybillOCRResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WaybillOCR", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WaybillOCRResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)