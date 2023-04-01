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


class CreateImageInputField(graphene.InputObjectType):
    url = graphene.String()
    metadata = graphene.String()


class UpdateImageInputField(graphene.InputObjectType):
    id = graphene.ID()
    url = graphene.String()
    metadata = graphene.String()


class CreateProductCollectionInputField(graphene.InputObjectType):
    title = graphene.String()
    handle = graphene.String()
    # products =
    metadata = graphene.String()


class UpdateProductCollectionInputField(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    handle = graphene.String()
    # products =
    metadata = graphene.String()


class CreateMoneyAmountInputField(graphene.InputObjectType):
    currency = graphene.ID()
    amount = graphene.Float()
    min_quantity = graphene.Int()
    max_quantity = graphene.Int()
    price_list = graphene.ID()
    variant = graphene.ID()
    region = graphene.ID()


class UpdateMoneyAmountInputField(graphene.InputObjectType):
    id = graphene.ID()
    currency = graphene.ID()
    amount = graphene.Float()
    min_quantity = graphene.Int()
    max_quantity = graphene.Int()
    price_list = graphene.ID()
    variant = graphene.ID()
    region = graphene.ID()


class CreateProductCategoryInputField(graphene.InputObjectType):
    name = graphene.String()
    handle = graphene.String()
    is_active = graphene.Boolean()
    is_internal = graphene.Boolean()
    parent_category = graphene.ID()


class UpdateProductCategoryInputField(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    handle = graphene.String()
    is_active = graphene.Boolean()
    is_internal = graphene.Boolean()
    parent_category = graphene.ID()


class CreateProductOptionInputField(graphene.InputObjectType):
    title = graphene.String()
    product = graphene.ID()
    metadata = graphene.JSONString()


class UpdateProductOptionInputField(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    product = graphene.ID()
    metadata = graphene.JSONString()


class CreateProductOptionValueInputField(graphene.InputObjectType):
    value = graphene.String()
    option = graphene.ID()
    variant = graphene.ID()
    metadata = graphene.JSONString()


class UpdateProductOptionValueInputField(graphene.InputObjectType):
    id = graphene.String()
    value = graphene.String()
    option = graphene.ID()
    variant = graphene.ID()
    metadata = graphene.JSONString()


class CreateProductTaxRateInputField(graphene.InputObjectType):
    product = graphene.ID()
    tax_rate = graphene.ID()
    metadata = graphene.JSONString()


class UpdateProductTaxRateInputField(graphene.InputObjectType):
    id = graphene.ID()
    product = graphene.ID()
    tax_rate = graphene.ID()
    metadata = graphene.JSONString()


class CreateProductTypeTaxRateInputField(graphene.InputObjectType):
    product_type = graphene.ID()
    tax_rate = graphene.ID()
    metadata = graphene.JSONString()


class UpdateProductTypeTaxRateInputField(graphene.InputObjectType):
    id = graphene.ID()
    product_type = graphene.ID()
    tax_rate = graphene.ID()
    metadata = graphene.JSONString()


class CreateProductVariantInventoryItemInputField(graphene.InputObjectType):
    inventory_item_id = graphene.String()
    variant_id = graphene.String()
    required_quantity = graphene.Int()


class UpdateProductVariantInventoryItemInputField(graphene.InputObjectType):
    id = graphene.ID()
    inventory_item_id = graphene.String()
    variant_id = graphene.String()
    required_quantity = graphene.Int()


class CreateProductVariantInputField(graphene.InputObjectType):
    title = graphene.String()
    product = graphene.ID()
    sku = graphene.String()
    barcode = graphene.String()
    ean = graphene.String()
    upc = graphene.String()
    variant_rank = graphene.Int()
    inventory_quantity = graphene.Int()
    allow_back_order = graphene.Boolean()
    manage_inventory = graphene.Boolean()
    hs_code = graphene.String()
    origin_country = graphene.String()
    mid_code = graphene.String()
    material = graphene.String()
    weight = graphene.Int()
    length = graphene.Int()
    height = graphene.Int()
    width = graphene.Int()
    metadata = graphene.JSONString()


class UpdateProductVariantInputField(graphene.InputObjectType):
    id = graphene.ID()
    title = graphene.String()
    product = graphene.ID()
    sku = graphene.String()
    barcode = graphene.String()
    ean = graphene.String()
    upc = graphene.String()
    variant_rank = graphene.Int()
    inventory_quantity = graphene.Int()
    allow_back_order = graphene.Boolean()
    manage_inventory = graphene.Boolean()
    hs_code = graphene.String()
    origin_country = graphene.String()
    mid_code = graphene.String()
    material = graphene.String()
    weight = graphene.Int()
    length = graphene.Int()
    height = graphene.Int()
    width = graphene.Int()
    metadata = graphene.JSONString()
