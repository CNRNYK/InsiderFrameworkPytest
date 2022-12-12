import pytest

from service import api_swagger


@pytest.mark.usefixtures('init_driver')
@pytest.mark.api
class TestAPI:
    """Client Reviews tests - """

    def test_post_pet(self):
        api_swagger.create_pet()
        api_swagger.get_pet()

    def test_get_pet(self):
        api_swagger.get_pet()

    def test_delete_pet(self):
        self.test_post_pet()
        api_swagger.delete_pet()

    def test_delete_negative_pet(self):
        api_swagger.delete_non_existing_pet()
