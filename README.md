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
配置Python镜像：
```
mkdir /application/search/.pip/
vim /application/search/.pip/pip.conf
```
在配置文件中写入如下：
```
[global]
trusted-host=mirrors.aliyun.com
index-url=http://mirrors.aliyun.com/pypi/simple
```
直接运行pip install 即可。在非虚拟环境或者虚拟环境都可以使用镜像。
另，如果pip安装包时，出现需要升级预装版本，可在安装时直接忽略预装版本。例如：
```
pip install numpy --ignore-intalled numpy
```
