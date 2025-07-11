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


# CAM签名/鉴权错误。
AUTHFAILURE = 'AuthFailure'

# 操作失败。
FAILEDOPERATION = 'FailedOperation'

# 动作消息不可达。
FAILEDOPERATION_ACTIONUNREACHABLE = 'FailedOperation.ActionUnreachable'

# 广播任务正在执行。
FAILEDOPERATION_BROADCASTTASKISRUNNING = 'FailedOperation.BroadcastTaskIsRunning'

# 云存 AI 套餐生效时长不能超过当前云存套餐生效时长
FAILEDOPERATION_CLOUDSTORAGEAIPACKAGEEXPIRETIMEEXCEEDED = 'FailedOperation.CloudStorageAIPackageExpireTimeExceeded'

# 产品未开通视频AI分析服务
FAILEDOPERATION_CLOUDSTORAGEAISERVICENOTENABLED = 'FailedOperation.CloudStorageAIServiceNotEnabled'

# 云存 AI 分析任务已存在，不支持重复创建
FAILEDOPERATION_CLOUDSTORAGEAISERVICETASKALREADYEXISTS = 'FailedOperation.CloudStorageAIServiceTaskAlreadyExists'

# 需先开通云存套餐
FAILEDOPERATION_CLOUDSTORAGEPACKAGEREQUIRED = 'FailedOperation.CloudStoragePackageRequired'

# 设备已经被禁用。
FAILEDOPERATION_DEVICEALREADYDISABLED = 'FailedOperation.DeviceAlreadyDisabled'

# 设备已为目标升级版本。
FAILEDOPERATION_DEVICEFIRMWAREISUPDATED = 'FailedOperation.DeviceFirmwareIsUpdated'

# 设备固件版本错误。
FAILEDOPERATION_DEVICEINFOOUTDATED = 'FailedOperation.DeviceInfoOutdated'

# 返回:消息发送失败，设备未订阅Topic。
FAILEDOPERATION_DEVICENOSUBSCRIPTION = 'FailedOperation.DeviceNoSubscription'

# 设备处于离线状态。
FAILEDOPERATION_DEVICEOFFLINE = 'FailedOperation.DeviceOffline'

# 存在其他升级任务。
FAILEDOPERATION_OTHERUPDATETASKEXIST = 'FailedOperation.OtherUpdateTaskExist'

# 产品未开通 IoT Video 服务
FAILEDOPERATION_PRODUCTIOTVIDEOSERVICENOTENABLED = 'FailedOperation.ProductIotVideoServiceNotEnabled'

# 产品尚未发布。
FAILEDOPERATION_PRODUCTNOTRELEASED = 'FailedOperation.ProductNotReleased'

# RRPC接口未收到设备端响应。
FAILEDOPERATION_RRPCTIMEOUT = 'FailedOperation.RRPCTimeout'

# 请求TRTC失败
FAILEDOPERATION_REQUESTTRTCFAIL = 'FailedOperation.RequestTRTCFail'

# 转发已经停止。
FAILEDOPERATION_RULEALREADYDISABLED = 'FailedOperation.RuleAlreadyDisabled'

# 该规则已被启用。
FAILEDOPERATION_RULEALREADYENABLED = 'FailedOperation.RuleAlreadyEnabled'

# 部分产品已经被绑定。
FAILEDOPERATION_SOMEPRODUCTISALREADYBINDED = 'FailedOperation.SomeProductIsAlreadyBinded'

# 超过时间。
FAILEDOPERATION_TIMEOUT = 'FailedOperation.Timeout'

# 内部错误。
INTERNALERROR = 'InternalError'

# DB操作错误。
INTERNALERROR_DBOPERATIONERROR = 'InternalError.DBOperationError'

# DB操作错误。
INTERNALERROR_DBOPERTAIONERROR = 'InternalError.DBOpertaionError'

# 内部LoRaServer错误。
INTERNALERROR_INTERNALLORASERVERERROR = 'InternalError.InternalLoRaServerError'

# 内部RPC错误。
INTERNALERROR_INTERNALRPCERROR = 'InternalError.InternalRPCError'

# 发生错误。
INTERNALERROR_INTERNALSERVEREXCEPTION = 'InternalError.InternalServerException'

