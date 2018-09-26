# Copyright 1999-2017 Tencent Ltd.
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
import sys


class AbstractModel(object):
    """Base class for all models."""

    def _serialize(self):
        """Get all params which are not None."""
        def dfs(obj):
            if isinstance(obj, AbstractModel):
                d = vars(obj)
                return {k[0].upper() + k[1:]: dfs(d[k]) for k in d if dfs(d[k]) is not None}
            elif isinstance(obj, list):
                return [dfs(o) for o in obj if dfs(o) is not None]
            else:
                return obj.encode("UTF-8") if isinstance(obj, type(u"")) and sys.version_info[0] == 2 else obj

        return dfs(self)

    def _deserialize(self, params):
        return None

    def to_json_string(self,json_indent=None):
        """Serialize obj to a JSON formatted str, ensure_ascii is true"""
        return json.dumps(self._serialize(),indent=json_indent,ensure_ascii=False)

    def from_json_string(self, jsonStr):
        """Deserialize a JSON formatted str to a Python object"""
        params = json.loads(jsonStr)
        self._deserialize(params)

    def __repr__(self):
        return "%s" % self.to_json_string()
