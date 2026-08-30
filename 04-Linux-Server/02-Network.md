# 🌐 Network

## 🖧 Network Configuration

The **yaml** file in `/etc/netplan/` was accessed and the static IP, DNS from the Windows Server (DC-01), and default gateway were configured.

![Network Configuration](../05-Screenshots/04-Linux-Server/02-Network/01-network-configuration.png)

The following commands were then utilized to safely apply the changes without breaking the SSH connection being used before the correct configuration was established:
- ```sudo netplan try```
- ```sudo netplan apply```

---

## 📡 Network Connectivity Testing

- `ip addr` verified the static IP change
- `ip route` verified the default gateway was reachable
- `resolvectl status` and the `dig` command verified DNS configuration, reachability, and resolver functionality

![Network Testing](../05-Screenshots/04-Linux-Server/02-Network/02-testing-verification.png)

SSH connection to server with new static IP

![SSH New IP](../05-Screenshots/04-Linux-Server/02-Network/03-ssh-new-ip.png)

The `Config` file was updated with the new IP
