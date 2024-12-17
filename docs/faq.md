{% include 'logo.md' %}

# Frequently Asked Questions

## IAM4NFDI

<details>
<summary>
Was ist IAM4NFDI?
</summary>

IAM4NFDI befasst sich mit der Vernetzung und Erweiterung bestehender und neu entstehender Identity and Access Management (IAM)-Systeme, um Forschenden unterschiedlicher Domänen und Institutionen möglichst einfachen Zugriff auf digitale Ressourcen innerhalb der NFDI zu ermöglichen, einschließlich des Zugangs zu und Austauschs mit externen Infrastrukturen und Ressourcen wie der European Open Science Cloud (EOSC). Dazu ist ein dezentrales, föderiertes IAM erforderlich. Auf diese Weise können Nutzerinnen und Nutzer von ca. 400 deutschen Forschungs- und Hochschuleinrichtungen sowie ca. 5000 Heimatorganisationen weltweit (Zahl steigend) auf Dienste und Ressourcen zugreifen, die von der NFDI Community Authentication & Authorisation Infrastructure (AAI) bereitgestellt werden.

</details>



<details>
<summary>
Warum braucht man die Federations?
</summary>

Identity federations bringen Nutzende aus verschiedenen Forschungs- und Bildungseinrichtungen mit verschiedenen Dienstbetreibern zusammen. Egal ob diese Dienste aus der eigenen Organisation heraus administriert werden oder nicht \- dadurch, dass Nutzende über den Login an ihrer Heimateinrichtung authentifiziert werden, weiß ein Dienstbetreiber, dass ein User einer bestimmten Organisation angehört und entsprechend vertrauenswürdig ist. Und eine Organisation kann ihren Nutzenden Services anbieten, die innerhalb der Federation von verschiedenen Anbietern betrieben werden. Es ist somit

- einfach (nur über ihren Organisations-Login),
- kostengünstig (weil der Dienst keinen organisationsinternen Admin benötigt) 
- und sicher (weil es innerhalb der Federation Sicherheitsregeln gibt)

</details>

<details>
<summary>
Inwiefern baut IAM4NFDI auf die Federations auf?
</summary>

Durch den Anschluss an IAM4NFDI ist man automatisch auch an die Federationen angeschlossen. IAM4NFDI setzt auf den bewährten und verlässlichen (well established and trusted) technischen Rahmen der DFN-AAI und eduGAIN. Dadurch wird z.B. möglich, dass sich Forschende (auch aus anderen Ländern) mit ihrem Instituts-Login bei Diensten anmelden (single-sign on). 


</details>

<details>
<summary>
Was bietet IAM4NFDI zusätzlich?
</summary>

Die IAM4NFDI bietet zusätzlich eine *Community Verwaltung*. Community Admins erhalten somit eine Möglichkeit ihre Community Mitglieder und deren Dienste-Berechtigungen an zentraler Stelle zu verwalten und Dienstbetreiber können die Nutzendenverwaltung nach ihren Anforderungen an die Community Admins delegieren.

</details>

<details>
<summary>
Wo liegen die Vorteile?
</summary>
Für Forschende stehen heute tausende von Werkzeugen und Datenquellen zur Verfügung. Um effizient arbeiten zu können, braucht es oft Zugang zu Diensten aus ihrer Forschungs- oder Bildungseinrichtung, aus ihrer Wissenschaftsdisziplin oder sogar aus einem ganz spezifischen Projekte. Wissenschaftseinrichtungen müssen Zugang zu diesen Diensten ermöglichen (damit ihre Forschenden arbeiten können) \- zusätzlich stellen sie aber auch Dienste zur Verfügung, die von Forschenden über das eigene Institut hinaus genutzt werden sollen.

Der Hauptvorteil des IAM4NFDI besteht in der Verbindung von Instituts-Login mit den digitalen Tools und Ressourcen in der NFDI & für jede Disziplin eine passende Lösung bereitstellen, die dann die Tools und Ressourcen verbindet, die Forschende in dieser Disziplin benötigen. Ohne Einbindung an IAM4NFDI müssen Dienstbetreiber z.B. Passwörter selbst zurücksetzen (ein ganz konkretes Beispiel) und Nutzende haben z.B. keine gesicherten Organisationszugehörigkeiten

