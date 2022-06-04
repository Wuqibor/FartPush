# 钉钉土味情话推送
每日通过钉钉定时推送一段土味情话

使用方法  
1.测试环境为 Python3.7.6 , 自行安装 Python3  
2.requirements.txt 是所需第三方模块, 执行 `pip install -r requirements.txt` 安装模块  
3.可在脚本内直接填写账号密码  
4.Python 和需要模块都装好了直接在目录 cmd 运行所要运行的脚本。  

# Github Actions说明
## 一、Fork此仓库
![](http://tu.yaohuo.me/imgs/2020/06/f059fe73afb4ef5f.png)
## 二、设置账号密码和钉钉推送
添加名为**DINGTOKEN**、**DINGSECRET**的变量  
值分别为**钉钉推送密钥**、**钉钉推送加签**  
钉钉推送支持加签模式, 如不需加签留空即可
示例：**DINGTOKEN:wy729c4z52x56acouvk7m8p2inlvldl3qezfpbnjxw7eidonsmf2q9x1gebpgegu**, **DINGSECRET:SEC32j3vxb30umqqcfq27k8d72dfxsjhz0tpcjd36wqg80os8x4ejfqydocvl7sbgee**  
![](http://tu.yaohuo.me/imgs/2020/06/748bf9c0ca6143cd.png)

## 三、启用Action
1 点击**Action**, 再点击**I understand my workflows, go ahead and enable them **  
2 修改任意文件后提交一次  
![](http://tu.yaohuo.me/imgs/2020/06/34ca160c972b9927.png)

## 四、查看运行结果
Actions > FartPush > build  
能看到类似如下所示:
```
### info There are 1 user | 共有 1 个账号 ###
### info Enable DingTalk push | 启用钉钉推送 ###
### info No. 1 user starting | 开始第 1 个账号 ###
### info Login *** successful | 登录 *** 成功 ###
### info *** chunckined , get 17 M | *** 已签到, 获得 17 M ###
### error #4 *** hava not chance  | *** 无机会 ###
### error #4 *** hava not chance  | *** 无机会 ###
天翼云签到
开始时间: 2022-05-29 04:37:09
结束时间: 2022-05-29 04:37:23
账号 签到结果 抽奖1结果 抽奖2结果
*** 已签到17M 无机会 无机会
### info DingTalk push successfully  | 钉钉推送成功 ###
```

此后, 将会在每天08:00和22:00推送一次 
若有需求, 可以在[.github/workflows/push.yml]中自行修改
