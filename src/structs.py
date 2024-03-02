from typing import List

from elasticsearch_dsl.response import Response


class EsResults:
    def __init__(self, results: Response):
        self.results = results

    @property
    def hits(self) -> int:
        return self.results.hits

    @property
    def aggregations(self) -> List[dict]:
        """ """
        return self.results.aggregations

    @property
    def source(self) -> List[dict]:
        return self.results.to_dict()
