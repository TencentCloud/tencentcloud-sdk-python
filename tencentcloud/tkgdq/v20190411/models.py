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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class DescribeEntityRequest(AbstractModel):
    r"""DescribeEntity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EntityName: 实体名称
        :type EntityName: str
        """
        self._EntityName = None

    @property
    def EntityName(self):
        r"""实体名称
        :rtype: str
        """
        return self._EntityName

    @EntityName.setter
    def EntityName(self, EntityName):
        self._EntityName = EntityName


    def _deserialize(self, params):
        self._EntityName = params.get("EntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEntityResponse(AbstractModel):
    r"""DescribeEntity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 返回查询实体相关信息
        :type Content: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._RequestId = None

    @property
    def Content(self):
        r"""返回查询实体相关信息
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class DescribeRelationRequest(AbstractModel):
    r"""DescribeRelation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LeftEntityName: 输入第一个实体
        :type LeftEntityName: str
        :param _RightEntityName: 输入第二个实体
        :type RightEntityName: str
        """
        self._LeftEntityName = None
        self._RightEntityName = None

    @property
    def LeftEntityName(self):
        r"""输入第一个实体
        :rtype: str
        """
        return self._LeftEntityName

    @LeftEntityName.setter
    def LeftEntityName(self, LeftEntityName):
        self._LeftEntityName = LeftEntityName

    @property
    def RightEntityName(self):
        r"""输入第二个实体
        :rtype: str
        """
        return self._RightEntityName

    @RightEntityName.setter
    def RightEntityName(self, RightEntityName):
        self._RightEntityName = RightEntityName


    def _deserialize(self, params):
        self._LeftEntityName = params.get("LeftEntityName")
        self._RightEntityName = params.get("RightEntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelationResponse(AbstractModel):
    r"""DescribeRelation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 返回查询实体间的关系
        :type Content: list of EntityRelationContent
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._RequestId = None

    @property
    def Content(self):
        r"""返回查询实体间的关系
        :rtype: list of EntityRelationContent
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = EntityRelationContent()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTripleRequest(AbstractModel):
    r"""DescribeTriple请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TripleCondition: 三元组查询条件
        :type TripleCondition: str
        """
        self._TripleCondition = None

    @property
    def TripleCondition(self):
        r"""三元组查询条件
        :rtype: str
        """
        return self._TripleCondition

    @TripleCondition.setter
    def TripleCondition(self, TripleCondition):
        self._TripleCondition = TripleCondition


    def _deserialize(self, params):
        self._TripleCondition = params.get("TripleCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTripleResponse(AbstractModel):
    r"""DescribeTriple返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 返回三元组信息
        :type Content: list of TripleContent
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._RequestId = None

    @property
    def Content(self):
        r"""返回三元组信息
        :rtype: list of TripleContent
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        r"""唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self._Content = []
            for item in params.get("Content"):
                obj = TripleContent()
                obj._deserialize(item)
                self._Content.append(obj)
        self._RequestId = params.get("RequestId")


class EntityRelationContent(AbstractModel):
    r"""返回的实体关系查询结果详细内容

    """

    def __init__(self):
        r"""
        :param _Object: 实体关系查询返回关系的object
        :type Object: list of EntityRelationObject
        :param _Subject: 实体关系查询返回关系的subject
        :type Subject: list of EntityRelationSubject
        :param _Relation: 实体关系查询返回的关系名称
        :type Relation: str
        """
        self._Object = None
        self._Subject = None
        self._Relation = None

    @property
    def Object(self):
        r"""实体关系查询返回关系的object
        :rtype: list of EntityRelationObject
        """
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object

    @property
    def Subject(self):
        r"""实体关系查询返回关系的subject
        :rtype: list of EntityRelationSubject
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def Relation(self):
        r"""实体关系查询返回的关系名称
        :rtype: str
        """
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self._Object = []
            for item in params.get("Object"):
                obj = EntityRelationObject()
                obj._deserialize(item)
                self._Object.append(obj)
        if params.get("Subject") is not None:
            self._Subject = []
            for item in params.get("Subject"):
                obj = EntityRelationSubject()
                obj._deserialize(item)
                self._Subject.append(obj)
        self._Relation = params.get("Relation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationObject(AbstractModel):
    r"""实体关系查询返回的Object类型

    """

    def __init__(self):
        r"""
        :param _Id: object对应id
        :type Id: list of str
        :param _Name: object对应name
        :type Name: list of str
        :param _Popular: object对应popular值
        :type Popular: list of int
        """
        self._Id = None
        self._Name = None
        self._Popular = None

    @property
    def Id(self):
        r"""object对应id
        :rtype: list of str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""object对应name
        :rtype: list of str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Popular(self):
        r"""object对应popular值
        :rtype: list of int
        """
        return self._Popular

    @Popular.setter
    def Popular(self, Popular):
        self._Popular = Popular


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationSubject(AbstractModel):
    r"""实体关系查询返回Subject

    """

    def __init__(self):
        r"""
        :param _Id: Subject对应id
        :type Id: list of str
        :param _Name: Subject对应name
        :type Name: list of str
        :param _Popular: Subject对应popular
        :type Popular: list of int
        """
        self._Id = None
        self._Name = None
        self._Popular = None

    @property
    def Id(self):
        r"""Subject对应id
        :rtype: list of str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""Subject对应name
        :rtype: list of str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Popular(self):
        r"""Subject对应popular
        :rtype: list of int
        """
        return self._Popular

    @Popular.setter
    def Popular(self, Popular):
        self._Popular = Popular


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TripleContent(AbstractModel):
    r"""三元组查询返回的元记录

    """

    def __init__(self):
        r"""
        :param _Id: 实体id
        :type Id: str
        :param _Name: 实体名称
        :type Name: str
        :param _Order: 实体order
        :type Order: int
        :param _Popular: 实体流行度
        :type Popular: int
        """
        self._Id = None
        self._Name = None
        self._Order = None
        self._Popular = None

    @property
    def Id(self):
        r"""实体id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""实体名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Order(self):
        r"""实体order
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Popular(self):
        r"""实体流行度
        :rtype: int
        """
        return self._Popular

    @Popular.setter
    def Popular(self, Popular):
        self._Popular = Popular


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Order = params.get("Order")
        self._Popular = params.get("Popular")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        