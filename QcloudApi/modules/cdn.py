# -*- coding: utf-8 -*-
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

import hashlib
import os

from QcloudApi.modules import base


class Cdn(base.Base):
    requestHost = 'cdn.api.qcloud.com'

    def UploadCdnEntity(self, params):
        action = 'UploadCdnEntity'
        if params.get('entityFile') is None:
            raise ValueError('entityFile can not be empty.')
        if os.path.isfile(params['entityFile']) is False:
            raise ValueError('entityFile is not exist.')

        file = params.pop('entityFile')
        if 'entityFileMd5' not in params:
            content = open(file, 'rb').read()
            params['entityFileMd5'] = hashlib.md5(content).hexdigest()

        files = {
            'entityFile': open(file, 'rb')
        }

        return self.call(action, params, files)
