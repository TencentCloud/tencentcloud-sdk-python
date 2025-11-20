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
from tencentcloud.ft.v20200304 import models
from typing import Dict


class FtClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ft.tencentcloudapi.com'
    _service = 'ft'

    async def CancelFaceMorphJob(
            self,
            request: models.CancelFaceMorphJobRequest,
            opts: Dict = None,
    ) -> models.CancelFaceMorphJobResponse:
        """
        撤销人像渐变任务请求
        """
        
        kwargs = {}
        kwargs["action"] = "CancelFaceMorphJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelFaceMorphJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeAgePic(
            self,
            request: models.ChangeAgePicRequest,
            opts: Dict = None,
    ) -> models.ChangeAgePicResponse:
        """
        用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸变老或变年轻的图片，支持实现人脸不同年龄的变化。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeAgePic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeAgePicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FaceCartoonPic(
            self,
            request: models.FaceCartoonPicRequest,
            opts: Dict = None,
    ) -> models.FaceCartoonPicResponse:
        """
        输入一张人脸照片，生成个性化的二次元动漫形象，可用于打造个性头像、趣味活动、特效类应用等场景，提升社交娱乐的体验。
        """
        
        kwargs = {}
        kwargs["action"] = "FaceCartoonPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FaceCartoonPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MorphFace(
            self,
            request: models.MorphFaceRequest,
            opts: Dict = None,
    ) -> models.MorphFaceResponse:
        """
        输入2-5张人脸照片，生成一段以人脸为焦点的渐变视频或GIF图，支持自定义图片播放速度、视频每秒传输帧数，可用于短视频、表情包、创意H5等应用场景，丰富静态图片的玩法。
        """
        
        kwargs = {}
        kwargs["action"] = "MorphFace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MorphFaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryFaceMorphJob(
            self,
            request: models.QueryFaceMorphJobRequest,
            opts: Dict = None,
    ) -> models.QueryFaceMorphJobResponse:
        """
        查询人像渐变处理进度
        """
        
        kwargs = {}
        kwargs["action"] = "QueryFaceMorphJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryFaceMorphJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwapGenderPic(
            self,
            request: models.SwapGenderPicRequest,
            opts: Dict = None,
    ) -> models.SwapGenderPicResponse:
        """
        用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸性别转换的图片。男变女可实现美颜、淡妆、加刘海和长发的效果；女变男可实现加胡须、变短发的效果。
        """
        
        kwargs = {}
        kwargs["action"] = "SwapGenderPic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwapGenderPicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)