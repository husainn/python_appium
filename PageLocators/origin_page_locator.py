from appium.webdriver.common.mobileby import MobileBy


class OriginPageLocator:
    #元素定位
    #初始化页面
    #权限
    permission_allow = (MobileBy.ID,'com.lbe.security.miui:id/permission_allow_foreground_only_button')
    #升级弹框
    update_cancel = (MobileBy.ID, 'com.paic.esale.activity:id/btn1')
    # 立即体验
    lijitiyan = (MobileBy.ID,'com.paic.esale.activity:id/btnStart')
    #未知
    unknow = (MobileBy.ID,'com.paic.esale.activity:id/btn1')
    #隐私政策
    yinsizhengce = (MobileBy.ID,'com.paic.esale.activity:id/cb_privacypolicy')
    #同意
    allow_btn = (MobileBy.ID,'com.paic.esale.activity:id/pbt_dialog_sure')