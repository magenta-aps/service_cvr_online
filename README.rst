This package contains integration to ServicePlatformen cvr entity lookup 
specifically using the service service_cpr_online

Here is an example looking up Magenta-aps' cvr number

We assume that SP_UUIDS hnd CERTIFICATE_FILE have been specified according to agreement with Serviceplatformen like these example values:

CERTIFICATE_FILE = 'my.crt'

SP_UUIDS = {
    "service_agreement": "fc258319-3a45-499b-a3ce-0fe449a1d6bd",
    "user_system": "42c1357e-67f1-451c-a7a9-f8cd886430a0",
    "user": "dd9f7e33-eb2c-4d60-8279-8fe3652aa019",
    "service": "2e87a902-dbe2-4fc4-8eff-9263eb8f1227",
}


in settings according to the documentation here:


    >>> from service_cvr_online import get_cvr_data
    >>> get_cvr_data("42424242", SP_UUIDS, CERTIFICATE_FILE)

This should return a dictionary like

    {
        'branchebeskrivelse': 'Branche 42'
        'branchekode': '424242',
        'dawa_uuid':'040bfb4c-1e58-49a3-bbb6-ae20ddce1c03',
        'doer': '',
        'etage': '42',
        'husnummer': '42',
        'kommunekode': '4242',
        'organisationsnavn': 'Org 42',
        'postboks': '',
        'postnummer': '4242',
        'vejkode': '4242',
        'vejnavn': 'Vej 42',
        'virksomhedsform': 42
    }

A non existent cvr number will raise a RuntimeError        
