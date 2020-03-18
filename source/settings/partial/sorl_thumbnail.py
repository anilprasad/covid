import os

THUMBNAIL_KEY_PREFIX = os.environ.get('APP_NAME', 'undefined_app_name') + '_'
THUMBNAIL_KVSTORE = 'sorl.thumbnail.kvstores.redis_kvstore.KVStore'
THUMBNAIL_ENGINE = 'sorl.thumbnail.engines.convert_engine.Engine'
THUMBNAIL_PRESERVE_FORMAT = False
THUMBNAIL_REDIS_URL = os.environ.get('APP_REDIS', 'redis://127.0.0.1:6379/0')
