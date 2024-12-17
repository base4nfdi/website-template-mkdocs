{% include 'logo.md' %}

# Authorising users for access to a service

NFDI AAI enables authorisation on three different types of information:

!!! info 
    All these methods can be combined, which can easily result in
    highly complex or even chaotic authorisation schemas if not planned well
    beforehand. If you as a service provider plan to establish a non-trivial
    authorisation schema to heterogenous user groups, please check the
    following methods carefully.

## Types of Authorisation


## Virtual Organisation

In this authorisation type, services provide resources to Virtual
Organisations. Membership is managed by the community itself, e.g. by VO
administrators that add (or remove) users to their VO. <br/> 

The VO membership is transmitted via `entitlements` claims and the `group`
keyword (see [AARC-G069](https://aarc-community.org/guidelines/aarc-g069).
This and the already registered VOs are defined at the Community AAI
instances.
Users can be organised in hierarchical (tree-topology) groups (i.e. VOs
and sub-VOs). 

Example:
```
    "urn:geant:dfn.de:nfdi.de:<consortium>:group:<vo-name>:<sub-vo>#login.antmaster.de",
```

## Resource capabilities

Some services or Communities require an additional authorisation
structure, that shifts the authorisation decision away from the service
towards the Community-AAI. Then, the Community AAI makes specific
statements about what a user may do, e.g. whether or not to start VMs, or
which datasets may be accessed.

This information is also transmitted via
the `entitlements` claim, but then using the `res` keyword (see
[AARC-G027](https://aarc-community.org/guidelines/aarc-g027)).

Example:

```
    "urn:geant:dfn.de:nfdi.de:<consortium>:res:ant-dataset-42:read#login.antmaster.de",
    "urn:geant:dfn.de:nfdi.de:<consortium>:res:start-vm#login.antmaster.de",
```

## Home-IdP based authorisation

Enables authorisation based on attributes that are administered by a
Home-IdP. This includes what kind of status or affiliation a person has
(e.g. student) or whether specific access legitimation was given to a
user. Attributes and values used in this case need to be agreed upon
between Identity Providers and Services.

In addition, a Home-IdP may communicate entitlements such as VO membership
or Resource capabilities. In order to prevent conflicting statements, this
should be done in close collaboration between the administrators of
Home-IdPs, Community-AAIs, VO Admins and Services.

## Assurance based authorisation

Assurance describes the quality of an identity. This enables to
differentiate between specific quality levels of an identity.

IdPs provide assurance information on the identity of the user,
for example stating that a photo ID has been checked and/or that multi
factor authentication is employed. This is expressed by the user's
Home organisation and forwarded within the AAI. If the organisation
provides only the assurance information but not the fulfilled profiles,
the AAI adds the profile information.

The [REFEDS Assurance Framework (RAF)](https://refeds.org/assurance)
defines individual assurance components that describe a users identity.
This allows for differentiation between the quality of the ID-Vetting, the
attribute freshness and the uniqueness of the identifiers used.

Further information is provided in [these slides of Wolfgang Pempe on
identity assurance[(https://download.aai.dfn.de/ws/2022/refeds_assurance_suite.pdf)

{% include 'gitinfo.md' %}
