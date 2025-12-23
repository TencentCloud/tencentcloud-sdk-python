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
from tencentcloud.aiart.v20221229 import models
from typing import Dict


class AiartClient(AbstractClient):
    _apiVersion = '2022-12-29'
    _endpoint = 'aiart.tencentcloudapi.com'
    _service = 'aiart'

    async def ChangeClothes(
            self,
            request: models.ChangeClothesRequest,
            opts: Dict = None,
    ) -> models.ChangeClothesResponse:
        """
        上传正面全身模特照和服装平铺图，生成模特换装后的图片。
        生成的换装图片分辨率和模特照分辨率一致。
        模特换装默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeClothes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeClothesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateToImageJob(
            self,
            request: models.DescribeTemplateToImageJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateToImageJobResponse:
        """
        查询图片特效任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateToImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateToImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateAvatar(
            self,
            request: models.GenerateAvatarRequest,
            opts: Dict = None,
    ) -> models.GenerateAvatarResponse:
        """
        百变头像接口将根据输入的人像照片，生成风格百变的头像。
        百变头像默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateAvatar"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateAvatarResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageInpaintingRemoval(
            self,
            request: models.ImageInpaintingRemovalRequest,
            opts: Dict = None,
    ) -> models.ImageInpaintingRemovalResponse:
        """
        局部消除接口通过图像 mask 指定需要消除的人、物、文字等区域，在选定区域对图像内容进行消除与重绘补全。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageInpaintingRemoval"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageInpaintingRemovalResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageOutpainting(
            self,
            request: models.ImageOutpaintingRequest,
            opts: Dict = None,
    ) -> models.ImageOutpaintingResponse:
        """
        扩图接口支持对输入图像按指定宽高比实现智能扩图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageOutpainting"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageOutpaintingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageToImage(
            self,
            request: models.ImageToImageRequest,
            opts: Dict = None,
    ) -> models.ImageToImageResponse:
        """
        图像风格化（图生图）接口提供生成式的图生图风格转化能力，将根据输入的图像及文本描述，智能生成风格转化后的图像。建议避免输入人像过小、姿势复杂、人数较多的人像图片。
        图像风格化（图生图）默认提供3个并发任务数，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageToImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageToImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryDrawPortraitJob(
            self,
            request: models.QueryDrawPortraitJobRequest,
            opts: Dict = None,
    ) -> models.QueryDrawPortraitJobResponse:
        """
        AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        生成图片分为提交任务和查询任务2个接口：

        - 提交生成写真图片任务：选择风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 生成写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryDrawPortraitJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryDrawPortraitJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryGlamPicJob(
            self,
            request: models.QueryGlamPicJobRequest,
            opts: Dict = None,
    ) -> models.QueryGlamPicJobResponse:
        """
        AI 美照接口将根据模板为用户生成精美照片。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个美照生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        AI 美照默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryGlamPicJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryGlamPicJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryMemeJob(
            self,
            request: models.QueryMemeJobRequest,
            opts: Dict = None,
    ) -> models.QueryMemeJobResponse:
        """
        表情动图生成接口将静态照片制作成动态的表情包。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个表情动图生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        表情动图生成默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryMemeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryMemeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTextToImageJob(
            self,
            request: models.QueryTextToImageJobRequest,
            opts: Dict = None,
    ) -> models.QueryTextToImageJobResponse:
        """
        混元生图接口，基于混元大模型，根据输入的文本描述快速生成图片。
        默认提供0个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTextToImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTextToImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTextToImageProJob(
            self,
            request: models.QueryTextToImageProJobRequest,
            opts: Dict = None,
    ) -> models.QueryTextToImageProJobResponse:
        """
        本接口已迁移至腾讯混元大模型-混元生图，即将停止此处维护，可切换至 [混元生图 API](https://cloud.tencent.com/document/product/1729/105970) 继续使用。
        文生图（高级版）接口基于高级版文生图大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个文生图（高级版）异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。文生图（高级版）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTextToImageProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTextToImageProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTrainPortraitModelJob(
            self,
            request: models.QueryTrainPortraitModelJobRequest,
            opts: Dict = None,
    ) -> models.QueryTrainPortraitModelJobResponse:
        """
        AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        如果选择免训练模式无需调用本接口。
        训练模型分为提交任务和查询任务2个接口：

        - 提交训练写真模型任务：完成上传图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTrainPortraitModelJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTrainPortraitModelJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefineImage(
            self,
            request: models.RefineImageRequest,
            opts: Dict = None,
    ) -> models.RefineImageResponse:
        """
        将图像变清晰，增强图像细节。变清晰后的图片将保持原图比例，长边为2048。
        默认提供1个并发，代表最多能同时处理1个已提交的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "RefineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceBackground(
            self,
            request: models.ReplaceBackgroundRequest,
            opts: Dict = None,
    ) -> models.ReplaceBackgroundResponse:
        """
        商品背景生成接口根据指定的背景描述 Prompt，将商品图中的原背景替换为自定义的新背景并保留商品主体形象，实现商品背景的自由生成与更换。

        商品背景生成默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceBackground"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceBackgroundResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SketchToImage(
            self,
            request: models.SketchToImageRequest,
            opts: Dict = None,
    ) -> models.SketchToImageResponse:
        """
        线稿生图接口支持上传一张黑白线稿图，按照指定的主体对象以及样式、颜色、材质、风格等的文本描述prompt ，对线稿图进行色彩填充与细节描绘，得到一张完整绘制的图像。生成图分辨率默认为1024:1024。
        线稿生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SketchToImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SketchToImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitDrawPortraitJob(
            self,
            request: models.SubmitDrawPortraitJobRequest,
            opts: Dict = None,
    ) -> models.SubmitDrawPortraitJobResponse:
        """
        AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        生成图片分为提交任务和查询任务2个接口：

        - 提交生成写真图片任务：选择风格模板，提交一个生成写真图片异步任务，根据写真模型 ID 生成写真图片，获得任务 ID。
        - 查询生成写真图片任务：根据任务 ID 查询生成图片任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        提交生成写真图片任务默认提供1个并发。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitDrawPortraitJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitDrawPortraitJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitGlamPicJob(
            self,
            request: models.SubmitGlamPicJobRequest,
            opts: Dict = None,
    ) -> models.SubmitGlamPicJobResponse:
        """
        AI 美照接口将根据模板为用户生成精美照片。分为提交任务和查询任务2个接口。
        - 提交任务：提交一个美照生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        AI 美照默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitGlamPicJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitGlamPicJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitMemeJob(
            self,
            request: models.SubmitMemeJobRequest,
            opts: Dict = None,
    ) -> models.SubmitMemeJobResponse:
        """
        表情动图生成接口将静态照片制作成动态的表情包。分为提交任务和查询任务2个接口。

        - 提交任务：提交一个表情动图生成异步任务，获得任务 ID。
        - 查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。

        表情动图生成默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitMemeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitMemeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTemplateToImageJob(
            self,
            request: models.SubmitTemplateToImageJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTemplateToImageJobResponse:
        """
        提交图片特效任务
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTemplateToImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTemplateToImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTextToImageJob(
            self,
            request: models.SubmitTextToImageJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTextToImageJobResponse:
        """
        混元生图接口，基于混元大模型，根据输入的文本描述快速生成图片。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTextToImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTextToImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTextToImageProJob(
            self,
            request: models.SubmitTextToImageProJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTextToImageProJobResponse:
        """
        本接口已迁移至腾讯混元大模型-混元生图，即将停止此处维护，可切换至 [混元生图 API](https://cloud.tencent.com/document/product/1729/105969) 继续使用。
        文生图（高级版）接口基于高级版文生图大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个文生图（高级版）异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。文生图（高级版）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTextToImageProJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTextToImageProJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTrainPortraitModelJob(
            self,
            request: models.SubmitTrainPortraitModelJobRequest,
            opts: Dict = None,
    ) -> models.SubmitTrainPortraitModelJobResponse:
        """
        AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        如果选择免训练模式无需调用本接口。
        训练模型分为提交任务和查询任务2个接口：
        - 提交训练写真模型任务：完成上传图片后，提交一个训练写真模型异步任务，根据写真模型 ID 开始训练模型。
        - 查询训练写真模型任务：根据写真模型 ID 查询训练任务的处理状态、处理结果。

        每个写真模型自训练完成起1年内有效，有效期内可使用写真模型 ID 生成图片，期满后需要重新训练。
        提交训练写真模型任务按并发计费，无默认并发额度。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTrainPortraitModelJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTrainPortraitModelJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToImageLite(
            self,
            request: models.TextToImageLiteRequest,
            opts: Dict = None,
    ) -> models.TextToImageLiteResponse:
        """
        混元文生图接口，基于混元大模型，根据输入的文本描述智能生成图片
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "TextToImageLite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToImageLiteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToImageRapid(
            self,
            request: models.TextToImageRapidRequest,
            opts: Dict = None,
    ) -> models.TextToImageRapidResponse:
        """
        混元文生图接口，基于混元大模型，根据输入的文本描述智能生成图片
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "TextToImageRapid"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToImageRapidResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadTrainPortraitImages(
            self,
            request: models.UploadTrainPortraitImagesRequest,
            opts: Dict = None,
    ) -> models.UploadTrainPortraitImagesResponse:
        """
        AI 写真分为上传训练图片、训练写真模型（可选跳过）、生成写真图片3个环节，需要依次调用对应接口。
        本接口用于上传人像图片并指定对应的写真模型 ID。上传的图片要求是同一个人，建议上传单人、正脸、脸部区域占比较大、脸部清晰无遮挡、无大角度偏转、无夸张表情的图片。
        可选模式：
        - 常规训练模式：上传20 - 25张图片用于模型训练，完成训练后可生成写真图片。
        - 快速训练模式：仅需上传1张图片用于模型训练，训练速度更快，完成训练后可生成写真图片。
        - 免训练模式：仅需上传1张图片，跳过训练环节，直接生成写真图片。

        上传写真训练图片默认提供1个并发。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadTrainPortraitImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadTrainPortraitImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)