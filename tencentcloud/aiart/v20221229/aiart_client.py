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
from tencentcloud.aiart.v20221229 import models


class AiartClient(AbstractClient):
    _apiVersion = '2022-12-29'
    _endpoint = 'aiart.tencentcloudapi.com'
    _service = 'aiart'


    def ChangeClothes(self, request):
        """上传正面全身模特照和服装平铺图，生成模特换装后的图片。
        生成的换装图片分辨率和模特照分辨率一致。
        模特换装默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for ChangeClothes.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ChangeClothesRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ChangeClothesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeClothes", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeClothesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateAvatar(self, request):
        """百变头像接口将根据输入的人像照片，生成风格百变的头像。
        百变头像默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for GenerateAvatar.
        :type request: :class:`tencentcloud.aiart.v20221229.models.GenerateAvatarRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.GenerateAvatarResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateAvatar", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateAvatarResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageInpaintingRemoval(self, request):
        """局部消除接口通过图像 mask 指定需要消除的人、物、文字等区域，在选定区域对图像内容进行消除与重绘补全。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。

        :param request: Request instance for ImageInpaintingRemoval.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ImageInpaintingRemovalRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ImageInpaintingRemovalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageInpaintingRemoval", params, headers=headers)
            response = json.loads(body)
            model = models.ImageInpaintingRemovalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageOutpainting(self, request):
        """扩图接口支持对输入图像按指定宽高比实现智能扩图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。

        :param request: Request instance for ImageOutpainting.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ImageOutpaintingRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ImageOutpaintingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageOutpainting", params, headers=headers)
            response = json.loads(body)
            model = models.ImageOutpaintingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageToImage(self, request):
        """图像风格化（图生图）接口提供生成式的图生图风格转化能力，将根据输入的图像及文本描述，智能生成风格转化后的图像。建议避免输入人像过小、姿势复杂、人数较多的人像图片。
        图像风格化（图生图）默认提供3个并发任务数，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for ImageToImage.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ImageToImageRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ImageToImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDrawPortraitJob(self, request):
        """AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        生成图片分为提交任务和查询任务2个接口：

        - 提交生成写真图片任务：选择风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 生成写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。

        :param request: Request instance for QueryDrawPortraitJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.QueryDrawPortraitJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.QueryDrawPortraitJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDrawPortraitJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDrawPortraitJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryGlamPicJob(self, request):
        """AI 美照接口将根据模板为用户生成精美照片。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个美照生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        AI 美照默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for QueryGlamPicJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.QueryGlamPicJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.QueryGlamPicJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryGlamPicJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryGlamPicJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMemeJob(self, request):
        """表情动图生成接口将静态照片制作成动态的表情包。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个表情动图生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        表情动图生成默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for QueryMemeJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.QueryMemeJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.QueryMemeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMemeJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMemeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryTextToImageProJob(self, request):
        """本接口已迁移至腾讯混元大模型-混元生图，即将停止此处维护，可切换至 [混元生图 API](https://cloud.tencent.com/document/product/1729/105970) 继续使用。
        文生图（高级版）接口基于高级版文生图大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个文生图（高级版）异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。文生图（高级版）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for QueryTextToImageProJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.QueryTextToImageProJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.QueryTextToImageProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTextToImageProJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTextToImageProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryTrainPortraitModelJob(self, request):
        """AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        如果选择免训练模式无需调用本接口。
        训练模型分为提交任务和查询任务2个接口：

        - 提交训练写真模型任务：完成上传图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。

        :param request: Request instance for QueryTrainPortraitModelJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.QueryTrainPortraitModelJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.QueryTrainPortraitModelJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTrainPortraitModelJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTrainPortraitModelJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefineImage(self, request):
        """将图像变清晰，增强图像细节。变清晰后的图片将保持原图比例，长边为2048。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。

        :param request: Request instance for RefineImage.
        :type request: :class:`tencentcloud.aiart.v20221229.models.RefineImageRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.RefineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefineImage", params, headers=headers)
            response = json.loads(body)
            model = models.RefineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceBackground(self, request):
        """商品背景生成接口根据指定的背景描述 Prompt，将商品图中的原背景替换为自定义的新背景并保留商品主体形象，实现商品背景的自由生成与更换。

        商品背景生成默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for ReplaceBackground.
        :type request: :class:`tencentcloud.aiart.v20221229.models.ReplaceBackgroundRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.ReplaceBackgroundResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceBackground", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceBackgroundResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SketchToImage(self, request):
        """线稿生图接口支持上传一张黑白线稿图，按照指定的主体对象以及样式、颜色、材质、风格等的文本描述prompt ，对线稿图进行色彩填充与细节描绘，得到一张完整绘制的图像。生成图分辨率默认为1024:1024。
        线稿生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SketchToImage.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SketchToImageRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SketchToImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SketchToImage", params, headers=headers)
            response = json.loads(body)
            model = models.SketchToImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitDrawPortraitJob(self, request):
        """AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        生成图片分为提交任务和查询任务2个接口：

        - 提交生成写真图片任务：选择风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 生成写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        提交生成写真图片任务默认提供1个并发。

        :param request: Request instance for SubmitDrawPortraitJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SubmitDrawPortraitJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SubmitDrawPortraitJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitDrawPortraitJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitDrawPortraitJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitGlamPicJob(self, request):
        """AI 美照接口将根据模板为用户生成精美照片。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个美照生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        AI 美照默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SubmitGlamPicJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SubmitGlamPicJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SubmitGlamPicJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitGlamPicJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitGlamPicJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitMemeJob(self, request):
        """表情动图生成接口将静态照片制作成动态的表情包。分为提交任务和查询任务2个接口。

        - 提交任务：提交一个表情动图生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        表情动图生成默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SubmitMemeJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SubmitMemeJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SubmitMemeJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitMemeJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitMemeJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTextToImageProJob(self, request):
        """本接口已迁移至腾讯混元大模型-混元生图，即将停止此处维护，可切换至 [混元生图 API](https://cloud.tencent.com/document/product/1729/105969) 继续使用。
        文生图（高级版）接口基于高级版文生图大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个文生图（高级版）异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。文生图（高级版）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SubmitTextToImageProJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SubmitTextToImageProJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SubmitTextToImageProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTextToImageProJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTextToImageProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTrainPortraitModelJob(self, request):
        """AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        如果选择免训练模式无需调用本接口。
        训练模型分为提交任务和查询任务2个接口：
        - 提交训练写真模型任务：完成上传图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        提交训练写真模型任务按并发计费，无默认并发额度。

        :param request: Request instance for SubmitTrainPortraitModelJob.
        :type request: :class:`tencentcloud.aiart.v20221229.models.SubmitTrainPortraitModelJobRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.SubmitTrainPortraitModelJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTrainPortraitModelJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTrainPortraitModelJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToImage(self, request):
        """**本接口已迁移至腾讯混元大模型-文生图轻量版，即将停止此处维护，可切换至 [文生图轻量版 API](https://cloud.tencent.com/document/product/1729/108738) 继续使用。**

        智能文生图接口基于文生图（标准版）模型，将根据输入的文本描述，智能生成与之相关的结果图。

        智能文生图默认提供3个并发任务数，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for TextToImage.
        :type request: :class:`tencentcloud.aiart.v20221229.models.TextToImageRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.TextToImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToImage", params, headers=headers)
            response = json.loads(body)
            model = models.TextToImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadTrainPortraitImages(self, request):
        """AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        本接口用于上传人像图片并指定对应的写真模型 ID。上传的图片要求是同一个人，建议上传单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的图片。
        可选模式：
        - 常规训练模式：上传20 - 25张图片用于模型训练，完成训练后可生成写真图片。
        - 快速训练模式：仅需上传1张图片用于模型训练，训练速度更快，完成训练后可生成写真图片。
        - 免训练模式：仅需上传1张图片，跳过训练环节，直接生成写真图片。

        上传写真训练图片默认提供1个并发。

        :param request: Request instance for UploadTrainPortraitImages.
        :type request: :class:`tencentcloud.aiart.v20221229.models.UploadTrainPortraitImagesRequest`
        :rtype: :class:`tencentcloud.aiart.v20221229.models.UploadTrainPortraitImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadTrainPortraitImages", params, headers=headers)
            response = json.loads(body)
            model = models.UploadTrainPortraitImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))