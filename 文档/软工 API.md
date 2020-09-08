# 软工 API

要求：

* 名字小写
* 单词间下划线空开
* 体现功能（返回值、参数）
* 发送数据用`send`开头
* 接收数据用`get`开头
* 参数使用驼峰

例子：get_user_image {id: userId} -> [{imgId : int, img : file}]

## 页面跳转 API

首页：index

登录页：login

注册页：register

个人相册页：selfAlbum

## 首页

首页根据热度（点赞数）推荐一系列的照片（具体后端实现）

* get_recmd_imgs {} -> [{albumId, albumName, url, desc, userId, date, praiseNnum}]
  * 获取推荐的照片，数组形式。相册ID、相册名、相册封面链接、相册用户ID、更新日期、点赞数
* send_praise {albumId, username} -> {res, num}
  * 通知服务器有点赞发生，返回结果 res: true | false；num：新的点赞数

## 登陆页

* send_loginInfo {username, pwd, permit} -> {res}
  * 发送登陆请求，用户名、密码、是否以管理员登陆（暂时不处理）；返回结果
* send_registerInfo {username, pwd} -> {res}
  * 发送注册信息

## 相册页

* get_user_imgs {userId} -> {imgId, url, date}

