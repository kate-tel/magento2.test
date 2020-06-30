import pytest
# from parameterized import parameterized
from mag_object import MainPage
from mag_object_catalog import Catalog


class Test_SB_Fixture():
    @pytest.mark.parametrize('value', ["fleece jacket", "red pants", "Luma",
                             "Navy"])
    def test_search_parametrized(self, sb, value):
        sb.open("https://magento2.test")
        sb.update_text(MainPage.search_input, value + '\n')
        sb.assert_element('p#toolbar-amount')
        sb.assert_element("div.search.results")

    @pytest.mark.parametrize('value', ["222", "#$%"])
    def test_search_invalid(self, sb, value):
        sb.open("https://magento2.test")
        sb.update_text(MainPage.search_input, value + '\n')
        sb.assert_text_visible('Your search returned no results.',
                               Catalog.suggestions)
        sb.assert_element_not_present(Catalog.suggestion)
