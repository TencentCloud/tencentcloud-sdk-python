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
from tencentcloud.lighthouse.v20200324 import models


class LighthouseClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'lighthouse.tencentcloudapi.com'
    _service = 'lighthouse'


    def ApplyDiskBackup(self, request):
        """本接口（ApplyDiskBackup）用于回滚指定云硬盘的备份点。
        * 仅支持回滚到原云硬盘。
        * 用于回滚的云硬盘备份点必须处于 NORMAL 状态。
          云硬盘备份点状态可以通过  [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379) 接口查询。
        * 回滚云硬盘备份点时，云硬盘的状态必须为 UNATTACHED或ATTACHED。
          云硬盘状态可通过 [DescribeDisks](https://cloud.tencent.com/document/api/1207/66093) 接口查询。
        * 如果云硬盘处于 ATTACHED状态，相关RUNNING 状态的实例会强制关机，然后回滚云硬盘备份点。

        :param request: Request instance for ApplyDiskBackup.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ApplyDiskBackupRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ApplyDiskBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyDiskBackup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyDiskBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyFirewallTemplate(self, request):
        """本接口 (ApplyFirewallTemplate) 用于应用防火墙模板到多个实例。

        :param request: Request instance for ApplyFirewallTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ApplyFirewallTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ApplyFirewallTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyFirewallTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyFirewallTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ApplyInstanceSnapshot(self, request):
        """本接口（ApplyInstanceSnapshot）用于回滚指定实例的系统盘快照。
        - 仅支持回滚到原系统盘。
        - 用于回滚的快照必须处于 NORMAL 状态。快照状态可以通过 [DescribeSnapshots](https://cloud.tencent.com/document/product/1207/54388) 接口查询，见输出参数中 SnapshotState 字段解释。
        - 回滚快照时，实例的状态必须为 STOPPED 或 RUNNING，可通过 [DescribeInstances](https://cloud.tencent.com/document/product/1207/47573) 接口查询实例状态。处于 RUNNING 状态的实例会强制关机，然后回滚快照。

        :param request: Request instance for ApplyInstanceSnapshot.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ApplyInstanceSnapshotRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ApplyInstanceSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyInstanceSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyInstanceSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateInstancesKeyPairs(self, request):
        """本接口（AssociateInstancesKeyPairs）用于绑定用户指定密钥对到实例。
        * 只支持 [RUNNING, STOPPED] 状态的 LINUX_UNIX 操作系统的实例。处于 RUNNING 状态的实例会强制关机，然后绑定。
        * 将密钥的公钥写入到实例的 SSH 配置当中，用户就可以通过该密钥的私钥来登录实例。
        * 如果实例原来绑定过密钥，那么原来的密钥将失效。
        * 如果实例原来是通过密码登录，绑定密钥后无法使用密码登录。
        * 支持批量操作。每次请求批量实例的上限为 100。如果批量实例存在不允许操作的实例，操作会以特定错误码返回。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for AssociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AssociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AssociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachCcn(self, request):
        """本接口 (AttachCcn) 用于建立与云联网的关联。

        :param request: Request instance for AttachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AttachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AttachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDisks(self, request):
        """本接口（AttachDisks）用于挂载一个或多个云硬盘。
        <li>只能挂载磁盘状态（DiskState）处于待挂载（UNATTACHED）状态的云硬盘，磁盘状态可通过接口查询云硬盘（DescribeDisks）获取</li>

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelShareBlueprintAcrossAccounts(self, request):
        """本接口（CancelShareBlueprintAcrossAccounts）用于取消镜像跨账号共享。
        指定的镜像ID必须为自定义镜像，且指定账号ID必须已进行共享。

        :param request: Request instance for CancelShareBlueprintAcrossAccounts.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CancelShareBlueprintAcrossAccountsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CancelShareBlueprintAcrossAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelShareBlueprintAcrossAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.CancelShareBlueprintAcrossAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBlueprint(self, request):
        """本接口 (CreateBlueprint) 用于创建镜像。

        :param request: Request instance for CreateBlueprint.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateBlueprintRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateBlueprintResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBlueprint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBlueprintResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDiskBackup(self, request):
        """本接口 ( CreateDiskBackup  ) 用于创建指定云硬盘（当前只支持数据盘）的备份点。

        :param request: Request instance for CreateDiskBackup.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateDiskBackupRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateDiskBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDiskBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDiskBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisks(self, request):
        """本接口(CreateDisks)用于创建一个或多个云硬盘。

        :param request: Request instance for CreateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFirewallRules(self, request):
        """本接口（CreateFirewallRules）用于在实例上添加防火墙规则。


        * FirewallVersion 为防火墙版本号，用户每次更新防火墙规则版本会自动加1，防止您更新的规则已过期，不填不考虑冲突。FirewallVersion可通过[DescribeFirewallRules](https://cloud.tencent.com/document/api/1207/48252)接口返回值中的FirewallVersion获取。

        在 FirewallRules 参数中：
        * Protocol 字段支持输入 TCP，UDP，ICMP，ICMPv6，ALL。
        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。
        * CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。租户之间网络隔离规则优先于防火墙中的内网规则。
        * Action 字段只允许输入 ACCEPT 或 DROP。
        * FirewallRuleDescription 字段长度不得超过 64。

        :param request: Request instance for CreateFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFirewallTemplate(self, request):
        """本接口 (CreateFirewallTemplate) 用于创建防火墙模板。

        :param request: Request instance for CreateFirewallTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFirewallTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFirewallTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFirewallTemplateRules(self, request):
        """本接口 (CreateFirewallTemplateRules) 用于创建防火墙模板规则。

        :param request: Request instance for CreateFirewallTemplateRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallTemplateRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallTemplateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFirewallTemplateRules", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFirewallTemplateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceSnapshot(self, request):
        """本接口（CreateInstanceSnapshot）用于创建指定实例的系统盘快照。

        :param request: Request instance for CreateInstanceSnapshot.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstanceSnapshotRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstanceSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        """本接口(CreateInstances)用于创建一个或多个指定套餐的轻量应用服务器实例。
        *创建实例时，如指定实例访问域名信息时，本次创建请求，仅支持购买一台实例。

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateKeyPair(self, request):
        """本接口（CreateKeyPair）用于创建一个密钥对。

        :param request: Request instance for CreateKeyPair.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBlueprints(self, request):
        """本接口 (DeleteBlueprints) 用于删除镜像。可删除的镜像应满足如下条件：
        1、删除镜像接口需要镜像状态为NORMAL（正常）、ISOLATED（已隔离）、CREATEFAILED（创建失败）、SYNCING_FAILED（目的地域同步失败），其他状态下的镜像不支持删除操作。镜像状态，可通过[DescribeBlueprints](https://cloud.tencent.com/document/product/1207/47689)接口返回值中的BlueprintState获取。
        2、仅支持删除自定义镜像。

        :param request: Request instance for DeleteBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDiskBackups(self, request):
        """本接口（DeleteDiskBackups）用于删除云硬盘备份点。
        云硬盘备份点必须处于 NORMAL 状态，云硬盘备份点状态可以通过 [DescribeDiskBackups](https://cloud.tencent.com/document/api/1207/84379)接口查询，见输出参数中 DiskBackupState 字段解释。

        :param request: Request instance for DeleteDiskBackups.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteDiskBackupsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteDiskBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDiskBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDiskBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFirewallRules(self, request):
        """本接口（DeleteFirewallRules）用于删除实例的防火墙规则。

        * FirewallVersion 用于指定要操作的防火墙的版本。传入 FirewallVersion 版本号若不等于当前防火墙的最新版本，将返回失败；若不传 FirewallVersion 则直接删除指定的规则。FirewallVersion可通过[DescribeFirewallRules](https://cloud.tencent.com/document/api/1207/48252)接口返回值中的FirewallVersion获取。

        在 FirewallRules 参数中：
        * Protocol 字段支持输入 TCP，UDP，ICMP，ICMPv6，ALL。
        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。
        * CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。租户之间网络隔离规则优先于防火墙中的内网规则。
        * Action 字段只允许输入 ACCEPT 或 DROP。
        * FirewallRuleDescription 字段长度不得超过 64。

        :param request: Request instance for DeleteFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFirewallTemplate(self, request):
        """本接口 (DeleteFirewallTemplate) 用于删除防火墙模板。

        :param request: Request instance for DeleteFirewallTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirewallTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirewallTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFirewallTemplateRules(self, request):
        """本接口 (DeleteFirewallTemplateRules) 用于删除防火墙模板规则。

        :param request: Request instance for DeleteFirewallTemplateRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallTemplateRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallTemplateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFirewallTemplateRules", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFirewallTemplateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteKeyPairs(self, request):
        """本接口（DeleteKeyPairs）用于删除密钥对。
        - 不能删除已被实例或镜像引用的密钥对，删除之前需要确保没有被任何实例和镜像引用。

        :param request: Request instance for DeleteKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """本接口（DeleteSnapshots）用于删除快照。
        快照必须处于 NORMAL 状态，快照状态可以通过 <a href="https://cloud.tencent.com/document/product/1207/54388" target="_blank">DescribeSnapshots</a> 接口查询，见输出参数中 SnapshotState 字段解释。

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAllScenes(self, request):
        """本接口(DescribeAllScenes)用于查询全地域使用场景列表。

        :param request: Request instance for DescribeAllScenes.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeAllScenesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeAllScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlueprintInstances(self, request):
        """本接口（DescribeBlueprintInstances）用于查询镜像实例信息。

        :param request: Request instance for DescribeBlueprintInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlueprintInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlueprintInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBlueprints(self, request):
        """本接口（DescribeBlueprints）用于查询镜像信息。该接口返回的镜像类型有：自定义镜像、共享镜像、公共镜像。

        :param request: Request instance for DescribeBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBundleDiscount(self, request):
        """本接口（DescribeBundleDiscount）用于查询套餐折扣信息。

        :param request: Request instance for DescribeBundleDiscount.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundleDiscountRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundleDiscountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBundleDiscount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBundleDiscountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBundles(self, request):
        """本接口（DescribeBundles）用于查询套餐信息。

        :param request: Request instance for DescribeBundles.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBundles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBundlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnAttachedInstances(self, request):
        """本接口 (DescribeCcnAttachedInstances) 用于查询云联网关联的实例信息。

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskBackups(self, request):
        """本接口（DescribeDiskBackups）用于查询云硬盘备份点的详细信息。

        :param request: Request instance for DescribeDiskBackups.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskBackupsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskBackupsDeniedActions(self, request):
        """本接口（DescribeDiskBackupsDeniedActions）用于查询一个或多个云硬盘备份点的操作限制列表信息。

        :param request: Request instance for DescribeDiskBackupsDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskBackupsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskBackupsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskBackupsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskBackupsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskConfigs(self, request):
        """本接口（DescribeDiskConfigs）用于查询云硬盘配置。

        :param request: Request instance for DescribeDiskConfigs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskConfigsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDiskDiscount(self, request):
        """本接口(DescribeDiskDiscount)用于查询云硬盘折扣信息。

        :param request: Request instance for DescribeDiskDiscount.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskDiscountRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDiskDiscountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDiskDiscount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDiskDiscountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisks(self, request):
        """本接口（DescribeDisks）用于查询云硬盘信息。

        :param request: Request instance for DescribeDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisksDeniedActions(self, request):
        """本接口（DescribeDisksDeniedActions）用于查询一个或多个云硬盘的操作限制列表信息。

        :param request: Request instance for DescribeDisksDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisksDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisksReturnable(self, request):
        """本接口（DescribeDisksReturnable）用于查询云硬盘是否可退还。

        :param request: Request instance for DescribeDisksReturnable.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksReturnableRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDisksReturnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisksReturnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksReturnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDockerActivities(self, request):
        """查询实例内的Docker活动列表。

        :param request: Request instance for DescribeDockerActivities.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerActivitiesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDockerActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDockerActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDockerContainerConfiguration(self, request):
        """查询实例内的Docker容器配置信息

        :param request: Request instance for DescribeDockerContainerConfiguration.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainerConfigurationRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainerConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDockerContainerConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDockerContainerConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDockerContainerDetail(self, request):
        """查询实例内的Docker容器详情

        :param request: Request instance for DescribeDockerContainerDetail.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainerDetailRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDockerContainerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDockerContainerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDockerContainers(self, request):
        """查询实例内的容器列表。

        :param request: Request instance for DescribeDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallRules(self, request):
        """本接口（DescribeFirewallRules）用于查询实例的防火墙规则。

        :param request: Request instance for DescribeFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallRulesTemplate(self, request):
        """本接口（DescribeFirewallRulesTemplate）用于查询防火墙规则模板。

        :param request: Request instance for DescribeFirewallRulesTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallRulesTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallRulesTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallTemplateApplyRecords(self, request):
        """本接口 (DescribeFirewallTemplateApplyRecords) 用于查询防火墙模板应用记录列表。

        :param request: Request instance for DescribeFirewallTemplateApplyRecords.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateApplyRecordsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateApplyRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallTemplateApplyRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallTemplateApplyRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallTemplateQuota(self, request):
        """本接口 (DescribeFirewallTemplateQuota) 用于查询防火墙模板配额。

        :param request: Request instance for DescribeFirewallTemplateQuota.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateQuotaRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallTemplateQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallTemplateQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallTemplateRuleQuota(self, request):
        """本接口 (DescribeFirewallTemplateRuleQuota) 用于查询防火墙模板规则配额。

        :param request: Request instance for DescribeFirewallTemplateRuleQuota.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateRuleQuotaRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateRuleQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallTemplateRuleQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallTemplateRuleQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallTemplateRules(self, request):
        """本接口 (DescribeFirewallTemplateRules) 用于查询防火墙模板规则列表。

        :param request: Request instance for DescribeFirewallTemplateRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallTemplateRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallTemplateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFirewallTemplates(self, request):
        """本接口 (DescribeFirewallTemplates) 用于查询防火墙模板列表。

        :param request: Request instance for DescribeFirewallTemplates.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplatesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFirewallTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFirewallTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGeneralResourceQuotas(self, request):
        """本接口（DescribeGeneralResourceQuotas）用于查询通用资源配额信息。

        :param request: Request instance for DescribeGeneralResourceQuotas.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeGeneralResourceQuotasRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeGeneralResourceQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGeneralResourceQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGeneralResourceQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceVncUrl(self, request):
        """本接口 ( DescribeInstanceVncUrl ) 用于查询实例管理终端地址，获取的地址可用于实例的 VNC 登录。

        * 仅处于 `RUNNING`，`RESCUE_MODE` 状态的机器，且当前机器无变更中操作，才可使用此功能。
        * 管理终端地址的有效期为 15 秒，调用接口成功后如果 15 秒内不使用该链接进行访问，管理终端地址自动失效，您需要重新查询。
        * 管理终端地址一旦被访问，将自动失效，您需要重新查询。
        * 如果连接断开，每分钟内重新连接的次数不能超过 30 次。
        * 参数 `InstanceVncUrl` ：调用接口成功后会返回的 `InstanceVncUrl` 的值。
        获取到 `InstanceVncUrl` 后，您需要在链接 `https://img.qcloud.com/qcloud/app/active_vnc/index.html?` 末尾加上参数 `InstanceVncUrl=xxxx`。
         最后组成的 URL 格式如下：

        ```
        https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
        ```

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceVncUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceVncUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """本接口（DescribeInstances）用于查询一个或多个实例的详细信息。

        * 可以根据实例 ID、实例名称或者实例的内网 IP 查询实例的详细信息。
        * 过滤信息详细请见过滤器 [Filters](https://cloud.tencent.com/document/product/1207/47576#Filter) 。
        * 如果参数为空，返回当前用户一定数量（Limit 所指定的数量，默认为 20）的实例。
        * 支持查询实例的最新操作（LatestOperation）以及最新操作状态（LatestOperationState）。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDeniedActions(self, request):
        """本接口（DescribeInstancesDeniedActions）用于查询一个或多个实例的操作限制列表信息。

        :param request: Request instance for DescribeInstancesDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesDiskNum(self, request):
        """本接口(DescribeInstancesDiskNum)用于查询实例挂载云硬盘数量。

        :param request: Request instance for DescribeInstancesDiskNum.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDiskNumRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesDiskNumResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDiskNum", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDiskNumResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesReturnable(self, request):
        """本接口（DescribeInstancesReturnable）用于查询实例是否可退还。

        :param request: Request instance for DescribeInstancesReturnable.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesReturnableRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesReturnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesReturnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesReturnableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesTrafficPackages(self, request):
        """本接口（DescribeInstancesTrafficPackages）用于查询一个或多个实例的流量包详情。

        :param request: Request instance for DescribeInstancesTrafficPackages.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeKeyPairs(self, request):
        """本接口 (DescribeKeyPairs) 用于查询用户密钥对信息。

        :param request: Request instance for DescribeKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModifyInstanceBundles(self, request):
        """本接口（DescribeModifyInstanceBundles）用于查询实例可变更套餐列表。

        :param request: Request instance for DescribeModifyInstanceBundles.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeModifyInstanceBundlesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeModifyInstanceBundlesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModifyInstanceBundles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModifyInstanceBundlesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """本接口（DescribeRegions）用于查询地域信息。

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResetInstanceBlueprints(self, request):
        """本接口（DescribeResetInstanceBlueprints）查询重置实例的镜像信息。对于游戏专区实例，该接口只会返回当前镜像，且不支持 Filters 参数。

        :param request: Request instance for DescribeResetInstanceBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeResetInstanceBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeResetInstanceBlueprintsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResetInstanceBlueprints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResetInstanceBlueprintsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenes(self, request):
        """本接口(DescribeScenes)用于查看使用场景列表。

        :param request: Request instance for DescribeScenes.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeScenesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """本接口（DescribeSnapshots）用于查询快照的详细信息。

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotsDeniedActions(self, request):
        """本接口（DescribeSnapshotsDeniedActions）用于查询一个或多个快照的操作限制列表信息。

        :param request: Request instance for DescribeSnapshotsDeniedActions.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeSnapshotsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """查询地域下可用区

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCcn(self, request):
        """本接口 (DetachCcn) 用于解除与云联网的关联。

        :param request: Request instance for DetachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DetachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DetachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachDisks(self, request):
        """本接口（DetachDisks）用于卸载一个或多个云硬盘。该操作目前仅支持云硬盘类型为数据盘的云硬盘。
        - 支持批量操作，卸载挂载在同一主机上的多块云硬盘。如果多块云硬盘中存在不允许卸载的云硬盘，则操作不执行，返回特定的错误码。
        - 本接口为异步接口，当请求成功返回时，云硬盘并未立即卸载，可通过接口[DescribeDisks](https://cloud.tencent.com/document/product/362/16315)来查询对应云硬盘的状态，如果云硬盘的状态由“ATTACHED”变为“UNATTACHED”，则为卸载成功。

        :param request: Request instance for DetachDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DetachDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DetachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateInstancesKeyPairs(self, request):
        """本接口（DisassociateInstancesKeyPairs）用于解除实例与指定密钥对的绑定关系。

        * 只支持 [RUNNING, STOPPED] 状态的 LINUX_UNIX 操作系统的实例。处于 RUNNING 状态的实例会强制关机，然后解绑。
        * 解绑密钥后，实例可以通过原来设置的密码登录。
        * 如果原来没有设置密码，解绑后将无法使用 SSH 登录。可以调用 <a href="https://cloud.tencent.com/document/product/1207/55546" target="_blank">ResetInstancesPassword</a> 接口来设置登录密码。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for DisassociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportKeyPair(self, request):
        """本接口（ImportKeyPair）用于导入用户指定密钥对。

        :param request: Request instance for ImportKeyPair.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ImportKeyPairRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.ImportKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateBlueprint(self, request):
        """本接口 (InquirePriceCreateBlueprint) 用于创建镜像询价。

        :param request: Request instance for InquirePriceCreateBlueprint.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateBlueprintRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateBlueprintResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateBlueprint", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateBlueprintResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDisks(self, request):
        """本接口（InquirePriceCreateDisks）用于新购云硬盘询价。

        :param request: Request instance for InquirePriceCreateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateInstances(self, request):
        """本接口（InquiryPriceCreateInstances）用于创建实例询价。

        :param request: Request instance for InquirePriceCreateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceCreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewDisks(self, request):
        """本接口（InquirePriceRenewDisks）用于续费云硬盘询价。

        :param request: Request instance for InquirePriceRenewDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewDisks", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewInstances(self, request):
        """本接口（InquirePriceRenewInstances）用于续费实例询价。

        :param request: Request instance for InquirePriceRenewInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.InquirePriceRenewInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDisks(self, request):
        """本接口(IsolateDisks)用于退还一个或多个轻量应用服务器云硬盘。

        只有状态为 UNATTACHED 的数据盘才可以进行此操作。
        接口调用成功后，云硬盘会进入SHUTDOWN 状态。
        支持批量操作。每次请求批量资源的上限为 20。
        本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。云硬盘操作结果可以通过调用 [DescribeDisks](https://cloud.tencent.com/document/product/1207/66093) 接口查询，如果云硬盘的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for IsolateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.IsolateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.IsolateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateInstances(self, request):
        """本接口(IsolateInstances)用于退还一个或多个轻量应用服务器实例。
        * 只有状态为 RUNNING 或 STOPPED 的实例才可以进行此操作。
        * 接口调用成功后，实例会进入SHUTDOWN 状态。
        * 支持批量操作。每次请求批量资源（包括实例与数据盘）的上限为 20。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for IsolateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.IsolateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.IsolateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBlueprintAttribute(self, request):
        """本接口 (ModifyBlueprintAttribute) 用于修改镜像属性。

        :param request: Request instance for ModifyBlueprintAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyBlueprintAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyBlueprintAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBlueprintAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBlueprintAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDiskBackupsAttribute(self, request):
        """本接口 (ModifyDiskBackupsAttribute) 用于修改云硬盘备份点属性。

        :param request: Request instance for ModifyDiskBackupsAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDiskBackupsAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDiskBackupsAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDiskBackupsAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDiskBackupsAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisksAttribute(self, request):
        """本接口(ModifyDisksAttribute)用于修改云硬盘属性。
        云硬盘必须处于以下状态:
        <li> ATTACHED（已挂载）</li>
        <li> UNATTACHED（待挂载）</li>

        :param request: Request instance for ModifyDisksAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisksAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisksAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisksBackupQuota(self, request):
        """本接口(ModifyDisksBackupQuota)用于调整云硬盘备份点配额。
        该操作目前仅支持云硬盘类型为数据盘且状态是ATTACHED（已挂载）或 UNATTACHED（待挂载）的云硬盘。
        支持批量操作。每次批量请求云硬盘数量上限为15个。

        :param request: Request instance for ModifyDisksBackupQuota.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksBackupQuotaRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksBackupQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisksBackupQuota", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisksBackupQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDisksRenewFlag(self, request):
        """本接口（ModifyDisksRenewFlag）用于修改云硬盘续费标识。
        云硬盘需要处于以下状态：
        <li> ATTACHED （已挂载）</li>
        <li> UNATTACHED （待挂载）</li>
        <li> ATTACHING （挂载中） </li>
        <li> DETACHING （卸载中）</li>

        :param request: Request instance for ModifyDisksRenewFlag.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksRenewFlagRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDisksRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDisksRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDisksRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDockerContainer(self, request):
        """修改实例内的Docker容器，之后可以通过返回的ActivityId调用<a href="https://cloud.tencent.com/document/product/1207/95476" target="_blank">DescribeDockerActivities</a>接口查询重建情况。
        请注意：本接口会重新创建并运行实例内的Docker容器。

        :param request: Request instance for ModifyDockerContainer.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDockerContainerRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyDockerContainerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDockerContainer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDockerContainerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFirewallRuleDescription(self, request):
        """本接口（ModifyFirewallRuleDescription）用于修改单条防火墙规则描述。

        * FirewallVersion 用于指定要操作的防火墙的版本。传入 FirewallVersion 版本号若不等于当前防火墙的最新版本，将返回失败；若不传 FirewallVersion 则直接修改防火墙规则备注。FirewallVersion可通过[DescribeFirewallRules](https://cloud.tencent.com/document/api/1207/48252)接口返回值中的FirewallVersion获取。

        用FirewallRule参数来指定要修改的防火墙规则，使用其中的Protocol， Port， CidrBlock，Action字段来匹配要修改的防火墙规则。

        在 FirewallRule 参数中：
        * Protocol 字段支持输入 TCP，UDP，ICMP，ICMPv6，ALL。
        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。
        * CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。租户之间网络隔离规则优先于防火墙中的内网规则。
        * Action 字段只允许输入 ACCEPT 或 DROP。
        * FirewallRuleDescription 字段长度不得超过 64。

        :param request: Request instance for ModifyFirewallRuleDescription.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRuleDescriptionRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRuleDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFirewallRuleDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFirewallRuleDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFirewallRules(self, request):
        """本接口（ModifyFirewallRules）用于重置实例防火墙规则。

        本接口先删除当前实例的所有防火墙规则，然后添加新的规则。

        * FirewallVersion 用于指定要操作的防火墙的版本。传入 FirewallVersion 版本号若不等于当前防火墙的最新版本，将返回失败；若不传 FirewallVersion 则直接重置防火墙规则。可通过[DescribeFirewallRules](https://cloud.tencent.com/document/api/1207/48252)接口返回值中的FirewallVersion获取。

        在 FirewallRules 参数中：
        * Protocol 字段支持输入 TCP，UDP，ICMP，ICMPv6，ALL。
        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。
        * CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。租户之间网络隔离规则优先于防火墙中的内网规则。
        * Action 字段只允许输入 ACCEPT 或 DROP。
        * FirewallRuleDescription 字段长度不得超过 64。

        :param request: Request instance for ModifyFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFirewallRules", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFirewallRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFirewallTemplate(self, request):
        """本接口 (ModifyFirewallTemplate) 用于修改防火墙模板。

        :param request: Request instance for ModifyFirewallTemplate.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallTemplateRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyFirewallTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFirewallTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFirewallTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesAttribute(self, request):
        """本接口（ModifyInstancesAttribute）用于修改实例的属性。
        * “实例名称”仅为方便用户自己管理之用。
        * 支持批量操作。每次请求批量实例的上限为 100。

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesBundle(self, request):
        """本接口(ModifyInstancesBundle)用于变更一个或多个轻量应用服务器实例套餐。
        * 只有状态为 RUNNING，STOPPED的实例才可以进行此操作。
        * 支持批量操作。每次请求批量实例的上限为 30。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for ModifyInstancesBundle.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesBundleRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesBundleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesBundle", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesBundleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancesRenewFlag(self, request):
        """本接口 (ModifyInstancesRenewFlag) 用于修改包年包月实例续费标识。

        * 实例被标识为自动续费后，每次在实例到期时，会自动续费一个月。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: Request instance for ModifyInstancesRenewFlag.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesRenewFlagRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifyInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancesRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotAttribute(self, request):
        """本接口（ModifySnapshotAttribute）用于修改指定快照的属性。
        <li>“快照名称”仅为方便用户自己管理之用。</li>

        :param request: Request instance for ModifySnapshotAttribute.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ModifySnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ModifySnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebootInstances(self, request):
        """本接口（RebootInstances）用于重启实例。

        * 只有状态为 RUNNING 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 REBOOTING 状态；重启实例成功时，实例会进入 RUNNING 状态。
        * 支持批量操作，每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveDockerContainers(self, request):
        """删除实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询删除情况。

        :param request: Request instance for RemoveDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RemoveDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RemoveDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameDockerContainer(self, request):
        """重命名实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询重命名情况。

        :param request: Request instance for RenameDockerContainer.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RenameDockerContainerRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenameDockerContainerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameDockerContainer", params, headers=headers)
            response = json.loads(body)
            model = models.RenameDockerContainerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDisks(self, request):
        """本接口(RenewDisks)用于续费一个或多个轻量应用服务器云硬盘。

        只有状态为 ATTACHED，UNATTACHED 或 SHUTDOWN 的数据盘才可以进行此操作。
        支持批量操作。每次请求批量云硬盘的上限为 50。
        本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。云硬盘操作结果可以通过调用 [DescribeDisks](https://cloud.tencent.com/document/product/1207/66093) 接口查询，如果云硬盘的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for RenewDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RenewDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDisks", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstances(self, request):
        """本接口(RenewInstances)用于续费一个或多个轻量应用服务器实例。
        * 只有状态为 RUNNING，STOPPED 或 SHUTDOWN 的实例才可以进行此操作。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for RenewInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RenewInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RenewInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceFirewallTemplateRule(self, request):
        """本接口 (ReplaceFirewallTemplateRules) 用于替换防火墙模板规则。

        :param request: Request instance for ReplaceFirewallTemplateRule.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ReplaceFirewallTemplateRuleRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ReplaceFirewallTemplateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceFirewallTemplateRule", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceFirewallTemplateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RerunDockerContainer(self, request):
        """重新创建并运行实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询重建情况。

        :param request: Request instance for RerunDockerContainer.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RerunDockerContainerRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RerunDockerContainerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunDockerContainer", params, headers=headers)
            response = json.loads(body)
            model = models.RerunDockerContainerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAttachCcn(self, request):
        """本接口 (ResetAttachCcn) 用于关联云联网实例申请过期时，重新申请关联操作。

        :param request: Request instance for ResetAttachCcn.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetAttachCcnRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetAttachCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAttachCcn", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAttachCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetFirewallTemplateRules(self, request):
        """本接口 (ResetFirewallTemplateRules) 用于重置防火墙模板下所有规则。

        :param request: Request instance for ResetFirewallTemplateRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetFirewallTemplateRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetFirewallTemplateRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetFirewallTemplateRules", params, headers=headers)
            response = json.loads(body)
            model = models.ResetFirewallTemplateRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstance(self, request):
        """本接口（ResetInstance）用于重装指定实例上的镜像。

        * 仅`RUNNING`，`STOPPED`状态的机器，且当前机器无变更中的操作，才支持重装系统。
        * 如果指定了 BlueprintId 参数，则使用指定的镜像重装，否则按照当前实例使用的镜像进行重装。
        * 非中国大陆地域的实例不支持使用该接口实现LIUNX_UNIX和WINDOWS操作系统切换。
        * 系统盘将会被格式化，并重置，请确保系统盘中无重要文件。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。
        * 对于游戏专区实例，仅支持重装当前镜像。

        :param request: Request instance for ResetInstance.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetInstancesPassword(self, request):
        """本接口（ResetInstancesPassword）用于将实例操作系统的密码重置为用户指定的密码。
        * 只修改管理员账号的密码。实例的操作系统不同，管理员账号也会不一样（Windows 为 Administrator，Ubuntu 为 ubuntu ，其它系统为 root）。
        * 支持批量操作。将多个实例操作系统的密码重置为相同的密码。每次请求批量实例的上限为 100。
        * 建议对运行中的实例先手动关机，然后再进行密码重置。如实例处于运行中状态，本接口操作过程中会对实例进行关机操作，尝试正常关机失败后进行强制关机。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。
        注意：强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏。

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstancesPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisks(self, request):
        """本接口(ResizeDisks)用于扩容云硬盘。该操作目前仅支持云硬盘类型为数据盘的云硬盘。

        :param request: Request instance for ResizeDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResizeDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResizeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDockerContainers(self, request):
        """重启实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询重启情况。

        :param request: Request instance for RestartDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RestartDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RestartDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunDockerContainers(self, request):
        """创建并运行多个Docker容器，之后可以通过返回的ActivityIds调用<a href="https://cloud.tencent.com/document/product/1207/95476" target="_blank">DescribeDockerActivities</a>接口查询创建情况。

        :param request: Request instance for RunDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RunDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RunDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.RunDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ShareBlueprintAcrossAccounts(self, request):
        """本接口（ShareBlueprintAcrossAccounts）用于跨账号共享镜像。
        仅支持共享自定义镜像， 且用于共享的镜像状态必须为NORMAL。
        共享的账号必须为主账号。

        :param request: Request instance for ShareBlueprintAcrossAccounts.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ShareBlueprintAcrossAccountsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ShareBlueprintAcrossAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ShareBlueprintAcrossAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.ShareBlueprintAcrossAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartDockerContainers(self, request):
        """启动实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询启动情况。

        :param request: Request instance for StartDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StartDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StartDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.StartDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstances(self, request):
        """本接口（StartInstances）用于启动一个或多个实例。

        * 只有状态为 STOPPED 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 STARTING 状态；启动实例成功时，实例会进入 RUNNING 状态。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDockerContainers(self, request):
        """停止实例内的Docker容器，之后可以通过返回的ActivityId调用[DescribeDockerActivities](https://cloud.tencent.com/document/product/1207/95476)接口查询停止情况。

        :param request: Request instance for StopDockerContainers.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StopDockerContainersRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StopDockerContainersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDockerContainers", params, headers=headers)
            response = json.loads(body)
            model = models.StopDockerContainersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstances(self, request):
        """本接口（StopInstances）用于关闭一个或多个实例。
        * 只有状态为 RUNNING 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 STOPPING 状态；关闭实例成功时，实例会进入 STOPPED 状态。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDisks(self, request):
        """本接口（TerminateDisks）用于销毁一个或多个云硬盘。
        云硬盘状态必须处于SHUTDOWN（已隔离）状态。

        :param request: Request instance for TerminateDisks.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.TerminateDisksRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.TerminateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        """本接口 (TerminateInstances) 用于销毁实例。

        * 处于 SHUTDOWN 状态的实例，可通过本接口销毁，且不可恢复。
        * 支持批量操作，每次请求批量实例的上限为100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 <a href="https://cloud.tencent.com/document/product/1207/47573" target="_blank">DescribeInstances</a> 接口查询，如果返回列表中不存在该实例，则代表操作成功。

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))