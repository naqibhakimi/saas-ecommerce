from graphql_relay import from_global_id

def to_database_id(id):
    return int(from_global_id(id).id)