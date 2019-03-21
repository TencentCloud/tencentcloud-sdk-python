# Copyright (c) 2018 Tencent Ltd.
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


class HttpProfile(object):
    def __init__(self, protocol=None, endpoint=None, reqMethod="POST", reqTimeout=60,
                 keepAlive=False):
        """HTTP profile.
        :param protocol: temporarily useless,set None
        :type protocol: str
        :param endpoint: The domain to access, like: cvm.tencentcloudapi.com
        :type endpoint: str
        :param reqMethod: the http method, valid choice: GET, POST
        :type reqMethod: str
        :param reqTimeout: The http timeout in second.
        :type reqTimeout: int
        """
        self.endpoint = endpoint
        self.reqTimeout = 60 if reqTimeout is None else reqTimeout
        self.reqMethod = "POST" if reqMethod is None else reqMethod
        self.protocol = protocol
        self.keepAlive = keepAlive

