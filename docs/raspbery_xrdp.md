# Sessione Desktop Remoto da Windows a Raspian (Raspberry OS)

Raspberry collegato a rete WiFi. Host name "raspberrypi"

- ora è possibile eseguire sessioni remote con sistema di acquisizione montato

- per aprire una sessione remota è necessario conoscere hostaname oppure indirizzo IP del raspberry

  - il raspberry è configurato per connetersi alle reti wifi ed ottenre l'indiirzzo IP tramite DHCP quindi è meglio utilizzare l'hostname

  - da Raspian:

    `hostname` per avere il nome host

    `hostname -I` per avere l'indirizzo IP

- Da PC windows ping -a raspberrypi` per ottenere indirizzo ip

  - su Raspian `sudo apt-get install xrdp`

Xrdp is an open-source implementation of Microsoft’s proprietary RDP Server, the same protocol that most installations of Windows can connect to and be connected from.

The xrdp software replicates Microsoft’s RDP protocol so that other remote desktop clients can connect to your device. The software package even works with Microsoft’s own remote desktop client built into Windows.

Nota3: in Raspian Buster (ad oggi 28-dic-2020) c'è un bug nella configurazione di XRDP che ne impedisce la corretta esecuzione dopo il rebbot. In pratica c'è un problema con i diritti di scrittura del file di log. Le soluzioni sono due: 

- modificare i permessi del file

Disable automatic start at boot time (`systemctl disable xrdp`)

```
touch /var/log/xrdp.log

chown xrdp:adm /var/log/xrdp.log

chmod 640 /var/log/xrdp.log

systemctl start xrdp

systemctl status xrdp
```

You may wish to add this to `/etc/crontab @reboot`

- modificare il percorso dle file di log nel file di configurazione /etc/xrdp/xrdp.ini

  ```
  LogFile=/tmp/xrdp.log
  ```

Nota4: c'è anche ul altro problema di configurazione di xRDP:

vedi [RDP on Raspberry Pi | I.T. Plays Well With Flavors](https://it.playswellwithflavors.com/2020/04/24/rdp-on-raspberry-pi/)

By default Xrdp uses the `/etc/ssl/private/ssl-cert-snakeoil.key` file which is readable only by users that are members of the “ssl-cert” group. You’ll need to add the user that runs the Xrdp server to the `ssl-cert` group.

```bash
sudo adduser xrdp ssl-cert 
```

![image-20201228150623568](media\rdp_raspberry.png)



![image-20201228150825761](media\remote_desktop_session_python.png)



Ora è possibile utilizzare l'ambiente desktop per sviluppo e debug remoto anche dopo il riavvio del Raspberry

Nota5: dalla sessione remota desktop sembra non funzionare l'arresto ed il riavvio del sistema. è necessario eseguire da terminale (o da sessione ssh) i comandi `sudo halt` e `sudo reboot`
