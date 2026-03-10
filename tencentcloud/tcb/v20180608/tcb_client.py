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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tcb.v20180608 import models


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'
    _service = 'tcb'


    def BindCloudBaseAccessDomain(self, request):
        r"""绑定云开发自定义域名，用于云接入和静态托管

        :param request: Request instance for BindCloudBaseAccessDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.BindCloudBaseAccessDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.BindCloudBaseAccessDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindCloudBaseAccessDomain", params, headers=headers)
            response = json.loads(body)
            model = models.BindCloudBaseAccessDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindCloudBaseGWDomain(self, request):
        r"""绑定自定义域名

        :param request: Request instance for BindCloudBaseGWDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.BindCloudBaseGWDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.BindCloudBaseGWDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindCloudBaseGWDomain", params, headers=headers)
            response = json.loads(body)
            model = models.BindCloudBaseGWDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTcbService(self, request):
        r"""检查是否开通Tcb服务

        :param request: Request instance for CheckTcbService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTcbService", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTcbServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthDomain(self, request):
        r"""增加安全域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名。

        注意⚠️
          安全域名绑定成功之后，需要几分钟时间逐步生效。

        :param request: Request instance for CreateAuthDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateAuthDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuthDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuthDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBillDeal(self, request):
        r"""创建云开发产品计费订单，用于以下几种场景：
        1. 购买云开发环境
        2. 续费云开发环境
        3. 变更云开发环境套餐
        4. 购买云开发资源包
        5. 购买云开发大促包

        该接口支持下单并支付(CreateAndPay=true时)，此时会自动在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for CreateBillDeal.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateBillDealRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateBillDealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBillDeal", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBillDealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudBaseGWAPI(self, request):
        r"""创建云开发网关API

        :param request: Request instance for CreateCloudBaseGWAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseGWAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseGWAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudBaseGWAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudBaseGWAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnv(self, request):
        r"""本接口用于购买云开发环境。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。
        环境下单成功之后会返回EnvId。EnvId是全局唯一表示。
        环境发货是异步行为，后续可以通过接口 [DescribeEnvs ](https://cloud.tencent.com/document/product/876/34820) 查询环境状态和各项资源信息；通过 [DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境套餐信息，包括 到期时间、当前套餐等。

        :param request: Request instance for CreateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostingDomain(self, request):
        r"""创建托管域名

        :param request: Request instance for CreateHostingDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateHostingDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostingDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostingDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMySQL(self, request):
        r"""开通Mysql

        开通后，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询开通结果

        :param request: Request instance for CreateMySQL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateMySQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMySQL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMySQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStaticStore(self, request):
        r"""创建静态托管资源，包括COS和CDN，异步任务创建，查看创建结果需要根据DescribeStaticStore接口来查看

        :param request: Request instance for CreateStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTable(self, request):
        r"""本接口(CreateTable)用于创建表，支持创建capped类型集合，暂时不支持分片表

        :param request: Request instance for CreateTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""创建tcb用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuthDomain(self, request):
        r"""删除合法域名。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [DescribeAuthDomains](https://cloud.tencent.com/document/product/876/42151) 获取当前已绑定生效的安全域名。

        注意⚠️
        安全域名被删除之后，可能会引起跨域问题，请谨慎操作。

        :param request: Request instance for DeleteAuthDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteAuthDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteAuthDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuthDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuthDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudBaseGWAPI(self, request):
        r"""删除网关API

        :param request: Request instance for DeleteCloudBaseGWAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseGWAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseGWAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudBaseGWAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudBaseGWAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudBaseGWDomain(self, request):
        r"""删除网关域名

        :param request: Request instance for DeleteCloudBaseGWDomain.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseGWDomainRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseGWDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudBaseGWDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudBaseGWDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTable(self, request):
        r"""本接口(DeleteTable)用于删除表，删除表后表中数据将会被删除且无法恢复，请谨慎操作

        接口入参中的 Tag 为 flexdb 的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取

        :param request: Request instance for DeleteTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        r"""删除tcb用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthDomains(self, request):
        r"""本接口用于获取当前环境的安全域名列表。
        云开发会校验网页应用请求的来源域名，您需要将来源域名加入到WEB安全域名列表中。
        可以通过接口 [CreateAuthDomain](https://cloud.tencent.com/document/product/876/42764) 增加安全域名。

        :param request: Request instance for DescribeAuthDomains.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeAuthDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuthDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuthDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaasPackageList(self, request):
        r"""获取新套餐列表，含详情，如果传了PackageId，则只获取指定套餐详情

        :param request: Request instance for DescribeBaasPackageList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeBaasPackageListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeBaasPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaasPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaasPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseBuildService(self, request):
        r"""获取云托管代码上传url

        :param request: Request instance for DescribeCloudBaseBuildService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseBuildServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseBuildServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseBuildService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseBuildServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseGWAPI(self, request):
        r"""获取网关API列表

        :param request: Request instance for DescribeCloudBaseGWAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseGWAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseGWAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseGWAPI", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseGWAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseGWService(self, request):
        r"""获取网关服务

        :param request: Request instance for DescribeCloudBaseGWService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseGWServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseGWServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseGWService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseGWServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCreateMySQLResult(self, request):
        r"""查询开通Mysql结果，`Response.Data.Status = "notexist"` 表示未开通，如果未开通，可以调用 [CreateMySQL](https://cloud.tencent.com/document/api/876/128186) 来开通
         `Response.Data. Status = "success"` 表示开通成功，Mysql开通成功后，可通过接口设置数据库账号相关功能包括但不限于【创建账号、删除账号、查询可授权权限列表、查询账号已有权限、修改主机、修改配置、修改账号库表权限】、集群操作相关【查询集群参数、修改集群参数】，连接设置相关【关闭外网、开通外网、查询集群信息】，备份回档相关【创建手动回档、删除手动回档、修改自动备份配置信息、查询备份文件列表、集群回档、查询任务列表、获取table列表、获取集群数据库列表、查询备份下载地址】，相关功能接口文档：[TDSQL-C MySQL API文档](https://cloud.tencent.com/document/product/1003/48106)

        :param request: Request instance for DescribeCreateMySQLResult.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResultRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCreateMySQLResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCreateMySQLResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreateMySQLResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseACL(self, request):
        r"""获取数据库权限

        :param request: Request instance for DescribeDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvAccountCircle(self, request):
        r"""查询环境计费周期。
        云开发环境的资源点都是按月结算的，每个月都有一定的抵扣额度。

        例如：
          某个环境在 2026-01-05 购买了3个月个人版(到期时间: 2026-04-05)，则他可以在以下3个周期内，分别享有40000资源点的额度：
          1. 2026-01-05 ~ 2026-02-05 23:59:59
          2. 2026-02-06 ~ 2026-03-05 23:59:59
          3. 2026-03-06 ~ 2026-04-05 23:59:59

        本接口，用于获取环境当前属于哪个计费周期内。

        :param request: Request instance for DescribeEnvAccountCircle.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvAccountCircleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvAccountCircleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvAccountCircle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvAccountCircleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvLimit(self, request):
        r"""查询环境个数上限

        :param request: Request instance for DescribeEnvLimit.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvs(self, request):
        r"""获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

        :param request: Request instance for DescribeEnvs.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostingDomainTask(self, request):
        r"""查询静态托管域名任务状态

        :param request: Request instance for DescribeHostingDomainTask.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeHostingDomainTaskRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeHostingDomainTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostingDomainTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostingDomainTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySQLClusterDetail(self, request):
        r"""查询Mysql集群信息

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有已开通的才能查到集群信息

        :param request: Request instance for DescribeMySQLClusterDetail.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLClusterDetailRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySQLClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySQLClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMySQLTaskStatus(self, request):
        r"""查询Mysql任务状态

        :param request: Request instance for DescribeMySQLTaskStatus.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLTaskStatusRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeMySQLTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMySQLTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMySQLTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotaData(self, request):
        r"""查询指定指标的配额使用量

        :param request: Request instance for DescribeQuotaData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeQuotaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotaData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSafeRule(self, request):
        r"""查询数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍](https://cloud.tencent.com/document/product/876/123478) 。

        :param request: Request instance for DescribeSafeRule.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeSafeRuleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeSafeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSafeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSafeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaticStore(self, request):
        r"""查看当前环境下静态托管资源信息，根据返回结果判断静态资源的状态

        :param request: Request instance for DescribeStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTable(self, request):
        r"""查询表的相关信息，包括索引等信息

        接口入参中的 Tag 为 flexdb 的实例 Id，可以通过 [DescribeEnvs](https://cloud.tencent.com/document/api/876/34820) 接口返回的 EnvList[0].Databases[0].InstanceId 获取

        :param request: Request instance for DescribeTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        r"""本接口(DescribeTables)用于查询所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserList(self, request):
        r"""查询tcb用户列表

        :param request: Request instance for DescribeUserList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyEnv(self, request):
        r"""本接口用于销毁云开发环境。
        云开发环境遵循腾讯云包年包月预付费产品生命周期，因此环境销毁需要分两步：
        1. 资源退费。此时会根据当前环境剩余有效期，自动退还相关费用(代金券不退)。退款后，环境进入隔离期。
        2. 环境删除。环境在进入隔离期后15天会自动删除。也可以通过本接口，指定 IsForce=true 来强制删除隔离期环境。

        **注意**⚠️
          1. 环境退费后进入隔离期，则所有资源均无法访问，控制台无法操作和管理。
          2. 环境被彻底删除后，所有数据均无法找回。请谨慎操作。

        可以通过接口 [tcb:DescribeBillingInfo](https://cloud.tencent.com/document/product/876/94390) 查询环境计费状态。

        :param request: Request instance for DestroyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyEnv", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyMySQL(self, request):
        r"""销毁Mysql

        销毁后可以通过 [DescribeMySQLTaskStatus](https://cloud.tencent.com/document/api/876/128183) 接口查询销毁结果，如果 `Response.Data. Status = FAILED ` 表示销毁失败，可以重新调用销毁接口重试

        :param request: Request instance for DestroyMySQL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyMySQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyMySQL", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyMySQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyStaticStore(self, request):
        r"""销毁静态托管资源，该接口创建异步销毁任务，资源最终状态可从DestroyStaticStore接口查看

        :param request: Request instance for DestroyStaticStore.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyStaticStoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyStaticStore", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyStaticStoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EditAuthConfig(self, request):
        r"""修改登录配置

        :param request: Request instance for EditAuthConfig.
        :type request: :class:`tencentcloud.tcb.v20180608.models.EditAuthConfigRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.EditAuthConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditAuthConfig", params, headers=headers)
            response = json.loads(body)
            model = models.EditAuthConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTables(self, request):
        r"""本接口(ListTables)用于查询所有表信息，包括表名、表中数据条数、表中数据量、索引个数及索引的大小等

        :param request: Request instance for ListTables.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ListTablesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ListTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTables", params, headers=headers)
            response = json.loads(body)
            model = models.ListTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudBaseGWAPI(self, request):
        r"""修改云开发网关API

        :param request: Request instance for ModifyCloudBaseGWAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseGWAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseGWAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudBaseGWAPI", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudBaseGWAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClsTopic(self, request):
        r"""修改日志主题

        :param request: Request instance for ModifyClsTopic.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyClsTopicRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyClsTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClsTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClsTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseACL(self, request):
        r"""修改数据库权限

        :param request: Request instance for ModifyDatabaseACL.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseACL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnv(self, request):
        r"""更新环境信息

        :param request: Request instance for ModifyEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyEnvPlan(self, request):
        r"""本接口用于变更云开发环境套餐。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for ModifyEnvPlan.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvPlanRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEnvPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySafeRule(self, request):
        r"""设置数据库安全规则。
        安全规则，用于控制C端用户的访问权限。详见 [安全规则介绍 ](https://cloud.tencent.com/document/product/876/123478)。

        :param request: Request instance for ModifySafeRule.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifySafeRuleRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifySafeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySafeRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySafeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""修改tcb用户

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReinstateEnv(self, request):
        r"""针对已隔离的免费环境，可以通过本接口将其恢复访问。

        :param request: Request instance for ReinstateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReinstateEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ReinstateEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewEnv(self, request):
        r"""本接口用于云开发环境套餐续费。
        该接口会自动下单并支付，会在腾讯云账户中扣除余额（余额不足会下单失败）。
        该接口支持自动扣除代金券（AutoVoucher=true时），符合条件的代金券会被自动扣除。

        :param request: Request instance for RenewEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RenewEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RenewEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewEnv", params, headers=headers)
            response = json.loads(body)
            model = models.RenewEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunCommands(self, request):
        r"""本接口用于执行数据库命令

        :param request: Request instance for RunCommands.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RunCommandsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RunCommandsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunCommands", params, headers=headers)
            response = json.loads(body)
            model = models.RunCommandsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunSql(self, request):
        r"""执行SQL语句

        调用该接口前需要先查询Mysql是否开通，可通过 [DescribeCreateMySQLResult ](https://cloud.tencent.com/document/api/876/128185) 查询，只有开通成功才能操作

        :param request: Request instance for RunSql.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RunSqlRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RunSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunSql", params, headers=headers)
            response = json.loads(body)
            model = models.RunSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        r"""搜索用户调用日志

        :param request: Request instance for SearchClsLog.
        :type request: :class:`tencentcloud.tcb.v20180608.models.SearchClsLogRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.SearchClsLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClsLog", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClsLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTable(self, request):
        r"""本接口(UpdateTable)用于修改表信息，当前可以支持创建和删除索引

        :param request: Request instance for UpdateTable.
        :type request: :class:`tencentcloud.tcb.v20180608.models.UpdateTableRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.UpdateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTable", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))