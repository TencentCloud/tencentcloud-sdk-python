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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DescribeEntityRequest(AbstractModel):
    """DescribeEntity请求参数结构体

    """

    def __init__(self):
        """
        :param EntityName: 实体名称
        :type EntityName: str
        """
        self.EntityName = None


    def _deserialize(self, params):
        self.EntityName = params.get("EntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeEntityResponse(AbstractModel):
    """DescribeEntity返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体相关信息
        :type Content: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRelationRequest(AbstractModel):
    """DescribeRelation请求参数结构体

    """

    def __init__(self):
        """
        :param LeftEntityName: 输入第一个实体
        :type LeftEntityName: str
        :param RightEntityName: 输入第二个实体
        :type RightEntityName: str
        """
        self.LeftEntityName = None
        self.RightEntityName = None


    def _deserialize(self, params):
        self.LeftEntityName = params.get("LeftEntityName")
        self.RightEntityName = params.get("RightEntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeRelationResponse(AbstractModel):
    """DescribeRelation返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体间的关系
        :type Content: list of EntityRelationContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EntityRelationContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTripleRequest(AbstractModel):
    """DescribeTriple请求参数结构体

    """

    def __init__(self):
        """
        :param TripleCondition: 三元组查询条件
        :type TripleCondition: str
        """
        self.TripleCondition = None


    def _deserialize(self, params):
        self.TripleCondition = params.get("TripleCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTripleResponse(AbstractModel):
    """DescribeTriple返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回三元组信息
        :type Content: list of TripleContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TripleContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EntityRelationContent(AbstractModel):
    """返回的实体关系查询结果详细内容

    """

    def __init__(self):
        """
        :param Object: 实体关系查询返回关系的object
        :type Object: list of EntityRelationObject
        :param Subject: 实体关系查询返回关系的subject
        :type Subject: list of EntityRelationSubject
        :param Relation: 实体关系查询返回的关系名称
        :type Relation: str
        """
        self.Object = None
        self.Subject = None
        self.Relation = None


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self.Object = []
            for item in params.get("Object"):
                obj = EntityRelationObject()
                obj._deserialize(item)
                self.Object.append(obj)
        if params.get("Subject") is not None:
            self.Subject = []
            for item in params.get("Subject"):
                obj = EntityRelationSubject()
                obj._deserialize(item)
                self.Subject.append(obj)
        self.Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EntityRelationObject(AbstractModel):
    """实体关系查询返回的Object类型

    """

    def __init__(self):
        """
        :param Id: object对应id
        :type Id: list of str
        :param Name: object对应name
        :type Name: list of str
        :param Popular: object对应popular值
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EntityRelationSubject(AbstractModel):
    """实体关系查询返回Subject

    """

    def __init__(self):
        """
        :param Id: Subject对应id
        :type Id: list of str
        :param Name: Subject对应name
        :type Name: list of str
        :param Popular: Subject对应popular
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TripleContent(AbstractModel):
    """三元组查询返回的元记录

    """

    def __init__(self):
        """
        :param Id: 实体id
        :type Id: str
        :param Name: 实体名称
        :type Name: str
        :param Order: 实体order
        :type Order: int
        :param Popular: 实体流行度
        :type Popular: int
        """
        self.Id = None
        self.Name = None
        self.Order = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        self.Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        