Weiter Vorteile für Institutionen sind ...
- größere Reichweite eigener Dienste mit geringem administrativen Aufwand (sie können von allen Nutzenden verwendet werden, deren Organisation bzw. Community bei IAM4NFDI angeschlossen ist), 
- einfacher, kostengünstiger Zugang zu Software-Diensten und Ressourcen für die eigenen Forschenden
- Diensteberechtigungen für einzelne Communities (=Forschungsdisziplinen oder Forschungsgruppen mit ähnlichen Bedürfnissen) können an Community Administratoren abgegeben werden 
- Dienstbetreiber & Community Administratoren
- Nutzendenverwaltung über ein einziges Interface statt für jede einzelne Organisation und jeden einzelnen Dienst
- Forschende
- einfacher Zugang zu Werkzeugen und Ressourcen ohne jeweils einen eigenen Account erstellen zu müssen \- nur mit dem eigenen Insituts-Login


</details>

<details>
<summary>
Was ist ein möglicher Use Case?
</summary>
RDMO (Research Data Management Organiser) unterstützt Forschungsprojekte bei der Planung, Umsetzung und Verwaltung aller Aufgaben des Forschungsdatenmanagements. Es ist ein Werkzeug um Datenmanagementpläne zu pflegen, also Daten, die im Rahmen eines Wissenschaftsprojekts benötigt und verwaltet werden zu planen. 

Das Tool an sich ist disziplinübergreifend einsetzbar. Verschiedene Community Administratoren verwalten die Berechtigungen und Templates für verschiedene Forschungs-Communities. Durch IAM4NFDI kann der Zugang zu RDMO mit dem Login der Heimatorganisation verwendet werden, man braucht keinen eigenen Login. Zudem kann die Herkunft der User verifiziert werden wodurch die Nutzung des Tools für alle User und den Dienstbetreiber sicherer wird. Community Administratoren können im IAM4NFDI Interface aber nicht nur die Nutzenden von RDMO und deren Rechte verwalten, sondern auch für alle anderen Tools, die für die Forschenden in ihrer Community relevant sind.



</details>



## NFDI AAI

<details>
<summary>
Ist die NFDI AAI nur mit einer der vier Community AAI Produkte kompatibel?
</summary>

Die NFDI AAI ist grundsätzlich so aufgebaut, dass möglichst viele unterschiedliche Komponenten verwendet werden können. Dies gilt insbesondere für Community AAI Produkte. Entsprechen die Attribute und Richtlinien den AEGIS-Endorsed Recommendations, können diese als Community AAIs eingebunden werden. Eine Liste der wachsenden Produkte können wir an dieser Stelle nicht führen, zumal manche Produkte unterschiedliche Attributprofile unterstützen. Die Kompatibilität hängt entscheidend davon ab. Ein guter Ausgangspunkt ist die Unterstützung der Standards SAML2 und OIDC. Wichtig ist, dass sich 1 Konsortium aus den vier Lösungen genau eine aussucht, die dann für alle seine Dienste anwendbar ist!

Für weitere Details siehe (<a href="https://doc.nfdi-aai.de/">Dokumentation</a>). 

Eine Merkmalsvergleichsmatrix finden Sie <a href="https://docs.google.com/spreadsheets/d/1EHUo3KS4KDaQZomR5c1LYK1fQA2_4ZjsIx9xlEXrKac/edit#gid=0">hier</a>

</details>

<details>
<summary> Kann die „NFDI-AAI“ Attribute von mehreren Community-AAIs abfragen? </summary>

Grundsätzlich ja, aber dies sollte nur verwendet werden, wenn das Sammeln von Attributen aus mehreren AAIs erforderlich ist.
</details>

## Community AAI

### Funktionalität und technische Umsetzung

<details> <summary>Existieren die vier Community-AAIs bereits oder werden diese als eigene Instanz neu aufgebaut? </summary>  

Dies hängt von jedem Instanzbetreiber individuell ab. Die Software ist vorhanden und mindestens eine Instanz wird von den jeweiligen Experten betrieben. Wenn die Lösung mandantenfähig ist, kann eine solche Instanz von mehreren Konsortien genutzt werden. Es wäre auch möglich, eine Instanz exklusiv für ein Konsortium zu betreiben, aufgrund begrenzter Ressourcen ist dies jedoch nicht kostenlos zur verfügbar gestellt werden. Dies bedeutet, dass alle zusätzlichen Kosten von den Konsortien selbst getragen werden müssen. 
</details>

<details>
<summary>Was sind die Unterschiede zwischen den vier Community-AAIs? </summary>

