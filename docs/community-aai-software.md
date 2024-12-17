{% include 'logo.md' %}

# Community AAI Software

The NFDI AAI Architecture requires the use of a so called "Community AAI".
Here we list the available software products that implement the
fuctionality of a Community AAI. Each of them can be used to run such a
Community AAI Service.

The software products were selected because of their relevance in the
context of NFDI and the German AAI ecosystem.

It is planned to offer an installation of each Community AAI to the NFDI
Consortia as a Service (Community-AAI as a Service). Each NFDI Consortium
needs to settle on a single Community-AAI.

## AcademicID

[`AcademicID`](https://docs.gwdg.de/doku.php?id=de:services:general_services:academicid:start)

- Operated and developed by: GWDG
- [Overview Presentation](slides/academic-id.pdf)
- Contact: Christof.Pohl at gwdg de

## didmos

[`didmos`](https://daasi.de/en/federated-identity-and-access-management/iam-solutions/didmos/)
didmos is a powerful software suite for Identity & Access Management
by DAASI International. It consists of six expandable open source
modules which also can be used to implement a Community AAI. didmos Core
allows VO and group management for both external and local users that
can be managed with the powerful self service and admin tool didmos LUI.
The AARC BPA compliant SSO proxy didmos Auth supports the protocols OIDC
and SAML both towards clients (acting as an IdP) and authentication
sources (acting as an SP).

- Operated and Developed by: DAASI
- [Overview Presentation](slides/didmos.pdf)
- Contact: P(eter).Gietz at daasi de

## RegApp

[RegApp](https://www.scc.kit.edu/en/services/regapp.php) is a federated
open source identity management system, which is mainly developed at the
Scientific Computing Centre (SCC) at KIT. The currently installed
solution enables more than 38,000 registered users from various research
institutions, including the Helmholtz Association and universities, to log
in to various services, secured by two-factor authorization (2FA). Users
can use the account provided by their home institution for this purpose.

- Operated and developed by: KIT
- [Overview Presentation](slides/reg-app.pdf)
- Contact: Michael.Simon at kit edu

## Unity

[Unity](https://unity-idm.eu/) is a complete solution for identity, federation and inter-
federation management. Or, looking from a different perspective, it is
an extremely flexible authentication service. It is a open-source
software, developed by Bixbit. The single-sign on proxy component,
which supports OIDC and SAML to authenticating services and to
consuming services, is AARC BPA compliant. Optional it offers further
features like VO management or multi-factor authentication.

- Operated by: FZ-Jülich
- [Overview Presentation](slides/unity.pdf)
- ds-support at fz-juelich de

## Feature Matrix

We maintain a feature matrix to allow a quick comparison between available
Community AAI softwares. Given that all of these implementations are very
complex software products, that are highly configurable, it is very difficult to
provide a detailed and adequate comparison of them. This feature matrix is
rather coarse grained. We'll gratefully collect your feedback, if you want to
share it with us.

[Feature Matrix (on google)](https://docs.google.com/spreadsheets/d/1EHUo3KS4KDaQZomR5c1LYK1fQA2_4ZjsIx9xlEXrKac)

{% include 'gitinfo.md' %}