# 内部DB错误。
INTERNALERROR_INTERNALSERVEREXCEPTIONDB = 'InternalError.InternalServerExceptionDB'

# 调用超时。
INTERNALERROR_TIMEOUT = 'InternalError.Timeout'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 动作输入参数不合法。
INVALIDPARAMETER_ACTIONINPUTPARAMSINVALID = 'InvalidParameter.ActionInputParamsInvalid'

# 固件已存在。
INVALIDPARAMETER_FIRMWAREALREADYEXIST = 'InvalidParameter.FirmwareAlreadyExist'

# 产品不是网关类型，无法绑定子产品。
INVALIDPARAMETER_PRODUCTISNOTGATEWAY = 'InvalidParameter.ProductIsNotGateway'

# RoomId已存在
INVALIDPARAMETER_ROOMIDEXIST = 'InvalidParameter.RoomIdExist'

# UserId数量超出限制
INVALIDPARAMETER_USERIDOVERLIMIT = 'InvalidParameter.UserIdOverLimit'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 规则行为未配置。
INVALIDPARAMETERVALUE_ACTIONNIL = 'InvalidParameterValue.ActionNil'

# 动作为空或不存在。
INVALIDPARAMETERVALUE_ACTIONNILORNOTEXIST = 'InvalidParameterValue.ActionNilOrNotExist'

# 应用描述过长。
INVALIDPARAMETERVALUE_APPDESCRIPTIONTOOLONG = 'InvalidParameterValue.AppDescriptionTooLong'

# App已存在。
INVALIDPARAMETERVALUE_APPEXISTS = 'InvalidParameterValue.AppExists'

# 应用名称过长。
INVALIDPARAMETERVALUE_APPNAMETOOLONG = 'InvalidParameterValue.AppNameTooLong'

# App无权限。
INVALIDPARAMETERVALUE_APPNOPERMISSION = 'InvalidParameterValue.AppNoPermission'

# App不存在。
INVALIDPARAMETERVALUE_APPNOTEXISTS = 'InvalidParameterValue.AppNotExists'

# 检查第三方URL超时或失败。
INVALIDPARAMETERVALUE_CHECKFORWARDURLFAIL = 'InvalidParameterValue.CheckForwardURLFail'

# 指定的云存 AI 套餐不存在
INVALIDPARAMETERVALUE_CLOUDSTORAGEAIPACKAGEIDNOTEXIST = 'InvalidParameterValue.CloudStorageAIPackageIdNotExist'

# 创建的设备名已存在。
INVALIDPARAMETERVALUE_DEVICEALREADYEXIST = 'InvalidParameterValue.DeviceAlreadyExist'

# 设备未绑定任何网关设备。
INVALIDPARAMETERVALUE_DEVICEHASNOTBINDGATEWAY = 'InvalidParameterValue.DeviceHasNotBindGateway'

# 设备不是网关类型。
INVALIDPARAMETERVALUE_DEVICEISNOTGATEWAY = 'InvalidParameterValue.DeviceIsNotGateway'

# 设备名称非法。
INVALIDPARAMETERVALUE_DEVICENAMEINVALID = 'InvalidParameterValue.DeviceNameInvalid'

# 设备不存在。
INVALIDPARAMETERVALUE_DEVICENOTEXIST = 'InvalidParameterValue.DeviceNotExist'

# 使用标准蓝牙广播协议的产品，DeviceName最多不超过8个字符。
INVALIDPARAMETERVALUE_ERRLLSYNCBROADCASTDEVICENAMELENGTHEXCEED = 'InvalidParameterValue.ErrLLSyncBroadcastDeviceNameLengthExceed'

# 任务不存在。
INVALIDPARAMETERVALUE_ERRORTASKNOTEXIST = 'InvalidParameterValue.ErrorTaskNotExist'

# 存失败，行为操作和转发错误行为数据目标不可为同一设备。
INVALIDPARAMETERVALUE_FAILACTIONHASSAMEDEVICE = 'InvalidParameterValue.FailActionHasSameDevice'

# 固件已经存在。
INVALIDPARAMETERVALUE_FIRMWAREALREADYEXIST = 'InvalidParameterValue.FirmwareAlreadyExist'