Alle vier AAI-Lösungen basieren auf der AARC Blueprint Architecture. Leider ist eine Vergleichstabelle recht politisch und unterliegt ständigen Änderungen.
Aus diesem Grund bieten wir eine <a href="https://docs.google.com/spreadsheets/d/1EHUo3KS4KDaQZomR5c1LYK1fQA2_4ZjsIx9xlEXrKac/edit#gid=0">Feature-Matrix</a> an, in der die bereitgestellten Features jeder Community-AAI-Lösung aufgelistet sind. Jedes Konsortium kann diese Matrix zur Auswahl eine CAAI-Lösung benutzen. Wenn es Probleme bei der Entscheidungsfindung gibt, werden wir dann überlegen, welche Community-AAI-Lösung am besten zum jeweiligen NFDI-Konsortium passt. Sofern für Sie kein bestimmtes Feature von Interesse ist, kann jede der Lösungen gewählt werden.


Alle vier AAI-Lösungen basieren auf der AARC Blueprint Architecture. Leider ist eine Vergleichstabelle sehr politisch und unterliegt immer noch ständigen Änderungen. Daher bieten wir eine Feature-Tabelle an, in der die Features jeder Community-AAI-Lösung nachgelesen werden können. Jedes Konsortium kann dort auch „Keine Präferenz“ angeben. Wir überlegen dann, welche Community-AAI-Lösung am besten zum jeweiligen NFDI-Konsortium passt. Sofern kein bestimmtes Feature für Sie von Interesse ist, kann jede der Lösungen gewählt werden.
</details>

<details> <summary>Stellt jede der vier Community-AAIs dem Dienst eine unterschiedliche Identität für die Anmeldung bereit?</summary>  

Im Prinzip ja, aber „unterschiedlich“ ist etwas zu allgemein. Generell hat jedes Konsortium eine AAI basierend auf einer der vier Lösungen. Eine Identität wird mit dem gleichen Satz an Attributen beschrieben, die Werte der Attribute können jedoch unterschiedlich sein. Es ist möglich, verschiedene Identitäten desselben Benutzers miteinander zu verknüpfen. Dies kann entweder zentral im Infrastruktur-Proxy oder dezentral in der Anwendung erfolgen.
</details>

<details> <summary>Gibt es einen automatischen Mechanismus im Umgang mit unterschiedlichen Identitäten?</summary> 

Nein, Duplikatsvermeidung (z.B. ID-Matching) ist im Projekt nicht vorgesehen. Da jedes Konsortium grundsätzlich eine AAI auf Basis einer der vier Lösungen besitzt, sollte dies i.d.R. nicht vorkommen. Grundsätzlich ist es möglich, dass ein Benutzer mehrere Accounts hat, wenn ein bestimmter Benutzer unterschiedliche Accounts aus unterschiedlichen Konsortien besitzt. Die manuelle Verwaltung dieser Accounts ist grundsätzlich möglich, bleibt aber den Diensten bzw. Benutzern überlassen.
</details>

<details> <summary>Werden Informationen zwischen den vier Community-AAIs ausgetauscht?</summary>

Nein, ein Austausch auf dieser Ebene ist nicht vorgesehen. Konsortien müssen sich daher für eine Lösung entscheiden und sich dort organisieren.

</details>

### Regulatorien und Anforderungen

<details>
<summary>Leisten die Community AAIs Hochverfügbarkeit (HA) und Service Level Agreement (SLA)?</summary>

Ja, dies ist für alle vier Community AAIs möglich, es hängt jedoch von der Implementierung ab, ob es in kostenlosen oder kostenpflichtigen Instanzen enthalten ist.
</details>

<details>
<summary>Gibt es ein Backup für den Notfall?</summary>

Ja, alle Konsortien haben Backups.
</details>

<details>
<summary>Wie wird die Datensicherheit bezüglich der einzelnen Lösungen gewährleistet?</summary>

Fragen zur Datensicherheit können Sie dem bereitgestellten <a href="https://zenodo.org/records/13149756">Betriebskonzept</a> entnehmen. Zudem wird es Demo-Instanzen geben, sodass Sie (die NFDI-Konsortien) sich eine Entscheidungsgrundlage für eine Lösung bilden können.

</details>

## Service-Verbindung

### Allgemeines

<details>
<summary>Wo soll eine Virtuelle Organisation (VO) eingefügt werden, die den Zugriff auf ELN/Repo regelt?
</summary>

Die VOs werden in der jeweiligen Community-AAI verwaltet. Das ist der Hauptzweck.
</details>

<details>
<summary>Kann ein Dienst Attribute aus der Heimatorganisation verwenden? </summary>

