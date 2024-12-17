{% include 'logo.md' %}

# NFDI AAI Attributes

Attributes are used to describe the user. They are meant to be used for
the authorisation decision. Different sets of attributes are available at
different layers in the infrastructure. This is somewhat logical, since
for example services that are connected to eduGAIN can not see those
attributes that are managed in the Community AAI.

More generally speaking, the set of attributes coming from "Home-IdPs" in
eduGAIN is different to the one that is passed on by the Community AAIs.
The set of attributes available from the Infrastructure Proxy will be very
similar to those of the Community AAIs.

We make use of standardised attribute sets, both for the attributes
expected from the Home-IdPs at the Community AAIs, as well as for those
that are sent from the Community AAIs to underlying services.

!!! Note
    This page is intended for easily accessible documentation purposes.
    It *should* be in sync with the [Infrastructure Attribute Profiles
    (IAP)](https://codebase.helmholtz.cloud/m-team/nfdi/nfdi-policies/-/jobs/artifacts/v0.9.2/raw/04_IAP.pdf?job=build-docs). The IAP has precedence
    over this webpage.


## Attributes available from the Community AAIs

These attributes are available to services connected below **any**
Community AAI. I.e. to services connected to any Community AAI or to the
Infrastructure Proxy.

We use the "Core Attribute Profile" and the "Extended Attribute Profile"
as defined within the EOSC AAI, which is based on the [AARC
recommendations](https://aarc-community.org/guidelines)

### Core Attribute Profile

Attributes listed here are **mandatory**.

The table uses this convention:

- **bold entries** in the table are the preferred and encourages
    attributes.
- Normal (non-bold) entries are possible alternatives to the bold entries.
- Whenever multiple options for attributes are available, content may be
    sent either in one of them, or in multiple attributes.
- Receiving ends should prefer the bold ones, and may use the normal ones.


| Identity Attribute Type                                      | SAML Attribute                     | OpenID Connect Claim                 | Comments |
|--------------------------------------------------------------|------------------------------------|--------------------------------------|----|
| Non-reassignable,<br/>persistent,<br/>unique user identifier |Any of the following: <br/>**voPersonID [[voPerson-2.0](https://github.com/voperson/voperson/blob/draft-2.0.0/voPerson.md)]** <br/>eduPersonUniqueId [[eduPerson](https://wiki.refeds.org/display/STAN/eduPerson)] <br/>subject-id [[SAML-SubjectID-v1.0](https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/saml-subject-id-attr-v1.0.html)] <br/>pairwise-id [[SAML-SubjectID-v1.0](https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/saml-subject-id-attr-v1.0.html)] <br/>SAML Persistent NameID [[SAML2Core](https://docs.oasis-open.org/security/saml-subject-id-attr/v1.0/cs01/saml-subject-id-attr-v1.0-cs01.html#SAML2Core)] |  Any of the following:<br/> **voperson_id [[voPerson-2.0](https://github.com/voperson/voperson/tree/draft-2.0.0)]**<br/> eduperson_unique_id [[eduPerson](https://wiki.refeds.org/display/STAN/eduPerson)]<br/> sub (public)+iss [[OIDC-Core](https://openid.net/specs/openid-connect-core-1_0.html)]<br/> sub (pairwise)+iss [[OIDC-Core](https://openid.net/specs/openid-connect-core-1_0.html)] | Created by the Community AAI |
| Name information | **displayName** | **name** [[OIDC-Core](https://openid.net/specs/openid-connect-core-1_0.html)]| E.g.: John Doe|
| Email information| Any of<br/> - mail<br/> - **voPersonVerifiedEmail [voPerson-2.0]**| Any of<br/> - email [OIDC-Core]<br/> - email_verified [OIDC-Core] <br/> - **voperson_verified_email [voPerson-2.0]**| There is currently no way of indicating a preferred email address (e.g. when sending multiple emails). One workaround may be to use the **first** entry of the list as a **preferred** email address of the user. This **MAY NOT work in all circumstances!!!**|
|Home organisation information| **schacHomeOrganization [[SCHAC-1.5](https://wiki.refeds.org/download/attachments/44957731/SCHAC%2B1.5.0.pdf?version=3&modificationDate=1429202342624&api=v2)]**| Either of<br/>- **org_domain** + org_name<br/>- schac_home_organization| The domain name of the users Home-Org.|
|Affiliation within the community|  **eduPersonScopedAffiliation [eduPerson]** | **eduperson_scoped_affiliation [eduPerson]**| A controlled vocabulary will be provided by NFDI-AAI (following EOSC/AARC conventions)|
| Affiliation at the Home-Org.|  **voPersonExternalAffiliation [voPerson-2.0]**| **voperson_external_affiliation [voPerson-2.0]**| Home-Org. Affiliation will be passed on "as is" in this attribute|
|Assurance| **eduPersonAssurance [eduPerson]**|** eduperson_assurance [eduPerson]**| As defined in [[RAF](https://refeds.org/assurance)], and detailed [here](assurance.md).|


### Extended Attribute Profile

Attributes listed here are **optional**.

| Identity Attribute Type      | SAML Attribute                                                                      | OpenID Connect Claim                                                                                                                                             | Comment                                                                                                                                                                                                                                            |
|------------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Groups and roles             | eduPersonEntitlement [[AARC-G002](https://aarc-community.org/guidelines/aarc-g002)] | One of the following:<br/> - eduperson_entitlement [AARC-G002]<br/> - entitlements [[RFC9068](https://datatracker.ietf.org/doc/html/rfc9068), AARC-G069]<br/> | urn:geant:dfn.de:nfdi.de:**group**:example#authority.host.de (indicates a group membership)<br/>Note: The authority part is optional. Still in NFDI-AAI we want to use it. A registry is operated at <https://www.nfdi.de/persistent-identifiers>. |
| Capabilities                 | eduPersonEntitlement [[AARC-G027](https://aarc-community.org/guidelines/aarc-g027)] | Any of the following:<br/> - eduperson_entitlement [AARC-G027]<br/> - entitlements [RFC9068, AARC-G027]                                                       | urn:geant:dfn.de:nfdi.de:**res**:example#authority.host.de (indicates a resource entitlement).  A registry is operated at <https://www.nfdi.de/persistent-identifiers>.                                                                            |
| Agreement to policies        | voPersonPolicyAgreement [voPerson-2.0]                                              | voperson_policy_agreement [voPerson-2.0]                                                                                                                         | Allows services to skip local policy clicking, if e.g. done at Community-AAI                                                                                                                                                                       |
| ORCID identifier             | eduPersonOrcid [eduPerson]                                                          | orcid                                                                                                                                                            |
| Preferred email              | ?                                                                                   | ?                                                                                                                                                                | Unclear if this will be used, since EOSC/AARC directions are unclear at the moment.
| Supplemental Name Information | givenName + sn                                                                      | given_name + family_name                                                                                                                                         |
| Authentication Profiles      | AuthenticationContextClassReference                                                 | acr                                                                                                                                                              | For indicating whether a 2nd factor was used                                                                                                                                                                                                       |
| External Idenfifier          | voPersonExternalID                                                                  | voperson_external_id                                                                                                                                             | An explicitly scoped identifier for a person, typically as issued by an external authentication service. Could be used for ID linking.                                                                                                             |
| SSH Keys                      | sshPublicKey                                                                        | ssh_public_key                                                                                                                                                | A list of ssh keys                                                                                                                                                                                                                                 |




## Attributes needed by the Community AAIs

These attributes are required to be released by the Home-IdPs, so that
users can reasonably use the services at the Community AAI. Precise
requirements may differ between different Instances and Software Products
used to implement a Community AAI.

### Personalized

[https://refeds.org/category/personalized](https://refeds.org/category/personalized)

| Identity Attribute Type | SAML Attribute                                                                                    | OpenID Connect Claim                                      |
|-------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| Organization            | schacHomeOrganization [SCHAC]                                                                     | schac_home_organization                                   |
| user identifier         | subject-id [SAMLSubId]                                                                            | sub (shared) + iss                                        |
| person name             | All of <br/> - displayName [eduPerson] <br/> - givenName [eduPerson] <br/> - sn [eduPerson] <br/> | All of <br/> - name<br/> - given_name <br/> - family_name |
| email address           | mail [eduPerson]                                                                                  | email [OIDC-COre]                                         |
| Affiliation             | eduPersonScopedAffiliation [eduPerson]                                                            | eduperson_scoped_affiliation                              |
| Assurance               | eduPersonAssurance [eduPerson]                                                                    | One of <br/> - eduperson_assurance<br/> - asr             |

### Pseudonomous

<https://refeds.org/category/pseudonymous>

The REFEDS Pseydonymous profile may be acceptable, if the Community AAI
provides a means to query the user for a Name (displayName, or givenName + sn),
and a (verified!) email address.

| Identity Attribute Type               | SAML Attribute                         | OpenID Connect Claim                         |
|---------------------------------------|----------------------------------------|----------------------------------------------|
| Organization                          | schacHomeOrganization [SCHAC]          | schac_home_organization                      |
| pseudonymous pairwise user identifier | pariwise-id [SAMLSubId]                | sub (pairwise) + iss                         |
| Affiliation                           | eduPersonScopedAffiliation [eduPerson] | eduperson_scoped_affiliation                 |
| Assurance                             | eduPersonAssurance [eduPerson]         | One of<br/> - eduperson_assurance<br/> - asr |


### Anonymous: Not sufficient

The anonymous profile
<https://refeds.org/category/anonymous>
does not provide a number of sufficient attributes.
For specific combinations of Community-AAI and Community-Service, an
exception may technically work. Please consult your Community-AAI contact.


## Attributes in different protocols

Attributes can be expressed in different protocols. We maintain a mapping
for SAML, OIDC, LDAP and SCIM. The list is available upon request.


{% include 'gitinfo.md' %}
