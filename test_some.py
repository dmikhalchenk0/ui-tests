import allure
import pytest


@allure.suite("Регистрация 1 кейс")
class TestRegistrationCase1:

    @pytest.mark.testomatio("@Tcba95025")
    @allure.title("Регистрация агента")
    @allure.description("Лист Регистрация. № п/п - 2")
    def test_case_1_step_2(self):
        assert "qwerty" == "qwerty1"