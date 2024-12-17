{% include 'logo.md' %}

# Assurance Details

As a base for expressing assurance we will rely on the [REFEDS
Assurance Framework (RAF)](https://refeds.org/assurance). Based on RAF,
additional assurance profiles are also defined in the
[AARC-G021](https://aarc-project.eu/guidelines/aarc-g021) guideline.

There are different assurance levels available within AAI. These
levels are expressed in **two** different ways, **all** of
which are transported in the `eduperson_assurance` claim.
The two different  ways are called **Profiles** and **Components**.

- **Profiles** are composed by a set of components and are believed to make
it easier for services to filter the users which they want to let in.

- **Components** are available, in case a more complex analysis of the
    users assurance is required.

## Available Assurance Profiles

We promote the use of these assurance profiles:

- `AARC Assam`: Users that logged in with a "social" identity, such as
  ORCID, Github, or Google.
- `IGTF Dogwood`: Users who belong to a home organisation that fulfils minimal
  security standards, such as permanently recording which user used which
  identifier.
- `RAF Cappuccino`: Users had to be verified by checking the passport at the
  home institution.
- `RAF Espresso` is very difficult to achieve, but may be developed for
  high-risk services in the future. For the user it means that his/her photo ID was
  successfully verified against a government database, and he/she uses
  multi-factor authentication for authentication.

Services should maintain a list of assurance-profiles that they expect
their users to comply with.

## Available Assurance Components

RAF (REFEDS Assurance Framework) defines individual components:

Available assurance information are:

- `ID`: Identifier uniqueness
    - `$PREFIX$/ID/unique`
    - `$PREFIX$/ID/no-eppn-reassign`
    - `$PREFIX$/ID/eppn-reassign-1y`

- `IAP`: Identity proofing
    - `$PREFIX$/IAP/low`
    - `$PREFIX$/IAP/medium`
    - `$PREFIX$/IAP/high`
    - `$PREFIX$/IAP/local-enterprise`

- `ATP`: Attribute quality and freshness
    - `$PREFIX$/ATP/ePA-1m`
    - `$PREFIX$/ATP/ePA-1d`


|                                                         | AARC Assam          | IGTF Dogwood                 | RAF Cappuccino                          | ICTF Birch                              | RAF Espresso               |
|:---------------------------------------------------------|:---------------------:|:------------------------------:|:----------------------------------------:|:-----------------------------------------:|:----------------------------:|
| ***Should identifier be unique, personal and traceable?***    | Yes                 | Yes                          | Yes                                     | Yes                                     | Yes                        |
| ***Should identifires be unique across the infrastructure?*** | Unspecified         | Yes                          | Unspecified                             | Yes                                     | Unspecified                |
| ***How fresh do attributes need to be?***                    | Unspecified         | 1 Month                      | 1 Month                                 | 1 Month                                 | 1 Month                    |
| ***What kind of ID proofing is required?***                   | Low (self asserted) | Low (self asserted)          | Medium (e.g postal credential delivery) | Medium (e.g postal credential delivery) | High (e.g face to face)    |
| ***Is Multi-factor Authentication required?***                | Unspecified         | Single factor authentication | Single factor authentication            | Single factor authentication            | Multifactor authentication |


## Examples

- A user's assurance from a german university could look similar to this:

    ```json
      "asr": [
            "https://refeds.org/assurance/ATP/ePA-1d",
            "https://refeds.org/assurance/ATP/ePA-1m",
            "https://refeds.org/assurance/IAP/local-enterprise",
            "https://refeds.org/assurance/IAP/low",
            "https://refeds.org/assurance/IAP/medium",
            "https://refeds.org/assurance/ID/eppn-unique-no-reassign",
            "https://refeds.org/assurance/ID/unique",
            "https://refeds.org/assurance/profile/cappuccino"
        ],
    ```

    In detail:

- `ATP/ePA-1d` User attributes are updated within **one day** after they changed.
- `ATP/ePA-1m` User attributes are updated within **one month** after they changed.
- `IAP/local-enterprise`: User would qualify for access to the Home Organisation’s internal administrative systems
- `IAP/low`: self-asserted identity together with verified e-mail address
- `IAP/medium`: sent a copy of their government issued photo-ID to the CSP and the CSP has had a remote live video conversation to verify the photo-ID
- `ID/eppn-unique-no-reassign`: `eduPersonPrincipalName` value is never reassigned to any other user
- `ID/unique`: User Identifier:
    - The user identifier represents a single natural person
    - The person to whom the identifier is issued can be contacted
    - The user identifier is never re-assigned
- `profile/cappuccino`: The profile information that asserts all of
    the above (see image).

- A user that came via a "social IdP" such as google, github or ORCID
    would look like this:

    ```json
      "eduperson_assurance": [
            "https://refeds.org/assurance/IAP/low",
            "https://refeds.org/assurance/ID/unique",
            "https://aarc-project.eu/policy/authn-assurance/assam",
        ]
    ```

    In detail:

    - Missing `ATP/`: We cannot make any statement about updates of attributes
    - `ID/unique`: Social IdPs are generally very good of keeping the
        identifier linked to the same user.
    - `https://aarc-project.eu/policy/authn-assurance/assam`: AARC-defined
        profile to describe social-IdP users.

### Check your Assurance
To see your own assurance, go to
<!--## FIXME-->
<https://orpheus.data.kit.edu/>, log in and look at
the "User Info From Userinfo Endpoint"


## Additional Information

Additional information on the REFEDS Assurance Framework is [collected
here](concepts.md#the-identity-assurance-concept).

Mapping attributes between SAML and OIDC is discussed in the 
[=> REFEDS OIDCre white paper](https://docs.google.com/document/d/1b-Mlet3Lq7qKLEf1BnHJ4nL1fq-vMe7fzpXyrq2wp08/edit),
especially Table 1.


## The Proxy and the Assurance

There are still IdPs that do not support the REFEDS Assurance Framework.
For the time being, we will use the Community AAI to assess the
originating IdP and then assert a given assurance profile (using the
`eduperson_assurance` claim).

- **Honoring the IdP**: essentially, we "honor" the info coming from the
  IdP, i.e. if the IdP is releasing any of the assurance info, we
  present it as such to downstream services.

- **IdP "whitelisting"**: for IdPs known to follow required procedures for
  expressing assurance components (e.g. have proper identity vetting),
  but do not express them via SAML assertions, we can (automatically)
  assert those claims downstream to SPs that consume this info. This
  may involve "translating" or "interpreting" certain
  attributes (e.g. value "staff" may translate to "medium", while
  "student" do not, etc.)

- **PI (Principal Investigator) action**: the PI is responsible of the VO he/she
  manages. The PI can accept members that do not meet the assurance
  requirement, but they cannot access services with assurance requirements
  that exceed those the users has.
    - We are therefore working on a method that allows authorised
      personnel to raise individual components of a users' assurance.
    - Please understand that this is quite complex and hence still under
      investigation.


{% include 'gitinfo.md' %}