# 转发重定向被拒绝。
INVALIDPARAMETERVALUE_FORWARDREDIRECTDENIED = 'InvalidParameterValue.ForwardRedirectDenied'

# 拉取产品列表失败。
INVALIDPARAMETERVALUE_GETPRODUCTSLISTERROR = 'InvalidParameterValue.GetProductsListError'

# 回调 Token 格式有误
INVALIDPARAMETERVALUE_INVALIDCALLBACKTOKEN = 'InvalidParameterValue.InvalidCallbackToken'

# 回调 URL 无效或格式有误
INVALIDPARAMETERVALUE_INVALIDCALLBACKURL = 'InvalidParameterValue.InvalidCallbackUrl'

# SQL语句含有非法字符。
INVALIDPARAMETERVALUE_INVALIDSQL = 'InvalidParameterValue.InvalidSQL'

# LoRa频点参数错误。
INVALIDPARAMETERVALUE_LORAFREQPARMSERROR = 'InvalidParameterValue.LoRaFreqParmsError'

# 物模型不符合产品模板。
INVALIDPARAMETERVALUE_MODELDEFINEDONTMATCHTEMPLATE = 'InvalidParameterValue.ModelDefineDontMatchTemplate'

# 物模型存在重复ID。
INVALIDPARAMETERVALUE_MODELDEFINEDUPID = 'InvalidParameterValue.ModelDefineDupID'

# 物模型事件/属性Model错误。
INVALIDPARAMETERVALUE_MODELDEFINEERRORMODEL = 'InvalidParameterValue.ModelDefineErrorModel'

# 物模型事件/属性Model Type错误。
INVALIDPARAMETERVALUE_MODELDEFINEERRORTYPE = 'InvalidParameterValue.ModelDefineErrorType'

# 物模型EVENT Parms存在重复ID。
INVALIDPARAMETERVALUE_MODELDEFINEEVENTPARAMSDUPID = 'InvalidParameterValue.ModelDefineEventParamsDupID'

# 物模型EVENT Parms数量超过限制。
INVALIDPARAMETERVALUE_MODELDEFINEEVENTPARAMSEXCEEDLIMIT = 'InvalidParameterValue.ModelDefineEventParamsExceedLimit'

# 物模型事件/属性参数错误。
INVALIDPARAMETERVALUE_MODELDEFINEEVENTPROPERROR = 'InvalidParameterValue.ModelDefineEventPropError'

# 物模型事件/属性 Name 错误。
INVALIDPARAMETERVALUE_MODELDEFINEEVENTPROPNAMEERROR = 'InvalidParameterValue.ModelDefineEventPropNameError'

# 物模型事件 Type 错误:lac 。
INVALIDPARAMETERVALUE_MODELDEFINEEVENTTYPEERROR = 'InvalidParameterValue.ModelDefineEventTypeError'

# 数据模板未定义。
INVALIDPARAMETERVALUE_MODELDEFINEINVALID = 'InvalidParameterValue.ModelDefineInvalid'

# 物模型为空。
INVALIDPARAMETERVALUE_MODELDEFINENIL = 'InvalidParameterValue.ModelDefineNil'

# 物模型事件/属性 BOOL类型 Mapping 定义错误。
INVALIDPARAMETERVALUE_MODELDEFINEPROPBOOLMAPPINGERROR = 'InvalidParameterValue.ModelDefinePropBoolMappingError'

# 物模型事件/属性 Enum类型 Mapping 定义错误。
INVALIDPARAMETERVALUE_MODELDEFINEPROPENUMMAPPINGERROR = 'InvalidParameterValue.ModelDefinePropEnumMappingError'

# 物模型事件/属性 Min/Max 定义错误。
INVALIDPARAMETERVALUE_MODELDEFINEPROPRANGEERROR = 'InvalidParameterValue.ModelDefinePropRangeError'

# 物模型事件/属性 Min/Max 范围超限。
INVALIDPARAMETERVALUE_MODELDEFINEPROPRANGEOVERFLOW = 'InvalidParameterValue.ModelDefinePropRangeOverflow'

# 属性ID不存在。
INVALIDPARAMETERVALUE_MODELPROPERTYNOTEXIST = 'InvalidParameterValue.ModelPropertyNotExist'

