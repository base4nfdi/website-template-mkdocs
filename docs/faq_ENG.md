{% include 'logo.md' %}

# Frequently Asked Questions

## IAM4NFDI

<details>
<summary>
What is IAM4NFDI?
</summary>

IAM4NFDI is concerned with connecting and expanding existing and emerging Identity and Access Management (IAM) systems in a way that researchers from different domains and institutions are able to access digital resources within NFDI as easily as possible, including access to and exchange with external infrastructures and resources like the European Open Science Cloud (EOSC). A decentralised, federated IAM is required. This way, users from approx. 400 German research and higher education institutions plus approx. 5000 home organisations worldwide \-number increasing \- will be able to access services and resources provided by the NFDI Community Authentication & Authorisation Infrastructure (AAI).

</details>



<details>
<summary>
Why do we need Federations?
</summary>

Identity federations bring users from different research and educational institutions together with different service providers. Regardless whether these services are administered from within the home organization or not. User authentication via login at home institution means that a service provider knows that a user belongs to a certain organization and is therefore trustworthy. An organization can offer its users services that are operated by different providers within the federation. It is therefore

- simple (only via their organization login),
- cost-effective (because the service does not require an internal organization admin)
- and secure (because there are security rules within the federation)

</details>

<details>
<summary>
How does IAM4NFDI build on the federations?
</summary>

By connecting to IAM4NFDI you are automatically connected to the federations. IAM4NFDI relies on the well established and trusted technical framework of DFN-AAI and eduGAIN. This makes it possible, for example, for researchers (including those from other countries) to log into services using their institute login (single sign on).


</details>

<details>
<summary>
What does IAM4NFDI offer in extension?
</summary>

The IAM4NFDI also offers *Community Management*. Here, The community admins are given the opportunity to manage their community members and their service authorizations centrally, and service providers can delegate user management to the community admins according to their requirements.

</details>

<details>
<summary>
What are the advantages?
</summary>
Today, researchers have thousands of tools and data sources at their disposal. In order to work efficiently, they often need access to services from their research or educational institution, from their scientific discipline or even from a very specific project. Scientific institutions must provide access to these services (so that their researchers can work), but they also provide services that are intended to be used by researchers beyond their own institute.

The main advantage of IAM4NFDI is to connect the institute login with the digital tools and resources in the NFDI & provide a suitable solution for each discipline, which then connects the tools and resources that researchers need in that discipline. Without integration with IAM4NFDI, service operators must reset passwords themselves (a very specific example) and users do not have secure organizational affiliations.

Other advantages for institutions are...
- greater reach of their own services with little administrative effort (they can be used by all users whose organization or community is connected to IAM4NFDI),

- simple, cost-effective access to software services and resources for their own researchers
- service authorizations for individual communities (= research disciplines or research groups with similar needs) can be given to community administrators

- service operators & community administrators
- user management via a single interface instead of for each individual organization and each individual service
- researchers
- easy access to tools and resources without having to create a separate account \- only with your own institute login


</details>

<details>
<summary>
What is a possible use case?
</summary>
RDMO (Research Data Management Organiser) supports research projects in the planning, implementation and administration of all research data management tasks. It is a tool for maintaining data management plans, i.e. planning data that is needed and managed as part of a scientific project.

The tool can be used across disciplines. Different community administrators manage the permissions and templates for different research communities. With IAM4NFDI, access to RDMO can be used with the login of the home organization, you do not need your own login. In addition, the origin of the user can be verified, which makes using the tool safer for all users and the service provider. Community administrators can not only manage the users of RDMO and their rights in the IAM4NFDI interface, but also for all other tools that are relevant to the researchers in their community.

</details>

## NFDI AAI


<details>
<summary>
Is the NFDI AAI only compatible with the four Community
AAI products mentioned?
</summary>

The NFDI AAI is basically structured in such a way that the largest
possible number of different components can be used. This is particularly
true for Community AAI products. If the attributes and policies correspond
to the AEGIS-Endorsed Recommendations, they can be integrated as Community
AAIs. We cannot maintain a list of growing products at this point,
especially since some products support different attribute profiles.
Compatibility depends crucially on this. A good starting point is support
of the standards SAML2 and OIDC. For details see
(<a href="https://doc.nfdi-aai.de/">documentation</a>). We also have a <a href="https://docs.google.com/spreadsheets/d/1EHUo3KS4KDaQZomR5c1LYK1fQA2_4ZjsIx9xlEXrKac/edit#gid=0">feature comparison matrix here</a>

It is important that 1 consortia should pick exactly one of the four solutions that is then applicable to all their services!

</details>


<details>
<summary> Can the "NFDI AAI" query attributes from multiple community AAIs? </summary>

In principle yes, but this should only be used if collecting attributes from multiple AAIs is nesseccary.
</details>

## Community AAI

### Functionality and Technical Implementation

<details> <summary>Do the four Community AAIs  already exist or will they be set up again as a separate instance? </summary>  

This depends on each instance operator individually. The software exist and at least one instance is run by the respective experts. If the solution supports tenants, such an instance can be used by multiple consortia. It would also be possible to run an instance exclusively for
one consortium, but due to limited ressources this is not available for free. This means that all additional costs must be paid by the consortia themselves. 
</details>

<details>
<summary>What are the differences between the four Community AAIs? </summary>

