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
from tencentcloud.iai.v20180301 import models


class IaiClient(AbstractClient):
    _apiVersion = '2018-03-01'
    _endpoint = 'iai.tencentcloudapi.com'


    def AnalyzeFace(self, request):
        """对请求图片进行五官定位（也称人脸关键点定位），计算构成人脸轮廓的 90 个点，包括眉毛（左右各 8 点）、眼睛（左右各 8 点）、鼻子（13 点）、嘴巴（22 点）、脸型轮廓（21 点）、眼珠[或瞳孔]（2点）。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for AnalyzeFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.AnalyzeFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.AnalyzeFaceResponse`

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
        """对指定的人员库进行查重，给出疑似相同人的信息。

        不支持跨算法模型版本查重，且目前仅支持算法模型为3.0的人员库使用查重功能。

        >
        - 若对完全相同的指定人员库进行查重操作，需等待上次操作完成才可。即，若两次请求输入的 GroupIds 相同，第一次请求若未完成，第二次请求将返回失败。<br>
        查重的人员库状态为腾讯云开始进行查重任务的那一刻，即您可以理解为当您发起查重请求后，若您的查重任务需要排队，在排队期间您对人员库的增删操作均会会影响查重的结果。腾讯云将以开始进行查重任务的那一刻人员库的状态进行查重。查重任务开始后，您对人员库的任何操作均不影响查重任务的进行。但建议查重任务开始后，请不要对人员库中人员和人脸进行增删操作。

        :param request: Request instance for CheckSimilarPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.CheckSimilarPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CheckSimilarPersonResponse`

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

        若您需要判断 “此人是否是某人”，即验证某张图片中的人是否是已知身份的某人，如常见的人脸登录场景，建议使用[人脸验证](https://cloud.tencent.com/document/product/867/32806)接口。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for CompareFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.CompareFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CompareFaceResponse`

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


    def CopyPerson(self, request):
        """将已存在于某人员库的人员复制到其他人员库，该人员的描述信息不会被复制。单个人员最多只能同时存在100个人员库中。
        >
        - 注：若该人员创建时算法模型版本为2.0，复制到非2.0算法模型版本的Group中时，复制操作将会失败。

        :param request: Request instance for CopyPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.CopyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CopyPersonResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.CreateFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreateFaceResponse`

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
        """用于创建一个空的人员库，如果人员库已存在返回错误。可根据需要创建自定义描述字段，用于辅助描述该人员库下的人员信息。1个APPID下最多创建2万个人员库（Group）、最多包含1000万张人脸（Face），单个人员库（Group）最多包含100万张人脸（Face）。

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreateGroupResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.CreatePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.CreatePersonResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.DeleteFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeleteFaceResponse`

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

        >
        - 删除人员库的操作为异步执行，删除单张人脸时间约为10ms，即一小时内可以删除36万张。删除期间，无法向该人员库添加人员。

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeleteGroupResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.DeletePersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeletePersonResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.DeletePersonFromGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DeletePersonFromGroupResponse`

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

        1） 人员库[创建人员](https://cloud.tencent.com/document/product/867/32793)/[增加人脸](https://cloud.tencent.com/document/product/867/32795)：保证人员人脸信息的质量，便于后续的业务处理。

        2） [人脸搜索](https://cloud.tencent.com/document/product/867/32798)：保证输入的图片质量，快速准确匹配到对应的人员。

        3） [人脸验证](https://cloud.tencent.com/document/product/867/32806)：保证人脸信息的质量，避免明明是本人却认证不通过的情况。

        4） [人脸融合](https://cloud.tencent.com/product/facefusion)：保证上传的人脸质量，人脸融合的效果更好。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。


        :param request: Request instance for DetectFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.DetectFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DetectFaceResponse`

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


    def DetectLiveFace(self, request):
        """用于对用户上传的静态图片进行人脸活体检测。与动态活体检测的区别是：静态活体检测中，用户不需要通过唇语或摇头眨眼等动作来识别。

        静态活体检测适用于手机自拍的场景，或对防攻击要求不高的场景。如果对活体检测有更高安全性要求，请使用[人脸核身·云智慧眼](https://cloud.tencent.com/product/faceid)产品。

        >
        - 图片的宽高比请接近3：4，不符合宽高比的图片返回的分值不具备参考意义。本接口适用于类手机自拍场景，非类手机自拍照返回的分值不具备参考意义。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for DetectLiveFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.DetectLiveFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.DetectLiveFaceResponse`

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


    def EstimateCheckSimilarPersonCostTime(self, request):
        """获取若要开始一个人员查重任务，这个任务结束的预估时间。

        若EndTimestamp符合您预期，请您尽快发起人员查重请求，否则导致可能需要更多处理时间。

        若预估时间超过5小时，则无法使用人员查重功能。

        :param request: Request instance for EstimateCheckSimilarPersonCostTime.
        :type request: :class:`tencentcloud.iai.v20180301.models.EstimateCheckSimilarPersonCostTimeRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.EstimateCheckSimilarPersonCostTimeResponse`

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


    def GetGroupList(self, request):
        """获取人员库列表。

        :param request: Request instance for GetGroupList.
        :type request: :class:`tencentcloud.iai.v20180301.models.GetGroupListRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetGroupListResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonBaseInfoResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonGroupInfoResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonListRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonListResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.GetPersonListNumRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetPersonListNumResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.GetSimilarPersonResultRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.GetSimilarPersonResultResponse`

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


    def ModifyGroup(self, request):
        """修改人员库名称、备注、自定义描述字段名称。

        :param request: Request instance for ModifyGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyGroupResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyPersonBaseInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyPersonBaseInfoResponse`

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
        :type request: :class:`tencentcloud.iai.v20180301.models.ModifyPersonGroupInfoRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.ModifyPersonGroupInfoResponse`

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


    def SearchFaces(self, request):
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopN 人员，识别结果按照相似度从大到小排序。单次搜索的人员库人脸总数量不得超过 100 万张。
        此接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)结合使用。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for SearchFaces.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchFacesRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchFacesResponse`

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
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopN 人员，按照人员库的维度以人员相似度从大到小顺序排列。
        此接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)结合使用。

        :param request: Request instance for SearchFacesReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchFacesReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchFacesReturnsByGroupResponse`

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
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopN 人员，按照相似度从大到小排列。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。

        人员搜索接口和人脸搜索接口的区别是：人脸搜索会比对该 Person 下所有 Face ，而人员搜索比对的是该 Person 的 Person 特征。
        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for SearchPersons.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchPersonsRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchPersonsResponse`

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
        """用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopN 人员，按照人员库的维度以人员相似度从大到小顺序排列。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人员）更加准确。

        人员搜索和人脸搜索的区别是：人脸搜索比对该 Person 下所有 Face ，而人员搜索比对的是该 Person 的 Person 特征。
        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for SearchPersonsReturnsByGroup.
        :type request: :class:`tencentcloud.iai.v20180301.models.SearchPersonsReturnsByGroupRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.SearchPersonsReturnsByGroupResponse`

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


    def VerifyFace(self, request):
        """给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)。 和[人脸比对](https://cloud.tencent.com/document/product/867/32802)接口不同的是，[人脸验证](https://cloud.tencent.com/document/product/867/32806)用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而[人脸比对](https://cloud.tencent.com/document/product/867/32802)用于判断两张人脸的相似度。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        :param request: Request instance for VerifyFace.
        :type request: :class:`tencentcloud.iai.v20180301.models.VerifyFaceRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.VerifyFaceResponse`

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
        """给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/32794)。
        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。

         和人脸比对相关接口不同的是，人脸验证相关接口用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而人脸比对相关接口用于判断两张人脸的相似度。


        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。

        :param request: Request instance for VerifyPerson.
        :type request: :class:`tencentcloud.iai.v20180301.models.VerifyPersonRequest`
        :rtype: :class:`tencentcloud.iai.v20180301.models.VerifyPersonResponse`

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