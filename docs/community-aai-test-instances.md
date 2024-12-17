{% include 'logo.md' %}

# Community AAI **Test** Instances

!!! Important
    The DEMO Instances are subject to an important migration: All
    Community AAIs will be migrated to using the [german edu-id](https://www.dfn.de/eine-fuer-alle-die-edu-id/) 
    by 2025. 

    THIS MAY INDUCE AN IDENTIFIER CHANGE ON YOUR CONNECTED
    SERVICES!

The following Community AAI Softwares provide a **test** instance at the
following location.

These test instances have several purposes:

1. Integration testing to validate the released attributes in SAML and OIDC
2. Test-integration of services that are planned to be integrated with
   NFDI AAI

All test instances should be available by October.

## Academic ID

- Link to instance: <https://academiccloud.de>
- How to get VO-Admin rights for testing the instance:
- Service Registry: sso-support@gwdg.de
- Connected Services:
    - SAML-SPs:
    - OIDC-RPs:
        - orpheus: <https://orpheus.data.kit.edu>
        - mytoken: <https://mytoken.data.kit.edu>
        - oidc-agent: public client

## didmos

- Link to instance: <https://portal.didmos.nfdi-aai.de>
- How to get VO-Admin rights for testing the instance:
- Service Registry:
    - Currently via Email david.huebner@daasi.de
    - Dynamic Client Registration Endpoint: <https://auth.didmos.nfdi-aai.de/OIDC/registration>
- Connected Services:
    - SAML-SPs:
    - OIDC-RPs:
        - orpheus: <https://orpheus.data.kit.edu>
        - mytoken: <https://mytoken.data.kit.edu>
        - oidc-agent: public client (packaged with v5.0)

## Reg-APP

- Link to instance: <https://regapp.nfdi-aai.de>
- How to get VO-Admin rights for testing the instance:
- Contact: fels@scc.kit.edu
- Service Registry:
    - Doku (DE): <https://www.scc.kit.edu/dienste/regapp.php>
    - Doku (EN): <https://www.scc.kit.edu/en/services/regapp.php>
- Connected Services:
    - SAML-SPs:
    - OIDC-RPs:
        - orpheus: <https://orpheus.data.kit.edu>
        - mytoken: <https://mytoken.data.kit.edu>
        - oidc-agent: public client (packaged with v5.0)

## Unity

- Link to instance: <https://login-dev.helmholtz.de>
- How to get VO-Admin rights for testing the instance: <https://hifis.net/doc/helmholtz-aai/howto-vos/>
- Service Registry: <https://hifis.net/doc/helmholtz-aai/howto-services/>
- Contact: ds-support@fz-juelich.de
- Connected Services:
    - SAML-SPs:
        - Test-SP3 (will be replaced by a dedicated NFDI-AAI attribute checker)
    - OIDC-RPs:
        - orpheus: <https://orpheus.data.kit.edu>
        - mytoken: <https://mytoken.data.kit.edu>
        - oidc-agent: public client (packaged with v5.0)

{% include 'gitinfo.md' %}
