
## 1.安装新的虚拟环境

由于部分环境设置于之前的不同，因此安装新的环境，命名为mmagics
```
conda creat -n mmagics
```
```
pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113
```
```
pip install mmcv==2.0.0rc4 -f https://download.openmmlab.com/mmcv/dist/cu113/torch1.12/index.html
```
## 2.配置mmagic
```
pip3 install -e .
```

## 3.配置mmagic
