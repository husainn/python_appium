### adb命令

- 查看当前运行的activity
  
  - adb shell "dumpsys window | grep mCurrentFocus"
  
- > 获取包名和入口的activity
  > aapt dump badging F:\360Downloads\Apk\baidu11.26.0.10.apk

  - 包名：package: name='com.baidu.searchbox'

- 入口：launchable-activity: name='com.baidu.searchbox.SplashActivity'

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
  
- PO模式
  - 页面对象 Common.BasePage、PageObject.xx_page
  - 测试用例 Testcase
  - 测试数据 TestDatas

- 重运行机制
  - pytest
  
- pytest

  - 自动发现测试模块和测试方法
  - 断言使用assert+表达式即可
  - 可以设置会话级、模块级、类级、函数级的fixtures 数据准备+清理工作
  - 有丰富的插件库，目前在300个以上。 ==allure
  - 安装命令
    - pip install pytest
    - pip install pytest-html
  - pytest插件地址：
    - http://plugincompat.herokuapp.com/

- pytest收集测试用例的规则

  - 默认从当前目录中收集测试用例，即在哪个目录下运行pytest命令，则从哪个目录文件中搜索
  - 搜索规则
    - 符合命名规则test\_* .py或者 *\_test.py
    - 以test\_开头的函数名
    - 以Test开头的测试类（没有\_\_init\_\_函数）当中，以test\_开头的函数

- pytest - mark

  - 对测试用例打标签，运行测试用例的时候，可根据标签名来过滤要运行的用例
  - 使用方法：
    - 在测试用例/测试类前面加上：@pytest.mark.标记名
    - 示例：@pytest.mark.smoke



