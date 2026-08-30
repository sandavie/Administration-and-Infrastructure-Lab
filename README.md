# 🖥️ Administration and Infrastructure Lab

## Overview

Welcome to my hybrid infrastructure home lab consisting of three core segments utilizing a combination of physical hardware and virtual machines. The Active Directory segment entails Windows Server, a Windows 10 Client, DNS, DHCP, users, OUs, GPO, permissions, as well as domain configuration & domain joining. The linux segment entails SSH, file permissions, user and group management, systemd services, and a Flask web application. The interconnected environment of these systems is demonstrated through network configuration and connectivity, DNS resolution, and consistent user and access management across the infrastructure.

---

## 📋 Table of Contents

### [Environment Setup](01-Environment-&-Network-Setup/README.md)

- Installation Media
- Hardware and Software Specification
  
### [Network Setup](01-Environment-&-Network-Setup/README.md#-network-setup)

- VirtualBox Network Configuration
- Windows Server Network Configuration
  
### [Windows Server Configuration](02-Windows-Server-Configuration/README.md)

- Active Directory Domain Services and Domain
- DNS
- DHCP
  
### [Active Directory Management](03-Active-Directory-Management/README.md)

- OUs-Users-Groups
- Joining Client to Domain
- Group Policy

### Linux Server
- [SSH](04-Linux-Server/01-SSH.md)
  - SSH Configuration
  - Rsync File Transfer
- [Network](04-Linux-Server/02-Network.md)
  - Network Configuration
  - Network Troubleshooting
- [User & Group Creation & Management](04-Linux-Server/03-User-Group-Permission-Management.md)
- [File Permissions](04-Linux-Server/03-User-Group-Permission-Management.md#%EF%B8%8F-file-permissions)
- [Web Application Service](04-Linux-Server/04-Web-Application-Service/README.md)
  - Description and Application Testing
  - systemd service
  - Application

### Screenshots
---
## 🎯 Objectives
- Administer an Windows Server with Active Directory Domain Services, DNS, and DHCP
- Construct network interconnected hybrid environment with physical and virtual machines
- Create and manage users, groups, and organizational units with access permissions and group policy
- Administer Ubuntu Linux server with SSH, networking, user/group management
- Creation and deployment of a web application as a service with systemd
