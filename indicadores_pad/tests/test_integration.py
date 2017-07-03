#! coding: utf-8

import unittest
from indicadores_pad.indicators import PADIndicators


class PADTest(unittest.TestCase):
    spreadsheet = '1uG68Yq9z1l6IX1kW8A3uO9yGHSNqDglFuagk7BxKOaw'

    def setUp(self):
        self.pad = PADIndicators()

    def test_count_indicators_add_up_to_the_same(self):
        indics = self.pad.generate_pad_indicators(self.spreadsheet)

        doc_count = indics['pad_items_documentados_cant'] +\
            indics['pad_items_no_documentados_cant']

        lic_count = indics['pad_items_licencia_cant'] +\
            indics['pad_items_sin_licencia_cant']

        self.assertEqual(doc_count, lic_count)

        update_count = indics['pad_items_actualizados_cant'] +\
            indics['pad_items_desactualizados_cant']

        self.assertEqual(doc_count, update_count)

        download_count = indics['pad_items_descarga_cant'] +\
            indics['pad_items_no_descarga_cant']

        self.assertEqual(doc_count, download_count)

