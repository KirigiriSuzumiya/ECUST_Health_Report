# ECUST_Health_Report
python脚本实现华理每日健康填报定时自动上传，解放双手。

你可以将该python脚本架设到服务器上实现定时周期任务，以彻底解放每日健康填报的折磨



## 小白爱看

访问：[华理健康填报自动化 (kirigirisuzumiya.xyz)](http://kirigirisuzumiya.xyz/)输入用户名密码就可以使用我们架设的服务器完成自动填报。

## 环境安装

### 1. 安装selenium

```shell
pip install selenium
```

### 2. 下载chrome驱动

前往[谷歌chrome驱动下载地址](http://chromedriver.storage.googleapis.com/index.html)下载对应您chrome浏览器版本的驱动，并放置在仓库根目录下

### 3. 安装chrome

* windows安装

  省略

* linux安装chrome

  ```
  ………………
  ```
  
  

## 开始使用

### 配置文件修改

简单的修改根目录下的`info.txt`即可完成配置。

每行输入一个用户的信息办用户与密码，用空格分隔，支持多用户，例如：

```
20002233 passwd
20002333 health_upload_sb
```

### 脚本运行

```shell
python health_upload.py
```

### 配置linux定时任务

使用crontab实现脚本的定时执行

```
# 配置crontab定时任务
crontab -e
```

打开文档修改器后填入，代表每天00:05执行一次脚本

```
5 0 * * * python /home/health/health_upload.py
```

### 架设服务器

后端使用django维护，项目目录在`health_upload`下

django服务启动：

```
python manage.py runserver 0.0.0.0:80
```

