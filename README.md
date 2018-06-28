### 安装python3
linux环境：
官网下载安装包：
```
https://www.python.org/downloads/release/python-366/
```
上传服务器，解压：

```
tar -zxvf Python-3.7.0.tgz
cd Python-3.7.0
mkdir /application/search/python3
./configure --enable-shared --  --predix=/application/search/python3
make
make install
```

激活虚拟环境：
```
mkdir /application/search/py37env
cd /application/search/py37env
/application/search/python3/bin/pyvenv py37env
source /application/search/py37env/py37env/bin/activate
```
退出虚拟环境：
```
deactivate
```
