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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ocr.v20181119 import models
from typing import Dict


class OcrClient(AbstractClient):
    _apiVersion = '2018-11-19'
    _endpoint = 'ocr.tencentcloudapi.com'
    _service = 'ocr'

    async def AdvertiseOCR(
            self,
            request: models.AdvertiseOCRRequest,
            opts: Dict = None,
    ) -> models.AdvertiseOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/33526">通用印刷体识别</a>。</b>

        支持广告商品图片内文字的检测和识别，返回文本框位置与文字内容。支持中英文、横排、竖排以及倾斜场景文字识别，支持90度、180度、270度翻转以及倾斜场景文字识别，具有较高召回率和准确率。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "AdvertiseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdvertiseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ArithmeticOCR(
            self,
            request: models.ArithmeticOCRRequest,
            opts: Dict = None,
    ) -> models.ArithmeticOCRResponse:
        """
        本接口支持作业算式题目的自动识别和判分，目前覆盖 K12 学力范围内的 11 种题型，包括加减乘除四则、加减乘除已知结果求运算因子、判断大小、约等于估算、带余数除法、分数四则运算、单位换算、竖式加减法、竖式乘除法、脱式计算和解方程，平均识别精度达到93%以上。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ArithmeticOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ArithmeticOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankCardOCR(
            self,
            request: models.BankCardOCRRequest,
            opts: Dict = None,
    ) -> models.BankCardOCRResponse:
        """
        本接口支持对中国大陆主流银行卡正反面关键字段的检测与识别，包括卡号、卡类型、卡名字、银行信息、有效期。支持竖排异形卡识别、多角度旋转图片识别。支持对复印件、翻拍件、边框遮挡的银行卡进行告警，可应用于各种银行卡信息有效性校验场景，如金融行业身份认证、第三方支付绑卡等场景。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "BankCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BankSlipOCR(
            self,
            request: models.BankSlipOCRRequest,
            opts: Dict = None,
    ) -> models.BankSlipOCRResponse:
        """
        本接口支持银行回单全字段的识别，包括付款开户行、收款开户行、付款账号、收款账号、回单类型、回单编号、币种、流水号、凭证号码、交易机构、交易金额、手续费、日期等字段信息。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "BankSlipOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BankSlipOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BizLicenseOCR(
            self,
            request: models.BizLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.BizLicenseOCRResponse:
        """
        本接口支持快速精准识别营业执照上的字段，包括统一社会信用代码、公司名称、主体类型、法定代表人、注册资本、组成形式、成立日期、营业期限和经营范围等字段。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "BizLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BizLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BusInvoiceOCR(
            self,
            request: models.BusInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.BusInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持识别公路汽车客票关键字段的识别，包括发票代码、发票号码、日期、票价、始发地、目的地、姓名、时间、发票消费类型、身份证号、省、市、开票日期、乘车地点、检票口、客票类型、车型、座位号、车次等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "BusInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BusInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BusinessCardOCR(
            self,
            request: models.BusinessCardOCRRequest,
            opts: Dict = None,
    ) -> models.BusinessCardOCRResponse:
        """
        本接口支持中英文名片各字段的自动定位与识别，包含姓名、电话、手机号、邮箱、公司、部门、职位、网址、地址、QQ、微信、MSN等。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "BusinessCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BusinessCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CarInvoiceOCR(
            self,
            request: models.CarInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.CarInvoiceOCRResponse:
        """
        本接口支持机动车销售统一发票和二手车销售统一发票的识别，包括发票号码、发票代码、合计金额、合计税额等二十多个字段。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "CarInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CarInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClassifyDetectOCR(
            self,
            request: models.ClassifyDetectOCRRequest,
            opts: Dict = None,
    ) -> models.ClassifyDetectOCRResponse:
        """
        支持身份证、护照、名片、银行卡、行驶证、驾驶证、港澳台通行证、户口本、港澳台来往内地通行证、港澳台居住证、不动产证、营业执照的智能分类。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ClassifyDetectOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClassifyDetectOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClassifyStoreName(
            self,
            request: models.ClassifyStoreNameRequest,
            opts: Dict = None,
    ) -> models.ClassifyStoreNameResponse:
        """
        本接口用于识别门头照分类标签信息
        默认接口请求频率限制：1次/秒
        """
        
        kwargs = {}
        kwargs["action"] = "ClassifyStoreName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClassifyStoreNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExtractDocAgentJob(
            self,
            request: models.DescribeExtractDocAgentJobRequest,
            opts: Dict = None,
    ) -> models.DescribeExtractDocAgentJobResponse:
        """
        用于查询文档处理任务。文档处理领域里常见的通用Agent 如抽取、比对之类的，目前我们提供的抽取，但未来可以根据实际情况和客户需求扩展。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExtractDocAgentJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExtractDocAgentJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DriverLicenseOCR(
            self,
            request: models.DriverLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.DriverLicenseOCRResponse:
        """
        本接口支持驾驶证主页和副页所有字段的自动定位与识别，重点字段的识别准确度达到99%以上。

        驾驶证主页：包括证号、姓名、性别、国籍、住址、出生日期、初次领证日期、准驾车型、有效期限、发证单位

        驾驶证副页：包括证号、姓名、档案编号、记录。

        另外，本接口还支持复印件、翻拍告警功能。同时支持识别交管12123 APP发放的电子驾驶证正页。

        电子驾驶证正页：包括证号、姓名、性别、国籍、出生日期、初次领证日期、准驾车型、有效期开始时间、有效期截止时间、档案编号、状态、累积记分。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "DriverLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DriverLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DutyPaidProofOCR(
            self,
            request: models.DutyPaidProofOCRRequest,
            opts: Dict = None,
    ) -> models.DutyPaidProofOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持对完税证明的税号、纳税人识别号、纳税人名称、金额合计大写、金额合计小写、填发日期、税务机关、填票人等关键字段的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "DutyPaidProofOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DutyPaidProofOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EduPaperOCR(
            self,
            request: models.EduPaperOCRRequest,
            opts: Dict = None,
    ) -> models.EduPaperOCRResponse:
        """
        本接口支持数学试题内容的识别和结构化输出，包括通用文本解析和小学/初中/高中数学公式解析能力（包括91种题型，180种符号），公式返回格式为 Latex 格式文本。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "EduPaperOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EduPaperOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnglishOCR(
            self,
            request: models.EnglishOCRRequest,
            opts: Dict = None,
    ) -> models.EnglishOCRResponse:
        """
        本接口支持图像英文文字的检测和识别，返回文字框位置与文字内容。支持多场景、任意版面下的英文、字母、数字和常见字符的识别，同时覆盖英文印刷体和英文手写体识别。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "EnglishOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnglishOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnterpriseLicenseOCR(
            self,
            request: models.EnterpriseLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.EnterpriseLicenseOCRResponse:
        """
        本接口支持智能化识别各类企业登记证书、许可证书、企业执照、三证合一类证书，结构化输出统一社会信用代码、公司名称、法定代表人、公司地址、注册资金、企业类型、经营范围、成立日期、有效期、开办资金、经费来源、举办单位等关键字段。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "EnterpriseLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnterpriseLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EstateCertOCR(
            self,
            request: models.EstateCertOCRRequest,
            opts: Dict = None,
    ) -> models.EstateCertOCRResponse:
        """
        本接口支持不动产权证关键字段的识别，包括使用期限、面积、用途、权利性质、权利类型、坐落、共有情况、权利人、权利其他状况等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "EstateCertOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EstateCertOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractDocAgent(
            self,
            request: models.ExtractDocAgentRequest,
            opts: Dict = None,
    ) -> models.ExtractDocAgentResponse:
        """
        用于查询文档处理任务。文档处理领域里常见的通用Agent 如抽取、比对之类的，目前我们提供的抽取，但未来可以根据实际情况和客户需求扩展。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractDocAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractDocAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractDocBasic(
            self,
            request: models.ExtractDocBasicRequest,
            opts: Dict = None,
    ) -> models.ExtractDocBasicResponse:
        """
        本接口支持识别并提取制式卡证、票据、表单等结构化场景的字段信息。无需任何配置，灵活高效。适用于各类结构化信息录入场景。点击[立即体验](https://ocrdemo.cloud.tencent.com/?action=ExtractDocBasic)。

        接口别名：SmartStructuralOCRV2

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractDocBasic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractDocBasicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractDocMulti(
            self,
            request: models.ExtractDocMultiRequest,
            opts: Dict = None,
    ) -> models.ExtractDocMultiResponse:
        """
        本接口支持识别并提取场景复杂、版式多等结构化场景的字段信息。重点场景包括：金融、医疗、交通、出行、保险。点击[立即体验](https://ocrdemo.cloud.tencent.com/?action=ExtractDocMulti)。

        接口别名：SmartStructuralPro

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractDocMulti"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractDocMultiResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExtractDocMultiPro(
            self,
            request: models.ExtractDocMultiProRequest,
            opts: Dict = None,
    ) -> models.ExtractDocMultiProResponse:
        """
        本接口当前仅支持复杂磅单收发货单抽取，更多强推理场景支持定制咨询。点击[立即体验](https://ocrdemo.cloud.tencent.com/?action=ExtractDocMultiPro)。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ExtractDocMultiPro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExtractDocMultiProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FinanBillOCR(
            self,
            request: models.FinanBillOCRRequest,
            opts: Dict = None,
    ) -> models.FinanBillOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持常见银行票据的自动分类和识别。整单识别包括支票（含现金支票、普通支票、转账支票），承兑汇票（含银行承兑汇票、商业承兑汇票）以及进账单等，适用于中国人民银行印发的 2010 版银行票据凭证版式（银发[2010]299 号）。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "FinanBillOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FinanBillOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FinanBillSliceOCR(
            self,
            request: models.FinanBillSliceOCRRequest,
            opts: Dict = None,
    ) -> models.FinanBillSliceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持常见银行票据的自动分类和识别。切片识别包括金融行业常见票据的重要切片字段识别，包括金额、账号、日期、凭证号码等。（金融票据切片：金融票据中待识别字段及其周围局部区域的裁剪图像。）

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "FinanBillSliceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FinanBillSliceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FlightInvoiceOCR(
            self,
            request: models.FlightInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.FlightInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持机票行程单关键字段的识别，包括旅客姓名、有效身份证件号码、电子客票号码、验证码、填开单位、其他税费、燃油附加费、民航发展基金、保险费、销售单位代号、始发地、目的地、航班号、时间、日期、座位等级、承运人、发票消费类型、票价、合计金额、填开日期、国内国际标签、印刷序号、客票级别/类别、客票生效日期、有效期截止日期、免费行李等字段，支持航班信息多行明细输出。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "FlightInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FlightInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FormulaOCR(
            self,
            request: models.FormulaOCRRequest,
            opts: Dict = None,
    ) -> models.FormulaOCRResponse:
        """
        本接口支持识别主流初高中数学符号和公式，返回公式的 Latex 格式文本。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "FormulaOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FormulaOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralAccurateOCR(
            self,
            request: models.GeneralAccurateOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralAccurateOCRResponse:
        """
        本接口支持图像整体文字的检测和识别。支持中文、英文、中英文、数字和特殊字符号的识别，并返回文字框位置和文字内容。

        适用于文字较多、版式复杂、对识别准召率要求较高的场景，如试卷试题、网络图片、街景店招牌、法律卷宗等场景。

        产品优势：与通用印刷体识别接口相比，本接口提供更高精度的通用文字识别服务，在手写体、文字较多、长串数字、小字、模糊字、倾斜文本等困难场景下，高精度版的准确率和召回率更高。

        通用文字识别不同版本的差异如下：
        <table style="width:715px">
              <thead>
                <tr>
                  <th style="width:150px"></th>
                  <th >【荐】通用文字识别（高精度版）</th>
                  <th style="width:300px"><a href="https://cloud.tencent.com/document/product/866/33526">【荐】通用印刷体识别</a></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 适用场景</td>
                  <td>适用于文字较多、长串数字、小字、模糊字、倾斜文本等困难场景</td>
                  <td>适用于所有通用场景的印刷体识别</td>
                </tr>
                <tr>
                  <td>识别准确率</td>
                  <td>99%</td>
                  <td>96%</td>
                </tr>
                <tr>
                  <td>价格</td>
                  <td>中</td>
                  <td>低</td>
                </tr>
                <tr>
                  <td>支持的语言</td>
                  <td>中文、英文、中英文、泰语、印尼语、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、哈萨克语、阿拉伯语、维吾尔语、藏语、捷克语、希腊语、西班牙语（智利）、西班牙语（墨西哥）、希伯来语、克罗地亚语、波兰语、葡萄牙语（巴西）、罗马尼亚语、斯洛伐克语、斯洛文尼亚语、土耳其语、保加利亚语、爱沙尼亚语、拉脱维亚语、立陶宛语</td>
                  <td>中文、英文、中英文、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语</td>
                </tr>
                <tr>
                  <td>自动语言检测</td>
                  <td>中英文支持;其他语言需要调整输入参数</td>
                  <td>支持</td>
                </tr>
                <tr>
                  <td>返回文本行坐标</td>
                  <td>支持</td>
                  <td>支持</td>
                </tr>
                <tr>
                  <td>自动旋转纠正</td>
                  <td>支持旋转识别，返回角度信息</td>
                  <td>支持旋转识别，返回角度信息</td>
                </tr>
              </tbody>
            </table>

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralAccurateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralAccurateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralBasicOCR(
            self,
            request: models.GeneralBasicOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralBasicOCRResponse:
        """
        本接口支持图像整体文字的检测和识别。可以识别中文、英文、中英文、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语，阿拉伯语20种语言，且各种语言均支持与英文混合的文字识别。

        适用于印刷文档识别、网络图片识别、广告图文字识别、街景店招牌识别、菜单识别、视频标题识别、头像文字识别等场景。

        产品优势：支持自动识别语言类型，可返回文本框坐标信息，对于倾斜文本支持自动旋转纠正。

        通用印刷体识别不同版本的差异如下：
        <table style="width:715px">
              <thead>
                <tr>
                  <th style="width:150px"></th>
                  <th style="width:250px">【荐】通用印刷体识别</th>
                  <th ><a href="https://cloud.tencent.com/document/product/866/34937">【荐】通用印刷体识别（高精度版）</a></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 适用场景</td>
                  <td>适用于所有通用场景的印刷体识别</td>
                  <td>适用于文字较多、长串数字、小字、模糊字、倾斜文本等困难场景</td>
                </tr>
                <tr>
                  <td>识别准确率</td>
                  <td>96%</td>
                  <td>99%</td>
                </tr>
                <tr>
                  <td>价格</td>
                  <td>低</td>
                  <td>中</td>
                </tr>
                <tr>
                  <td>支持的语言</td>
                  <td>中文、英文、中英文、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语</td>
                  <td>中文、英文、中英文、泰语、印尼语、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、哈萨克语</td>
                </tr>
                <tr>
                  <td>自动语言检测</td>
                  <td>支持</td>
                  <td>中英文支持；其他语种需要调整输入参数</td>
                </tr>
                <tr>
                  <td>返回文本行坐标</td>
                  <td>支持</td>
                  <td>支持</td>
                </tr>
                <tr>
                  <td>自动旋转纠正</td>
                  <td>支持旋转识别，返回角度信息</td>
                  <td>支持旋转识别，返回角度信息</td>
                </tr>
              </tbody>
            </table>

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralBasicOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralBasicOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralEfficientOCR(
            self,
            request: models.GeneralEfficientOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralEfficientOCRResponse:
        """
        本接口支持图像整体文字的检测和识别。支持中文、英文、中英文、数字和特殊字符号的识别，并返回文字框位置和文字内容。

        适用于快速文本识别场景。

        产品优势：与通用印刷体识别接口相比，精简版虽然在准确率和召回率上有一定损失，但价格更加优惠。

        通用印刷体识别不同版本的差异如下：
        <table style="width:715px">
              <thead>
                <tr>
                  <th style="width:150px"></th>
                  <th >通用印刷体识别（精简版）</th>
                  <th style="width:200px"><a href="https://cloud.tencent.com/document/product/866/33526">【荐】通用印刷体识别</a></th>
                  <th><a href="https://cloud.tencent.com/document/product/866/34937">【荐】通用印刷体识别（高精度版）</a></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> 适用场景</td>
                  <td>适用于快速文本识别场景，准召率有一定损失，价格更优惠</td>
                  <td>适用于所有通用场景的印刷体识别</td>
                  <td>适用于文字较多、长串数字、小字、模糊字、倾斜文本等困难场景</td>
                </tr>
                <tr>
                  <td>识别准确率</td>
                  <td>91%</td>
                  <td>96%</td>
                  <td>99%</td>
                </tr>
                <tr>
                  <td>价格</td>
                  <td>低</td>
                  <td>中</td>
                  <td>高</td>
                </tr>
                <tr>
                  <td>支持的语言</td>
                  <td>中文、英文、中英文</td>
                  <td>中文、英文、中英文、日语、韩语、西班牙语、法语、德语、葡萄牙语、越南语、马来语、俄语、意大利语、荷兰语、瑞典语、芬兰语、丹麦语、挪威语、匈牙利语、泰语</td>
                  <td>中文、英文、中英文</td>
                </tr>
                <tr>
                  <td>自动语言检测</td>
                  <td>支持</td>
                  <td>支持</td>
                  <td>支持</td>
                </tr>
                <tr>
                  <td>返回文本行坐标</td>
                  <td>支持</td>
                  <td>支持</td>
                  <td>支持</td>
                </tr>
                <tr>
                  <td>自动旋转纠正</td>
                  <td>支持旋转识别，返回角度信息</td>
                  <td>支持旋转识别，返回角度信息</td>
                  <td>支持旋转识别，返回角度信息</td>
                </tr>
              </tbody>
            </table>

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralEfficientOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralEfficientOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralFastOCR(
            self,
            request: models.GeneralFastOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralFastOCRResponse:
        """
        本接口支持图片中整体文字的检测和识别，返回文字框位置与文字内容。相比通用印刷体识别接口，识别速度更快。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralFastOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralFastOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GeneralHandwritingOCR(
            self,
            request: models.GeneralHandwritingOCRRequest,
            opts: Dict = None,
    ) -> models.GeneralHandwritingOCRResponse:
        """
        <b>此接口为通用手写体识别的旧版本服务，不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/34937">通用印刷体识别(高精度)识别服务</a>。</b>

        本接口支持图片内手写体文字的检测和识别，针对手写字体无规则、字迹潦草、模糊等特点进行了识别能力的增强。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "GeneralHandwritingOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GeneralHandwritingOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOCRResult(
            self,
            request: models.GetOCRResultRequest,
            opts: Dict = None,
    ) -> models.GetOCRResultResponse:
        """
        获取ocr结果
        """
        
        kwargs = {}
        kwargs["action"] = "GetOCRResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOCRResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOCRToken(
            self,
            request: models.GetOCRTokenRequest,
            opts: Dict = None,
    ) -> models.GetOCRTokenResponse:
        """
        获取ocr的token值
        """
        
        kwargs = {}
        kwargs["action"] = "GetOCRToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOCRTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HKIDCardOCR(
            self,
            request: models.HKIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.HKIDCardOCRResponse:
        """
        本接口支持中国香港身份证人像面中关键字段的识别，包括中文姓名、英文姓名、姓名电码、出生日期、性别、证件符号、首次签发日期、最近领用日期、身份证号、是否是永久性居民身份证；具备人像照片裁剪等扩展功能。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "HKIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HKIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HandwritingEssayOCR(
            self,
            request: models.HandwritingEssayOCRRequest,
            opts: Dict = None,
    ) -> models.HandwritingEssayOCRResponse:
        """
        本接口专为教育场景设计，可高精度识别中英文手写字符，智能分栏并按阅读顺序分割内容，自动过滤手写与印刷体混排干扰，精准返回词、行、段落及标题的文本与坐标信息。点击[立即体验](https://ocrdemo.cloud.tencent.com/)。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "HandwritingEssayOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HandwritingEssayOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HmtResidentPermitOCR(
            self,
            request: models.HmtResidentPermitOCRRequest,
            opts: Dict = None,
    ) -> models.HmtResidentPermitOCRResponse:
        """
        港澳台居住证OCR支持港澳台居住证正反面全字段内容检测识别功能，包括姓名、性别、出生日期、地址、身份证号、签发机关、有效期限、签发次数、通行证号码关键字段识别。可以应用于港澳台居住证信息识别场景，例如银行开户、用户注册等。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "HmtResidentPermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HmtResidentPermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IDCardOCR(
            self,
            request: models.IDCardOCRRequest,
            opts: Dict = None,
    ) -> models.IDCardOCRResponse:
        """
        本接口支持中国大陆居民二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限，识别准确度达到99%以上。

        另外，本接口还支持多种扩展能力，满足不同场景的需求。如身份证照片、人像照片的裁剪功能，同时具备7种告警功能，如下表所示。

        <table style="width:650px">
              <thead>
                <tr>
               <th width="150">扩展能力</th>
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
                  <td>身份证疑似存在PS痕迹告警</td>
                </tr>
                  <tr>
                  <td>图片模糊告警（可根据图片质量分数判断）</td>
                </tr>
              </tbody>
            </table>

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "IDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageEnhancement(
            self,
            request: models.ImageEnhancementRequest,
            opts: Dict = None,
    ) -> models.ImageEnhancementResponse:
        """
        文本图像增强是面向文档类图片提供的图像增强处理能力，包括切边增强、图像矫正、阴影去除、摩尔纹去除等；可以有效优化文档类的图片质量，提升文字的清晰度。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageEnhancement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageEnhancementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InsuranceBillOCR(
            self,
            request: models.InsuranceBillOCRRequest,
            opts: Dict = None,
    ) -> models.InsuranceBillOCRResponse:
        """
        本接口支持病案首页、费用清单、结算单、医疗发票四种保险理赔单据的文本识别和结构化输出。

        默认接口请求频率限制：1次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "InsuranceBillOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InsuranceBillOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InvoiceGeneralOCR(
            self,
            request: models.InvoiceGeneralOCRRequest,
            opts: Dict = None,
    ) -> models.InvoiceGeneralOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持对通用机打发票的发票代码、发票号码、日期、合计金额(小写)、合计金额(大写)、购买方识别号、销售方识别号、校验码、购买方名称、销售方名称、时间、种类、发票消费类型、省、市、是否有公司印章、发票名称、购买方地址、电话、销售方地址、电话、购买方开户行及账号、销售方开户行及账号、经办人取票用户、经办人支付信息、经办人商户号、经办人订单号、货物或应税劳务、服务名称、数量、单价、税率、税额、金额、单位、规格型号、合计税额、合计金额、备注、收款人、复核、开票人、密码区、行业分类等字段的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "InvoiceGeneralOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InvoiceGeneralOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LicensePlateOCR(
            self,
            request: models.LicensePlateOCRRequest,
            opts: Dict = None,
    ) -> models.LicensePlateOCRResponse:
        """
        本接口支持对中国大陆机动车车牌的自动定位和识别，返回地域编号和车牌号码与车牌颜色信息。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "LicensePlateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LicensePlateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MLIDCardOCR(
            self,
            request: models.MLIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.MLIDCardOCRResponse:
        """
        本接口支持马来西亚身份证识别，识别字段包括身份证号、姓名、性别、地址；具备身份证人像照片的裁剪功能和翻拍、复印件告警功能。
        本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)
        """
        
        kwargs = {}
        kwargs["action"] = "MLIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MLIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MLIDPassportOCR(
            self,
            request: models.MLIDPassportOCRRequest,
            opts: Dict = None,
    ) -> models.MLIDPassportOCRResponse:
        """
        本接口支持中国大陆地区及中国港澳台地区、其他国家以及地区的护照识别。识别字段包括护照ID、姓名、出生日期、性别、有效期、发行国、国籍、国家地区代码，具备护照人像照片的裁剪功能和翻拍、复印件告警功能。
        本接口支持地区范围：可机读护照国家。包括中国大陆地区、中国港澳台地区、新加坡、马来西亚、泰国、美国、韩国、越南、澳大利亚、缅甸、印度尼西亚、日本、加拿大、老挝、巴基斯坦、哈萨克斯坦、法国、英国、德国、菲律宾、新西兰、印度、意大利、蒙古、孟加拉国、尼日利亚、柬埔寨、西班牙、摩洛哥、吉尔吉斯斯坦、埃及、荷兰、塔吉克斯坦、巴西、乌兹别克斯坦、伊拉克、阿尔及利亚、土耳其、南非、墨西哥、尼泊尔、白俄罗斯、叶门、阿富汗、沙特、肯尼亚、波兰、比利时、瑞典、奥地利、坦桑尼亚、委内瑞拉、阿根廷、喀麦隆、斯里兰卡、衣索比亚、约旦、瑞士、加纳、爱尔兰、哥伦比亚、苏丹、匈牙利、罗马尼亚、阿联酋、文莱、希腊、以色列、巴拿马、丹麦、伊朗、乌干达、挪威、秘鲁、葡萄牙、智利、塞尔维亚、芬兰、尚比亚、亚美尼亚、叙利亚、黎巴嫩、斯洛伐克、卡塔尔、古巴、朝鲜。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "MLIDPassportOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MLIDPassportOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MainlandPermitOCR(
            self,
            request: models.MainlandPermitOCRRequest,
            opts: Dict = None,
    ) -> models.MainlandPermitOCRResponse:
        """
        智能识别并结构化港澳台通行证及来往内地通行证正面全部字段，包含中文姓名、英文姓名、性别、出生日期、签发机关、有效期限、证件号、签发地点、签发次数、证件类别。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "MainlandPermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MainlandPermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MixedInvoiceDetect(
            self,
            request: models.MixedInvoiceDetectRequest,
            opts: Dict = None,
    ) -> models.MixedInvoiceDetectResponse:
        """
        本接口支持多张、多类型票据的混合检测和自动分类，返回对应票据类型。目前已支持增值税发票、增值税发票（卷票）、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票、酒店账单、客运限额发票、购物小票、完税证明共15种票据。
        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "MixedInvoiceDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MixedInvoiceDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MixedInvoiceOCR(
            self,
            request: models.MixedInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.MixedInvoiceOCRResponse:
        """
        本接口支持 单张、多张、多类型 票据的混合识别，同时支持自选需要识别的票据类型，已支持票种包括：增值税发票（专票、普票、卷票）、全电发票、非税发票、定额发票、通用机打发票、购车发票、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票共14种标准报销发票，并支持其他类发票的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "MixedInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MixedInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PassportOCR(
            self,
            request: models.PassportOCRRequest,
            opts: Dict = None,
    ) -> models.PassportOCRResponse:
        """
        <b>此接口为护照识别（中国大陆地区护照）的旧版本服务，不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/37657">护照识别（多国多地区护照）</a>。</b>

        本接口支持中国大陆地区护照个人资料页多个字段的检测与识别。已支持字段包括英文姓名、中文姓名、国家码、护照号、出生地、出生日期、国籍英文、性别英文、有效期、签发地点英文、签发日期、持证人签名、护照机读码（MRZ码）等。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "PassportOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PassportOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PermitOCR(
            self,
            request: models.PermitOCRRequest,
            opts: Dict = None,
    ) -> models.PermitOCRResponse:
        """
        本接口支持对卡式港澳台通行证的识别，包括签发地点、签发机关、有效期限、性别、出生日期、英文姓名、姓名、证件号等字段。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "PermitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PermitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QrcodeOCR(
            self,
            request: models.QrcodeOCRRequest,
            opts: Dict = None,
    ) -> models.QrcodeOCRResponse:
        """
        本接口支持条形码和二维码的识别（包括 DataMatrix 和 PDF417）。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "QrcodeOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QrcodeOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuestionOCR(
            self,
            request: models.QuestionOCRRequest,
            opts: Dict = None,
    ) -> models.QuestionOCRResponse:
        """
        题目识别是教育的基础OCR识别能力。可支持扫描、拍照场景的单题题目识别。接口支持印刷体文本、手写体文本及公式的OCR识别和坐标返回，此外，接口还可对题目中的配图位置进行检测并返回坐标位置。适用于智能批改等场景的题目内容识别作为检索输入。

        默认接口请求频率限制：2次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "QuestionOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuestionOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuestionSplitLayoutOCR(
            self,
            request: models.QuestionSplitLayoutOCRRequest,
            opts: Dict = None,
    ) -> models.QuestionSplitLayoutOCRResponse:
        """
        试卷切题（仅检测）可将整页练习册、试卷或教辅中的题目进行自动切题，返回试题边框和题目元素的坐标位置。

        默认接口请求频率限制：2次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "QuestionSplitLayoutOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuestionSplitLayoutOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuestionSplitOCR(
            self,
            request: models.QuestionSplitOCRRequest,
            opts: Dict = None,
    ) -> models.QuestionSplitOCRResponse:
        """
        试卷切题识别可将整页练习册、试卷或教辅中的题目进行自动切题，并识别出其中的文字内容和坐标位置。

        默认接口请求频率限制：2次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "QuestionSplitOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuestionSplitOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QuotaInvoiceOCR(
            self,
            request: models.QuotaInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.QuotaInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持定额发票的发票号码、发票代码、金额(大小写)、发票消费类型、地区及是否有公司印章等关键字段的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "QuotaInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QuotaInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeContainerOCR(
            self,
            request: models.RecognizeContainerOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeContainerOCRResponse:
        """
        本接口支持集装箱箱门信息识别，识别字段包括集装箱箱号、类型、总重量、有效承重、容量、自身重量，具备集装箱箱号、类型不完整或者不清晰的告警功能。
        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeContainerOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeContainerOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeEncryptedIDCardOCR(
            self,
            request: models.RecognizeEncryptedIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeEncryptedIDCardOCRResponse:
        """
        身份证识别（安全加密版）接口实现了数据加密传输，能够有效防止个人身份证隐私信息不被窃取泄露。

        本接口支持中国大陆居民二代身份证正反面所有字段的识别，包括姓名、性别、民族、出生日期、住址、公民身份证号、签发机关、有效期限，识别速度快、准确度高。

        另外，本接口还支持多种扩展能力，满足不同场景的需求。如身份证照片、人像照片的裁剪功能，同时具备9种告警功能，如下表所示。

        <table style="width:650px">
              <thead>
                <tr>
               <th width="150">扩展能力</th>
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
                  <td>身份证有效日期不合法，即有效日期不符合5年、10年、20年、长期期限

        </td>
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
                  <td>身份证疑似存在PS痕迹告警</td>
                </tr>
                  <tr>
                  <td>图片模糊告警（可根据图片质量分数判断）</td>
                </tr>
              </tbody>
            </table>

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeEncryptedIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeEncryptedIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeFormulaOCR(
            self,
            request: models.RecognizeFormulaOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeFormulaOCRResponse:
        """
        公式识别是教育的基础OCR识别能力，可支持理科（数学、物理、化学、生物）的印刷体和手写体的公式识别。

        默认接口请求频率限制：2次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeFormulaOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeFormulaOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeGeneralCardWarn(
            self,
            request: models.RecognizeGeneralCardWarnRequest,
            opts: Dict = None,
    ) -> models.RecognizeGeneralCardWarnResponse:
        """
        支持通用证照的有效性检测告警，包括卡证复印件告警、卡证翻拍告警等功能，支持通用证照的ps伪造检测，可以应用于各种证件信息有效性校验场景。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeGeneralCardWarn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeGeneralCardWarnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeGeneralInvoice(
            self,
            request: models.RecognizeGeneralInvoiceRequest,
            opts: Dict = None,
    ) -> models.RecognizeGeneralInvoiceResponse:
        """
        本接口支持 PDF多页（最多30页）、一页中单张、多张、类型票据的混合识别，同时支持单选识别某类票据，已支持票种包括：增值税发票（专票、普票、卷票、区块链发票、通行费发票）、全电发票（专票、普票）、非税发票（通用票据、统一缴纳书）、定额发票、通用机打发票、购车发票（机动车销售发票、二手车发票）、火车票、出租车发票、机票行程单、汽车票、轮船票、过路过桥费发票等常用标准报销发票，支持OFD格式的 增值税电子普通发票、增值税电子专用发票、电子发票（普通发票）、电子发票（增值税专用发票）、电子发票（机票行程单）、电子发票（铁路电子客票）的第一页识别，并支持非上述类型的其他发票的智能识别，点击[立即试用](https://cloud.tencent.com/product/ocr)。

        默认接口请求频率限制：5次/秒。


        支持返回的细项目子票种SubType、子票种中文TypeDescription、以及对应所属大类票种Type 的说明如下列表：
        <table style="width:715px">
              <thead>
                <tr>
                  <th style="width:200px">SubType 子票种英文</th>
                  <th style="width:200px">TypeDescription子票种中文</th>
                  <th >Type 所属大类票种</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td> VatSpecialInvoice</td>
                  <td> 增值税专用发票 </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatCommonInvoice</td>
                  <td> 增值税普通发票 </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicCommonInvoice </td>
                  <td> 增值税电子普通发票 </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicSpecialInvoice </td>
                  <td> 增值税电子专用发票 </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceBlockchain</td>
                  <td> 区块链电子发票 </td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceToll</td>
                  <td> 增值税电子普通发票(通行费)</td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatSalesList</td>
                  <td> 增值税销货清单</td>
                  <td> 3 </td>
                </tr>
                <tr>
                  <td> VatElectronicSpecialInvoiceFull</td>
                  <td> 电子发票(专用发票)</td>
                  <td> 16 </td>
                </tr>
                <tr>
                  <td> VatElectronicInvoiceFull</td>
                  <td> 电子发票(普通发票) </td>
                  <td> 16 </td>
                </tr>
                 <tr>
                  <td> ElectronicFlightTicketFull</td>
                  <td> 电子发票(机票行程单)</td>
                  <td> 16 </td>
                </tr>
                 <tr>
                  <td> ElectronicTrainTicketFull</td>
                  <td> 电子发票(铁路电子客票)</td>
                  <td> 16 </td>
                </tr>
                <tr>
                  <td> MotorVehicleSaleInvoice </td>
                  <td> 机动车销售统一发票 </td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> UsedCarPurchaseInvoice </td>
                  <td> 二手车销售统一发票 </td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> MotorVehicleSaleInvoiceElectronic </td>
                  <td> 机动车销售统一发票（电子）</td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> UsedCarPurchaseInvoiceElectronic </td>
                  <td> 二手车销售统一发票（电子）</td>
                  <td> 12 </td>
                </tr>
                <tr>
                  <td> VatInvoiceRoll </td>
                  <td> 增值税普通发票(卷票) </td>
                  <td> 11 </td>
                </tr>
                <tr>
                  <td> TaxiTicket </td>
                  <td> 出租车发票 </td>
                  <td> 0 </td>
                </tr>
                <tr>
                  <td> QuotaInvoice </td>
                  <td> 定额发票 </td>
                  <td> 1 </td>
                </tr>
                <tr>
                  <td> TrainTicket </td>
                  <td> 火车票 </td>
                  <td> 2 </td>
                </tr>
                <tr>
                  <td> AirTransport </td>
                  <td> 机票行程单 </td>
                  <td> 5 </td>
                </tr>
                <tr>
                  <td> MachinePrintedInvoice </td>
                  <td> 通用机打发票 </td>
                  <td> 8 </td>
                </tr>
                <tr>
                  <td> BusInvoice </td>
                  <td> 汽车票 </td>
                  <td> 9 </td>
                </tr>
                <tr>
                  <td> ShippingInvoice </td>
                  <td> 轮船票 </td>
                  <td> 10 </td>
                </tr>
                <tr>
                  <td> NonTaxIncomeGeneralBill </td>
                  <td> 非税收入通用票据 </td>
                  <td> 15 </td>
                </tr>
                <tr>
                  <td> NonTaxIncomeElectronicBill </td>
                  <td> 非税收入一般缴款书(电子) </td>
                  <td> 15 </td>
                </tr>
                <tr>
                  <td> TollInvoice </td>
                  <td> 过路过桥费发票 </td>
                  <td> 13 </td>
                </tr>
                <tr>
                  <td> MedicalOutpatientInvoice </td>
                  <td> 医疗门诊收费票据（电子） </td>
                  <td> 17 </td>
                </tr>
                <tr>
                  <td> MedicalHospitalizedInvoice </td>
                  <td> 医疗住院收费票据（电子） </td>
                  <td> 17 </td>
                </tr>
                <tr>
                  <td> TaxPayment </td>
                  <td> 完税凭证 </td>
                  <td> 18 </td>
                </tr>
                <tr>
                  <td> CustomsPaymentReceipt </td>
                  <td> 海关缴款 </td>
                  <td> 19 </td>
                </tr>
                <tr>
                  <td> BankSlip </td>
                  <td> 银行回单 </td>
                  <td> 20 </td>
                </tr>
                <tr>
                  <td> OnlineTaxiItinerary </td>
                  <td> 网约车行程单 </td>
                  <td> 21 </td>
                </tr>
                <tr>
                  <td> CustomsDeclaration </td>
                  <td> 海关进/出口货物报关单 </td>
                  <td> 22 </td>
                </tr>
                <tr>
                  <td> OverseasInvoice </td>
                  <td> 海外发票 </td>
                  <td> 23 </td>
                </tr>
                <tr>
                  <td> ShoppingReceipt </td>
                  <td> 购物小票 </td>
                  <td> 24 </td>
                </tr>
                <tr>
                  <td> SaleInventory </td>
                  <td> 销货清单 </td>
                  <td> 25 </td>
                </tr>
                <tr>
                   <td> ElectronicTollSummary </td>
                  <td> 通行费电子票据汇总单 </td>
                  <td> 26 </td>
                </tr>
                <tr>
                   <td> OtherInvoice </td>
                  <td> 其他发票 </td>
                  <td> -1 </td>
                </tr>
              </tbody>
            </table>
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeGeneralInvoice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeGeneralInvoiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeHealthCodeOCR(
            self,
            request: models.RecognizeHealthCodeOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeHealthCodeOCRResponse:
        """
        产品规划

        本接口支持北京、上海、广东、江苏、吉林、黑龙江、天津、辽宁、浙江、河南、四川、贵州、山东、安徽、福建、江西、湖北、湖南等省份健康码的识别，包括持码人姓名、持码人身份证号、健康码更新时间、健康码颜色、核酸检测结果、核酸检测间隔时长、核酸检测时间，疫苗接种信息，八个字段的识别结果输出。不同省市健康码显示的字段信息有所不同，上述字段的识别结果可能为空，以图片上具体展示的信息为准。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeHealthCodeOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeHealthCodeOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeMedicalInvoiceOCR(
            self,
            request: models.RecognizeMedicalInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeMedicalInvoiceOCRResponse:
        """
        医疗发票识别目前支持全国统一门诊发票、全国统一住院发票、以及部分地方的门诊和住院发票的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeMedicalInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeMedicalInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeOnlineTaxiItineraryOCR(
            self,
            request: models.RecognizeOnlineTaxiItineraryOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeOnlineTaxiItineraryOCRResponse:
        """
        本接口支持网约车行程单关键字段的识别，包括行程起止日期、上车时间、起点、终点、里程、金额等字段。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeOnlineTaxiItineraryOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeOnlineTaxiItineraryOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeStoreName(
            self,
            request: models.RecognizeStoreNameRequest,
            opts: Dict = None,
    ) -> models.RecognizeStoreNameResponse:
        """
        本接口用于识别门头照文字识别结果以及对应分类标签信息
        默认接口请求频率限制：1次/秒
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeStoreName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeStoreNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeTableAccurateOCR(
            self,
            request: models.RecognizeTableAccurateOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeTableAccurateOCRResponse:
        """
        本接口支持中英文图片/PDF内常规表格、无线表格、多表格的检测和识别，返回每个单元格的文字内容，支持旋转的表格图片识别，且支持将识别结果保存为 Excel 格式。识别效果比表格识别V2更好，覆盖场景更加广泛，对表格难例场景，如无线表格、嵌套表格（有线表格中包含无线表格）的识别效果均优于表格识别V2。

        默认接口请求频率限制：2次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeTableAccurateOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeTableAccurateOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeTableMultiOCR(
            self,
            request: models.RecognizeTableMultiOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeTableMultiOCRResponse:
        """
        基于MLLM(多模态大语言模型)的表格识别能力，针对复杂表格的算法识别效果更佳，适配财务报表识别场景，并可输出直接对接业务系统的Excel数据。

        默认接口请求频率限制：1次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeTableMultiOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeTableMultiOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeTableOCR(
            self,
            request: models.RecognizeTableOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeTableOCRResponse:
        """
        本接口支持中英文图片/ PDF内常规表格、无线表格、多表格的检测和识别，支持日文有线表格识别，返回每个单元格的文字内容，支持旋转的表格图片识别，且支持将识别结果保存为 Excel 格式。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeTableOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeTableOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeThaiIDCardOCR(
            self,
            request: models.RecognizeThaiIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeThaiIDCardOCRResponse:
        """
        本接口支持泰国身份证识别，识别字段包括泰文姓名、英文姓名、地址、出生日期、身份证号码、首次领用日期、签发日期等字段。
        本接口暂未完全对外开放，如需咨询，请[联系商务](https://cloud.tencent.com/about/connect)

        默认接口请求频率限制：10次/秒
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeThaiIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeThaiIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeTravelCardOCR(
            self,
            request: models.RecognizeTravelCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeTravelCardOCRResponse:
        """
        产品规划

        本接口支持通信大数据行程卡识别，包括行程卡颜色、更新时间、途经地、存在中高风险地区的城市、电话号码，五个字段的识别结果输出。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeTravelCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeTravelCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecognizeValidIDCardOCR(
            self,
            request: models.RecognizeValidIDCardOCRRequest,
            opts: Dict = None,
    ) -> models.RecognizeValidIDCardOCRResponse:
        """
        本接口支持二代身份证、临时身份证、港澳台居住证、外国人永久居留证，字段内容识别功能，包括姓名、性别、民族、出生、出生日期、住址、公民身份号码、签发机关、有效期限、国籍、通行证号码、持证人持有号码；支持返回证件类型；支持翻拍、复印、边框不完整、遮挡、字段级反光和字段级完整性告警；支持卡片主体框裁剪和头像裁剪。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RecognizeValidIDCardOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecognizeValidIDCardOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResidenceBookletOCR(
            self,
            request: models.ResidenceBookletOCRRequest,
            opts: Dict = None,
    ) -> models.ResidenceBookletOCRResponse:
        """
        本接口支持居民户口簿户主页及成员页关键字段的识别，包括姓名、户别、地址、籍贯、身份证号码等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ResidenceBookletOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResidenceBookletOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RideHailingDriverLicenseOCR(
            self,
            request: models.RideHailingDriverLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.RideHailingDriverLicenseOCRResponse:
        """
        本接口支持网约车驾驶证关键字段的识别，包括姓名、证号、起始日期、截止日期、发证日期。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RideHailingDriverLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RideHailingDriverLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RideHailingTransportLicenseOCR(
            self,
            request: models.RideHailingTransportLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.RideHailingTransportLicenseOCRResponse:
        """
        本接口支持网约车运输证关键字段的识别，包括交运管许可字号、车辆所有人、车辆号牌、起始日期、截止日期、发证日期。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "RideHailingTransportLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RideHailingTransportLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SealOCR(
            self,
            request: models.SealOCRRequest,
            opts: Dict = None,
    ) -> models.SealOCRResponse:
        """
        本接口支持各类印章主体内容、印章其他内容及形状识别，支持单图多印章识别，包括发票章、财务章等，适用于公文票据等场景。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "SealOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SealOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ShipInvoiceOCR(
            self,
            request: models.ShipInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.ShipInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持识别轮船票的发票代码、发票号码、日期、姓名、票价、始发地、目的地、姓名、时间、发票消费类型、省、市、币种字段。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "ShipInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ShipInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SmartStructuralOCR(
            self,
            request: models.SmartStructuralOCRRequest,
            opts: Dict = None,
    ) -> models.SmartStructuralOCRResponse:
        """
        本接口支持识别并提取各类证照、票据、表单、合同等结构化场景的字段信息。无需任何配置，灵活高效。适用于各类结构化信息录入场景。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "SmartStructuralOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SmartStructuralOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitExtractDocAgentJob(
            self,
            request: models.SubmitExtractDocAgentJobRequest,
            opts: Dict = None,
    ) -> models.SubmitExtractDocAgentJobResponse:
        """
        文档处理领域里常见的通用Agent 如抽取、比对之类的，目前我们提供的抽取，但未来可以根据实际情况和客户需求扩展。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitExtractDocAgentJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitExtractDocAgentJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TableOCR(
            self,
            request: models.TableOCRRequest,
            opts: Dict = None,
    ) -> models.TableOCRResponse:
        """
        <b>此接口为表格识别的旧版本服务，不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/49525">新版表格识别</a>。</b>

        本接口支持图片内表格文档的检测和识别，返回每个单元格的文字内容，支持将识别结果保存为 Excel 格式。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "TableOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TableOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TaxiInvoiceOCR(
            self,
            request: models.TaxiInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.TaxiInvoiceOCRResponse:
        """
        本接口支持出租车发票关键字段的识别，包括发票号码、发票代码、金额、日期、上下车时间、里程、车牌号、发票类型及所属地区等字段。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "TaxiInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TaxiInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextDetect(
            self,
            request: models.TextDetectRequest,
            opts: Dict = None,
    ) -> models.TextDetectResponse:
        """
        本接口通过检测图片中的文字信息特征，快速判断图片中有无文字并返回判断结果，帮助用户过滤无文字的图片。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "TextDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TollInvoiceOCR(
            self,
            request: models.TollInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.TollInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持过路过桥费发票关键字段的识别，包括发票代码、发票号码、日期、金额、入口、出口、时间、发票消费类型、高速标志等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "TollInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TollInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TrainTicketOCR(
            self,
            request: models.TrainTicketOCRRequest,
            opts: Dict = None,
    ) -> models.TrainTicketOCRResponse:
        """
        本接口支持火车票全字段的识别，包括编号、出发站、到达站、出发时间、车次、座位号、姓名、票价、席别、身份证号、发票消费类型、序列号、加收票价、手续费、大写金额、售票站、原票价、发票类型、收据号码、是否仅供报销使用等字段的识别。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "TrainTicketOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TrainTicketOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VatInvoiceOCR(
            self,
            request: models.VatInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.VatInvoiceOCRResponse:
        """
        本接口支持增值税专用发票、增值税普通发票、增值税电子专票、增值税电子普票、电子发票（普通发票）、电子发票（增值税专用发票）全字段的内容检测和识别，包括发票代码、发票号码、打印发票代码、打印发票号码、开票日期、合计金额、校验码、税率、合计税额、价税合计、购买方识别号、复核、销售方识别号、开票人、密码区1、密码区2、密码区3、密码区4、发票名称、购买方名称、销售方名称、服务名称、备注、规格型号、数量、单价、金额、税额、收款人等字段，点击[立即试用](https://cloud.tencent.com/product/ocr)。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VatInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VatInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VatInvoiceVerifyNew(
            self,
            request: models.VatInvoiceVerifyNewRequest,
            opts: Dict = None,
    ) -> models.VatInvoiceVerifyNewResponse:
        """
        本接口支持增值税发票的准确性核验，您可以通过输入增值税发票的关键字段提供所需的验证信息，接口返回真实的票面相关信息，包括发票代码、发票号码、开票日期、金额、消费类型、购方名称、购方税号、销方名称、销方税号等多个常用字段。支持多种发票类型核验，包括增值税专用发票、增值税普通发票（含电子普通发票、卷式发票、通行费发票）、全电发票、机动车销售统一发票、货物运输业增值税专用发票、二手车销售统一发票、通用机打电子发票（广东和浙江）。

        默认接口请求频率限制：20次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VatInvoiceVerifyNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VatInvoiceVerifyNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VatRollInvoiceOCR(
            self,
            request: models.VatRollInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.VatRollInvoiceOCRResponse:
        """
        <b>此接口不再进行服务升级，建议您使用识别能力更强、服务性能更优的<a href="https://cloud.tencent.com/document/product/866/90802">通用票据识别（高级版）</a>。</b>
        本接口支持对增值税发票（卷票）关键字段的识别，包括的发票代码、合计金额(小写)、合计金额(大写)、开票日期、发票号码、购买方识别号、销售方识别号、校验码、销售方名称、购买方名称、发票消费类型、省、市、是否有公司印章、单价、金额、数量、服务类型、品名、种类等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VatRollInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VatRollInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VehicleLicenseOCR(
            self,
            request: models.VehicleLicenseOCRRequest,
            opts: Dict = None,
    ) -> models.VehicleLicenseOCRResponse:
        """
        本接口支持行驶证主页和副页所有字段的自动定位与识别。

        行驶证主页：车牌号码、车辆类型、所有人、住址、使用性质、品牌型号、识别代码、发动机号、注册日期、发证日期、发证单位。

        行驶证副页：号牌号码、档案编号、核定载人数、总质量、整备质量、核定载质量、外廓尺寸、准牵引总质量、备注、检验记录。

        另外，本接口还支持复印件、翻拍告警功能。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VehicleLicenseOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VehicleLicenseOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VehicleRegCertOCR(
            self,
            request: models.VehicleRegCertOCRRequest,
            opts: Dict = None,
    ) -> models.VehicleRegCertOCRResponse:
        """
        本接口支持国内机动车登记证书主要字段的结构化识别，包括机动车所有人、身份证明名称、号码、车辆型号、车辆识别代号、发动机号、制造厂名称等。

        默认接口请求频率限制：5次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VehicleRegCertOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VehicleRegCertOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyOfdVatInvoiceOCR(
            self,
            request: models.VerifyOfdVatInvoiceOCRRequest,
            opts: Dict = None,
    ) -> models.VerifyOfdVatInvoiceOCRResponse:
        """
        本接口支持OFD格式的增值税电子普通发票、增值税电子专用发票、电子发票（普通发票）、电子发票（增值税专用发票）、电子发票（铁路电子客票）、电子发票（航空运输电子客票行程单）识别，返回发票代码、发票号码、开票日期、验证码、机器编号、密码区，购买方和销售方信息，包括名称、纳税人识别号、地址电话、开户行及账号，以及价税合计、开票人、收款人、复核人、税额、不含税金额等字段信息。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyOfdVatInvoiceOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyOfdVatInvoiceOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VinOCR(
            self,
            request: models.VinOCRRequest,
            opts: Dict = None,
    ) -> models.VinOCRResponse:
        """
        本接口支持图片内车辆识别代号（VIN）的检测和识别。
        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "VinOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VinOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WaybillOCR(
            self,
            request: models.WaybillOCRRequest,
            opts: Dict = None,
    ) -> models.WaybillOCRResponse:
        """
        本接口支持市面上主流版式电子运单的识别，包括收件人和寄件人的姓名、电话、地址以及运单号等字段。

        默认接口请求频率限制：10次/秒。
        """
        
        kwargs = {}
        kwargs["action"] = "WaybillOCR"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WaybillOCRResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)