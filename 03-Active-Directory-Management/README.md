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

![OU Creation](../05-Screenshots/03-Active-Directory-Management/01-ou-creation.png)

📷 User Creation

![User Creation](../05-Screenshots/03-Active-Directory-Management/02-user-creation.png)

![User Creation 2](../05-Screenshots/03-Active-Directory-Management/03-user-creation-2.png)

📷 Group Creation

![Group Creation](../05-Screenshots/03-Active-Directory-Management/04-group-creation.png)

![Group Member Integration](../05-Screenshots/03-Active-Directory-Management/05-group-member-integration.png)

📷 Final Structure

![Final Structure](../05-Screenshots/03-Active-Directory-Management/06-final-structure.png)

---

## 📁 File Permissions

- A folder `data` was created and access to this folder was given to users that are members of the group `IT Staff`
- Their specific permissions were configured as well.

![Permissions](../05-Screenshots/03-Active-Directory-Management/07-permissions.png)

![Permissions 2](../05-Screenshots/03-Active-Directory-Management/08-permissions-2.png)

---

## 👥 Joining Client to Domain 
- Prior to joining the domain, network connectivity was verified with a series of commands in Command Prompt
- `ipconfig /all` shows the DHCP server, DNS, default gateway, IP from DHCP (within the IP address range configured in the DHCP setup) were all as expected  `ping` commands test network connectivity while the `nslookup` commands test DNS name resolution 

📷 DHCP Verification

![DHCP Verification](../05-Screenshots/03-Active-Directory-Management/09-dhcp-verification.png)

📷 DNS Verification

![DNS Verification](../05-Screenshots/03-Active-Directory-Management/10-dns-verification.png)

- The client was then joined to the domain using the Administrator account in Active Directory Domain Services.
- The client was then restarted and after the screenshots provided below the computer name was changed to `WIN10-CLIENT01`

![Joining Domain](../05-Screenshots/03-Active-Directory-Management/11-joining-domain.png)

![Joining Domain Confirmation](../05-Screenshots/03-Active-Directory-Management/12-joining-domain-confirmation.png)

- The computer account was then added to the `Computers` sub organizational unit of the IT organizational unit
- The credentials of Jean Grey were then used to login to the Windows 10 client

![Computer OU](../05-Screenshots/03-Active-Directory-Management/13-computer-ou.png)

📷 Domain Verification

![Domain Verification](../05-Screenshots/03-Active-Directory-Management/14-domain-verification.png)

---

## 📃 Group Policy 

- A GPO was created for the IT organizational unit which will be used to deploy software across computers in the OU

![GPO Creation](../05-Screenshots/03-Active-Directory-Management/15-gpo-creation.png)

- A folder `Software` was created in the C: disk with a 7-Zip installation file inside
- The folder was then shared with domain users and computers who were given read permissions
- For NTFS permissions, domain computers were given read and execute permissions 

📷 Software Folder Sharing

![Software Folder Sharing](../05-Screenshots/03-Active-Directory-Management/16-software-sharing.png)

📷 Share Permissions

![Share Permissions](../05-Screenshots/03-Active-Directory-Management/17-share-permissions.png)

📷 NTFS Permissions

![NTFS Permissions](../05-Screenshots/03-Active-Directory-Management/18-ntfs_permissions.png)

- The Windows client (**WIN10-CLIENT01**) had access to the file indicating the share permissions worked as intended
- The deployment method was then selected

![Client Permission Verification](../05-Screenshots/03-Active-Directory-Management/19-client-permission-verification.png)

📷 Software Deployment Configuration

![Software Deployment Configuration](../05-Screenshots/03-Active-Directory-Management/20-software-deployment-configuration.png)

![Software Deployment Configuration 2](../05-Screenshots/03-Active-Directory-Management/21-software-deployment-configuration-2.png)

- On the client, (**WIN10-CLIENT01**) `gpupdate /force` was ran and the system was subsequently restarted
- The software was successfully installed

![Installation Verification](../05-Screenshots/03-Active-Directory-Management/22-installation-verification.png)

### 🔑 Password Policy

- Using the default domain policy in group policy management, password policy was implemented
- Beyond what is already displayed in the visuals below the lockout duration was set to 20 minutes and the minimum password duration was momentarily set to 0 days to test the changes
- After password policy verification, `gpupdate /force` was ran

📷 Password Policy

![Password Policy](../05-Screenshots/03-Active-Directory-Management/23-password-policy.png)

📷 Group Policy Update

![Group Policy Update](../05-Screenshots/03-Active-Directory-Management/24-group-policy-update.png)

📷 Password Policy Verification

![Password Policy Verification](../05-Screenshots/03-Active-Directory-Management/25-password-policy-verification.png)

- A password of the same complexity as the initial password before the password policy chnages was attempted and failed

![Password Policy Verification 2](../05-Screenshots/03-Active-Directory-Management/26-password-policy-check.png)



