
## 1.安装新的虚拟环境

由于部分环境设置于之前的不同，因此安装新的环境，命名为mmagics

Windows 下的环境配置

```
conda creat -n mmagics
```
```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
这里是2.0.0
```
pip install mmcv==2.0.0 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.12/index.html
```
## 2.配置mmagic
```
pip3 install -e .
```

## 3.使用mmagic

使用下面的代码，第一次运行提示显存不足，于是改成了cpu

```python
import cv2
import numpy as np
import mmcv
from mmengine import Config
from PIL import Image
from mmagic.registry import MODELS
from mmagic.utils import register_all_modules
register_all_modules()
cfg = Config.fromfile('configs/controlnet/controlnet-canny.py')
controlnet = MODELS.build(cfg.model).cpu()

control_url = '.../MMagic/mmagic/pic/maopifang.png'
control_img = mmcv.imread(control_url)
control = cv2.Canny(control_img, 100, 200)
control = control[:, :, None]
control = np.concatenate([control] * 3, axis=2)
control = Image.fromarray(control)

prompt = 'Room with blue walls and a yellow ceiling.'
output_dict = controlnet.infer(prompt, control=control)
samples = output_dict['samples']
for idx, sample in enumerate(samples):
    sample.show()
controls = output_dict['controls']
for idx, control_item in enumerate(controls):
    control_item.show()
```
提示安装：
```
pip install accelerate
```
