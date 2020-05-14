import pytest
from base.base_yml import yml_with_file
from pages.customer_page import CustomerAction


class TestSearch:

    cus_action = CustomerAction()

    # @pytest.mark.parametrize('keys', yml_with_file('search_data')['test_search'])
    def test_search(self):
        self.cus_action.customer_search()





