import graphene

class CreateCustomerInput(graphene.InputObjectType):
    email = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    billing_address = graphene.ID(required=True)
    phone = graphene.String()
    has_account = graphene.Boolean()
    metadata = graphene.JSONString()


class UpdateCustomerInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    email = graphene.String(required=True)
    billing_address = graphene.ID(required=True)
    phone = graphene.String()
    has_account = graphene.Boolean()
    metadata = graphene.JSONString()


class CreateCustomerGroupInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    customers = graphene.String()
    price_lists = graphene.String()
    metadata = graphene.String()
    deleted_at = graphene.String()


class UpdateCustomerGroupInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    customers = graphene.String()
    price_lists = graphene.String()
    metadata = graphene.String()
    deleted_at = graphene.String()


class CreateCountryInput(graphene.InputObjectType):
    iso_2 = graphene.String()
    iso_3 = graphene.String()
    num_code = graphene.String()
    name = graphene.String(required=True)
    display_name = graphene.String()
    region = graphene.ID()


class UpdateCountryInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    iso_2 = graphene.String()
    iso_3 = graphene.String()
    num_code = graphene.String()
    name = graphene.String(required=True)
    display_name = graphene.String()
    region = graphene.ID()


class CreateAddressInput(graphene.InputObjectType):
    company = graphene.String()
    address_1 = graphene.String(required=True)
    address_2 = graphene.String()
    city = graphene.String(required=True)
    country_code = graphene.String()
    country = graphene.String(required=True)
    province = graphene.String()
    postal_code = graphene.String(required=True)
    phone = graphene.String()
    metadata = graphene.String()


class UpdateAddressInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    company = graphene.String()
    address_1 = graphene.String(required=True)
    address_2 = graphene.String()
    city = graphene.String(required=True)
    country_code = graphene.String()
    country = graphene.String(required=True)
    province = graphene.String()
    postal_code = graphene.String(required=True)
    phone = graphene.String()
    metadata = graphene.String()


class CreateRegionInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    currency = graphene.String(required=True)
    tax_rates = graphene.String()
    tax_code = graphene.String()
    gift_cards_taxable = graphene.String()
    automatic_taxes = graphene.String()
    tax_provider = graphene.String()
    metadata = graphene.String()
    includes_tax = graphene.String()


class UpdateRegionInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    currency = graphene.String(required=True)
    tax_rates = graphene.String()
    tax_code = graphene.String()
    gift_cards_taxable = graphene.String()
    automatic_taxes = graphene.String()
    tax_provider = graphene.String()
    metadata = graphene.String()
    includes_tax = graphene.String()
