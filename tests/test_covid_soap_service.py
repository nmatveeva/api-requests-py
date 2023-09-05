from assertpy import assert_that
from lxml import etree

from api_clinet.covid_soap_client import CovidSoapClient
from tests.helpers.covid_soap_helpers import get_overal_cases

client = CovidSoapClient()


def test_overall_covid_cases_is_greater_than_a_million():
    """
    Test the COVID SOAP service has overall covid cases is greater than a million
    """
    xml_tree = client.get_soap_response().xml_tree
    overall_cases = get_overal_cases(xml_tree)
    assert_that(overall_cases).is_greater_than(1000000)


def test_overall_covid_cases_match_sum_of_total_cases_by_country():
    """
    Test the COVID SOAP service overall cases match sum of total cases by country
    """
    xml_tree = client.get_soap_response().xml_tree

    overall_cases = get_overal_cases(xml_tree)
    search_for = etree.XPath("//data//regions//total_cases")

    cases_by_country = 0
    for region in search_for(xml_tree):
        cases_by_country += int(region.text)

    assert_that(overall_cases).is_greater_than(cases_by_country)
