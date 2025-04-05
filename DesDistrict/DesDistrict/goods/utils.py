from django.db.models import Q
from django.contrib.postgres.search import (
    SearchVector,
    SearchQuery,
    SearchRank,
    SearchHeadline,
)

from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))

    vector = SearchVector("name", "description", config="russian")
    query = SearchQuery(query, config="russian")

    result = (
        Products.objects.annotate(rank=SearchRank(vector, query))
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    result = result.annotate(
        headline_name=SearchHeadline(
            "name",
            query,
            config="russian",
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ),
        headline_description=SearchHeadline(
            "description",
            query,
            config="russian",
            start_sel='<span style="background-color: yellow;">',
            stop_sel="</span>",
        ),
    )
    
    return result