# 消息内容非法。
INVALIDPARAMETERVALUE_MSGCONTENTINVALID = 'InvalidParameterValue.MsgContentInvalid'

# 消息等级非法。
INVALIDPARAMETERVALUE_MSGLEVELINVALID = 'InvalidParameterValue.MsgLevelInvalid'

# 消息标题非法。
INVALIDPARAMETERVALUE_MSGTITLEINVALID = 'InvalidParameterValue.MsgTitleInvalid'

# 消息类型非法。
INVALIDPARAMETERVALUE_MSGTYPEINVALID = 'InvalidParameterValue.MsgTypeInvalid'

# 无权限。
INVALIDPARAMETERVALUE_NOPERMISSION = 'InvalidParameterValue.NoPermission'

# 操作不支持。
INVALIDPARAMETERVALUE_OPERATIONDENIED = 'InvalidParameterValue.OperationDenied'

# 消息Payload超出限制。
INVALIDPARAMETERVALUE_PAYLOADOVERLIMIT = 'InvalidParameterValue.PayloadOverLimit'

# 创建的产品名已存在。
INVALIDPARAMETERVALUE_PRODUCTALREADYEXIST = 'InvalidParameterValue.ProductAlreadyExist'

# 产品ID非法。
INVALIDPARAMETERVALUE_PRODUCTIDINVALID = 'InvalidParameterValue.ProductIDInvalid'

# 产品不是网关类型，无法绑定子产品。
INVALIDPARAMETERVALUE_PRODUCTISNOTGATEWAY = 'InvalidParameterValue.ProductIsNotGateway'

# 产品参数错误。
INVALIDPARAMETERVALUE_PRODUCTPARMSERROR = 'InvalidParameterValue.ProductParmsError'

# 项目参数错误。
INVALIDPARAMETERVALUE_PROJECTPARMSERROR = 'InvalidParameterValue.ProjectParmsError'

# PushEnvironment 非法。
INVALIDPARAMETERVALUE_PUSHENVIRONMENTINVALID = 'InvalidParameterValue.PushEnvironmentInvalid'

# 转发的topic格式错误。
INVALIDPARAMETERVALUE_REPUBLISHTOPICFORMATERROR = 'InvalidParameterValue.RepublishTopicFormatError'

# 规则数量超过限制。
INVALIDPARAMETERVALUE_RULENUMBERBEYONDLIMIT = 'InvalidParameterValue.RuleNumberBeyondLimit'

# 二进制数据格式只可利用 * 将数据进行转发。
INVALIDPARAMETERVALUE_SELECTKEYFROMBINARYPAYLOAD = 'InvalidParameterValue.SelectKeyFromBinaryPayload'

# 开始时间晚于结束时间。
INVALIDPARAMETERVALUE_STARTTIMELATERENDTIME = 'InvalidParameterValue.StartTimeLaterEndTime'

# TPNSAndroidAccessID, TPNSAndroidSecretKey, TPNSAndroidRegion validation failed。
INVALIDPARAMETERVALUE_TPNSANDROIDVALIDATIONFAILED = 'InvalidParameterValue.TPNSAndroidValidationFailed'

# TPNSiOSAccessID, TPNSiOSSecretKey, TPNSiOSRegion validation failed。
INVALIDPARAMETERVALUE_TPNSIOSVALIDATIONFAILED = 'InvalidParameterValue.TPNSiOSValidationFailed'

# Topic已存在。
INVALIDPARAMETERVALUE_TOPICPOLICYALREADYEXIST = 'InvalidParameterValue.TopicPolicyAlreadyExist'

# 规则已存在。
INVALIDPARAMETERVALUE_TOPICRULEALREADYEXIST = 'InvalidParameterValue.TopicRuleAlreadyExist'

# 规则sql未编辑。
INVALIDPARAMETERVALUE_TOPICRULESQLNOTEDITED = 'InvalidParameterValue.TopicRuleSqlNotEdited'

# 请确认规则相关数据是否有更新。
INVALIDPARAMETERVALUE_UPDATETOPICRULEDBFAIL = 'InvalidParameterValue.UpdateTopicRuleDBFail'

