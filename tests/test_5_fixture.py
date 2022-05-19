class Tests:
    def test_fixture_body_success(self,create_random_user_data_conftest):
        assert create_random_user_data_conftest.json().find("saved") == 7

    def test_fixture_body_userId(self, create_random_user_data_conftest):
        assert create_random_user_data_conftest.json().find("saved") == 7