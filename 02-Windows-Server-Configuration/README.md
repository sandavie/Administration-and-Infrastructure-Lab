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

![DC-01 Network Configuration 2](../05-Screenshots/02-Windows-Server-Configuration/02-network-adapter-2-configuration.png)

The commands `ping` and `ipconfig` were utilized to test and verify successful IP configuration, DNS resolution, and gateway reachability.

![DC-01 Network Verification 1](../05-Screenshots/02-Windows-Server-Configuration/03-server-network-verification.png)

![DC-01 Network Verification 2](../05-Screenshots/02-Windows-Server-Configuration/04-server-network-verification-2.png)

## Server Roles 

The selected server roles were added along with the accompanying features and supplementary roles required for their functionality.

![DC-01 Server Roles](../05-Screenshots/02-Windows-Server-Configuration/01-network-adapter-1-configuration.png)