# 用户ID非法。
INVALIDPARAMETERVALUE_USERIDINVALID = 'InvalidParameterValue.UserIDInvalid'

# VPN参数错误。
INVALIDPARAMETERVALUE_VPNPARMSERROR = 'InvalidParameterValue.VPNParmsError'

# 应用数量超出限制。
LIMITEXCEEDED_APPLICATIONEXCEEDLIMIT = 'LimitExceeded.ApplicationExceedLimit'

# 量产超出限制。
LIMITEXCEEDED_BATCHPRODUCTIONEXCEEDLIMIT = 'LimitExceeded.BatchProductionExceedLimit'

# 量产为空。
LIMITEXCEEDED_BATCHPRODUCTIONNULL = 'LimitExceeded.BatchProductionNull'

# 绑定的产品数量超过限制。
LIMITEXCEEDED_BINDPRODUCTSEXCEEDLIMIT = 'LimitExceeded.BindProductsExceedLimit'

# 设备数量超过限制。
LIMITEXCEEDED_DEVICEEXCEEDLIMIT = 'LimitExceeded.DeviceExceedLimit'

# 固件数量超出限制。
LIMITEXCEEDED_FIRMWAREEXCEEDLIMIT = 'LimitExceeded.FirmwareExceedLimit'

# 消息数量超过限制。
LIMITEXCEEDED_MESSAGESAVED = 'LimitExceeded.MessageSaved'

# 超过产品数量限制。
LIMITEXCEEDED_PRODUCTEXCEEDLIMIT = 'LimitExceeded.ProductExceedLimit'

# 项目数量超出限制。
LIMITEXCEEDED_PROJECTEXCEEDLIMIT = 'LimitExceeded.ProjectExceedLimit'

# LoRa频点数量超出限制。
LIMITEXCEEDED_STUDIOLORAFREQEXCEEDLIMIT = 'LimitExceeded.StudioLoRaFreqExceedLimit'

# 产品数量超出限制。
LIMITEXCEEDED_STUDIOPRODUCTEXCEEDLIMIT = 'LimitExceeded.StudioProductExceedLimit'

# 物模型超出限制。
LIMITEXCEEDED_THINGMODELEXCEEDLIMIT = 'LimitExceeded.ThingModelExceedLimit'

# Topic数量超出限制。
LIMITEXCEEDED_TOPICPOLICYEXCEEDLIMIT = 'LimitExceeded.TopicPolicyExceedLimit'

# 物模型事件 Type 错误。
MISSINGPARAMETER_MODELDEFINEEVENTTYPEERROR = 'MissingParameter.ModelDefineEventTypeError'

# 资源不足。
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# 已有量产进行，请等待量产完成。
RESOURCEINSUFFICIENT_BATCHPRODUCTIONISRUNNING = 'ResourceInsufficient.BatchProductionIsRunning'

# 云存 AI 分析任务创建额度不足
RESOURCEINSUFFICIENT_CLOUDSTORAGEAISERVICETASKQUOTAINSUFFICIENT = 'ResourceInsufficient.CloudStorageAIServiceTaskQuotaInsufficient'

# 资源不存在。
RESOURCENOTFOUND = 'ResourceNotFound'

# App不存在。
RESOURCENOTFOUND_APPNOTEXISTS = 'ResourceNotFound.AppNotExists'

# 量产不存在。
RESOURCENOTFOUND_BATCHPRODUCTIONNOTEXIST = 'ResourceNotFound.BatchProductionNotExist'

# 上传URL无法获取。
RESOURCENOTFOUND_CANNOTGETFROMURL = 'ResourceNotFound.CannotGetFromUrl'

# 云存AI分析任务不存在
RESOURCENOTFOUND_CLOUDSTORAGEAISERVICETASK = 'ResourceNotFound.CloudStorageAIServiceTask'

# 云存AI分析任务输出文件不存在
RESOURCENOTFOUND_CLOUDSTORAGEAISERVICETASKFILE = 'ResourceNotFound.CloudStorageAIServiceTaskFile'

# 存在重复设备。
RESOURCENOTFOUND_DEVICEDUPKEYEXIST = 'ResourceNotFound.DeviceDupKeyExist'

