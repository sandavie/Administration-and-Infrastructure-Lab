# 🛠️ Environment Setup

## 🏗️ Hardware and Software Specifications

#### Host Machine

- **CPU**: AMD Ryzen 7 3700X 8-Core Processor
- **RAM**: 16GB
- **Storage**: SSD with 551 GB Free
- **Operating System**: Windows 11
- **Virtualization Software**: VirtualBox

#### Physical Linux Server

- Dell OptiPlex 3060 MT
- **RAM**: 16GB
- **Storage**: 1TB HDD
- **ISO**: Ubuntu 26.04.1 LTS

#### Virtual Machines

| Machine Name  | VM Operating System  | Memory  | Processors | Network Adapter                    |
|---------------|----------------------|---------|------------|------------------------------------|
| DC-01         | Windows Server 2025  | 4.15 GB | 2          | Bridged Adapter & Internal Network |
| WIN10-CLIENT01| Windows 10           | 3 GB    | 2          | Internal Network                   |

- ISO: Acquired via Microsoft Evaluation Center

### 📋 Additional Tools and Specifications
- Domain: ad.example.com
- Internal Network Name: labnet1
- Visual Studio Code
- Powershell
- Command Prompt
- 7-Zip 26.02

---

## 🖧 Network Setup

## 🗺️ Overview

| Machine Name                    | IP Address(es) |
|---------------------------------|----------------|
| Windows Server (DC-01)          | 192.168.1.10<br>10.0.0.1  |     
| Windows Client (WIN10-CLIENT01) | DHCP           |
| Linux Server                    | 192.168.1.20   |
- Default Gateway: 192.168.1.1
- DNS: 192.168.1.10/10.0.0.1

---

## 🗺️ Project Outline
The documentation is organized to reflect the development process
1. Environment Setup
- Setup and verify essential hardware functionality
- Configure virtual machines (network adapters and operating system installation)
- Plan physical and network topology for entire lab
2. Windows Server Configuration
- Configure roles and deploy: ADDS, DNS, DHCP
- Configure and verify networking for both adapters (default gateway, static ip, DNS)
3. Active Directory Domain Services Setup & Management
- Create users, groups, and OUs with documentation for consistency across all systems in the environment
- Deploy group policy
- Implement file permissions
4. Windows Client Setup and Verification of Windows Services
- Join client to domain and test DNS, and DHCP functionality
- Test user and computer group policy and file permissions
5. Linux Server Setup
- Configure SSH and utilize rsync to send web application to linux server
- Network configuration and troubleshooting
- Create and manage users and groups matching earlier documentation from ADDS
- Configure and test file permissions
6. Web Application Deployment
  - Deploy and document web application service using systemd
