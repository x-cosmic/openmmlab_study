import numpy as np

import os.path as osp
from tqdm import tqdm

import mmcv
import mmengine

from mmengine import Config
cfg = Config.fromfile('pspnet-WatermelonDataset.py')

from mmengine.runner import Runner
from mmseg.utils import register_all_modules

if __name__ == '__main__':
    register_all_modules(init_default_scope=False)
    runner = Runner.from_cfg(cfg)

    runner.train()

