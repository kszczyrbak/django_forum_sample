import graphene
from graphene_django.types import DjangoObjectType
from .models import Section, Post, Thread, User
from graphene import ObjectType, Schema
from graphene_django import DjangoListField, DjangoObjectType


class SectionType(DjangoObjectType):
    class Meta:
        name = 'Section'
        model = Section


class ThreadType(DjangoObjectType):
    class Meta:
        name = 'Thread'
        model = Thread


class PostType(DjangoObjectType):
    class Meta:
        name = 'Post'
        model = Post


class UserType(DjangoObjectType):
    class Meta:
        name = 'User'
        model = User


# TODO: security
# TODO: parametrized queries
# TODO: mutations
# TODO: add resolvers and solve n+1 (dataloader?)

class Query(graphene.ObjectType):
    sections = DjangoListField(SectionType)
    section = graphene.Field(SectionType, id=graphene.Int())
    posts = DjangoListField(PostType)
    threads = DjangoListField(ThreadType)
    users = DjangoListField(UserType)

    def resolve_section(self, info, id):
        return Section.objects.get(pk=id)
