"""
微信小程序自动化测试项目
"""

import minium


class DemoTest(minium.MiniTest):
    def test_case_01(self):
        self.page.wait_for(30)
        self.page.get_element('view', inner_text='商城').click()

