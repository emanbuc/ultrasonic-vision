# Sessione remota SSH verso Raspberry

Per aprire una sessione remota è necessario conoscere hostaname oppure indirizzo IP del raspberry

Per impostazione predefinita il raspberry è configurato per connetersi alle reti wireless o cablate ed ottenre un indirizzo IP dinamico tramite DHCP quindi è meglio utilizzare l'hostname che invece rimane costante.

hostname predfinito configugrato durante l'installazione di Raspberry OS è "raspberrypi", ma può essere cambiato.

Da terminale Raspian OS:

 `hostname` per avere il nome host

`hostname -I` per avere l'indirizzo IP

Da terminale su PC windows:
`ping -a raspberrypi` per ottenere indirizzo ip

Nota: l'utente root di defualt di Raspian è username: pi password: raspberry

Nota2: nelle versioni recenti il server SSH su RaspberryOS è disabilitato per defaut e deve essere abilitato dal pannello `Preferenze-> configurazioni`

Vedi [SSH (Secure Shell) - Raspberry Pi Documentation](https://www.raspberrypi.org/documentation/remote-access/ssh/) nella documentazione ufficiale.

Dopo aver avviato il server SSH su Raspberry è possibile avviare la sessione remota da PC Linux/Windows.
