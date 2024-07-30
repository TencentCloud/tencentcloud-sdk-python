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
        """AI 写真提供 AI 写真形象照的训练与生成能力，分为上传训练图片、训练模型、生成图片3个环节，需要依次调用对应接口。
        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        生成图片分为提交任务和查询任务2个接口。
        - 提交生成写真图片任务：完成训练写真模型后，选择写真风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 开始生成人物形象在指定风格上的写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

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
        """AI 写真提供 AI 写真形象照的训练与生成能力，分为上传训练图片、训练模型、生成图片3个环节，需要依次调用对应接口。
        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        训练模型分为提交任务和查询任务2个接口。
        - 提交训练写真模型任务：完成上传训练图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。

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


    def SubmitDrawPortraitJob(self, request):
        """AI 写真提供 AI 写真形象照的训练与生成能力，分为上传训练图片、训练模型、生成图片3个环节，需要依次调用对应接口。
        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        生成图片分为提交任务和查询任务2个接口。
        - 提交生成写真图片任务：完成训练写真模型后，选择风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 开始生成人物形象在指定风格上的写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

        提交生成写真图片任务默认提供1个并发任务数。

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
        """AI 写真提供 AI 写真形象照的训练与生成能力，分为上传训练图片、训练模型、生成图片3个环节，需要依次调用对应接口。
        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        训练模型分为提交任务和查询任务2个接口。
        - 提交训练写真模型任务：完成上传训练图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。
        提交训练写真模型任务按并发任务数计费，无默认并发额度。

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
        """AI 写真提供 AI 写真形象照的训练与生成能力，分为上传训练图片、训练模型、生成图片3个环节，需要依次调用对应接口。
        本接口用于指定一个人物形象的写真模型 ID，上传用于训练该模型的图片。一个写真模型仅用于一个人物形象的写真生成，上传的训练图片要求所属同一人，建议上传单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的图片。
        上传写真训练图片默认提供1个并发任务数。

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