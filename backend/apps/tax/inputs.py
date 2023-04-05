import graphene


class CrateTaxRateInputField(graphene.InputObjectType):
    rate = graphene.Float()
    code = graphene.String()
    name = graphene.String()
    metadata = graphene.JSONString()
    product_count = graphene.Int()
    product_type_count = graphene.Int()
    shipping_option_count = graphene.Int()


class UpdateTaxRateInputField(graphene.InputObjectType):
    id = graphene.String()
    rate = graphene.Float()
    code = graphene.String()
    name = graphene.String()
    metadata = graphene.JSONString()
    product_count = graphene.Int()
    product_type_count = graphene.Int()
    shipping_option_count = graphene.Int()
