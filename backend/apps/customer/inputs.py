import graphene


class CreateCustomerInputField(graphene.InputObjectType):
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    phone = graphene.String()
    has_account = graphene.Boolean()
    metadata = graphene.JSONString()


class UpdateCustomerInputField(graphene.InputObjectType):
    id = graphene.ID(required=True)
    email = graphene.String()
    billing_address = graphene.ID()
    phone = graphene.String()
    has_account = graphene.Boolean()
    metadata = graphene.JSONString()


class CreateCustomerGroupInputField(graphene.InputObjectType):
    name = graphene.String(required=True)
    customers = graphene.List(graphene.ID)
    # price_lists = graphene.String()
    metadata = graphene.String()
    # deleted_at = graphene.String()


class UpdateCustomerGroupInputField(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    customers = graphene.List(graphene.ID)
    # price_lists = graphene.String()
    metadata = graphene.String()
    # deleted_at = graphene.String()


class CreateCountryInputField(graphene.InputObjectType):
    iso_2 = graphene.String()
    iso_3 = graphene.String()
    num_code = graphene.Int()
    name = graphene.String(required=True)
    display_name = graphene.String()
    region = graphene.ID()


class UpdateCountryInputField(graphene.InputObjectType):
    id = graphene.ID(required=True)
    iso_2 = graphene.String()
    iso_3 = graphene.String()
    num_code = graphene.Int()
    name = graphene.String()
    display_name = graphene.String()
    region = graphene.ID()


class CreateAddressInputField(graphene.InputObjectType):
    company = graphene.String()
    address_1 = graphene.String(required=True)
    address_2 = graphene.String()
    city = graphene.String(required=True)
    country_code = graphene.String()
    country = graphene.ID()
    province = graphene.String()
    postal_code = graphene.String(required=True)
    phone = graphene.String()
    metadata = graphene.String()


class UpdateAddressInputField(graphene.InputObjectType):
    id = graphene.ID(required=True)
    company = graphene.String()
    address_1 = graphene.String(required=True)
    address_2 = graphene.String()
    city = graphene.String(required=True)
    country_code = graphene.String()
    country = graphene.ID()
    province = graphene.String()
    postal_code = graphene.String(required=True)
    phone = graphene.String()
    metadata = graphene.String()


class CreateRegionInputField(graphene.InputObjectType):
    name = graphene.String(required=True)
    currency = graphene.String()
    tax_rates = graphene.String()
    tax_code = graphene.String()
    gift_cards_taxable = graphene.String()
    automatic_taxes = graphene.String()
    tax_provider = graphene.ID()
    metadata = graphene.String(required=False)
    includes_tax = graphene.String()


class UpdateRegionInputField(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    currency = graphene.String()
    tax_rates = graphene.String()
    tax_code = graphene.String()
    gift_cards_taxable = graphene.String()
    automatic_taxes = graphene.String()
    tax_provider = graphene.String()
    metadata = graphene.String()
    includes_tax = graphene.String()
