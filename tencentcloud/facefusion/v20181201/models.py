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


class DescribeMaterialListRequest(AbstractModel):
    """DescribeMaterialList请求参数结构体

    """

    def __init__(self):
        """
        :param ActivityId: 活动Id
        :type ActivityId: int
        :param MaterialId: 素材Id
        :type MaterialId: str
        :param Limit: 每次拉取条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.ActivityId = None
        self.MaterialId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ActivityId = params.get("ActivityId")
        self.MaterialId = params.get("MaterialId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeMaterialListResponse(AbstractModel):
    """DescribeMaterialList返回参数结构体

    """

    def __init__(self):
        """
        :param MaterialInfos: 素材列表数据
        :type MaterialInfos: list of PublicMaterialInfos
        :param Count: 素材条数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaterialInfos = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MaterialInfos") is not None:
            self.MaterialInfos = []
            for item in params.get("MaterialInfos"):
                obj = PublicMaterialInfos()
                obj._deserialize(item)
                self.MaterialInfos.append(obj)
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class FaceFusionLiteRequest(AbstractModel):
    """FaceFusionLite请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。默认url, url有效期为30天。
        :type RspImgType: str
        :param CelebrityIdentify: 请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
        :type CelebrityIdentify: int
        :param Engine: 算法引擎参数:  1）选脸版 - youturecreat; 2）优享版 - youtu1vN； 3）畅享版 - ptu； 4）随机 - ALL;  默认为活动选择的算法
        :type Engine: str
        """
        self.ProjectId = None
        self.ModelId = None
        self.MergeInfos = None
        self.RspImgType = None
        self.CelebrityIdentify = None
        self.Engine = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        if params.get("MergeInfos") is not None:
            self.MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self.MergeInfos.append(obj)
        self.RspImgType = params.get("RspImgType")
        self.CelebrityIdentify = params.get("CelebrityIdentify")
        self.Engine = params.get("Engine")


class FaceFusionLiteResponse(AbstractModel):
    """FaceFusionLite返回参数结构体

    """

    def __init__(self):
        """
        :param Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type Image: str
        :param ReviewResultSet: 鉴政结果
注意：此字段可能返回 null，表示取不到有效值。
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
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为30天。
        :type RspImgType: str
        :param PornDetect: 历史遗留字段，无需填写。因为融合只需提取人脸特征，不需要鉴黄。
        :type PornDetect: int
        :param CelebrityIdentify: 0表示不需要鉴政，1表示需要鉴政。默认值为0。
请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
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
        :param Image: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type Image: str
        :param ReviewResultSet: 鉴政结果
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


class FaceInfo(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        """
        :param X: 人脸框的横坐标
        :type X: int
        :param Y: 人脸框的纵坐标
        :type Y: int
        :param Width: 人脸框的宽度
        :type Width: int
        :param Height: 人脸框的高度
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class FaceRect(AbstractModel):
    """人脸框信息

    """

    def __init__(self):
        """
        :param X: 人脸框左上角横坐标。
        :type X: int
        :param Y: 人脸框左上角纵坐标。
        :type Y: int
        :param Width: 人脸框宽度。
        :type Width: int
        :param Height: 人脸框高度。
        :type Height: int
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")


class FuseFaceRequest(AbstractModel):
    """FuseFace请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 活动 ID，请在人脸融合控制台查看。
        :type ProjectId: str
        :param ModelId: 素材 ID，请在人脸融合控制台查看。
        :type ModelId: str
        :param RspImgType: 返回图像方式（url 或 base64) ，二选一。url有效期为30天。
        :type RspImgType: str
        :param MergeInfos: 用户人脸图片、素材模板图的人脸位置信息。
        :type MergeInfos: list of MergeInfo
        :param FuseProfileDegree: 脸型融合比例，数值越高，融合后的脸型越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中脸型参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseProfileDegree: int
        :param FuseFaceDegree: 五官融合比例，数值越高，融合后的五官越像素材人物。取值范围[0,100] 
若此参数不填写，则使用人脸融合控制台中五官参数数值。（换脸版算法暂不支持此参数调整）
        :type FuseFaceDegree: int
        :param CelebrityIdentify: 0表示不需要鉴政，1表示需要鉴政。默认值为0。
请注意，鉴政服务开启后，您需要根据返回结果自行判断是否调整您的业务逻辑。例如提示您的用户图片非法，请更换图片。
        :type CelebrityIdentify: int
        """
        self.ProjectId = None
        self.ModelId = None
        self.RspImgType = None
        self.MergeInfos = None
        self.FuseProfileDegree = None
        self.FuseFaceDegree = None
        self.CelebrityIdentify = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ModelId = params.get("ModelId")
        self.RspImgType = params.get("RspImgType")
        if params.get("MergeInfos") is not None:
            self.MergeInfos = []
            for item in params.get("MergeInfos"):
                obj = MergeInfo()
                obj._deserialize(item)
                self.MergeInfos.append(obj)
        self.FuseProfileDegree = params.get("FuseProfileDegree")
        self.FuseFaceDegree = params.get("FuseFaceDegree")
        self.CelebrityIdentify = params.get("CelebrityIdentify")


class FuseFaceResponse(AbstractModel):
    """FuseFace返回参数结构体

    """

    def __init__(self):
        """
        :param FusedImage: RspImgType 为 url 时，返回结果的 url， RspImgType 为 base64 时返回 base64 数据。
        :type FusedImage: str
        :param ReviewResultSet: 鉴政结果。该数组的顺序和请求中mergeinfo的顺序一致，一一对应
