from elasticsearch_dsl.query import Q, MultiMatch, SF
from .documents import UserDocument


# def get_search_query(phrase):
#     query = Q(
#         'function_score',
#         query=MultiMatch(
#             fields=['id', 'username', 'location'],
#             query=phrase
#         ),
#         functions=[
#             SF('field_value_factor', field='id')
#         ]
#     )
#     return UserDocument.search().query(query)
#
#
# def search(phrase):
#     return get_search_query(phrase).to_queryset()

