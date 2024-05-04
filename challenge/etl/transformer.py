from typing import List, Optional

from .models import CakeModel


class Transformer:
    def __init__(self, raw_data: List[dict]):
        """
        This class transforms extracted data according to the desired model

        Args:
            raw_data: extracted data
        """
        self.raw_data = raw_data

    def transform_data(self) -> List[CakeModel]:
        """
        Transforms data

        Returns:
            transformed data as a list of models
        """
        transformed_cakes = list()
        for in_cake in self.raw_data:
            out_cake = self.transform_single_item(in_cake)
            if out_cake:
                transformed_cakes.append(out_cake)
        return transformed_cakes

    def transform_single_item(self, input_item: dict) -> Optional[CakeModel]:
        """
        Transforms single item of extracted data

        Args:
            input_item: part of extracted data

        Returns:
            model if transformation was successful
        """
        raise NotImplementedError()
