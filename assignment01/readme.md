源代码是在Linux下的，我平时项目都是在Windows，因此也在windows配置

1、下载安装pytorch等，win系统配置的常规操作

注意使用conda 单独设立一个环境

2、安装mmcv，在以下网站找到对应版本：

https://mmcv.readthedocs.io/zh_CN/latest/get_started/installation.html


3、下载mmpose的示例教程

 https://github.com/TommyZihao/MMPose_Tutorials

4、按照教程里说的安装MMDetection和MMPose

注意：不需要前面的感叹号：！

安装时可使用 pip install -v -e .

5、运行训练代码

我的报错

（1）RuntimeError: albumentations is not installed

解决：通过pip安装

（2）opencv的问题，需要降低opencv的版本

注意，除了pip install opencv-python=4.5.4.60
还需要pip install opencv-python-headless==4.5.4.60 也就是说还需要处理这个headless.

可通过 pip list 确认已安装的版本

6、训练：

MMDetection + MMPose

7、测试

使用以下代码得到预测图：

python demo/topdown_demo_with_mmdet.py rtmdet_tiny_ear.py checkpoint/detect.pth rtmpose-s-ear.py checkpoint/pose.pth --input inputs/0101.jpg --output-root outputs --device cuda:0 --bbox-thr 0.5 --kpt-thr 0.5 --nms-thr 0.3 --radius 36 --thickness 30 --draw-bbox --draw-heatmap --show-kpt-idx
测试图像没有使用自己的照片（不太好看哈哈），使用New Bing 生成了照片，然后测试

![input](https://github.com/x-cosmic/openmmlab_study/blob/main/assignment01/input.jpg)

![output](https://github.com/x-cosmic/openmmlab_study/blob/main/assignment01/output.jpg)

说明: 由于一些资源限制，MMPose我只用了210个epoch，默认是300epoch，如果跑完了300个效果可能更好哈！
