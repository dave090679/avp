# NVDA-Erweiterung für Kaspersky Internet Security #

Diese Erweiterung verbessert die Zugänglichkeit von Kaspersky Internet Security 2013 bis 2019. der größte Teil der Oberfläche von KIS wird aussagekräftig beschriftet. Folgende Punkte sind jedoch (noch) beim Umgang mit KIS zu beachten

## Installation von Kaspersky Internet Security

Aufgrund von Unzulänglichkeiten bei der Barrierefreiheit von KIS werden Sie Zum Auslesen des Installationsprogramms eine optische Zeichenerkennung (OCR) benutzen müssen. Bisherige Erfahrungen mit KIS ab 2016 zeigten unter Windows 7 und windows 8.1, dass sich dafür die OCR des Marktbegleitenden Screenreaders Jaws von Freedom Scientific sehr gut eignet. Jaws kann von der [Downloadseite von Freedomscientific](http://www.freedomsci.de/serv01.htm) heruntergeladen werden.

Seit Windows 10 1703 enthält Windows OneCore unter anderem eine optische Zeichenerkennung für viele Sprachen, die Sie mit NVDA ab Version 2017.3 verwenden können, um Kaspersky Internet Security zu installieren. Dies bedeutet, dass Sie keinen zweiten Bildschirmleser mehr verwenden müssen, wenn Sie KIS installieren. 

### so installieren Sie Kaspersky Internet Security unter Zuhilfenahme von Jaws

* beenden Sie NVDA und starten Sie Jaws für Windows
* Starten Sie die Installation von Kaspersky Internet Security
* Wenn Sie von der Benutzerkontensteuerung von Windows gefragt werden, ob Sie zulassen möchten, dass durch das Programm Veränderungen an dem Computer vorgenommen werden, bestätigen Sie diese Abfrage mit "ja". Eventuell öffnet sich das Dialogfeld im hintergrund, sodass Sie es zunächst mit alt+tab in den Vordergrund holen müssen.
* Gehen Sie folgendermaßen vor, um einen bildschirminhalt bei der Installation mit der OCR von Jaws auszulesen:
 - drücken Sie die Tastenkombination einfügen+o, s Bzw. Feststelltaste+o, s, um die Texterkennung von Jaws zu Starten. nach Abschluss der Texterkennung wird der jaws-Cursor (der Mauszeiger) automatisch aktiviert.
 - Verwenden Sie die Pfeiltasten, die navigationstasten an Ihrer Braillezeile oder die Pfeiltasten des Nummernblocks, um den Jaws-Cursor über den Bildschirminhalt zu bewegen Bzw. den Bildschirminhalt zu lesen.
 - Verwenden Sie das Divisionszeichen des Nummernblocks, um an der gewünschten Stelle des Bildschirms einen Linksklick zu emulieren.
* Wiederholen Sie die oben beschriebenen Schritte für jeden HinweisBildschirm des Installationsprogramms von Kaspersky Internet Security
* Nach Abschluss der Installation können Sie Jaws beenden und zu NVDA zurückkehren.

### so installieren Sie Kaspersky Internet Security unter Zuhilfenahme der Texterkennung unter Windows 10

* Starten Sie die Installation von Kaspersky Internet Security
* Wenn Sie von der Benutzerkontensteuerung von Windows gefragt werden, ob Sie zulassen möchten, dass durch das Programm Veränderungen an dem Computer vorgenommen werden, bestätigen Sie diese Abfrage mit "ja". Eventuell öffnet sich das Dialogfeld im hintergrund, sodass Sie es zunächst mit alt+tab in den Vordergrund holen müssen.
* Gehen Sie folgendermaßen vor, um einen bildschirminhalt bei der Installation mit der OCR von Windows 10 auszulesen:
 - drücken Sie die Tastenkombination nvda+r, um die Texterkennung von NVDA zu Starten. nach Abschluss der Texterkennung wird das Erkennungsergebnis in einem virtuellen Dokument im Lesemodus angezeigt.
 - Verwenden Sie die Pfeiltasten, die navigationstasten an Ihrer Braillezeile oder die Pfeiltasten des Nummernblocks, um den Cursor über den Bildschirminhalt zu bewegen Bzw. den Bildschirminhalt zu lesen.
 - Drücken Sie die Leertaste Bzw. die Eingabetaste, um an der gewünschten Stelle des Bildschirms einen Linksklick zu emulieren.
 - Drücken Sie ESC, um das Erkennungsergebnis zu schließen.
* Wiederholen Sie die oben beschriebenen Schritte für jeden HinweisBildschirm des Installationsprogramms von Kaspersky Internet Security.

#### Hinweis zu Kaspersky Internet Security 2019
Aufgrund geänderter Datenschutzbestimmungen durch die DSGVO sah sich Kaspersky Lab gezwungen, einen zusätzlichen Lizenzvertrag während der Installation zwischenzuschalten. Dieser Lizenzvertrag wird angezeigt, nachdem Sie den Eröffnungsbildschirm mit "fortsetzen" quittiert haben. In diesem Lizenzvertrag gibt es zwei Kontrollkästchen, die aktiviert werden müssen, bevor Sie den Lizenzvertrag mit der Schaltfläche "akzeptieren" annehmen können. Diese Kontrollkästchen verstecken sich unter dem Satz "ich bestätige dass ich die Lizenzbestimmungen vollständig gelesen und verstanden habe und akzeptiere sie." bzw. "ich bestätige dass ich die Datenschutzerklärung vollständig gelesen und verstanden habe und akzeptiere sie". Bisherige Erfahrungen mit KIS 2019 und NVDA legen nahe, dass sich das Kontrollkästchen unter dem Wort "akzeptiere" zu verbergen scheint. Gehen Sie daher nach dem Aufrufen der Texterkennung wie folgt vor, um die Kontrollkästchen zu aktivieren.

* Verwenden Sie die Pfeiltasten nach unten Bzw. nach oben, um nach dem Satz "ich bestätige, dass ich die Lizenzbestimmungen Bzw. die Datenschutzerklärung vollständig gelesen und verstanden habe und akzeptiere sie." zu suchen.
* Verwenden Sie die Tastenkombination strg+Pfeiltaste nach rechts Bzw. strg+Pfeiltaste nach links, um innerhalb des Satzes das Wort "akzeptiere" aufzusuchen.
* Drücken Sie die Eingabetaste, um einen Linksklick auf das Wort "akzeptiere" zu emulieren und dadurch das Kontrollkästchen zu aktivieren.


## Hinweise zur Verwendung von Kaspersky Internet Security

### Selbstschutz

Die Selbstschutzfunktion von Kaspersky Internet Security soll verhindern, dass Programme die Schutzkomponenten von KIS unbemerkt deaktivieren. Dies bedeutet, dass bei dem Versuch manche Funktionen von KIS zu verwenden, ein Bestätigungsdialog angezeigt wird, in dem der Benutzer seine Zustimmung geben (auf "zulassen" klicken) muss. Dies ist durchaus buchstäblich zu verstehen, denn bei der Bedienung der Dialogfelder ist die Tastatur vollkommen ausgeklammert; der Anwender kann die Dialoge nur mit einer Maus bedienen. Das Ausklammern der Tastatur schließt auch etwaige Mausemulationen (z. B. die Tastaturmaus von Windows) mit ein. 

Selbst die mausbezogenen Hilfsfunktionen von NVDA werden durch den Selbstschutz von KIS blockiert; die Maustöne sind beim Bewegen der Maus immer stumm, wenn ein Dialog des Selbstschutzes von KIS im Vordergrund zu sehen ist.

der Selbstschutz von KIS stellt deshalb eine Barriere für Nutzer von Bildschirmleseprogrammen dar. Zur Umgehung der durch den Selbstschutz bedingten Behinderungen gibt es jedoch einige Lösungswege, die in den folgenden Abschnitten gezeigt werden sollen.

### Einrichten des Kennwortschutzes

Beim Umgang mit KIS stellt der Selbstschutz (siehe oben) manchmal eine Behinderung dar, weil die Dialoge des Selbstschutzes mit Bildschirmlesern nicht ausgelesen Bzw. nicht mit der Tastatur bedient werden können. Dies betrifft z. B. das Beenden von KIS oder das Deaktivieren von Schutzkomponenten. Mit dem Kommandozeilenprogramm AVP, das zu KIS gehört, ist es jedoch möglich, diese Aufgaben auszuführen, ohne durch den Selbstschutz behindert zu werden. Das Kommandozeilenprogramm AVP verlangt jedoch für manche Aufgaben ein Kennwort, das zuvor in den Einstellungen von KIS festgelegt werden muss.

#### So aktivieren Sie den Kennwortschutz von KIS

* Rufen Sie über das Kontextmenü des KIS-Symbols im Infobereich der Taskleiste die Einstellungen von KIS auf. 
* Drücken Sie in der Kategorie Allgemein den Schalter "kennwortschutz einrichten". Ein entsprechendes Dialogfeld erscheint.
* Tragen Sie in beide Eingabefelder ein kennwort ein.
* Legen Sie mit den Kontrollkästchen fest, wann der kennwortschutz wirksam sein soll. Folgende Optionen sollten Sie aktivieren:
 - Programmeinstellungen anpassen: Das kennwort wird abgefragt, sobald Sie die Einstellungen von KIS aufrufen oder Schutzkomponenten deaktivieren möchten. Das Aktivieren dieser option ist nötig, weil das Kommandozeilenprogramm avp (siehe unten) zwingend ein Kennwort voraussetzt, wenn Sie Schutzkomponenten deaktivieren.
 - Programm beenden: Das kennwort wird abgefragt, wenn Sie KIS beenden wollen. Die aktivierung dieser option ist nötig, weil das Kommandozeilenprogramm AVP zwingend ein Kennwort voraussetzt, wenn Sie KIS beenden.
* bestätigen Sie die Einstellungen durch Drücken der Schaltfläche "Speichern".
* Geben Sie das kennwort ein, wenn Sie dazu aufgefordert werden und betätigen Sie den Schalter "fortsetzen".

### Deaktivieren von Schutzkomponenten

Manchmal kann es sinnvoll sein, einzelne Schutzkomponenten zu deaktivieren. Hierzu können beispielsweise bestimmte Installationsprogramme zählen, die sehr tief ins System eingreifen. 

Benutzer von Bildschirmleseprogrammen haben dabei das Problem, dass der Selbstschutz (siehe oben) eine Deaktivierung von Schutzkomponenten über die einstellungen von KIS verhindert. Sie können jedoch das Kommandozeilenprogramm avp verwenden, um bestimmte Schutzkomponenten zu deaktivieren.

#### So deaktivieren Sie Schutzkomponenten von KIS mit Hilfe des Kommandozeilenprogramms AVP

* rufen Sie eine Eingabeaufforderung (cmd) auf.
* Wechseln Sie in das Programmverzeichnis, in dem Sie KIS installiert haben (zum Beispiel "c:\Program files (x86)\Kaspersky lab\Kaspersky Internet Security 19.0.0")
* Verwenden Sie den Befehl avp  stop Schutzkomponente, um die angegebene Schutzkomponente zu deaktivieren. Folgende Schutzkomponenten sind in Kaspersky Internet Security 2019 verfügbar (die in Klammern stehenden Namen können als Abkürzungen verwendet werden):
 - AgreementsStatisticsSendTask
 - Anti_Spam (AS)
 - AntiBannerTask
 - ApplicationInvestigatorTask
 - AVStreamMonitorTask
 - DntTask
 - File_Monitoring (FM)
 - Firewall (FW)
 - FirewallGroup
 - HipsTask (HIPS)
 - httpscan (HTTP)
 - ids
 - IM_Monitoring (IM)
 - Inventory_Scan
 - KsnqTask
 - Mail_Monitoring (EM)
 - P2PStorAiTask
 - ParCtl (PC)
 - PatchManagement
 - PatchManagementScan
 - PatchManagementScanBackground
 - PluginActivator
 - Protection (RTP)
 - RollbackUpdate
 - SafeBanking
 - Scan_My_Computer
 - Scan_Objects
 - Scan_Qscan
 - Scan_Quarantine
 - Scan_Startup (STARTUP)
 - Scan_System_Memory
 - Scan_Vulnerabilities (SECURITY)
 - SISettingsUpdaterTask
 - SW2
 - TrafficProcessingPreloader
 - TrustedBoot
 - UiSettingsStorage
 - UnwantedProductDiscoveryTask
 - UnwantedProductDiscoveryTaskBackground
 - Updater
 - Web_Monitoring (WM)
 - WebToolBar
 - WiFiProtection
* Geben Sie das Kennwort ein, wenn Sie dazu aufgefordert werden.
* Beenden Sie die Eingabeaufforderung.

### beenden von Kaspersky Internet Security

Manchmal kann es erforderlich sein, Kaspersky Internet Security zu beenden.  Dies kann z. B. bei (Installations-)Programmen nötig werden, die sehr tief ins System eingreifen. Die Selbstschutzkomponente von KIS verhindert jedoch ein Beenden über das Kontextmenü des Symbols im Infobereich.

#### So beenden Sie Kaspersky Internet Security mit Hilfe des Kommandozeilenprogramms AVP

* Rufen sie eine Eingabeaufforderung (cmd.exe) auf.
* wechseln Sie in das Verzeichnis, in dem Sie KIS installiert haben (z. B. c:\program files (x86)\Kaspersky Lab\Kaspersky Internet security 19.0.0
* verwenden Sie den folgenden Befehl, um Kaspersky Internet Security zu beenden: avp exit
* Geben Sie das Kennwort ein, wenn Sie dazu aufgefordert werden.
* schließen Sie die Eingabeaufforderung

### Deinstallieren von Kaspersky Internet Security

Der Selbstschutz von KIS verhindert eine Deinstallation über Systemsteuerung --> Programme und Funktionen. Sie können KIS jedoch mit Hilfe eines speziellen Entfernungswerkzeugs deinstallieren. Das Entfernungswerkzeug kann mit NVDA unter Umständen nicht richtig bedient werden. Sie können jedoch einen anderen Bildschirmleser wie Jaws für Windows verwenden, um das Entfernungswerkzeug zu bedienen. In der folgenden Anleitung wird davon ausgegangen, dass Jaws bereits gestartet wurde.

#### so deinstallieren Sie KIS mit Hilfe des Entfernungswerkzeugs

* Beenden Sie KIS mit Hilfe des Kommandozeilenprogramms AVP (siehe oben).
* Laden Sie sich das Entfernungstool für KIS von der [Webseite des Herstellers](http://support.kaspersky.com/de/common/service/1464#block1) herunter und führen Sie es aus.
* akzeptieren Sie den Lizenzvertrag
* Wählen Sie das zu entfernende Produkt aus und lösen Sie das Captcha. Seien Sie beim Auslesen des Bildschirminhalts aufmerksam, weil sich die angezeigten (und einzugebenden) Zeichen des Captchas sehr großräumig verteilen können.
* ist das Captcha korrekt, so beginnt das Entfernungswerkzeug nach dem Betätigen des Schalters "löschen", Kaspersky Internet Security zu entfernen.


## weitere Informationen zur Barrierefreiheit von Kaspersky Internet Security

Im Benutzerforum von Kaspersky Lab finden Sie weitere aktuelle Informationen rund um die Barrierefreiheit von Kaspersky Internet Security. Das Forum ist unter dem folgenden Link zu finden: 
<https://forum.kaspersky.com/index.php?/topic/210098-kis-2012-barrierefreier-modus/>

Dort finden Sie auch die aktuelle Version der Erweiterung zum Download.

