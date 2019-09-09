import json
import os


__all__ = (
    'BLOG_POST_DOCUMENT_NAME',
    'SITE_USER_DOCUMENT_NAME',
    'FARM_ANIMAL_DOCUMENT_NAME',
    'ELASTICSEARCH_CONNECTION',
)


ELASTICSEARCH_CONNECTION = os.environ.get(
    "GRAPHENE_ELASTIC_EXAMPLE_ELASTICSEARCH_CONNECTION",
    {
        'hosts': ['localhost'],
        'timeout': 20,
    }
)

if isinstance(ELASTICSEARCH_CONNECTION, str):
    try:
        ELASTICSEARCH_CONNECTION = json.loads(ELASTICSEARCH_CONNECTION)
    except:
        ELASTICSEARCH_CONNECTION = {}


BLOG_POST_DOCUMENT_NAME = os.environ.get(
    "GRAPHENE_ELASTIC_EXAMPLE_BLOG_POST_DOCUMENT_NAME",
    "blog_post"
)

SITE_USER_DOCUMENT_NAME = os.environ.get(
    "GRAPHENE_ELASTIC_EXAMPLE_SITE_USER_DOCUMENT_NAME",
    "site_user"
)


FARM_ANIMAL_DOCUMENT_NAME = os.environ.get(
    "GRAPHENE_ELASTIC_EXAMPLE_FARM_ANIMAL_DOCUMENT_NAME",
    "farm_animal"
)
