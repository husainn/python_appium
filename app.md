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

- 切换到H5
