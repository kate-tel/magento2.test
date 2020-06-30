import pytest
# from parameterized import parameterized
from ..page_objects.mag_object_main import MainPage
from ..page_objects.mag_object_catalog import Catalog

base_url = "https://magento2.test"


class Test_SB_Fixture():

    @pytest.mark.parametrize('value', ["fleece jacket", "red pants", "Luma",
                             "Navy"])
    def test_search_parametrized(self, sb, value):
        sb.open(base_url)
        sb.update_text(MainPage.search_input, value + '\n')
        sb.assert_element('p#toolbar-amount')
        sb.assert_element("div.search.results")

    @pytest.mark.parametrize('value', ["222", "#$%"])
    def test_search_invalid(self, sb, value):
        sb.open(base_url)
        sb.update_text(MainPage.search_input, value + '\n')
        sb.assert_text_visible('Your search returned no results.',
                               Catalog.suggestions)
        sb.assert_element_not_present(Catalog.suggestion)
