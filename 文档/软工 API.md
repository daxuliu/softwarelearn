# 软工 API

## 域名

"https://xxx.xxx/"

## 上传图片接口

上传时要在数据库中加上每张图片的上传时间, 成功上传返回true, 失败返回false.

```text
接口：upload
请求方式：POST
表单name：username, file
```

## 获取所有相册接口

返回所有相册的图片链接和相关用户名数组和相册中最新的图片的时间和该相册点赞数, 如下:

```js
list:[ {src:'statics/images/1.png', username:'name1', date:'time1', heat:'num'} ...{...}]
```

```text
接口: album
请求方式: GET
表单name: null
```

## 获取用户图片接口

返回用户的图片描述和连接数组和时间, 如下:

```js
list:[ {src:'statics/images/1.png', desc:'这是图片的描述', date:'time1'} ...{...}]
```

```text
接口: user
请求方式: GET
表单name: username
```

## 登录验证接口

密码正确返回true, 失败返回false.

```text
接口: login
请求方式: GET
表单name: username, pwd
```

## 注册用户接口

成功返回true, 失败返回false.

```text
接口: register
请求方式: POST
表单name: username, pwd
```