All four AAI solutions are based on the AARC Blueprint Architecture. Unfortunately, a comparison table is quite political and is still subject to constant change. 
Therefore, we offer a <a href="https://docs.google.com/spreadsheets/d/1EHUo3KS4KDaQZomR5c1LYK1fQA2_4ZjsIx9xlEXrKac/edit#gid=0">feature table</a>, where each community AAI solution specifies their features. Each consortia can use this matrix to choose the CAAI solution. If there are issues in decision-making, we will then consider which Community AAI solution suits best to the respective NFDI consortium. Unless, there is a particular feature of interest for you, any of the solutions can be choosen.

</details>

<details> <summary>Does each of the four Community AAIs provide a different identity to the service for login?</summary>  

In principle yes, but “different” is a bit too general. In general, each consotiom has one AAI based on one of the four solutions. An identity is described with the same set of attributes, the values of the attributes can be different. It is possible to link different identities of the same user together. This can either be done centrally in the Infrastructur-Proxy or decentrally in the application.
</details>


<details> <summary>Is there an automatic mechanism for dealing with different identities?</summary> 

No, duplicate avoidance (e.g. ID matching) is not intended in the project. In general, each consortia has one AAI based on one of the four solutions which is why this should generally not happen. In principle, it is possible for a user to have multiple accounts if a certain user has different accounts from different consortia. In general, managing these accounts manuelly is possible, but is left to the services or users respectively.
</details>

<details> <summary>Is information shared between the four Community
AAIs?</summary>

No, an exchange at this level is not planned. Therefore, consortia must
choose a solution and organize themselves only there.

</details>

### Regulations and Requirements


<details>
<summary>Do the Community AAIs provide High Availability (HA) and Service Level Agreement (SLA)?</summary>

Yes, this is possible for all four Community AAIs, but it depends on implementation if it is include in free instances or chargeable ones.
</details>


<details>
<summary>Is there a backup in case of an emergency?</summary>

Yes, all consortia have backups.
</details>


<details>
<summary>How is data security ensured in the solution?</summary>

Questions regarding data security can be found in the provided <a href="https://zenodo.org/records/13149756">operating concept</a>. There will also be demo instances such that you (the NFDI consortia) can form a basis for deciding on a solution.

</details>



## Service Connection

### General

<details>
<summary>Where should a virtual organization (VO) that regulates access to ELN/Repo be inserted?
</summary>

The VOs are maintained in the respective community AAI. That is main purpose.
</details>

<details>
<summary>Can a service use attributes from home organization? </summary>

Yes. It is intended to forward selected attributes from the home organization to the service. This is intended to enable the service, for example, to use the status of a user (student, staff, ...) or permissions via "entitlements". The “assurance” is also forwarded by the home organization (if they provide it).
</details>

<details>
<summary>What does a service have to consider regarding to service connection?</summary>

This depends on the number of consortia that are to be connected to the service. If only one consortia have to be considered this should be clarified be the consortia itself. If more than one consortia is involved the service has to be consider the NFDI proxy and should talk with the NFDI Team.
</details>

### Roles, Groups and Users

<details>
<summary>Where are the rights regarding roles/groups or users to specific data sets maintained?</summary>

In the Community AAI.
</details>

<details>
<summary>Do users have a set of linked IdPs to identities from which attributes can be requested? </summary>

No. Services do not request the attributes directly from the IdPs, but receive them exclusively via the proxy to which they are connected. Of course, services are free to collect additional attributes. This is not intended in the architecture and cannot be supported for the time being.
</details>

<details>
<summary>How to deal with external users?</summary>

All users from universities can use the login from their home institution via DFN-AAI or eduGAIN. All CAAI softwares have solutions to include other users, e.g. via ORCID or "social" logins. Also from 2025 on all users can use an DFN-Edu-ID-Login <a href="https://www.dfn.de/eine-fuer-alle-die-edu-id/">(see here)</a>.

</details>


### Responsibilities and Organizational Issues (Support Model)

<details>
<summary>Who takes care of the setup, configuration and operation? </summary>

As a part of the <a href="documents/iam4nfdi_initialization.pdf">[just requested]</a> B4N/IAM projects, the four solutions are operated as part of the IAM project.
</details>


<details>
<summary>Who makes the decision for a software solution for the AAI community </summary>

A community can be seen as well-organized unit which is typically an NFDI consortium.
</details>

<details>
<summary>How will support look like for IAM4NFDI?
</summary>

We intend to provide the following support:
- Level 1 - Community admins (training for support required)
- Level 2 - IAM project team
- after the end of the project, support will be provided by the Community
    AAI providers (to be contracted with the individual provider) 
- operations and support for the central components can be provided, e.g.
    by the DFN (operating model yet to be defined)

</details>


<details>
<summary>Is the usage of a CAAI free of charge?	
</summary>

Usage of a central CAAI instance is free of charge. However, if the
functionality needs to be adapted to specific requirements and an
individual CAAI instance is needed, this will come with associated costs.
Incubators offer a framework to implement additional functionality in the
CENTRAL components or the CAAIs. This is free of charge but limited up to
a certain level of complexity.

</details>

<details>
<summary>Can we migrate our users between CAAIs?
</summary>

The interopeable definition of users and groups is currently being
develeoped in standardisation groups. Also the CAAIs have already started
implementing support for interoperable protocols (e.g. SCIM).
Since both is under development, a migration service between two CAAI
solutions can currently not be offered. In case a migration needs to be
undertaken, this will involve manual work and needs to be assed by the
CAAIs involved into the migration reqest.

</details>

{% include 'gitinfo.md' %}
