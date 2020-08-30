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

- pytest常用指令
  - pytest -m smoke 运行标记为smoke的用例
  - pytest -m smoke --html=HtmlReports/report.html  指定测试报告的路径
  - pytest -m smoke Testcase 运行指定目录下的用例
  - pytest -m smoke Testcase/testlogin.py 运行指定模块下的用例
  - pytest -k 'xxx'  匹配文件名、类名、方法名匹配表达式的用例
  - 运行指定的用例，使用节点id：  py模块名::类名::函数名 或者 py模块名::函数名
    - 示例pytest test_xxx.py::TestXXX::func_xxx 



- fixture
  - conftest.py  == pytest自动识别的文件。名字不可以更改，存放的fixture，可以放多个
  - 一个fixture表示一个前置和后置
  - 可以放多个
- 实现fixture：
  - 装饰器加函数实现，@pytest.fixture
  - 使用yield返回数据，用在用例中用方法名称进行传参
- 调用的时候：测试用例/测试类的前面
  - @pytest.mark.usefixture('fixture函数名称') 

- pytest - 参数化
  - 在测试用例前面加上：@pytest.mark.parametrize('参数名'，列表数据)
    - 参数名：用来接收每一项数据，并作为测试用例的参数
    - 列表数据：一组测试数据
- pytest - 重运行机制
  - Pytest提供了重运行机制
    - 插件名称：rerunfailures
    - 安装方法：pip install pytest-rerunfailures
  - 使用方式：
    - 命令行参数形式
    - 命令：pytest --rerun重试次数
      - 比如：pytest --rerun 2表示：运行失败的用例可以重新运行两次
    - 命令：pytest --rerun重试次数 --reruns-delay 次数之间的延时设置（单位：秒）
      - 比如：pytest --rerun 2 --reruns-delay 5 表示失败的用例可以重新运行2次，第一次和第二次的间隔时间为5秒钟