# 设备固件信息不存在。
RESOURCENOTFOUND_DEVICEFIRMWARENOTEXIST = 'ResourceNotFound.DeviceFirmWareNotExist'

# 固件不存在。
RESOURCENOTFOUND_DEVICEHASNOFIRMWARE = 'ResourceNotFound.DeviceHasNoFirmware'

# 设备未绑定家庭。
RESOURCENOTFOUND_DEVICENOTBIND = 'ResourceNotFound.DeviceNotBind'

# 设备不存在。
RESOURCENOTFOUND_DEVICENOTEXIST = 'ResourceNotFound.DeviceNotExist'

# 设备影子未创建或是已删除。
RESOURCENOTFOUND_DEVICESHADOWNOTEXIST = 'ResourceNotFound.DeviceShadowNotExist'

# 围栏未绑定该设备。
RESOURCENOTFOUND_FENCEBINDNOTEXIST = 'ResourceNotFound.FenceBindNotExist'

# 围栏未创建或是已删除。
RESOURCENOTFOUND_FENCENOTEXIST = 'ResourceNotFound.FenceNotExist'

# 固件不存在。
RESOURCENOTFOUND_FIRMWARENOTEXIST = 'ResourceNotFound.FirmwareNotExist'

# 固件升级任务不存在。
RESOURCENOTFOUND_FIRMWARETASKNOTEXIST = 'ResourceNotFound.FirmwareTaskNotExist'

# 存在重复网关。
RESOURCENOTFOUND_GATEWAYDUPKEYEXIST = 'ResourceNotFound.GatewayDupKeyExist'

# 网关不存在。
RESOURCENOTFOUND_GATEWAYNOTEXIST = 'ResourceNotFound.GatewayNotExist'

# 实例未创建或是已删除。
RESOURCENOTFOUND_INSTANCENOTEXIST = 'ResourceNotFound.InstanceNotExist'

# 模组不存在或改动未生效。
RESOURCENOTFOUND_MODULENOTEXIST = 'ResourceNotFound.ModuleNotExist'

# 产品不存在。
RESOURCENOTFOUND_PRODUCTNOTEXIST = 'ResourceNotFound.ProductNotExist'

# 产品或设备不存在。
RESOURCENOTFOUND_PRODUCTORDEVICENOTEXIST = 'ResourceNotFound.ProductOrDeviceNotExist'

# 产品资源不存在。
RESOURCENOTFOUND_PRODUCTRESOURCENOTEXIST = 'ResourceNotFound.ProductResourceNotExist'

# 项目不存在。
RESOURCENOTFOUND_PROJECTNOTEXIST = 'ResourceNotFound.ProjectNotExist'

# 位置空间未创建或是已删除。
RESOURCENOTFOUND_SPACENOTEXIST = 'ResourceNotFound.SpaceNotExist'

# LoRa频点尚未创建或已被删除。
RESOURCENOTFOUND_STUDIOLORAFREQNOTEXIST = 'ResourceNotFound.StudioLoRaFreqNotExist'

# 产品不存在。
RESOURCENOTFOUND_STUDIOPRODUCTNOTEXIST = 'ResourceNotFound.StudioProductNotExist'

# Topic不存在。
RESOURCENOTFOUND_TOPICPOLICYNOTEXIST = 'ResourceNotFound.TopicPolicyNotExist'

# 规则不存在。
RESOURCENOTFOUND_TOPICRULENOTEXIST = 'ResourceNotFound.TopicRuleNotExist'

# 未授权操作。
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# APP对产品没有权限。
UNAUTHORIZEDOPERATION_APPNOPERMISSIONTOSTUDIOPRODUCT = 'UnauthorizedOperation.APPNoPermissionToStudioProduct'

# App无权限。
UNAUTHORIZEDOPERATION_APPNOPERMISSION = 'UnauthorizedOperation.AppNoPermission'

# 该设备绑定了网关设备，无法删除。
UNAUTHORIZEDOPERATION_DEVICEHASALREADYBINDGATEWAY = 'UnauthorizedOperation.DeviceHasAlreadyBindGateway'

# 设备未启用。
UNAUTHORIZEDOPERATION_DEVICEISNOTENABLED = 'UnauthorizedOperation.DeviceIsNotEnabled'

