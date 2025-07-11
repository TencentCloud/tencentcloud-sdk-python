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

# 当前用户鉴权失败。
AUTHFAILURE_UNAUTHORIZEDOPERATION = 'AuthFailure.UnauthorizedOperation'

# 操作失败。
FAILEDOPERATION = 'FailedOperation'

# 调用API服务失败。
FAILEDOPERATION_APISERVERFAIL = 'FailedOperation.APIServerFail'

# 客户端已离线。
FAILEDOPERATION_AGENTOFFLINE = 'FailedOperation.AgentOffline'

# 导出文件失败。
FAILEDOPERATION_EXPORT = 'FailedOperation.Export'

# 可用license数量不足，缺少1个license，请购买新license。
FAILEDOPERATION_LICENSEEXCEEDED = 'FailedOperation.LicenseExceeded'

# 卸载主机。
FAILEDOPERATION_MACHINEDELETE = 'FailedOperation.MachineDelete'

# 无专业版主机。
FAILEDOPERATION_NOPROFESSIONHOST = 'FailedOperation.NoProfessionHost'

# 多台主机隔离，部分或全部失败。
FAILEDOPERATION_PARTSEPARATE = 'FailedOperation.PartSeparate'

# 开启防护失败。
FAILEDOPERATION_PROTECTSTARTFAIL = 'FailedOperation.ProtectStartFail'

# 回复木马失败。
FAILEDOPERATION_RECOVER = 'FailedOperation.Recover'

# 重新检测漏洞失败。
FAILEDOPERATION_RESCANVUL = 'FailedOperation.RescanVul'

# 单台主机隔离失败。
FAILEDOPERATION_SINGLESEPARATE = 'FailedOperation.SingleSeparate'

# 创建基线策略超过上限。
FAILEDOPERATION_TOOMANYSTRATEGY = 'FailedOperation.TooManyStrategy'

# 内部错误。
INTERNALERROR = 'InternalError'

# 操作数据失败。
INTERNALERROR_MAINDBFAIL = 'InternalError.MainDBFail'

# 参数错误。
INVALIDPARAMETER = 'InvalidParameter'

# 时间区间格式错误。
INVALIDPARAMETER_DATERANGE = 'InvalidParameter.DateRange'

# 非法请求。
INVALIDPARAMETER_ILLEGALREQUEST = 'InvalidParameter.IllegalRequest'

# 参数格式错误。
INVALIDPARAMETER_INVALIDFORMAT = 'InvalidParameter.InvalidFormat'

# IP格式不合法。
INVALIDPARAMETER_IPNOVALID = 'InvalidParameter.IpNoValid'

# 参数缺失。
INVALIDPARAMETER_MISSINGPARAMETER = 'InvalidParameter.MissingParameter'

# 名字已重复。
INVALIDPARAMETER_NAMEHASREPETITION = 'InvalidParameter.NameHasRepetition'

# 参数解析错误。
INVALIDPARAMETER_PARSINGERROR = 'InvalidParameter.ParsingError'

# 端口格式不合法。
INVALIDPARAMETER_PORTNOVALID = 'InvalidParameter.PortNoValid'

# 正则参数格式错误。
INVALIDPARAMETER_REGEXRULEERROR = 'InvalidParameter.RegexRuleError'

# 进程名/目标IP/目标端口，不能同时为空。
INVALIDPARAMETER_REVERSHELLKEYFIELDALLEMPTY = 'InvalidParameter.ReverShellKeyFieldAllEmpty'

# 规则类接口，主机重复。
INVALIDPARAMETER_RULEHOSTDUPLICATEERR = 'InvalidParameter.RuleHostDuplicateErr'

# 规则类接口，主机IP不正确。
INVALIDPARAMETER_RULEHOSTIPERR = 'InvalidParameter.RuleHostipErr'

# 参数取值错误。
INVALIDPARAMETERVALUE = 'InvalidParameterValue'

# 标签名称长度不能超过15个字符。
INVALIDPARAMETERVALUE_TAGNAMELENGTHLIMIT = 'InvalidParameterValue.TagNameLengthLimit'

# 超过配额限制。
LIMITEXCEEDED = 'LimitExceeded'

# 超出批量添加数量。
LIMITEXCEEDED_AREAQUOTA = 'LimitExceeded.AreaQuota'

# 缺少参数错误。
MISSINGPARAMETER = 'MissingParameter'

# 操作被拒绝。
OPERATIONDENIED = 'OperationDenied'

# 资源被占用。
RESOURCEINUSE = 'ResourceInUse'

# 资源不足。
RESOURCEINSUFFICIENT = 'ResourceInsufficient'

# 资源不存在。
RESOURCENOTFOUND = 'ResourceNotFound'

# 扫描机器不存在。
RESOURCENOTFOUND_MACHINENOTFOUND = 'ResourceNotFound.MachineNotFound'

# 资源不可用。
RESOURCEUNAVAILABLE = 'ResourceUnavailable'

# 未授权操作。
UNAUTHORIZEDOPERATION = 'UnauthorizedOperation'

# 未知参数错误。
UNKNOWNPARAMETER = 'UnknownParameter'

# 操作不支持。
UNSUPPORTEDOPERATION = 'UnsupportedOperation'
