from django.test import TestCase, tag

from edc_reference.site_reference import site_reference_configs


class TestReference(TestCase):

    def test_(self):
        site_reference_configs.registry
