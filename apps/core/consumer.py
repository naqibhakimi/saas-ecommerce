import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .constants import GQL_DATA, WS_PROTOCOL
from graphql import graphql
from django.conf import settings
from django.utils.module_loading import import_string


class GraphQLSubscriptionConsumer(AsyncJsonWebsocketConsumer):
    def get_graphql_params(self, payload):
        return {
            "query": payload.get("query"),
            "variable_values": payload.get("variables"),
            "operation_name": payload.get("operationName"),
            "context_value": self.scope
        }

    def build_message(self, id, op_type, payload):
        message = {}
        if id is not None:
            message["id"] = id
        if op_type is not None:
            message["type"] = op_type
        if payload is not None:
            message["payload"] = payload
        assert message, "You need to send at least one thing"
        return message

    async def connect(self):
        self.connection_context = None
        if WS_PROTOCOL in self.scope["subprotocols"]:
            await self.accept(subprotocol=WS_PROTOCOL)
        else:
            await self.close()

    async def disconnect(self, code):
        if self.connection_context:
            self.connection_context.socket_closed = True

    async def receive_json(self, content):
        self.schema =  import_string(settings.GRAPHENE.get('SCHEMA'))
        if content.get('type') == 'start':
            result = await self.schema.subscribe(**dict(self.get_graphql_params(content.get('payload'))))
            if hasattr(result, '__aiter__'):
                async for single_result in result:
                    await self.send_json(content=self.build_message(
                        content.get('id'),
                        GQL_DATA,
                        single_result.data))
            else:
                await self.send_json(content=self.build_message(
                        content.get('id'),
                        GQL_DATA,
                        single_result.data))