# 该设备下仍有绑定的设备。
UNAUTHORIZEDOPERATION_GATEWAYHASBINDEDDEVICES = 'UnauthorizedOperation.GatewayHasBindedDevices'

# 此家庭无权操作。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOFAMILY = 'UnauthorizedOperation.NoPermissionToFamily'

# 实例ACL错误。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOINSTANCE = 'UnauthorizedOperation.NoPermissionToInstance'

# 项目ACL错误。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOPROJECT = 'UnauthorizedOperation.NoPermissionToProject'

# 围栏ACL错误。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOSTUDIOFENCE = 'UnauthorizedOperation.NoPermissionToStudioFence'

# 实例ACL错误。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOSTUDIOINSTANCE = 'UnauthorizedOperation.NoPermissionToStudioInstance'

# 产品ACL错误。
UNAUTHORIZEDOPERATION_NOPERMISSIONTOSTUDIOPRODUCT = 'UnauthorizedOperation.NoPermissionToStudioProduct'

# 无权操作该房间
UNAUTHORIZEDOPERATION_NOPERMISSIONTOTRTCROOM = 'UnauthorizedOperation.NoPermissionToTRTCRoom'

# 您的账号未实名认证，请登录腾讯云进行实名认证
UNAUTHORIZEDOPERATION_NOVERIFIED = 'UnauthorizedOperation.NoVerified'

# 没有权限。
UNAUTHORIZEDOPERATION_PERMISSIONDENIED = 'UnauthorizedOperation.PermissionDenied'

# 产品不支持密钥认证。
UNAUTHORIZEDOPERATION_PRODUCTNOTSUPPORTPSK = 'UnauthorizedOperation.ProductNotSupportPSK'

# License数量不足。
UNAUTHORIZEDOPERATION_USERLICENSEEXCEEDLIMIT = 'UnauthorizedOperation.UserLicenseExceedLimit'

# 未知参数错误。
UNKNOWNPARAMETER = 'UnknownParameter'

# 操作不支持。
UNSUPPORTEDOPERATION = 'UnsupportedOperation'

# 围栏下还存在绑定的设备。
UNSUPPORTEDOPERATION_BINDSEXISTUNDERFENCE = 'UnsupportedOperation.BindsExistUnderFence'

# 存在重复的绑定关系。
UNSUPPORTEDOPERATION_CANNOTREBINDFAMILY = 'UnsupportedOperation.CannotReBindFamily'

# 云存套餐与云存 AI 套餐时长不匹配
UNSUPPORTEDOPERATION_CLOUDSTORAGEPACKAGETIMEMISMATCH = 'UnsupportedOperation.CloudStoragePackageTimeMismatch'

# 云存套餐与云存 AI 套餐类型不匹配
UNSUPPORTEDOPERATION_CLOUDSTORAGEPACKAGETYPEMISMATCH = 'UnsupportedOperation.CloudStoragePackageTypeMismatch'

# 创建的设备已经存在。
UNSUPPORTEDOPERATION_DEVICEDUPKEYEXIST = 'UnsupportedOperation.DeviceDupKeyExist'

# 设备数量超出实例限制。
UNSUPPORTEDOPERATION_DEVICEEXCEEDLIMIT = 'UnsupportedOperation.DeviceExceedLimit'

# 设备ota升级中。
UNSUPPORTEDOPERATION_DEVICEOTATASKINPROGRESS = 'UnsupportedOperation.DeviceOtaTaskInProgress'

# 设备类型错误。
UNSUPPORTEDOPERATION_DEVICETYPE = 'UnsupportedOperation.DeviceType'

# 产品下还存在未删除的设备。
UNSUPPORTEDOPERATION_DEVICESEXISTUNDERPRODUCT = 'UnsupportedOperation.DevicesExistUnderProduct'

# 该项目下存在物联使能SaaS服务。
UNSUPPORTEDOPERATION_ENABLESAASSERVICEEXISTUNDERPROJECT = 'UnsupportedOperation.EnableSaasServiceExistUnderProject'

# 网关产品下存在设备绑定了子设备。
UNSUPPORTEDOPERATION_EXISTBINDEDDEVICESUNDERGATEWAYPRODUCT = 'UnsupportedOperation.ExistBindedDevicesUnderGatewayProduct'

