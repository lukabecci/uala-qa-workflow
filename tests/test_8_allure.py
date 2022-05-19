import pytest
import allure

class TestReports:
    @pytest.mark.cashin
    @allure.severity(allure.severity_level.CRITICAL)
    def test_1(self):
        '''Test que prueba Allure'''
        assert True

    @pytest.mark.cashin
    @allure.severity(allure.severity_level.BLOCKER)
    def test_2(self):
        '''Test que prueba Allure de nuevo'''
        assert True

    @pytest.mark.cashin
    @allure.severity(allure.severity_level.MINOR)
    def test_3(self):
        '''Test que prueba otra cosa'''
        assert True