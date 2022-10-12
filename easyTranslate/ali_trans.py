# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import logging
import sys

from typing import List, Optional

from alibabacloud_alimt20181012.client import Client as alimt20181012Client
from alibabacloud_alimt20181012.models import TranslateGeneralResponse
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_alimt20181012 import models as alimt_20181012_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class TransApi:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
            access_key_id: str,
            access_key_secret: str,
    ) -> alimt20181012Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的 AccessKey ID,
            access_key_id=access_key_id,
            # 您的 AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f'mt.cn-hangzhou.aliyuncs.com'
        return alimt20181012Client(config)

    @staticmethod
    def get_result(ak, sk, mode, source_text) -> Optional[str]:
        source_language, target_language = '', ''
        client = TransApi.create_client(ak, sk)
        if mode == 'c2e':
            source_language = 'zh'
            target_language = 'en'
        elif mode == 'e2c':
            source_language = 'en'
            target_language = 'zh'
        else:
            logging.warning('mode超出范围')

        translate_general_request = alimt_20181012_models.TranslateGeneralRequest(
            format_type='text',
            source_language=source_language,
            target_language=target_language,
            source_text=source_text,
            scene='general'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = client.translate_general_with_options(translate_general_request, runtime)
            return response.body.data.translated
        except Exception as error:
            # 如有需要，请打印 error
            logging.error(UtilClient.assert_as_string(error.message))


