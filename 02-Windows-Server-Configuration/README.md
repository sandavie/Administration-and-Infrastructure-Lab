# ⚙️ Windows Server Configuration

### Initial Setup

The virtual machine for the Windows Server was created and the ISO file was mounted and installed. 
- 64 GB virtual storage
- 2 CPU cores
- 4.15 GB of RAM

---

## 🖧 Network Configuration

The bridged and internal network adapters were configured with static IP addresses. The DNS of both adapters use the servers own internal IP. The bridged interface provides network connectivity while the internal interface is used for Active Directory and DNS.

🖼️ DC-01 Network Configuration

![DC-01 Network Configuration](../05-Screenshots/02-Windows-Server-Configuration/01-network-adapter-1-configuration.png)

![DC-01 Network Configuration 2](../05-Screenshots/02-Windows-Server-Configuration/02-network-adapter-2-configuration.png)

The commands `ping` and `ipconfig` were utilized to test and verify successful IP configuration, DNS resolution, and gateway reachability.

🖼️ DC-01 Network Verification

![DC-01 Network Verification 1](../05-Screenshots/02-Windows-Server-Configuration/03-server-network-verification.png)

![DC-01 Network Verification 2](../05-Screenshots/02-Windows-Server-Configuration/04-server-network-verification-2.png)

---

## 🔨 Server Roles 

The selected server roles were added along with the accompanying features and supplementary roles required for their functionality.

![DC-01 Server Roles](../05-Screenshots/02-Windows-Server-Configuration/05-server-roles.png)

## 🏢 Active Directory Domain Services Deployment

🖼️ Domain Controller

![Domain Controller](../05-Screenshots/02-Windows-Server-Configuration/06-domain-controller.png)

🖼️ Active Directory Domain Systems Deployment

![ADDS Deployment](../05-Screenshots/02-Windows-Server-Configuration/07-adds-deployment.png)

- NetBIOS name was set: `AD`
- AD DS database, log, and SYSVOL paths were left as default

---

## 🌐 DNS 
After the Active Directory Domain Services were configured and installed, the system was restarted. In the DNS Manager, the zone for the domain can be viewed and the name server record confirms the machine is hosting the zone. Then the DNS registration for the bridged adapter was removed and a series of commands were used to flush the DNS Resolver Cache and register the DNS resource records. 

🖼️ Active Directory DNS Zone

![AD DNS Zone](../05-Screenshots/02-Windows-Server-Configuration/08-ad-dns-zone.png)

🖼️ Bridged Adapter DNS Removed

![Bridged Adapter DNS Removed](../05-Screenshots/02-Windows-Server-Configuration/09-removed-bridged-dns.png)

🖼️ DNS Resolver Flush and Resource Record Registration

![DNS Resolver Flush and Resource Record Registration](../05-Screenshots/02-Windows-Server-Configuration/10-refresh-dns-registration.png)

🖼️ Active Directory DNS Zone

- Confirmation that the DNS registration for the bridged adapter was successfully removed

![AD DNS Zone 2](../05-Screenshots/02-Windows-Server-Configuration/11-ad-dns-zone-2.png)

- An `nslookup` command confirms the DNS server can resolve its domain to the appropriate internal IP

![nslookup](../05-Screenshots/02-Windows-Server-Configuration/12-nslookup.png)

- Google's public DNS server was set as a forwarder for queries outside the servers zones. This was then tested by disabling root hints and using `nslookup` to confirm external domains could still be resolved

![forwarder](../05-Screenshots/02-Windows-Server-Configuration/13-forwarder-configuration.png)

- A pointer record was created to enable reverse DNS lookups with the server's IP and this was verified with an `nslookup` command

![forwarder](../05-Screenshots/02-Windows-Server-Configuration/14-ptr-reverse-lookup.png)

🖼️ Reverse Lookup

![Reverse Lookup](../05-Screenshots/02-Windows-Server-Configuration/15-reverse-lookup-verification.png) 

---

## 📡 DHCP

- Server options were configured after DHCP role installation with the appropriate server IP and domain name
- Scope name was set: `DC Scope`
  
🖼️ Server Options

![Server Options Router](../05-Screenshots/02-Windows-Server-Configuration/16-server-options-router.png)

![Server Options NS](../05-Screenshots/02-Windows-Server-Configuration/17-server-options-ns.png) 

![Server Options DNS DN](../05-Screenshots/02-Windows-Server-Configuration/18-server-options-dnsdn.png) 

- IP address range was set to 10.0.0.100 - 10.0.0.200 to allow for assignment of static IP outside of that range as well as organization of dynamic IP assignment in the network

![Scope IP Range](../05-Screenshots/02-Windows-Server-Configuration/19-scope-ip-range.png) 

- Lease Duration was set to 8 days

🖼️ Domain Name DNS

![Domain Name DNS](../05-Screenshots/02-Windows-Server-Configuration/20-domain-name-dns.png) 

- DNS service was then successfully validated
- The scope was activated
- DHCP was then authorized

🖼️ Scope Activation

![Scope Activation](../05-Screenshots/02-Windows-Server-Configuration/21-scope-active.png) 
