from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


try:
    import importlib
except ImportError:
    from django.utils import importlib

DEFAULT_ENGINE = 'inlinecss.engines.PynlinerEngine'


def get_engine():
    from django.conf import settings
    engine_path = getattr(settings, 'INLINECSS_ENGINE', DEFAULT_ENGINE)
    i = engine_path.rfind('.')
    module_path, class_name = engine_path[:i], engine_path[i + 1:]
    module = importlib.import_module(module_path)
    return getattr(module, class_name)
