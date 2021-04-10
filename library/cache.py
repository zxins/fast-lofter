# -*- coding: utf-8 -*-
import json
from typing import Any

import redis

from config import config


class RedisCache:
    def __init__(self):
        self._cache = redis.StrictRedis(
            host=config.REDIS_HOST,
            port=config.REDIS_PORT,
            password=config.REDIS_PASS,
            db=config.REDIS_CACHE_DB
        )

    def _get_cache_info(self, feature_name: str, **key_options: dict):
        """ 获取缓存配置信息 """

        # key信息
        key_config = config.CACHE_EXPIRED[feature_name]
        # 拼接key
        template = key_config.key_template or ''
        options_key = template.format(**key_options)
        cache_key = config.CACHE_PREFIX + feature_name + options_key
        return key_config, cache_key

    def set_value_expired(self, value, feature_name: str, **key_options: dict) -> bool:
        """ 写入缓存 """

        # key信息
        key_config, cache_key = self._get_cache_info(feature_name, **key_options)
        # set key
        value_type = key_config.value_type
        if value_type == 'dict' or value_type == 'array':  # todo: 封装字段类型
            value = json.dumps(value)
        return self._cache.set(cache_key, value, key_config.expired)

    def get_value(self, feature_name: str, **key_options: dict) -> Any:
        """ 获取缓存值 """

        # key信息
        key_config, cache_key = self._get_cache_info(feature_name, **key_options)
        # get key
        result = self._cache.get(cache_key)

        if not result:
            return result
        value_type = key_config.value_type
        if value_type == 'dict' or value_type == 'array':
            return json.loads(result)
        if value_type == 'int':
            return int(result)
        return result

    def get_ttl(self, feature_name: str, **key_options: dict) -> Any:
        """ 获取过期时间 """

        # key信息
        key_config, cache_key = self._get_cache_info(feature_name, **key_options)
        # get key ttl
        return self._cache.ttl(cache_key)

    def delete_value(self, feature_name: str, **key_options: dict) -> bool:
        """ 删除缓存 """

        # key信息
        _, cache_key = self._get_cache_info(feature_name, **key_options)
        return self._cache.delete(cache_key)


if __name__ == '__main__':
    cache = RedisCache()
    cache.set_value_expired({"name": "张三"}, 'account.detail', **{'uid': 123})