Ja. Es ist vorgesehen, ausgewählte Attribute von der Heimatorganisation an den Dienst weiterzuleiten. Damit soll dem Dienst beispielsweise ermöglicht werden, den Status eines Benutzers (Student, Mitarbeiter, …) oder Berechtigungen über „entitlements“ zu verwenden. Die „assurance“ wird ebenfalls von der Heimatorganisation weitergeleitet (sofern diese diese bereitstellt).
</details>

<details>
<summary>Was muss ein Service beim Serviceanschluss beachten?</summary>

Dies hängt von der Anzahl der Konsortien ab, die an den Dienst angeschlossen werden sollen. Wenn nur ein Konsortium berücksichtigt werden muss, sollte dies vom Konsortium selbst geklärt werden. Wenn mehr als ein Konsortium beteiligt ist, muss der Dienst den NFDI-Proxy berücksichtigen und mit dem NFDI-Team sprechen.
</details>

### Roles, Groups and Users

<details>
<summary>Wo werden die Rechte bezüglich Rollen/Gruppen oder Benutzern auf bestimmte Datensätze gepflegt?</summary>

In den Community AAIs.
</details>

<details>
<summary>Verfügen Benutzer über eine Menge verknüpfter IdPs mit Identitäten, von denen Attribute angefordert werden können? </summary>

Nein. Dienste fordern die Attribute nicht direkt bei den IdPs an, sondern erhalten diese ausschließlich über den Proxy, an den sie angebunden sind. Natürlich steht es den Diensten frei, weitere Attribute zu erfassen. Dies ist in der Architektur jedoch nicht vorgesehen und kann vorerst auch nicht unterstützt werden.
</details>

<details>
<summary>Wie gehe ich mit externen Benutzern um?</summary>

Alle Nutzerinnen und Nutzer von Universitäten können den Login ihrer Heimatinstitution über DFN-AAI oder eduGAIN nutzen. Alle CAAI-Softwares verfügen über Lösungen, um weitere Nutzerinnen und Nutzer einzubinden, z.B. über ORCID oder „soziale“ Logins. Ebenfalls ab 2025 können alle Nutzerinnen und Nutzer einen DFN-Edu-ID-Login <a href="https://www.dfn.de/eine-fuer-alle-die-edu-id/">(siehe hier)</a> nutzen.

</details>

### Verantwortlichkeiten und Organisatorische Fragen (Support Model)

<details>
<summary>Wer kümmert sich um Einrichtung, Konfiguration und Betrieb? </summary>

Im Rahmen der <a href="documents/iam4nfdi_initialization.pdf">[gerade angefordert]</a> B4N/IAM-Projekte werden die vier Lösungen im Rahmen des IAM-Projekts betrieben.
</details>

<details>
<summary>Wer trifft die Entscheidung für eine Softwarelösung für die AAI-Community </summary>

Eine Community kann als gut organisierte Einheit betrachtet werden, typischerweise ein NFDI-Konsortium.
</details>

<details>
<summary>Wie wird die Unterstützung für IAM4NFDI aussehen?
</summary>

Folgender Support ist vorgesehen:
- Level 1 - Community-Admins (Schulung für Support erforderlich)
- Level 2 - IAM-Projektteam
- Nach Projektende erfolgt Support durch die Community
AAI-Anbieter (wird mit dem jeweiligen Anbieter vertraglich vereinbart)
- Betrieb und Support der zentralen Komponenten können z.B.
durch den DFN erfolgen (Betriebsmodell noch zu definieren)

</details>

<details>
<summary>Ist die Nutzung einer CAAI kostenlos?
</summary>

Die Nutzung einer zentralen CAAI-Instanz ist kostenfrei. Wenn die Funktionalität jedoch an spezielle Anforderungen angepasst werden muss und eine individuelle CAAI-Instanz benötigt wird, fallen Kosten an. Inkubatoren bieten ein Framework an, um zusätzliche Funktionalität in die CENTRAL-Komponenten oder die CAAIs zu implementieren. Dies ist kostenfrei, jedoch bis zu einem bestimmten Komplexitätsgrad begrenzt.

</details>

<details>
<summary>Ist die Migration zwischen CAAI möglich?
</summary>

An der interoperablen Definition von Nutzern und Gruppen wird aktuell von
Standardisierungsgremien gearbeitet. Dies soll auch an den einzelnen CAAI
Lösungen unterstützt werden. Da derzeit beides noch in der Entwicklung
befindlich ist, ist eine Migration zwischen CAAI Lösungen nicht
vorgesehen. Im Einzelfall müsste im Vorfeld der händische Aufwand mit den
betroffenen Lösungen abgeklärt werden.

</details>

{% include 'gitinfo.md' %}
