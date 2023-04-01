import asyncio
import datetime
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import graphene

from apps.auth.mutations import Mutation as AuthMutations
from apps.auth.queries import Query as AuthQueries
from apps.store.mutations import Mutation as StoreMutations
from apps.customer.mutations import Mutation as CustomMutations
from apps.customer.queries import Query as CustomerQuery
from apps.product.queries import Query as ProductQuery
from apps.product.mutations import Mutation as ProductMutations
from apps.payment.queries import Query as PaymentQuery
from apps.payment.mutations import Mutation as PaymentMutations


channel_layer = get_channel_layer()


class Query(AuthQueries, CustomerQuery,
            ProductQuery,
            PaymentQuery,
            graphene.ObjectType):
    test = graphene.String(name=graphene.String())

    def resolve_test(root, info, name):
        async_to_sync(channel_layer.group_send)("new_message", {"data": name})


class Mutatation(AuthMutations, StoreMutations,
                 CustomMutations, ProductMutations,
                 PaymentMutations,
                 graphene.ObjectType):
    test_object = graphene.String()


class Subscription(graphene.ObjectType):
    test = graphene.String()
    test1 = graphene.String()

    async def subscribe_test1(root, info):
        channel_name = await channel_layer.new_channel()
        await channel_layer.group_add("new_message", channel_name)
        try:
            while True:
                message = await channel_layer.receive(channel_name)
                yield message["data"]
        finally:
            await channel_layer.group_discard("new_message", channel_name)

    async def subscribe_test(root, info):
        while True:
            yield datetime.datetime.now().isoformat()
            await asyncio.sleep(1)


schema = graphene.Schema(query=Query, mutation=Mutatation, subscription=Subscription)
