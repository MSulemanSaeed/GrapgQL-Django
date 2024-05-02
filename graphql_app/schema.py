import graphene
from graphene_django import DjangoObjectType
from .models import *

class RestaurantType(DjangoObjectType):
  class Meta:
    model = Restaurant
    fields = ("id", "name", "staff_member", "location")

class PersonType(DjangoObjectType):
  class Meta:
    model = Person
    fields = '__all__'

class Query(graphene.ObjectType):
  """
  Queries for the Restaurant model
  """
  restaurant = graphene.List(RestaurantType)
  person = graphene.List(PersonType)

  def resolve_restaurant(self, info, **kwargs):
    return Restaurant.objects.all()
  def resolve_person(self, info, **kwargs):
    return Person.objects.all()

schema = graphene.Schema(query=Query)

class CreateRestaurant(graphene.Mutation):
  class Arguments:
    name = graphene.String()
    location = graphene.String()
    staff_member = graphene.Int()

  ok = graphene.Boolean() 
  restaurant = graphene.Field(RestaurantType)

  def mutate(self, name, location, staff_member):
    restaurant = Restaurant(name=name, location=location, staff_member=staff_member)
    restaurant.save()
    return CreateRestaurant(ok=True, restaurant=restaurant)
  

class DeleteRestaurant(graphene.Mutation):
  class Arguments:
    id = graphene.Int()

  ok = graphene.Boolean()

  def mutate(self, id):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.delete()
    return DeleteRestaurant(ok=True)
  

class UpdateRestaurant(graphene.Mutation):
  class Arguments:
    id = graphene.Int()
    name = graphene.String()
    location = graphene.String()
    staff_member = graphene.Int()

  ok = graphene.Boolean()
  restaurant = graphene.Field(RestaurantType)

  def mutate(self, id, name, location, staff_member):
    restaurant = Restaurant.objects.get(id=id)
    restaurant.name = name
    restaurant.location = location
    restaurant.staff_member = staff_member
    restaurant.save()
    return UpdateRestaurant(ok=True, restaurant=restaurant)





#------------*Person Api*-------------#

class CreatePerson(graphene.Mutation):
  class Arguments:
    name = graphene.String()
    age = graphene.Int()

  ok = graphene.Boolean()
  person = graphene.Field(PersonType)

  def mutate(self, name, age):
    person = Person(name=name, age=age)
    person.save()
    return CreatePerson(ok=True, person=person)


class DeletePerson(graphene.Mutation):
  class Arguments:
    id = graphene.Int()

  ok = graphene.Boolean()

  def mutate(self, id):
    person = Person.objects.get(id=id)
    person.delete()
    return DeletePerson(ok=True)
  

class UpdatePerson(graphene.Mutation):
  class Arguments:
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Int()

  ok = graphene.Boolean()
  person = graphene.Field(PersonType)

  def mutate(self, id, name, age):
    person = Person.objects.get(id=id)
    person.name = name
    person.age = age
    person.save()
    return UpdatePerson(ok=True, person=person)


class Mutation(graphene.ObjectType):
  create_restaurant = CreateRestaurant.Field()
  delete_restaurant = DeleteRestaurant.Field()
  update_restaurant = UpdateRestaurant.Field()
  create_person = CreatePerson.Field()
  delete_person = DeletePerson.Field()
  update_person = UpdatePerson.Field()
schema = graphene.Schema(query=Query, mutation=Mutation)


