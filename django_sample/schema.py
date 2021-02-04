import graphene
import forum.schema

from graphene_django.debug import DjangoDebug


class Query(forum.schema.Query, graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
