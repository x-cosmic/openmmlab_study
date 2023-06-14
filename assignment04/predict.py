import numpy as np
import matplotlib.pyplot as plt


from mmseg.apis import init_model, inference_model, show_result_pyplot
import mmcv
import cv2
from mmengine import Config
cfg = Config.fromfile('pspnet-WatermelonDataset.py')

from mmengine.runner import Runner
from mmseg.utils import register_all_modules
import numpy as np
import matplotlib.pyplot as plt

# register all modules in mmseg into the registries
# do not init the default scope here because it will be init in the runner

if __name__ == '__main__':
    register_all_modules(init_default_scope=False)
    runner = Runner.from_cfg(cfg)

    checkpoint_path = 'work_dirs/WatermelonDataset/iter_3000.pth'
    model = init_model(cfg, checkpoint_path, 'cuda:0')
    img = mmcv.imread('datapre/denn-ke-11-7.jpg')

    result = inference_model(model, img)
    result.keys()
    pred_mask = result.pred_sem_seg.data[0].cpu().numpy()
    #pred_mask.shape
    #np.unique(pred_mask)
    #plt.imshow(pred_mask)
    #plt.show()

    
    height, width = pred_mask.shape
    color_image = np.zeros((height, width, 3), dtype=np.uint8)


    color_map = {
        0: (128, 128, 128),    # 背景
        1: (255, 0, 0),        # 西瓜红瓤
        2: (34,139,34),        # 西瓜外壳
        3: (144,238,144),      # 西瓜白皮
        4: (0, 0, 0),          # 西瓜黑籽
        5: (255, 255, 255),    # 习惯白籽
    }

    for i in range(height):
        for j in range(width):
            value = pred_mask[i, j]
            color = color_map[value]
            color_image[i, j] = color

    plt.imshow(color_image)
    plt.axis('off') 
    plt.show()


