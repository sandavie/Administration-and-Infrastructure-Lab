# ⚙️ Windows Server Configuration

### Initial Setup

The virtual machine for the Windows Server was created and the ISO file was mounted and installed. 
- 64 GB virtual storage
- 2 CPU cores
- 4.15 GB of RAM

---

## 🖧 Network Configuration

The bridged and internal network adapters were configured with static IP addresses. The DNS of both adapters use the servers own internal IP. The bridged interface provides network connectivity while the internal interface is used for Active Directory and DNS.

![DC-01 Network Configuration](../05-Screenshots/02-Windows-Server-Configuration/01-network-adapter-1-configuration.png)


