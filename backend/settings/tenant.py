TENANT_TYPES = {
    "public": {
        "URLCONF": "secureconsole.urls",
    },
    "tenant": {
        "URLCONF": "multitenant.urls",
    },
}
