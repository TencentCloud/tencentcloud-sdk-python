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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.iai.v20200303 import models


class IaiClient(AbstractClient):
    _apiVersion = '2020-03-03'
    _endpoint = 'iai.tencentcloudapi.com'
    _service = 'iai'


    def AnalyzeDenseLandmarks(self, request):
        """对请求图片进行五官定位（也称人脸关键点定位），获得人脸的精准信息，返回多达888点关键信息，对五官和脸部轮廓进行精确定位。

        :param request: Request instance for AnalyzeDenseLandmarks.
        :type request: :class:`tencentcloud.iai.v20200303.models.AnalyzeDenseLandmarksRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.AnalyzeDenseLandmarksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AnalyzeDenseLandmarks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AnalyzeDenseLandmarksResponse()
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


    def AnalyzeFace(self, request):
        """对请求图片进行五官定位（也称人脸关键点定位），计算构成人脸轮廓的 90 个点，包括眉毛（左右各 8 点）、眼睛（左右各 8 点）、鼻子（13 点）、嘴巴（22 点）、脸型轮廓（21 点）、眼珠[或瞳孔]（2点）。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for AnalyzeFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.AnalyzeFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.AnalyzeFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AnalyzeFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AnalyzeFaceResponse()
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


    def CheckSimilarPerson(self, request):
        """对指定的人员库进行人员查重，给出疑似相同人的信息。

        可以使用本接口对已有的单个人员库进行人员查重，避免同一人在单个人员库中拥有多个身份；也可以使用本接口对已有的多个人员库进行人员查重，查询同一人是否同时存在多个人员库中。

        不支持跨算法模型版本查重，且目前仅支持算法模型为3.0的人员库使用查重功能。

        >
        - 若对完全相同的指定人员库进行查重操作，需等待上次操作完成才可。即，若两次请求输入的 GroupIds 相同，第一次请求若未完成，第二次请求将返回失败。

        >
        - 查重的人员库状态为腾讯云开始进行查重任务的那一刻，即您可以理解为当您发起查重请求后，若您的查重任务需要排队，在排队期间您对人员库的增删操作均会会影响查重的结果。腾讯云将以开始进行查重任务的那一刻人员库的状态进行查重。查重任务开始后，您对人员库的任何操作均不影响查重任务的进行。但建议查重任务开始后，请不要对人员库中人员和人脸进行增删操作。

        :param request: Request instance for CheckSimilarPerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.CheckSimilarPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CheckSimilarPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckSimilarPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckSimilarPersonResponse()
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


    def CompareFace(self, request):
        """对两张图片中的人脸进行相似度比对，返回人脸相似度分数。

        若您需要判断 “此人是否是某人”，即验证某张图片中的人是否是已知身份的某人，如常见的人脸登录场景，建议使用[人脸验证](https://cloud.tencent.com/document/product/867/44983)或[人员验证](https://cloud.tencent.com/document/product/867/44982)接口。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for CompareFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.CompareFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CompareFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareFaceResponse()
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


    def CompareMaskFace(self, request):
        """对两张图片中的人脸进行相似度比对，返回人脸相似度分数。

        戴口罩人脸比对接口可在人脸戴口罩情况下使用，口罩遮挡程度最高可以遮挡鼻尖。

        如图片人脸不存在戴口罩情况，建议使用人脸比对服务。

        :param request: Request instance for CompareMaskFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.CompareMaskFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CompareMaskFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareMaskFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareMaskFaceResponse()
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


    def CopyPerson(self, request):
        """将已存在于某人员库的人员复制到其他人员库，该人员的描述信息不会被复制。单个人员最多只能同时存在100个人员库中。
        >
        - 注：若该人员创建时算法模型版本为2.0，复制到非2.0算法模型版本的Group中时，复制操作将会失败。

        :param request: Request instance for CopyPerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.CopyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CopyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyPersonResponse()
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


    def CreateFace(self, request):
        """将一组人脸图片添加到一个人员中。一个人员最多允许包含 5 张图片。若该人员存在多个人员库中，所有人员库中该人员图片均会增加。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for CreateFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreateFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFaceResponse()
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


    def CreateGroup(self, request):
        """用于创建一个空的人员库，如果人员库已存在返回错误。
        可根据需要创建自定义描述字段，用于辅助描述该人员库下的人员信息。

        1个APPID下最多创建10万个人员库（Group）、最多包含5000万张人脸（Face）。

        不同算法模型版本（FaceModelVersion）的人员库（Group）最多可包含人脸（Face）数不同。算法模型版本为2.0的人员库最多包含100万张人脸，算法模型版本为3.0的人员库最多可包含300万张人脸。

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreatePerson(self, request):
        """创建人员，添加人脸、姓名、性别及其他相关信息。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for CreatePerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.CreatePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonResponse()
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


    def DeleteFace(self, request):
        """删除一个人员下的人脸图片。如果该人员只有一张人脸图片，则返回错误。

        :param request: Request instance for DeleteFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeleteFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFaceResponse()
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


    def DeleteGroup(self, request):
        """删除该人员库及包含的所有的人员。同时，人员对应的所有人脸信息将被删除。若某人员同时存在多个人员库中，该人员不会被删除，但属于该人员库中的自定义描述字段信息会被删除，属于其他人员库的自定义描述字段信息不受影响。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
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


    def DeletePerson(self, request):
        """删除该人员信息，此操作会导致所有人员库均删除此人员。同时，该人员的所有人脸信息将被删除。

        :param request: Request instance for DeletePerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeletePersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonResponse()
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


    def DeletePersonFromGroup(self, request):
        """从某人员库中删除人员，此操作仅影响该人员库。若该人员仅存在于指定的人员库中，该人员将被删除，其所有的人脸信息也将被删除。

        :param request: Request instance for DeletePersonFromGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.DeletePersonFromGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DeletePersonFromGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonFromGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonFromGroupResponse()
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


    def DetectFace(self, request):
        """检测给定图片中的人脸（Face）的位置、相应的面部属性和人脸质量信息，位置包括 (x，y，w，h)，面部属性包括性别（gender）、年龄（age）、表情（expression）、魅力（beauty）、眼镜（glass）、发型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)，人脸质量信息包括整体质量分（score）、模糊分（sharpness）、光照分（brightness）和五官遮挡分（completeness）。


        其中，人脸质量信息主要用于评价输入的人脸图片的质量。在使用人脸识别服务时，建议您对输入的人脸图片进行质量检测，提升后续业务处理的效果。该功能的应用场景包括：

        1） 人员库[创建人员](https://cloud.tencent.com/document/product/867/45014)/[增加人脸](https://cloud.tencent.com/document/product/867/45016)：保证人员人脸信息的质量，便于后续的业务处理。

        2） [人脸搜索](https://cloud.tencent.com/document/product/867/44994)：保证输入的图片质量，快速准确匹配到对应的人员。

        3） [人脸验证](https://cloud.tencent.com/document/product/867/44983)：保证人脸信息的质量，避免明明是本人却认证不通过的情况。

        4） 人脸融合：保证上传的人脸质量，人脸融合的效果更好。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。


        :param request: Request instance for DetectFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectFaceResponse()
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


    def DetectFaceAttributes(self, request):
        """检测给定图片中的人脸（Face）的位置、相应的面部属性和人脸质量信息，位置包括 (x，y，w，h)，面部属性包括性别（gender）、年龄（age）、表情（expression）、魅力（beauty）、眼镜（glass）、发型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)，人脸质量信息包括整体质量分（score）、模糊分（sharpness）、光照分（brightness）和五官遮挡分（completeness）。


        其中，人脸质量信息主要用于评价输入的人脸图片的质量。在使用人脸识别服务时，建议您对输入的人脸图片进行质量检测，提升后续业务处理的效果。该功能的应用场景包括：

        1） 人员库[创建人员](https://cloud.tencent.com/document/product/867/32793)/[增加人脸](https://cloud.tencent.com/document/product/867/32795)：保证人员人脸信息的质量，便于后续的业务处理。

        2） [人脸搜索](https://cloud.tencent.com/document/product/867/32798)：保证输入的图片质量，快速准确匹配到对应的人员。

        3） [人脸验证](https://cloud.tencent.com/document/product/867/32806)：保证人脸信息的质量，避免明明是本人却认证不通过的情况。

        4） [人脸融合](https://cloud.tencent.com/product/facefusion)：保证上传的人脸质量，人脸融合的效果更好。

        >
        - 本接口是[人脸检测与分析](https://cloud.tencent.com/document/product/867/44989)的升级，具体在于：
        1.本接口可以指定需要计算返回的人脸属性，避免无效计算，降低耗时；
        2.本接口支持更多属性细项数，也会持续增加更多功能。
        请您使用本接口完成相应的人脸检测与属性分析需求。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectFaceAttributes.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectFaceAttributesRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectFaceAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectFaceAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectFaceAttributesResponse()
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


    def DetectLiveFace(self, request):
        """用于对用户上传的静态图片进行人脸活体检测。与动态活体检测的区别是：静态活体检测中，用户不需要通过唇语或摇头眨眼等动作来识别。

        静态活体检测适用于手机自拍的场景，或对防攻击要求不高的场景。如果对活体检测有更高安全性要求，请使用[人脸核身·云智慧眼](https://cloud.tencent.com/product/faceid)产品。

        >
        - 图片的宽高比请接近3：4，不符合宽高比的图片返回的分值不具备参考意义。本接口适用于类手机自拍场景，非类手机自拍照返回的分值不具备参考意义。

        >
        - 使用过程中建议正对摄像头，不要距离太远，使面部可以完整地显示在识别的框内，识别过程中不要移动设备或遮挡面部。不要选择光线过强或过弱的环境进行面部识别，识别时不要添加任何滤镜。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLiveFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLiveFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLiveFaceResponse()
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


    def DetectLiveFaceAccurate(self, request):
        """人脸静态活体检测（高精度版）可用于对用户上传的静态图片进行防翻拍活体检测，以判断是否是翻拍图片。

        相比现有静态活体检测服务，高精度版在维持高真人通过率的前提下，增强了对高清屏幕、裁剪纸片、3D面具等攻击的防御能力，攻击拦截率约为业内同类型产品形态4-5倍。同时支持多场景人脸核验，满足移动端、PC端各类型场景的图片活体检验需求，适用于各个行业不同的活体检验应用。

        :param request: Request instance for DetectLiveFaceAccurate.
        :type request: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceAccurateRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.DetectLiveFaceAccurateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetectLiveFaceAccurate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetectLiveFaceAccurateResponse()
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


    def EstimateCheckSimilarPersonCostTime(self, request):
        """获取若要开始一个人员查重任务，这个任务结束的预估时间。

        若EndTimestamp符合您预期，请您尽快发起人员查重请求，否则导致可能需要更多处理时间。

        若预估时间超过5小时，则无法使用人员查重功能。

        :param request: Request instance for EstimateCheckSimilarPersonCostTime.
        :type request: :class:`tencentcloud.iai.v20200303.models.EstimateCheckSimilarPersonCostTimeRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.EstimateCheckSimilarPersonCostTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EstimateCheckSimilarPersonCostTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EstimateCheckSimilarPersonCostTimeResponse()
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


    def GetCheckSimilarPersonJobIdList(self, request):
        """获取人员查重任务列表，按任务创建时间逆序（最新的在前面）。

        只保留最近1年的数据。

        :param request: Request instance for GetCheckSimilarPersonJobIdList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetCheckSimilarPersonJobIdListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetCheckSimilarPersonJobIdListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCheckSimilarPersonJobIdList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCheckSimilarPersonJobIdListResponse()
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


    def GetGroupInfo(self, request):
        """获取人员库信息。

        :param request: Request instance for GetGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupInfoResponse()
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


    def GetGroupList(self, request):
        """获取人员库列表。

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGroupListResponse()
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


    def GetPersonBaseInfo(self, request):
        """获取指定人员的信息，包括姓名、性别、人脸等。

        :param request: Request instance for GetPersonBaseInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonBaseInfoResponse()
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


    def GetPersonGroupInfo(self, request):
        """获取指定人员的信息，包括加入的人员库、描述内容等。

        :param request: Request instance for GetPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonGroupInfoResponse()
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


    def GetPersonList(self, request):
        """获取指定人员库中的人员列表。

        :param request: Request instance for GetPersonList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonListResponse()
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


    def GetPersonListNum(self, request):
        """获取指定人员库中人员数量。

        :param request: Request instance for GetPersonListNum.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetPersonListNumRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetPersonListNumResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPersonListNum", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPersonListNumResponse()
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


    def GetSimilarPersonResult(self, request):
        """获取人员查重接口（CheckSimilarPerson）结果。

        :param request: Request instance for GetSimilarPersonResult.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetSimilarPersonResultRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetSimilarPersonResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSimilarPersonResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSimilarPersonResultResponse()
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


    def GetUpgradeGroupFaceModelVersionJobList(self, request):
        """获取人员库升级任务列表

        :param request: Request instance for GetUpgradeGroupFaceModelVersionJobList.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetUpgradeGroupFaceModelVersionJobListRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetUpgradeGroupFaceModelVersionJobListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUpgradeGroupFaceModelVersionJobList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUpgradeGroupFaceModelVersionJobListResponse()
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


    def GetUpgradeGroupFaceModelVersionResult(self, request):
        """人员库升级结果查询

        :param request: Request instance for GetUpgradeGroupFaceModelVersionResult.
        :type request: :class:`tencentcloud.iai.v20200303.models.GetUpgradeGroupFaceModelVersionResultRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.GetUpgradeGroupFaceModelVersionResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUpgradeGroupFaceModelVersionResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUpgradeGroupFaceModelVersionResultResponse()
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


    def ModifyGroup(self, request):
        """修改人员库名称、备注、自定义描述字段名称。

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.ModifyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGroupResponse()
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


    def ModifyPersonBaseInfo(self, request):
        """修改人员信息，包括名称、性别等。人员名称和性别修改会同步到包含该人员的所有人员库。

        :param request: Request instance for ModifyPersonBaseInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.ModifyPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.ModifyPersonBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonBaseInfoResponse()
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


    def ModifyPersonGroupInfo(self, request):
        """修改指定人员库人员描述内容。

        :param request: Request instance for ModifyPersonGroupInfo.
        :type request: :class:`tencentcloud.iai.v20200303.models.ModifyPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.ModifyPersonGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonGroupInfoResponse()
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


    def RevertGroupFaceModelVersion(self, request):
        """本接口用于回滚人员库的人脸识别算法模型版本。单个人员库有且仅有一次回滚机会。

        回滚操作会在10s内生效，回滚操作中，您对人员库的操作可能会失效。

        :param request: Request instance for RevertGroupFaceModelVersion.
        :type request: :class:`tencentcloud.iai.v20200303.models.RevertGroupFaceModelVersionRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.RevertGroupFaceModelVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevertGroupFaceModelVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevertGroupFaceModelVersionResponse()
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


    def SearchFaces(self, request):
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，识别结果按照相似度从大到小排序。

        支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        与[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而人员搜索及人员搜索按库返回接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。


        本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)结合使用。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        >
        - 不可同时搜索不同算法模型版本（FaceModelVersion）的人员库。

        :param request: Request instance for SearchFaces.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchFacesRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchFacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchFaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchFacesResponse()
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


    def SearchFacesReturnsByGroup(self, request):
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。

        支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        与[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。

        本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)结合使用。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        >
        - 不可同时搜索不同算法模型版本（FaceModelVersion）的人员库。

        :param request: Request instance for SearchFacesReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchFacesReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchFacesReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchFacesReturnsByGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchFacesReturnsByGroupResponse()
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


    def SearchPersons(self, request):
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照相似度从大到小排列。

        支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/44994)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/44993)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for SearchPersons.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchPersonsRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchPersonsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchPersons", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchPersonsResponse()
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


    def SearchPersonsReturnsByGroup(self, request):
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。

        支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/44994)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/44993)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。
        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for SearchPersonsReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20200303.models.SearchPersonsReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.SearchPersonsReturnsByGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchPersonsReturnsByGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchPersonsReturnsByGroupResponse()
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


    def UpgradeGroupFaceModelVersion(self, request):
        """升级人员库。升级过程中，人员库仍然为原算法版本，人员库相关操作仍然支持。升级完成后，人员库为新算法版本。
        单个人员库有且仅支持一次回滚操作。

        升级是一个耗时的操作，执行时间与人员库的人脸数相关，升级的人员库中的人脸数越多，升级的耗时越长。升级接口是个异步任务，调用成功后返回JobId，通过GetUpgradeGroupFaceModelVersionResult查询升级进度和结果。如果升级成功，人员库版本将切换到新版本。如果想回滚到旧版本，可以调用RevertGroupFaceModelVersion进行回滚。

        注：某些接口无法进行跨人员库版本操作，例如SearchFaces，SearchPersons和CopyPerson等。当业务有多个Group操作的场景时，如同时搜索Group1和Group2，如果升级了Group1，此时Group1和Group2版本不同，造成了跨版本操作，将导致Search接口无法正常执行，返回不允许执行跨版本操作错误，升级前需考虑业务是否有多库操作的场景，否则会影响线上接口表现。

        :param request: Request instance for UpgradeGroupFaceModelVersion.
        :type request: :class:`tencentcloud.iai.v20200303.models.UpgradeGroupFaceModelVersionRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.UpgradeGroupFaceModelVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeGroupFaceModelVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeGroupFaceModelVersionResponse()
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


    def VerifyFace(self, request):
        """给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)。

        与[人脸比对](https://cloud.tencent.com/document/product/867/44987)接口不同的是，人脸验证用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而[人脸比对](https://cloud.tencent.com/document/product/867/44987)用于判断两张人脸的相似度。

        与[人员验证](https://cloud.tencent.com/document/product/867/44982)接口不同的是，人脸验证将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员验证](https://cloud.tencent.com/document/product/867/44982)会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person下有4张 Face，人员验证接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for VerifyFace.
        :type request: :class:`tencentcloud.iai.v20200303.models.VerifyFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.VerifyFaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyFace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyFaceResponse()
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


    def VerifyPerson(self, request):
        """给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)。
        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。

         和人脸比对相关接口不同的是，人脸验证相关接口用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而人脸比对相关接口用于判断两张人脸的相似度。


        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for VerifyPerson.
        :type request: :class:`tencentcloud.iai.v20200303.models.VerifyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20200303.models.VerifyPersonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyPerson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyPersonResponse()
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