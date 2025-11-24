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
from tencentcloud.iai.v20200303 import models
from typing import Dict


class IaiClient(AbstractClient):
    _apiVersion = '2020-03-03'
    _endpoint = 'iai.tencentcloudapi.com'
    _service = 'iai'

    async def AnalyzeDenseLandmarks(
            self,
            request: models.AnalyzeDenseLandmarksRequest,
            opts: Dict = None,
    ) -> models.AnalyzeDenseLandmarksResponse:
        """
        对请求图片进行五官定位（也称人脸关键点定位），获得人脸的精准信息，返回多达888点关键信息，对五官和脸部轮廓进行精确定位。
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeDenseLandmarks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeDenseLandmarksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AnalyzeFace(
            self,
            request: models.AnalyzeFaceRequest,
            opts: Dict = None,
    ) -> models.AnalyzeFaceResponse:
        """
        对请求图片进行五官定位（也称人脸关键点定位），计算构成人脸轮廓的 90 个点，包括眉毛（左右各 8 点）、眼睛（左右各 8 点）、鼻子（13 点）、嘴巴（22 点）、脸型轮廓（21 点）、眼珠[或瞳孔]（2点）。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareFace(
            self,
            request: models.CompareFaceRequest,
            opts: Dict = None,
    ) -> models.CompareFaceResponse:
        """
        对两张图片中的人脸进行相似度比对，返回人脸相似度分数。

        若您需要判断 “此人是否是某人”，即验证某张图片中的人是否是已知身份的某人，如常见的人脸登录场景，建议使用[人脸验证](https://cloud.tencent.com/document/product/867/44983)或[人员验证](https://cloud.tencent.com/document/product/867/44982)接口。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "CompareFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareMaskFace(
            self,
            request: models.CompareMaskFaceRequest,
            opts: Dict = None,
    ) -> models.CompareMaskFaceResponse:
        """
        对两张图片中的人脸进行相似度比对，返回人脸相似度分数。

        防疫场景人脸比对接口可在人脸戴口罩情况下使用，口罩遮挡程度最高可以遮挡鼻尖。

        如图片人脸不存在防疫场景下戴口罩的情况，建议使用人脸比对服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CompareMaskFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareMaskFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyPerson(
            self,
            request: models.CopyPersonRequest,
            opts: Dict = None,
    ) -> models.CopyPersonResponse:
        """
        将已存在于某人员库的人员复制到其他人员库，该人员的描述信息不会被复制。单个人员最多只能同时存在100个人员库中。
        >
        - 注：若该人员创建时算法模型版本为2.0，复制到非2.0算法模型版本的Group中时，复制操作将会失败。
        """
        
        kwargs = {}
        kwargs["action"] = "CopyPerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyPersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFace(
            self,
            request: models.CreateFaceRequest,
            opts: Dict = None,
    ) -> models.CreateFaceResponse:
        """
        将一组人脸图片添加到一个人员中。一个人员最多允许包含 5 张图片。若该人员存在多个人员库中，所有人员库中该人员图片均会增加。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroup(
            self,
            request: models.CreateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateGroupResponse:
        """
        用于创建一个空的人员库，如果人员库已存在返回错误。
        可根据需要创建自定义描述字段，用于辅助描述该人员库下的人员信息。

        1个APPID下最多创建10万个人员库（Group）、最多包含5000万张人脸（Face）。

        不同算法模型版本（FaceModelVersion）的人员库（Group）最多可包含人脸（Face）数不同。算法模型版本为2.0的人员库最多包含100万张人脸，算法模型版本为3.0的人员库最多可包含300万张人脸。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePerson(
            self,
            request: models.CreatePersonRequest,
            opts: Dict = None,
    ) -> models.CreatePersonResponse:
        """
        创建人员，添加人脸、姓名、性别及其他相关信息。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFace(
            self,
            request: models.DeleteFaceRequest,
            opts: Dict = None,
    ) -> models.DeleteFaceResponse:
        """
        删除一个人员下的人脸图片。如果该人员只有一张人脸图片，则返回错误。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroup(
            self,
            request: models.DeleteGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupResponse:
        """
        删除该人员库及包含的所有的人员。同时，人员对应的所有人脸信息将被删除。若某人员同时存在多个人员库中，该人员不会被删除，但属于该人员库中的自定义描述字段信息会被删除，属于其他人员库的自定义描述字段信息不受影响。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePerson(
            self,
            request: models.DeletePersonRequest,
            opts: Dict = None,
    ) -> models.DeletePersonResponse:
        """
        删除该人员信息，此操作会导致所有人员库均删除此人员。同时，该人员的所有人脸信息将被删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePersonFromGroup(
            self,
            request: models.DeletePersonFromGroupRequest,
            opts: Dict = None,
    ) -> models.DeletePersonFromGroupResponse:
        """
        从某人员库中删除人员，此操作仅影响该人员库。若该人员仅存在于指定的人员库中，该人员将被删除，其所有的人脸信息也将被删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePersonFromGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePersonFromGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFace(
            self,
            request: models.DetectFaceRequest,
            opts: Dict = None,
    ) -> models.DetectFaceResponse:
        """
        检测给定图片中的人脸（Face）的位置、相应的面部属性和人脸质量信息，位置包括 (x，y，w，h)，面部属性包括性别（gender）、年龄（age）、表情（expression）、魅力（beauty）、眼镜（glass）、发型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)，人脸质量信息包括整体质量分（score）、模糊分（sharpness）、光照分（brightness）和五官遮挡分（completeness）。


        其中，人脸质量信息主要用于评价输入的人脸图片的质量。在使用人脸识别服务时，建议您对输入的人脸图片进行质量检测，提升后续业务处理的效果。该功能的应用场景包括：

        1） 人员库[创建人员](https://cloud.tencent.com/document/product/867/45014)/[增加人脸](https://cloud.tencent.com/document/product/867/45016)：保证人员人脸信息的质量，便于后续的业务处理。

        2） [人脸搜索](https://cloud.tencent.com/document/product/867/44994)：保证输入的图片质量，快速准确匹配到对应的人员。

        3） [人脸验证](https://cloud.tencent.com/document/product/867/44983)：保证人脸信息的质量，避免明明是本人却认证不通过的情况。

        4） 人脸融合：保证上传的人脸质量，人脸融合的效果更好。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFaceAttributes(
            self,
            request: models.DetectFaceAttributesRequest,
            opts: Dict = None,
    ) -> models.DetectFaceAttributesResponse:
        """
        检测给定图片中的人脸（Face）的位置、相应的面部属性和人脸质量信息，位置包括 (x，y，w，h)，面部属性包括性别（gender）、年龄（age）、表情（expression）、魅力（beauty）、眼镜（glass）、发型（hair）、口罩（mask）和姿态 (pitch，roll，yaw)。


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
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFaceAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectFaceSimilarity(
            self,
            request: models.DetectFaceSimilarityRequest,
            opts: Dict = None,
    ) -> models.DetectFaceSimilarityResponse:
        """
        对两张图片中的人脸进行相似度比对，返回人脸相似度分数。

        若您需要判断 “此人是否是某人”，即验证某张图片中的人是否是已知身份的某人，如常见的人脸登录场景，建议使用[人脸验证](https://cloud.tencent.com/document/product/867/44983)或[人员验证](https://cloud.tencent.com/document/product/867/44982)接口。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectFaceSimilarity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectFaceSimilarityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetectLiveFaceAccurate(
            self,
            request: models.DetectLiveFaceAccurateRequest,
            opts: Dict = None,
    ) -> models.DetectLiveFaceAccurateResponse:
        """
        人脸静态活体检测（高精度版）可用于对用户上传的静态图片进行防翻拍活体检测，以判断是否是翻拍图片。

        相比现有静态活体检测服务，高精度版在维持高真人通过率的前提下，增强了对高清屏幕、裁剪纸片、3D面具等攻击的防御能力，攻击拦截率约为业内同类型产品形态4-5倍。同时支持多场景人脸核验，满足移动端、PC端各类型场景的图片活体检验需求，适用于各个行业不同的活体检验应用。

        人脸静态活体检测（高精度版）接口于2022年8月1日 00:00起正式开始计费，采取后付费按量计费模式，详见[计费概述](https://cloud.tencent.com/document/product/867/17640)。
        """
        
        kwargs = {}
        kwargs["action"] = "DetectLiveFaceAccurate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetectLiveFaceAccurateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupInfo(
            self,
            request: models.GetGroupInfoRequest,
            opts: Dict = None,
    ) -> models.GetGroupInfoResponse:
        """
        获取人员库信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetGroupList(
            self,
            request: models.GetGroupListRequest,
            opts: Dict = None,
    ) -> models.GetGroupListResponse:
        """
        获取人员库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonBaseInfo(
            self,
            request: models.GetPersonBaseInfoRequest,
            opts: Dict = None,
    ) -> models.GetPersonBaseInfoResponse:
        """
        获取指定人员的信息，包括姓名、性别、人脸等。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonGroupInfo(
            self,
            request: models.GetPersonGroupInfoRequest,
            opts: Dict = None,
    ) -> models.GetPersonGroupInfoResponse:
        """
        获取指定人员的信息，包括加入的人员库、描述内容等。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonList(
            self,
            request: models.GetPersonListRequest,
            opts: Dict = None,
    ) -> models.GetPersonListResponse:
        """
        获取指定人员库中的人员列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPersonListNum(
            self,
            request: models.GetPersonListNumRequest,
            opts: Dict = None,
    ) -> models.GetPersonListNumResponse:
        """
        获取指定人员库中人员数量。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPersonListNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPersonListNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUpgradeGroupFaceModelVersionJobList(
            self,
            request: models.GetUpgradeGroupFaceModelVersionJobListRequest,
            opts: Dict = None,
    ) -> models.GetUpgradeGroupFaceModelVersionJobListResponse:
        """
        避免官网歧义

        获取人员库升级任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetUpgradeGroupFaceModelVersionJobList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUpgradeGroupFaceModelVersionJobListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetUpgradeGroupFaceModelVersionResult(
            self,
            request: models.GetUpgradeGroupFaceModelVersionResultRequest,
            opts: Dict = None,
    ) -> models.GetUpgradeGroupFaceModelVersionResultResponse:
        """
        避免官网歧义

        人员库升级结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "GetUpgradeGroupFaceModelVersionResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetUpgradeGroupFaceModelVersionResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGroup(
            self,
            request: models.ModifyGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyGroupResponse:
        """
        修改人员库名称、备注、自定义描述字段名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonBaseInfo(
            self,
            request: models.ModifyPersonBaseInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonBaseInfoResponse:
        """
        修改人员信息，包括名称、性别等。人员名称和性别修改会同步到包含该人员的所有人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPersonGroupInfo(
            self,
            request: models.ModifyPersonGroupInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyPersonGroupInfoResponse:
        """
        修改指定人员库人员描述内容。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPersonGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPersonGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevertGroupFaceModelVersion(
            self,
            request: models.RevertGroupFaceModelVersionRequest,
            opts: Dict = None,
    ) -> models.RevertGroupFaceModelVersionResponse:
        """
        同理

        本接口用于回滚人员库的人脸识别算法模型版本。单个人员库有且仅有一次回滚机会。

        回滚操作会在10s内生效，回滚操作中，您对人员库的操作可能会失效。
        """
        
        kwargs = {}
        kwargs["action"] = "RevertGroupFaceModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevertGroupFaceModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFaces(
            self,
            request: models.SearchFacesRequest,
            opts: Dict = None,
    ) -> models.SearchFacesResponse:
        """
        用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，识别结果按照相似度从大到小排序。

        支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        与[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而人员搜索及人员搜索按库返回接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。


        本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)结合使用。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        >
        - 不可同时搜索不同算法模型版本（FaceModelVersion）的人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchFacesReturnsByGroup(
            self,
            request: models.SearchFacesReturnsByGroupRequest,
            opts: Dict = None,
    ) -> models.SearchFacesReturnsByGroupResponse:
        """
        用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。

        支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        与[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口不同的是，本接口将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员搜索](https://cloud.tencent.com/document/product/867/44992)及[人员搜索按库返回](https://cloud.tencent.com/document/product/867/44991)接口 会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使搜索更加准确。

        本接口需与[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)结合使用。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。

        >
        - 不可同时搜索不同算法模型版本（FaceModelVersion）的人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchFacesReturnsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchFacesReturnsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchPersons(
            self,
            request: models.SearchPersonsRequest,
            opts: Dict = None,
    ) -> models.SearchPersonsResponse:
        """
        用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照相似度从大到小排列。

        支持一次性识别图片中的最多 10 张人脸，支持一次性跨 100 个人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/44994)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/44993)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPersons"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchPersonsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchPersonsReturnsByGroup(
            self,
            request: models.SearchPersonsReturnsByGroupRequest,
            opts: Dict = None,
    ) -> models.SearchPersonsReturnsByGroupResponse:
        """
        用于对一张待识别的人脸图片，在一个或多个人员库中识别出最相似的 TopK 人员，按照**人员库的维度**以人员相似度从大到小顺序排列。

        支持一次性识别图片中的最多 10 张人脸，支持跨人员库（Group）搜索。

        单次搜索的人员库人脸总数量和人员库的算法模型版本（FaceModelVersion）相关。算法模型版本为2.0的人员库，单次搜索人员库人脸总数量不得超过 100 万张；算法模型版本为3.0的人员库，单次搜索人员库人脸总数量不得超过 300 万张。

        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person 下有4张 Face ，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员搜索（确定待识别的人脸图片是某人）更加准确。而[人脸搜索](https://cloud.tencent.com/document/product/867/44994)及[人脸搜索按库返回接口](https://cloud.tencent.com/document/product/867/44993)将该人员（Person）下的每个人脸（Face）都作为单独个体进行搜索。
        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "SearchPersonsReturnsByGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchPersonsReturnsByGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeGroupFaceModelVersion(
            self,
            request: models.UpgradeGroupFaceModelVersionRequest,
            opts: Dict = None,
    ) -> models.UpgradeGroupFaceModelVersionResponse:
        """
        避免官网歧义

        升级人员库。升级过程中，人员库仍然为原算法版本，人员库相关操作仍然支持。升级完成后，人员库为新算法版本。
        单个人员库有且仅支持一次回滚操作。

        升级是一个耗时的操作，执行时间与人员库的人脸数相关，升级的人员库中的人脸数越多，升级的耗时越长。升级接口是个异步任务，调用成功后返回JobId，通过GetUpgradeGroupFaceModelVersionResult查询升级进度和结果。如果升级成功，人员库版本将切换到新版本。如果想回滚到旧版本，可以调用RevertGroupFaceModelVersion进行回滚。

        注：某些接口无法进行跨人员库版本操作，例如SearchFaces，SearchPersons和CopyPerson等。当业务有多个Group操作的场景时，如同时搜索Group1和Group2，如果升级了Group1，此时Group1和Group2版本不同，造成了跨版本操作，将导致Search接口无法正常执行，返回不允许执行跨版本操作错误，升级前需考虑业务是否有多库操作的场景，否则会影响线上接口表现。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeGroupFaceModelVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeGroupFaceModelVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyFace(
            self,
            request: models.VerifyFaceRequest,
            opts: Dict = None,
    ) -> models.VerifyFaceResponse:
        """
        给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)。

        与[人脸比对](https://cloud.tencent.com/document/product/867/44987)接口不同的是，人脸验证用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而[人脸比对](https://cloud.tencent.com/document/product/867/44987)用于判断两张人脸的相似度。

        与[人员验证](https://cloud.tencent.com/document/product/867/44982)接口不同的是，人脸验证将该人员（Person）下的每个人脸（Face）都作为单独个体进行验证，而[人员验证](https://cloud.tencent.com/document/product/867/44982)会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个 Person下有4张 Face，人员验证接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。

        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyPerson(
            self,
            request: models.VerifyPersonRequest,
            opts: Dict = None,
    ) -> models.VerifyPersonResponse:
        """
        给定一张人脸图片和一个 PersonId，判断图片中的人和 PersonId 对应的人是否为同一人。PersonId 请参考[人员库管理相关接口](https://cloud.tencent.com/document/product/867/45015)。
        本接口会将该人员（Person）下的所有人脸（Face）进行融合特征处理，即若某个Person下有4张 Face，本接口会将4张 Face 的特征进行融合处理，生成对应这个 Person 的特征，使人员验证（确定待识别的人脸图片是某人员）更加准确。

         和人脸比对相关接口不同的是，人脸验证相关接口用于判断 “此人是否是此人”，“此人”的信息已存于人员库中，“此人”可能存在多张人脸图片；而人脸比对相关接口用于判断两张人脸的相似度。


        >
        - 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。
        - 仅支持算法模型版本（FaceModelVersion）为3.0的人员库。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyPerson"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyPersonResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)