# 存在重复围栏。
UNSUPPORTEDOPERATION_FENCEDUPKEYEXIST = 'UnsupportedOperation.FenceDupKeyExist'

# 位置空间下还存在未删除的围栏。
UNSUPPORTEDOPERATION_FENCEEXISTUNDERSPACE = 'UnsupportedOperation.FenceExistUnderSpace'

# 网关产品还绑定子产品，无法删除。
UNSUPPORTEDOPERATION_GATEWAYPRODUCTHASBINDEDPRODUCT = 'UnsupportedOperation.GatewayProductHasBindedProduct'

# 由于实例到期已被禁用，请续费后使用。
UNSUPPORTEDOPERATION_INSTANCEISOLATED = 'UnsupportedOperation.InstanceIsolated'

# 存在重复LoRa频点。
UNSUPPORTEDOPERATION_LORAFREQDUPKEYEXIST = 'UnsupportedOperation.LoRaFreqDupKeyExist'

# LoRa设备未上报数据。
UNSUPPORTEDOPERATION_LORANOUPLINK = 'UnsupportedOperation.LoRaNoUpLink'

# Lora设备没有激活。
UNSUPPORTEDOPERATION_LORANOTACTIVATE = 'UnsupportedOperation.LoRaNotActivate'

# VPN下还存在未删除的设备。
UNSUPPORTEDOPERATION_NODESEXISTUNDERVPN = 'UnsupportedOperation.NodesExistUnderVPN'

# 该项目下还存在人员库，需删除人员库后才允许删除项目。
UNSUPPORTEDOPERATION_POOLEXISTUNDERPROJECT = 'UnsupportedOperation.PoolExistUnderProject'

# 存在重复产品。
UNSUPPORTEDOPERATION_PRODUCTDUPKEYEXIST = 'UnsupportedOperation.ProductDupKeyExist'

# 项目下有产品。
UNSUPPORTEDOPERATION_PRODUCTEXISTUNDERPROJECT = 'UnsupportedOperation.ProductExistUnderProject'

# 产品被绑定到网关产品。
UNSUPPORTEDOPERATION_PRODUCTHASBINDEDGATEWAYPRODUCT = 'UnsupportedOperation.ProductHasBindedGateWayProduct'

# 产品已被共享，请先解除共享。
UNSUPPORTEDOPERATION_PRODUCTHASSHARED = 'UnsupportedOperation.ProductHasShared'

# 存在重复项目。
UNSUPPORTEDOPERATION_PROJECTDUPKEYEXIST = 'UnsupportedOperation.ProjectDupKeyExist'

# 存在重复位置空间。
UNSUPPORTEDOPERATION_SPACEDUPKEYEXIST = 'UnsupportedOperation.SpaceDupKeyExist'

# 人员库名称已存在。
UNSUPPORTEDOPERATION_STAFFPOOLDUPNAMEEXIST = 'UnsupportedOperation.StaffPoolDupNameExist'

# LoRa频点还被节点或网关使用。
UNSUPPORTEDOPERATION_STUDIOLORAFREQINUSED = 'UnsupportedOperation.StudioLoRaFreqInUsed'

# TRTC增值服务未开通
UNSUPPORTEDOPERATION_TRTCSERVICENOTOPEN = 'UnsupportedOperation.TRTCServiceNotOpen'

# 账户有未支付订单。
UNSUPPORTEDOPERATION_UNPAIDORDER = 'UnsupportedOperation.UnpaidOrder'

# 存在重复VPN。
UNSUPPORTEDOPERATION_VPNDUPKEYEXIST = 'UnsupportedOperation.VPNDupKeyExist'

# Video账户未创建，请检查后重新操作。
UNSUPPORTEDOPERATION_VIDEOACCOUNTNOTEXIST = 'UnsupportedOperation.VideoAccountNotExist'

# Video平台license数量不足。
UNSUPPORTEDOPERATION_VIDEOINSUFFICIENTLICENSES = 'UnsupportedOperation.VideoInsufficientLicenses'

# Video平台产品不存在。
UNSUPPORTEDOPERATION_VIDEOPRODUCTNOTEXIST = 'UnsupportedOperation.VideoProductNotExist'
