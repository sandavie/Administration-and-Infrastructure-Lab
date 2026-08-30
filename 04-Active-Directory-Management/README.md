# 🏢 Active Directory Management
## Overview
In Active Directory Users and Computers, various organizational units, users, and groups were created to represent a company structure. The OUs are as follows:
- IT
- Managers
- Marketing
- Sales
In the IT organizational unit for instance there are users:
- Aristotle
- Robert Oppenheimer
- James Howlett
- Jean Grey
- Scott Summers
With the last three belonging to a group IT Staff. Each user was created with sophisticated credentials. The OUs have sub OUs Users and Computers to distinguish components for group policy that will be implemented. There are many other users and groups in the other OUs but those mentioned here will be present throughout the other systems in the lab environment as well.

---

## 🗂️ Active Directory Users and Computers

📷 Organizational Unit Creation

![OU Creation](../05-Screenshots/02-Windows-Server-Configuration/01-ou-creation.png)

📷 User Creation

![User Creation](../05-Screenshots/02-Windows-Server-Configuration/02-user-creation.png)

![User Creation 2](../05-Screenshots/02-Windows-Server-Configuration/03-user-creation-2.png)

📷 Group Creation

![Group Creation](../05-Screenshots/02-Windows-Server-Configuration/04-group-creation.png)

![Group Member Integration](../05-Screenshots/02-Windows-Server-Configuration/05-group-member-integration.png)

📷 Final Structure

![Final Structure](../05-Screenshots/02-Windows-Server-Configuration/06-final-structure.png)

---

## 📁 File Permissions

- A folder `data` was created and access to this folder was given to users that are members of the group `IT Staff`
- Their specific permissions were configured as well.

![Permissions](../05-Screenshots/02-Windows-Server-Configuration/07-permissions.png)

![Permissions 2](../05-Screenshots/02-Windows-Server-Configuration/08-permissions-2.png)

---

## 👥 Joining Client to Domain 
- Prior to joining the domain, network connectivity was verified with a series of commands in Command Prompt
- `ipconfig /all` shows the DHCP server, DNS, default gateway, IP from DHCP (within the IP address range configured in the DHCP setup) were all as expected  `ping` commands test network connectivity while the `nslookup` commands test DNS name resolution 

📷 DHCP Verification

![DHCP Verification](../05-Screenshots/02-Windows-Server-Configuration/9-dhcp-verification.png)

📷 DNS Verification

![DNS Verification](../05-Screenshots/02-Windows-Server-Configuration/10-dns-verification)

- The client was then joined to the domain using the Administrator account in Active Directory Domain Services.
- The client was then restarted and after the screenshots provided below the computer name was changed to `WIN10-CLIENT01`

![Joining Domain](../05-Screenshots/02-Windows-Server-Configuration/11-joining-domain.png)

![Joining Domain Confirmation](../05-Screenshots/02-Windows-Server-Configuration/12-joining-domain-confirmation.png)

- The computer account was then added to the `Computers` sub organizational unit of the IT organizational unit
- The credentials of Jean Grey were then used to login to the Windows 10 client

![Computer OU](../05-Screenshots/02-Windows-Server-Configuration/13-computer-ou.png)

📷 Domain Verification

![Domain Verification](../05-Screenshots/02-Windows-Server-Configuration/14-domain-verification.png)

---

