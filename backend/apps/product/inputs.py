import graphene


class CreateProductInputField(graphene.InputObjectType):
    title = graphene.String()
    subtitle = graphene.String()
    description = graphene.String()
    handle = graphene.String()
    is_gift_card = graphene.Boolean()
    status = graphene.String()
    images = graphene.List(graphene.ID)
    thumbnail = graphene.String()
    profile = graphene.ID()
    weight = graphene.Int()
    length = graphene.Int()
    height = graphene.Int()
    width = graphene.Int()
    hs_code = graphene.String()
    origin_country = graphene.String()
    mid_code = graphene.String()
    material = graphene.String()
    collection = graphene.ID()
    type = graphene.ID()
    tags = graphene.List(graphene.ID)
    discountable = graphene.String()
    external_id = graphene.String()
    sales_channels = graphene.List(graphene.ID)
    metadata = graphene.String()


class UpdateProductInputField(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    subtitle = graphene.String()
    description = graphene.String()
    handle = graphene.String()
    is_gift_card = graphene.Boolean()
    status = graphene.String()
    images = graphene.List(graphene.ID)
    thumbnail = graphene.String()
    profile = graphene.ID()
    weight = graphene.Int()
    length = graphene.Int()
    height = graphene.Int()
    width = graphene.Int()
    hs_code = graphene.String()
    origin_country = graphene.String()
    mid_code = graphene.String()
    material = graphene.String()
    collection = graphene.ID()
    type = graphene.ID()
    tags = graphene.List(graphene.ID)
    discountable = graphene.String()
    external_id = graphene.String()
    sales_channels = graphene.List(graphene.ID)
    metadata = graphene.String()


class createPriceListInputField(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    type = graphene.String()
    status = graphene.String()
    starts_at = graphene.DateTime()
    ends_at = graphene.DateTime()
    # customer_groups = graphene.String()
    includes_tax = graphene.Boolean()


class UpdatePriceListInputField(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()
    type = graphene.String()
    status = graphene.String()
    starts_at = graphene.DateTime()
    ends_at = graphene.DateTime()
    # customer_groups = graphene.String()
    includes_tax = graphene.Boolean()


class CreateProductTypeInputField(graphene.InputObjectType):
    value = graphene.String()
    metadata = graphene.String()


class UpdateProductTypeInputField(graphene.InputObjectType):
    id = graphene.ID()
    value = graphene.String()
    metadata = graphene.String()


class CreateProductTagInputField(graphene.InputObjectType):
    value = graphene.String()
    metadata = graphene.String()


class UpdateProductTagInputField(graphene.InputObjectType):
    id = graphene.ID()
    value = graphene.String()
    metadata = graphene.String()
