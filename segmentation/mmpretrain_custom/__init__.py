# Copyright (c) OpenMMLab. All rights reserved.
import mmcv_custom
# import mmcv
import mmengine_custom
from mmengine_custom.utils import digit_version

from .apis import *  # noqa: F401, F403
from .version import __version__

mmcv_minimum_version = '2.0.0rc4'
mmcv_maximum_version = '2.1.0'
mmcv_version = digit_version(mmcv_custom.__version__)
# mmcv_version = digit_version(mmcv.__version__)

mmengine_minimum_version = '0.7.1'
mmengine_maximum_version = '1.0.0'
mmengine_version = digit_version(mmengine_custom.__version__)

assert (mmcv_version >= digit_version(mmcv_minimum_version)
        and mmcv_version < digit_version(mmcv_maximum_version)), \
    f'MMCV=={mmcv_custom.__version__} is used but incompatible. ' \
    f'Please install mmcv>={mmcv_minimum_version}, <{mmcv_maximum_version}.'

assert (mmengine_version >= digit_version(mmengine_minimum_version)
        and mmengine_version < digit_version(mmengine_maximum_version)), \
    f'MMEngine=={mmengine_custom.__version__} is used but incompatible. ' \
    f'Please install mmengine>={mmengine_minimum_version}, ' \
    f'<{mmengine_maximum_version}.'

__all__ = ['__version__']
