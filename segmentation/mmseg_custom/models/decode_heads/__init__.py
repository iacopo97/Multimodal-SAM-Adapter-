# Copyright (c) OpenMMLab. All rights reserved.
from .mask2former_head import Mask2FormerHead
from .maskformer_head import MaskFormerHead
from .segformer_head import SegformerHead

__all__ = [
    'MaskFormerHead',
    'Mask2FormerHead',
    'SegformerHead'
]
