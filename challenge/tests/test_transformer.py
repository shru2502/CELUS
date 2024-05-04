from unittest.case import TestCase

from challenge.etl.transformer import Transformer


class TestTransformer(TestCase):
    def test_transformer_valid_unit_mm(self):
        transformer = Transformer(
            raw_data=[
                {
                    "entry": "1",
                    "cake_diameter": "56.78",
                    "diam_unit": "mm",
                    "flavor": "caramel",
                    "is_cake_vegan": "No",
                }
            ]
        )
        res = transformer.transform_data()[0]
        self.assertEqual(res.entry_id, 1)
        self.assertEqual(res.name, "caramel")
        self.assertEqual(res.diameter_in_mm, 56.78)
        self.assertFalse(res.vegan)
        self.assertEqual(res.original_unit, "mm")
