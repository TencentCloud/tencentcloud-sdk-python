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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DescribeEntityRequest(AbstractModel):
    """DescribeEntity请求参数结构体

    """

    def __init__(self):
        """
        :param EntityName: 实体名称\n        :type EntityName: str\n        """
        self.EntityName = None


    def _deserialize(self, params):
        self.EntityName = params.get("EntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEntityResponse(AbstractModel):
    """DescribeEntity返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体相关信息\n        :type Content: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")


class DescribeRelationRequest(AbstractModel):
    """DescribeRelation请求参数结构体

    """

    def __init__(self):
        """
        :param LeftEntityName: 输入第一个实体\n        :type LeftEntityName: str\n        :param RightEntityName: 输入第二个实体\n        :type RightEntityName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelationResponse(AbstractModel):
    """DescribeRelation返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体间的关系\n        :type Content: list of EntityRelationContent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTripleRequest(AbstractModel):
    """DescribeTriple请求参数结构体

    """

    def __init__(self):
        """
        :param TripleCondition: 三元组查询条件\n        :type TripleCondition: str\n        """
        self.TripleCondition = None


    def _deserialize(self, params):
        self.TripleCondition = params.get("TripleCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTripleResponse(AbstractModel):
    """DescribeTriple返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回三元组信息\n        :type Content: list of TripleContent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class EntityRelationContent(AbstractModel):
    """返回的实体关系查询结果详细内容

    """

    def __init__(self):
        """
        :param Object: 实体关系查询返回关系的object\n        :type Object: list of EntityRelationObject\n        :param Subject: 实体关系查询返回关系的subject\n        :type Subject: list of EntityRelationSubject\n        :param Relation: 实体关系查询返回的关系名称\n        :type Relation: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationObject(AbstractModel):
    """实体关系查询返回的Object类型

    """

    def __init__(self):
        """
        :param Id: object对应id\n        :type Id: list of str\n        :param Name: object对应name\n        :type Name: list of str\n        :param Popular: object对应popular值\n        :type Popular: list of int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationSubject(AbstractModel):
    """实体关系查询返回Subject

    """

    def __init__(self):
        """
        :param Id: Subject对应id\n        :type Id: list of str\n        :param Name: Subject对应name\n        :type Name: list of str\n        :param Popular: Subject对应popular\n        :type Popular: list of int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TripleContent(AbstractModel):
    """三元组查询返回的元记录

    """

    def __init__(self):
        """
        :param Id: 实体id\n        :type Id: str\n        :param Name: 实体名称\n        :type Name: str\n        :param Order: 实体order\n        :type Order: int\n        :param Popular: 实体流行度\n        :type Popular: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        