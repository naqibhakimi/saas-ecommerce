import graphene


class CreateCurrencyInputField(graphene.InputObjectType):
    code = graphene.String()
    symbol = graphene.String()
    symbol_native = graphene.String()
    name = graphene.String()
    includes_tax = graphene.Boolean()


class UpdateCurrencyInputField(graphene.InputObjectType):
    id = graphene.ID()
    code = graphene.String()
    symbol = graphene.String()
    symbol_native = graphene.String()
    name = graphene.String()
    includes_tax = graphene.Boolean()
