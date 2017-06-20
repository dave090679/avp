# NVDA-Erweiterung für Kaspersky Internet Security #

Diese Erweiterung verbessert die Zugänglichkeit von Kaspersky Internet Security 2013 bis 2017. der größte Teil der Oberfläche von KIS wird aussagekräftig beschriftet. Folgende Punkte sind jedoch (noch) beim Umgang mit KIS zu beachten

## Installation von Kaspersky Internet Security

Aufgrund von Unzulänglichkeiten bei der Barrierefreiheit von KIS ist es leider nicht möglich, das Programm unter Zuhilfenahme von NVDA zu installieren. Zum Auslesen der oberfläche werden Sie aus diesem Grund eine optische Zeichenerkennung (OCR) benutzen müssen. Bisherige Erfahrungen mit KIS 2016 und 2017 zeigten, dass sich dafür die OCR des Marktbegleitenden Screenreaders Jaws von Freedom Scientific sehr gut eignet. Jaws kann von der [Downloadseite von Freedomscientific](http://www.freedomsci.de/serv01.htm)

### so installieren Sie Kaspersky Internet Security unter Zuhilfenahme von Jaws

* beenden Sie NVDA und starten Sie Jaws für Windows
* Starten Sie die Installation von Kaspersky Internet Security
* Wenn Sie von der Benutzerkontensteuerung von Windows gefragt werden, ob Sie zulassen möchten, dass durch das Programm Veränderungen an dem Computer vorgenommen werden, bestätigen Sie diese Abfrage mit "ja". Eventuell öffnet sich das Dialogfeld im hintergrund, sodass Sie es zunächst mit alt+tab in den Vordergrund holen müssen.
* Gehen Sie folgendermaßen vor, um einen bildschirminhalt bei der Installation mit der OCR von Jaws auszulesen:
 - drücken Sie die Tastenkombination einfügen+o, s Bzw. Feststelltaste+o, s, um die Texterkennung von Jaws zu Starten. nach Abschluss der Texterkennung wird der jaws-Cursor (der Mauszeiger) automatisch aktiviert.
 - Verwenden Sie die Pfeiltasten, die navigationstasten an Ihrer Braillezeile oder die Pfeiltasten des Nummernblocks, um den Jaws-Cursor über den Bildschirminhalt zu bewegen Bzw. den Bildschirminhalt zu lesen.
 - Verwenden Sie das Divisionszeichen des Nummernblocks, um an der gewünschten Stelle des Bildschirms einen Linksklick zu emulieren.
* Wiederholen Sie die oben beschriebenen Schritte für jeden (Hinweis)Bildschirm des Installtionsprogramms von Kaspersky Internet Security
* Nach Abschluss der Installation können Sie Jaws beenden und zu NVDA zurückkehren.

## Hinweise zur Verwendung von Kaspersky Internet Security

### Selbstschutz

Die Selbstschutzfunktion von Kaspersky Internet Security soll verhindern, dass Programme die Schutzkomponenten von KIS unbemerkt deaktivieren. Dies bedeutet, dass bei dem Versuch manche Funktionen von KIS zu verwenden, ein Bestätigungsdialog angezeigt wird, in dem der Benutzer seine Zustimmung geben (auf "zulassen" klicken) muss. Dies ist durchaus buchstäblich zu verstehen, denn bei der Bedienung der Dialogfelder ist die Tastatur vollkommen ausgeklammert; der Anwender kann ihn nur mit einer Maus bedienen. Das Ausklammern der Tastatur schließt auch etwaige Mausemulationen (etwa die Tastaturmaus von Windows) mit ein. 

Selbst die mausbezogenen Hilfsfunktionen von NVDA werden durch den Selbstschutz von KIS blockiert; die Maustöne sind beim Bewegen der Maus immer stumm, ein Dialog des Selbstschutzes von KIS im Vordergrund zu sehen ist.

der Selbstschutz von KIS stellt deshalb eine Barriere für Nutzer von Bildschirmleseprogrammen dar. Zur Umgehung der durch den Selbstschutz bedingten Behinderungen gibt es jedoch einige Lösungswege, die in den folgenden Abschnitten gezeigt werden sollen.

### Einrichten des Kennwortschutzes

Beim Umgang mit KIS ist es manchmal erforderlich, den kennwortschutz zu aktivieren, so z. B. beim Deaktivieren von Schutzkomponenten oder beim Beenden von KIS (siehe unten)

#### So aktivieren Sie den Kennwortschutz von KIS

* Rufen Sie über das Kontextmenü des KIS-Symbols im Infobereich der Taskleiste die Einstellungen von KIS auf. 
* Drücken Sie in der Kategorie Allgemein des Schalter "kennwortschutz einrichten". Ein entsprechendes Dialogfeld erscheint.
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
* Wechseln Sie in das Programmverzeichnis, in dem Sie KIS installiert haben (zum Beispiel "c:\Program files (x86)\Kaspersky lab\Kaspersky Internet Security 2017")
* Verwenden Sie den Befehl avp  stop Schutzkomponente, um die angegebene Schutzkomponente zu deaktivieren. Folgende Schutzkomponenten sind in Kaspersky Internet Security 2017 verfügbar (die in Klammern stehenden Namen können als Abkürzungen verwendet werden):
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
 - MpmUpdateTaskDummy
 - P2PStorAiTask
 - ParCtl (PC)
 - PatchManagement
 - PatchManagementScan
 - PluginActivator
 - PluginSupportServiceTask
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
 - UnwantedProductDiscoveryTask
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
* wechseln Sie in das Verzeichnis, in dem Sie KIS installiert haben (z. B. c:\program files (x86)\Kaspersky Lab\Kaspersky Internet security 17.0.0
* verwenden Sie den folgenden Befehl, um Kaspersky Internet Security zu beenden: avp exit
* Geben Sie das Kennwort ein, wenn Sie dazu aufgefordert werden.
* schließen Sie die Eingabeaufforderung

### Deinstallieren von Kaspersky Internet Security

Der Selbstschutz von KIS verhindert eine Deinstallation über Systemsteuerung --> Programme und Funktionen. Sie können KIS jedoch mit Hilfe eines speziellen Entfernungswerkzeugs deinstallieren. Das Entfernungswerkzeug kann mit NVDA unter Umständen nicht richtig bedient werden (siehe anmerkung unten). Sie können jedoch einen anderen Bildschirmleser wie Jaws für Windows verwenden, um das Entfernungswerkzeug zu bedienen. In der folgenden Anleitung wird davon ausgegangen, dass Jaws bereits gestartet wurde.

#### so deinstallieren Sie KIS mit Hilfe des Entfernungswerkzeugs

* Beenden Sie KIS mit Hilfe des Kommandozeilenprogramms AVP (siehe oben).
* Laden Sie sich das Entfernungstool für KIS von der [Webseite des Herstellers](http://support.kaspersky.com/de/common/service/1464#block1) herunter und rühren Sie es aus.
* akzeptieren Sie den Lizenzvertrag
* Wählen Sie das zu entfernende Produkt aus und lösen Sie das Captcha. Seien Sie beim Auslesen des Bildschirminhalts aufmerksam, weil sich die angezeigten (und einzugebenden) Zeichen des Captchas sehr großräumig verteilen können.
* ist das Captcha korrekt, so beginnt das Entfernungswerkzeug nach dem Betätigen des Schalters "löschen", Kaspersky Internet Security zu entfernen.