注意：此字段可能返回 null，表示取不到有效值。
        :type ReviewResultSet: list of FuseFaceReviewResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FusedImage = None
        self.ReviewResultSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FusedImage = params.get("FusedImage")
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
        :param Field: 保留字段
        :type Field: str
        :param Label: 人员名称
        :type Label: str
        :param Confidence: 对应识别label的置信度，分数越高意味涉政可能性越大。 
0到70，Suggestion建议为PASS； 
70到80，Suggestion建议为REVIEW； 
80到100，Suggestion建议为BLOCK。
        :type Confidence: float
        :param Suggestion: 识别场景的审核结论：  
PASS：正常 
REVIEW：疑似  
BLOCK：违规
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
        :param Category: 保留字段
        :type Category: str
        :param Code: 状态码， 0为处理成功，其他值为处理失败
        :type Code: str
        :param CodeDescription: 对应状态码信息描述
        :type CodeDescription: str
        :param Confidence: 保留字段
        :type Confidence: float
        :param Suggestion: 保留字段
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


class MaterialFaceList(AbstractModel):
    """人脸信息

    """

    def __init__(self):
        """
        :param FaceId: 人脸序号
        :type FaceId: str
        :param FaceInfo: 人脸框信息
        :type FaceInfo: :class:`tencentcloud.facefusion.v20181201.models.FaceInfo`
        """
        self.FaceId = None
        self.FaceInfo = None


    def _deserialize(self, params):
        self.FaceId = params.get("FaceId")
        if params.get("FaceInfo") is not None:
            self.FaceInfo = FaceInfo()
            self.FaceInfo._deserialize(params.get("FaceInfo"))


class MergeInfo(AbstractModel):
    """人脸图片和待被融合的素材模板图的人脸位置信息。

    """

    def __init__(self):
        """
        :param Image: 输入图片base64
        :type Image: str
        :param Url: 输入图片url
        :type Url: str
        :param InputImageFaceRect: 上传的图片人脸位置信息（人脸框）
        :type InputImageFaceRect: :class:`tencentcloud.facefusion.v20181201.models.FaceRect`
        :param TemplateFaceID: 控制台上传的素材人脸ID
        :type TemplateFaceID: str
        """
        self.Image = None
        self.Url = None
        self.InputImageFaceRect = None
        self.TemplateFaceID = None


    def _deserialize(self, params):
        self.Image = params.get("Image")
        self.Url = params.get("Url")
        if params.get("InputImageFaceRect") is not None:
            self.InputImageFaceRect = FaceRect()
            self.InputImageFaceRect._deserialize(params.get("InputImageFaceRect"))
        self.TemplateFaceID = params.get("TemplateFaceID")


class PublicMaterialInfos(AbstractModel):
    """素材信息

    """

    def __init__(self):
        """
        :param MaterialId: 素材Id
        :type MaterialId: str
        :param MaterialStatus: 素材状态
        :type MaterialStatus: int
        :param BlendParamPtu: 脸型参数P图
        :type BlendParamPtu: int
        :param PositionParamPtu: 五官参数P图
        :type PositionParamPtu: int
        :param BlendParamYoutu: 脸型参数优图
        :type BlendParamYoutu: int
        :param PositionParamYoutu: 五官参数优图
        :type PositionParamYoutu: int
        :param Url: 素材COS地址
        :type Url: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 修改时间
        :type UpdateTime: str
        :param MaterialFaceList: 人脸信息
        :type MaterialFaceList: list of MaterialFaceList
        """
        self.MaterialId = None
        self.MaterialStatus = None
        self.BlendParamPtu = None
        self.PositionParamPtu = None
        self.BlendParamYoutu = None
        self.PositionParamYoutu = None
        self.Url = None
        self.CreateTime = None
        self.UpdateTime = None
        self.MaterialFaceList = None


    def _deserialize(self, params):
        self.MaterialId = params.get("MaterialId")
        self.MaterialStatus = params.get("MaterialStatus")
        self.BlendParamPtu = params.get("BlendParamPtu")
        self.PositionParamPtu = params.get("PositionParamPtu")
        self.BlendParamYoutu = params.get("BlendParamYoutu")
        self.PositionParamYoutu = params.get("PositionParamYoutu")
        self.Url = params.get("Url")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("MaterialFaceList") is not None:
            self.MaterialFaceList = []
            for item in params.get("MaterialFaceList"):
                obj = MaterialFaceList()
                obj._deserialize(item)
                self.MaterialFaceList.append(obj)