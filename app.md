### adb命令

- 查看当前运行的activity
  
- adb shell "dumpsys window | grep mCurrentFocus"
  
- > 获取包名和入口的activity
  >
  > aapt dump badging F:\360Downloads\Apk\baidu11.26.0.10.apk

  - 包名：package: name='com.baidu.searchbox'

![1597765621625](C:\Users\Mloong\AppData\Roaming\Typora\typora-user-images\1597765621625.png)

- 入口：launchable-activity: name='com.baidu.searchbox.SplashActivity'

![1597765696285](C:\Users\Mloong\AppData\Roaming\Typora\typora-user-images\1597765696285.png)



- appium定位元素的五种方法

  - id: resource-id
  - classname
  - content-desc
  - AndroidUiAutomator
  - xpath

- 滑屏操作
  - swipe(起始X，起始Y，结束X，结束Y)  

- 手势密码
  - ![1598195080443](C:\Users\Mloong\AppData\Roaming\Typora\typora-user-images\1598195080443.png)

- webview
  - hybird混合应用自动化方案，基于UiAutomator+Chromedriver
  - native走UiAutomator，webview部分走Chromedriver，二者结合
  - 要求：
    - Android4.4+
    - webview必须为debug版本
  - 获取webview页面的三种方式
    - chrome://inspect,需要FQ
    - 使用driver.page_source获取html页面
    - 找开发人员要源文件
    - uc_devtools不需要FQ
  - 切换到webview的步骤
    - 
- Chromedriver文件替换路径
  - C:\Users\Administrator\AppData\Local\Programs\Appium\resources\app\node_modules\appium\node_modules\appium-chromedriver\chromedriver\win

- 更新