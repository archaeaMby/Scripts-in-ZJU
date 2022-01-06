# R markdown使用指南
## 0. R-studio server
### 0.1 使用R-studio server
* 在官网 https://www.rstudio.com/products/rstudio/download-server/
* 选择相应的系统，注意是服务器哦
```bash
sudo apt-get install gdebi-core
wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1717-amd64.deb
sudo gdebi rstudio-server-1.4.1717-amd64.deb
```
* 然后它是自动开启的，可以通过 sudo rstudio-server 各项来控制
* 前往 http:// 服务器地址 :8787 （端口可以自己设置）
* 用户名和密码不能用root，所以需要自己创建一个
```bash
sudo useradd -m user_name
user_name passwd
```
* 如果R没问题的话那进去也没有问题 ~
* 要用R Markdown的话进去再创建即可

## 1. setup头文件
### 1.1 工作目录的设置
* 在chunk（就是每个块）中设置路径是只会影响到该chunk的！所以需要在头中设置
* knitr::opts_knit$set(root.dir = "path")
* 说起来，Windows里设置wd是不是有亿————点点问题，需要手动在console里设置
* 而且是 setwd("波浪线/") 的形式

### 1.2 头文件YAML格式
* 在 knitr::opts_chunk$set() 中可以设置多种参数
* eval=TRUE 在块中运行代码    highlight=T 高亮显示    echo=F 输出包含源代码
* tidy=TRUE 整理代码    error=T 输出包含错误信息    warning=F 包含警告
* message=F 包含参考信息    cache=F

---
# Jupyter使用指南
## 0. R语言环境的配置
* 推荐使用conda来进行全部管理（因为方便更改和删除）
```
conda create -n r4 python=3.9
conda activate r4
conda install -c conda-forge r-base=4.1.1
```
## 0.Alter (不推荐) R的两种手动安装
### 0.1 官网直接安装（方便快捷，但版本控制很麻烦）
* 地址：https://cran.r-project.org/bin/bash/ubuntu/
* 在/etc/apt/sources.list file中添加对应版本的地址
```bash
sudo apt-get update
sudo apt-get install r-base r-base-dev r-base-core
```

### 0.2 安装包安装（慢，手动安装的包很多）
* 地址：随便找个镜像网站下载下来
```bash
mkdir /usr/local/R
./configure --enable-R-shlib=yes --with-tcltk --prefix=/usr/local/R     到R安装文件夹中
sudo apt-get install 什么什么什么
根据报错安装相应的包
sudo apt-cache search 什么什么什么
查询可以直接网上搜索 / 使用
make
make install
```
* 配置环境  vim /etc/profile中加入 R_HOME=/usr/local/R PATH=\$PATH:\$R_HOME/bin  然后source /etc/profile
* 最后R召唤
## 1. 安装
* 推荐使用conda来进行全部管理（因为方便更改和删除）
```bash
conda install -c conda-forge jupyterlab
```
### 1.1 Jupyter加入R环境
```bash
conda install -c conda-forge r-irkernel
```
* 如果用conda下载了，就不需要R下载了
```r
install.packages('IRkernel')
IRkernel::installspec()
# 只下到自己的用户
IRkernel::installspec(user=FALSE)
# 在系统中下，不然只下到该用户
```
### 1.2 R环境查看
```r
.libPaths() #可查看当前包路径
capabilities() #可查看R语言能否支持一些基本功能（不能的话就重装吧Kora
Sys.envget("name") #可根据name抓取R环境配置
Sys.envset(LANG="") #设置环境
```
## 2. 配置与使用
### 2.1 基础配置
```bash
jupyter notebook --generate-config #生成配置文件
vim ~/.jupyter/jupyter_notebook_config.py
#更改配置
c.NotebookApp.ip="*"
c.NotebookApp.port=8888
c.NotebookApp.notebook_dir="dir"
c.NotebookApp.allow_root=True #自己服务器才存在的问题
```
### 2.2 基础使用
* 可以在127.0.0.1/lab里使用Jupyter lab, 在127.0.0.1/tree里使用Jnb
* 使用前需设置密码
```bash
jupyter notebook password
```
* 另外建议单开tmux实现后端持续运行
```bash
tmux new -s jupyter
jupyter lab --no-browser --port=????
```
### 2.3 进阶使用
* 参考官方文档：https://jupyterlab.readthedocs.io/en/latest/
* 参考：https://zhuanlan.zhihu.com/p/146288279
* 参考：https://www.zhihu.com/question/59392251/answer/560977151
## 3. 插件与拓展
### 3.1 Jupyter拓展
* 新鲜出炉的新问题：拓展需要Nodejs
* 需要注意的是conda和apt自带的Nodejs版本都是10点几，不支持Jupyter>12的要求
* 所以需要通过curl或者官网之类的方法下载更高版本的Nodejs

### 3.2 Jupyter notebook插件
* conda install -c conda-forge jupyter_contrib_nbextensions安装nbextensions
* jupyter contrib nbextension install --user

---
# R语言的综合使用及大量问题
## 1. R安装一些包的问题
### 1.0 增加library
* 在 Rprofile.site 文件中增加 .libPaths(c("a","b"))来实现库的增加

### 1.1 最常见的是跳出来“XXX had non-zero exit status”
* 检查安装过程具体 ERROR 报了什么错
* 搜索引擎搜索该语句，一般是系统缺少相应的包，使用 sudo apt-get install 安装上 

### 1.2 使用install.packages()下载的问题
* 如下载irkernel，在install.packages()需要下载几个包： ‘repr', 'IRdisplay', 'crayon', 'pbdZMQ', 'uuid', 'digest'
* 反而不用下'devtools' 因为它是个包管理器，目前没用而且问题很多

### 1.3 遇到Error in Dyn.load 问题
> Error in dyn.load(file, DLLpath = DLLpath, ...) :
>  unable to load shared object '/share/home/qlab/qlab_gyx/miniconda3/envs/r4/lib/R/library/openssl/libs/openssl.so':
>  libssl.so.3: cannot open shared object file: No such file or directory  

首先找到openssl库
```r
which openssl
ldd $path #查看包版本
```
* 发现当前版本是 libssl.so.1.1
```r
install.packages("openssl")
```
* 然后发现，只是没有下载openssl的问题
* 怒！！！！




---
