# Basic Lambda example for a custom callback

This example shows you how to call back to the firetail platform with your own observations. 

event example

```
{
    'api_details': {
        'UUID': 'ded296d8-daed-450c-b83f-b4b8d89cbe95',
        'api_appUUID': 'cca39d04-7b6e-4727-9688-3f908492b620',
        'api_orgUUID': '665002ee-0066-435f-9654-20eb209cdd18',
        'api_type': 'rest',
        'createdBy': 'example@example.com',
        'dateAddedInMicroSeconds': 1710854022659491,
        'g_apiUUID': 'ded296d8-daed-450c-b83f-b4b8d89cbe95',
        'g_appUUID': 'cca39d04-7b6e-4727-9688-3f908492b620',
        'g_orgUUID': '665002ee-0066-435f-9654-20eb209cdd18',
        'name': 'api name'
    },
    'action_type': 'api_schedule_action',
    'invoke_epoch_time': 1712227639,
    'jwt_token': 'example.example.example',
    'action_details': {
        'UUID': '13eec790-73a7-4612-ab09-c122240b52b7',
        'actionType': 'api_schedule_action',
        'actionVersion': 'v0.0.1',
        'action_apiUUID': 'ded296d8-daed-450c-b83f-b4b8d89cbe95',
        'action_appUUID': 'cca39d04-7b6e-4727-9688-3f908492b620',
        'action_orgUUID': '665002ee-0066-435f-9654-20eb209cdd18',
        'createdBy': 'example@example.com',
        'dateAddedInMicroSeconds': 1711050404116639,
        'description': '',
        'enabled': True,
        'g_orgUUID': '665002ee-0066-435f-9654-20eb209cdd18',
        'integrationType': 'custom',
        'integrationUUID': 'd0b7faa9-6ec6-41dd-ae58-e6f528908252',
        'itemType': 'action',
        'name': 'lambda function',
        'scheduledRate': 15,
    },
    'context': {
        'inputs': {
            'api_endpoint': 'https://example.com/health'
        }
    },
    'callback_url': 'https://api.saas.eu-west-1.prod.firetail.app/organisations/665002ee-0066-435f-9654-20eb209cdd18/actions/13eec790-73a7-4612-ab09-c122240b52b7/callback'
}
```