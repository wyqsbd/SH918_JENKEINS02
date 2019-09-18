import allure


class Test01:

    @allure.step("方法的步骤描述")
    def test_01(self):
        allure.attach("附件的名称", "附件的内容")
        print('测试方法')
        assert True
