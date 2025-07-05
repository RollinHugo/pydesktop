# Installation

## 1. Arch install

- create a VM (**UEFI Mode**)
- run install script:

```shell
loadkeys fr
curl https://https://raw.githubusercontent.com/RollinHugo/tmp/refs/heads/main/README.md > run.sh
sh run.sh
```

- once done, you are still in chroot. Set passwords:

```shell
passwd
passwd myuser
exit
shutdown now
```


