import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')
django.setup()

from main_app.models import Domain, Subdomain, Control

# Data to populate the database
data = [
    {
        "name": "1 - Cybersecurity Governance",
        "subdomains": [
            {
                "name": "1-1 Cybersecurity Strategy",
                "controls": [
                    {
                        "name": "Define Cybersecurity Strategy",
                        "description": "Establish a strategy for cybersecurity governance.",
                        "section": "1-1",
                        "purpose": "To ensure alignment of cybersecurity goals with business objectives.",
                        "implementation_steps": """
1. Develop a strategy framework.
2. Align cybersecurity goals with business strategy.
3. Obtain executive buy-in.
""",
                        "examples": """
Example 1: Strategy for securing critical infrastructure.
Example 2: Cybersecurity governance framework for financial institutions.
""",
                        "tools": """
Tool 1: Cybersecurity Strategy Templates.
Tool 2: Risk Assessment Tools.
""",
                        "deliverables": """
Deliverable 1: Cybersecurity Governance Strategy.
Deliverable 2: Risk Assessment Report.
""",
                    },
                ],
            },
        ],
    },
    {
        "name": "2 - Cybersecurity Defense",
        "subdomains": [
            {
                "name": "2-1 Asset Management",
                "controls": [
                    {
                        "name": "2-1-1: Define, Document, and Approve Cybersecurity Requirements",
                        "description": "Establish a Documnet to define the scope, retention, and monitoring of Secuity Needs.",
                        "section": "2-1-1",
                        "purpose": "Establish a Document to define the scope, retention, and Secuity Needs.",
                        "implementation_steps": """
1.	Identify cybersecurity requirements for asset types, lifecycle stages, and roles.
2.	Classify assets based on sensitivity and criticality.
3.	Document requirements in an Asset Management Policy or Standard.
4.	Obtain executive approval for these requirements.
""",
                        "examples": """
Asset Type	Lifecycle Stage	Cybersecurity Requirements	Responsible Role
Servers	Deployment	Hardening with baseline configurations.	IT Security Team
Applications	Operation	Regular vulnerability scans, patch management, logging, and backup.	DevOps Team
Customer Data	Processing/Retention	Data encryption (at rest and in transit), access control policies.	Data Protection Officer
Workstations	Decommissioning	Secure wipe before disposal.	IT Support
Asset Name	Description	Classification	Criticality Level
Customer Database	Contains personal data	Restricted	High
Office Workstations	Employee laptops and desktops	Internal Use	Medium
Public Website	Company marketing website	Public	Low

""",
                        "tools": """
Tool 1: Documentation Tools: Microsoft Word, Google Docs.
""",
                        "deliverables": """
Deliverable 1: Approved cybersecurity policy or standard for asset management.
Deliverable 2: Signed approval (e.g., email confirmation, electronic signature).
""",
                    },
                                      {
                        "name": "2-1-2: Implement Cybersecurity Requirements",
                        "description": "Establish a policy to define the scope, retention, and monitoring of event logs.",
                        "section": "2-1-2",
                        "purpose": "Establish a policy to define the scope, retention, and monitoring of event logs.",
                        "implementation_steps": """
1.Classify all assets and encode them based on approved classifications.
2.	Document assets in a centralized inventory (e.g., CMDB).
3.	Establish and implement procedures for handling assets per classification.
""",
                        "examples": """
Asset Name	Description	Classification	Criticality Level
Customer Database	Contains personal data	Restricted	High
Email Server	Organizational email system	Internal Use	High
Marketing Website	Public-facing website	Public	Low
Employee Workstations	Laptops and desktops	Internal Use	Medium
.
""",
                        "tools": """
Tool 1: Inventory Management: ServiceNow, SolarWinds, Lansweeper.
Tool 2:Classification and Tagging: Microsoft Information Protection, Asset Panda.
Tool 3:Monitoring: Splunk, Qualys Asset Inventory.
Tool 4:Documentation: Microsoft Word, SharePoint for procedure documentation. Expected 
""",
                        "deliverables": """
Deliverable 1:Asset Inventory Record:
•	 A spreadsheet or automated CMDB record that lists all assets, their classifications, owners, and handling requirements.
Deliverable 2: Procedures Document:
•	A formalized document describing handling requirements for each asset classification (e.g., Restricted, Internal Use).
Deliverable 3: Evidence of Implementation:
•	Screenshots or reports from tools used (e.g., ServiceNow CMDB, Microsoft Information Protection).
•	Logs of assets classified and tagged.

""",
                     },
                      {
                        "name": "2-1-3: Define, Document, and Approve Acceptable Use Policy",
                        "description": "",
                        "section": "2-1-3",
                        "purpose": "",
                        "implementation_steps": """
1.	Develop an Acceptable Use Policy (AUP) for assets.
2.	Include specific rules for access, usage, and consequences for violations.
3.	Communicate the policy to employees and stakeholders.
4.	Obtain executive approval.
""",
                        "examples": """
Develop the Acceptable Use Policy
•	Define acceptable use rules for information and technology assets.

""",
                        "tools": """
Tool 1: Policy Templates: Acceptable Use Policy Template.
Tool 2:Communication Tools: Microsoft Teams, email

""",
                        "deliverables": """
                        Policy Elements:
1.	Specific Regulations for Access and Use of Assets:
o	Only authorized users are permitted to access organizational data and technology assets.
o	Personal use of work devices must be limited and comply with organizational rules.
2.	Unacceptable Use:
o	Using organizational email for sending personal bulk emails or spam.
o	Installing unauthorized software or accessing illegal websites.

Expected Deliverables:
•	Approved Acceptable Use Policy (AUP).
•	Evidence of communication (e.g., emails, acknowledgment logs).
•	Signed approval by executive management.
""",
                     },
                      {
                        "name": "2-1-4: Implement Acceptable Use Policy",
                        "description": "",
                        "section": "2-1-4",
                        "purpose": "",
                        "implementation_steps": """
1.	Ensure all employees sign and acknowledge the AUP.
2.	Communicate the AUP through official channels.
3.	Implement monitoring mechanisms to detect violations.
Example Implementation:
1.	Distribute the AUP to all employees via email with a link for acknowledgment.
2.	Use a digital signature tool (e.g., DocuSign, Adobe Sign) to collect signatures.
3.	For employees without access to digital tools, provide physical copies and collect signed forms.
""",
                        "examples": """
Ensure Acknowledgment of the Acceptable Use Policy (AUP)
•	All employees and stakeholders must review and formally acknowledge the policy.

""",
                        "tools": """
Tool1: Employee Acknowledgment: DocuSign, HR portals (e.g., BambooHR).
Tool2: Monitoring Tools: Splunk, CrowdStrike.


""",
                        "deliverables": """
                        Policy Elements:
1.	Specific Regulations for Access and Use of Assets:
o	Only authorized users are permitted to access organizational data and technology assets.
o	Personal use of work devices must be limited and comply with organizational rules.
2.	Unacceptable Use:
o	Using organizational email for sending personal bulk emails or spam.
o	Installing unauthorized software or accessing illegal websites.

Expected Deliverables:
•	Action plan for implementing the AUP.
•	Evidence of employee acknowledgment.
•	Monitoring and compliance records.
""",
                     },
                    {
                        "name": "2-1-5: Classify, Label, and Handle Assets",
                        "description": "",
                        "section": "2-1-5",
                        "purpose": "",
                        "implementation_steps": """
1.	Identify all assets (infrastructure, networks, applications, etc.).
2.	Document assets in a centralized register with attributes (e.g., owner, criticality).
3.	Assign labels or codes to assets based on classification.
4.	Handle assets as per approved procedures and regulatory requirements.
""",
                        "examples": """
Identify All Information and Technology Assets
•	Collaborate with departments to list all assets, including:
o	Infrastructure: Servers, storage systems.
o	Applications: Business software, databases.
o	Networks: Routers, switches.
o	End-User Devices: Workstations, laptops.
o	Peripherals: Printers, scanners.




Classify Assets Based on Sensitivity and Criticality
•	Assign a classification level to each asset using predefined categories:
o	Public: Accessible without restrictions.
o	Internal Use: Confidential to employees.
o	Restricted: Highly sensitive; access limited.

Example Output:
Asset Name	Type	Owner	Classification	Criticality	Lifecycle Stage
Database Server	Server	IT Manager	Restricted	High	Operation
Public Website	Application	Marketing Lead	Public	Low	Maintenance

""",
                        "tools": """
Tool 1: Asset Classification Tools: Microsoft Information Protection.
Tool 2: Inventory Management: ServiceNow, Lansweeper.
Tool 3: Labeling Tools: QR/barcode systems, automated tagging solutions.
""",
                        "deliverables": """
Deliverable 1: Up-to-date asset register (e.g., Excel, CMDB).
Deliverable 2: Action plan for asset classification and labeling.
Deliverable 3: Evidence of classification, labeling, and compliant handling

""",
                    },
                     {
                        "name": "2-1-6: Review Cybersecurity Requirements Periodically",
                        "description": "",
                        "section": "2-1-6",
                        "purpose": "",
                        "implementation_steps": """
1.	Define a review schedule for asset management cybersecurity requirements.
2.	Conduct periodic reviews and update requirements based on regulatory changes.
3.	Document updates and obtain executive approval for changes.

""",
                        "examples": """
Example1: Define a Review Schedule
•	Establish a documented and approved plan for periodic reviews, considering:
o	Organizational needs.
o	Regulatory updates.
Example2: Review Schedule:
•	Quarterly review for restricted assets.
•	Annual review for all assets.
•	Ad hoc reviews triggered by:
Example3: Conduct a Review of Cybersecurity Requirements
•	Evaluate the implementation of existing cybersecurity requirements for assets.
•	Identify areas for improvement based on:
•	Compliance reports.
•	Incident response logs.

""",
                        "tools": """
Tool 1:Compliance Tools: RSA Archer, MetricStream.
Tool 2:Policy Review Tools: Microsoft SharePoint, Confluence.
""",
                        "deliverables": """
Deliverable 1: Review Schedule Document
Deliverable 2: Compliance Assessment Report
Deliverable 3: Updated Policy Document
Deliverable 4: Change Log
Deliverable 5: Compliance Evidence
Deliverable 6: Approval Record
""",
                     },
                ],
                "name": "2-2 Identity and Access Management",
                "controls": [
                    {
                        "name": "2-2-1 Define and Approve Identity and Access Management Cybersecurity Requirements",
                        "description": "",
                        "section": "2-2-1",
                        "purpose": "Develop an IAM policy detailing account management, access levels, password policies, and review mechanisms.",
                        "implementation_steps": """
1.	Develop an IAM Policy including:
o	Granting, revoking, and reviewing access.
o	Managing privileged access accounts.
o	Password management standards (complexity, expiration).
o	Remote access guidelines.
2.	Obtain formal approval from executive management.
""",
                        "examples": """
Example1: Policy Highlights:
User Account Management: Only authorized users can access organizational systems.
Password Policy: Minimum length of 12 characters, complexity rules, and expiration every 90 days.
Privileged Access: Restricted to specific personnel and monitored for compliance.
Remote Access: Multi-factor authentication (MFA) required for VPN access.
""",
                        "tools": """
Tool 1:Policy Templates: ISO 27001 IAM Policy Template.
Tool 2:Documentation: Microsoft Word.
""",
                        "deliverables": """
Deliverable 1:Signed approval from leadership
Deliverable 2:Approved IAM Policy (hard copy or electronic).
""",
                     },
                               {
                        "name": "2-2-2 Implement IAM Requirements",
                        "description": "",
                        "section": "2-2-2",
                        "purpose": "Ensure the IAM policy is enforced across systems and processes",
                        "implementation_steps": """
1.	User Authentication:
o	Enforce unique IDs and strong passwords.
o	Password management based on the organization's password policy.
2.	Authorization Management:
o	Grant access based on least privilege and need-to-know principles.
3.	Remote Access:
o	Configure VPNs with MFA for secure connections.
4.	Access Updates:
o	Revoke access immediately when roles change or employment ends.

""",
                        "examples": """
Example1:   Assign unique IDs for all employees based on their job numbers.
Example2: Enforce password policies:
•	Minimum password length: 12 characters.
•	Password expiration: Every 90 days.
•	Account lockout: After 5 failed login attempts.
Example3: Use Single Sign-On (SSO) for integrated authentication.
Example4: A finance department employee is only granted access to financial applications.
Exampl5: HR informs IT when an employee resigns:
Example6: IT revokes all access to systems (e.g., email, network shares) within 24 hours.
""",
                        "tools": """
Tool 1:Identity Providers: Okta, Azure Active Directory (AD).
Tool 2:Remote Access: Cisco AnyConnect, Palo Alto GlobalProtect.
Tool 3:Password Management: CyberArk, LastPass Enterprise
""",
                        "deliverables": """
Deliverable 1:Action plan for IAM implementation.
Deliverable 2:Evidence of applied controls (e.g., AD configurations, VPN settings).

""",
                     },
                               {
                        "name": " 2-2-3 Specific IAM Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                           
                                        {
                        "name": " 2-2-3-1 User Authentication (Username and Password)",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "Enforce secure username/password practices.",
                        "implementation_steps": """
1.	Assign unique identifiers for all users.
2.	Configure password policies.

""",
                        "examples": """
Usernames are based on employee IDs or a combination of first and last names (e.g., EMP12345).
Configure a password policy adhering to best practices:
•	Minimum length: 12 characters.
•	Complexity: Include uppercase, lowercase, numbers, and special characters.
•	Expiration: Passwords expire every 90 days.
•	History: Prevent reuse of the last 5 passwords.
•	Lockout: Lock accounts after 5 failed login attempts.

""",
                        "tools": """
Tool1:User Management: Active Directory, JumpCloud.
Tool2:Password Enforcement: Azure AD Password Protection.


""",
                        "deliverables": """
Deliverable 1:Approved password policy document.
Deliverable 2:Evidence of password settings (e.g., screenshots from AD).

""",
                     },
                     
           {
                        "name": "2-3-1 Periodic Review of Information System and Processing Facilities Protection",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "Ensure that cybersecurity measures protecting information systems and processing facilities are periodically reviewed, updated, and aligned with organizational needs and industry standards.",
                        "implementation_steps": """
                        1.	Define Review Requirements:
o	Identify the scope of the review, including systems, devices, and applications covered by the policy.
o	Specify roles and responsibilities for conducting reviews.
2.	Review Protection Mechanisms:
o	Evaluate the effectiveness of implemented protection measures such as:
	Next-Generation Firewalls (NGFW).
	Endpoint Detection and Response (EDR).
	Security Information and Event Management (SIEM) systems.
o	Check for updated configurations and alignment with modern cybersecurity standards.
3.	Review Vulnerability Assessment Procedures:
o	Verify the schedule and results of vulnerability assessments.
o	Ensure findings are addressed in a timely manner.
4.	Review External Storage Media Usage:
o	Assess compliance with the policy restricting external media use.
o	Ensure encryption and access control measures are implemented.
5.	Patch Management Review:
o	Audit patch logs for consistency and ensure all critical patches have been applied.
o	Verify the effectiveness of the routine for identifying and applying patches.
6.	Time Synchronization Review:
o	Verify synchronization across all systems and devices with defined time sources.
7.	Update Policies and Procedures:
o	Revise cybersecurity policies based on review findings, new threats, or regulatory changes.
o	Obtain formal approval for updated policies.

""",
                        "examples": """
Develop a Review Schedule and Plan:
1.	Conduct quarterly reviews of all cybersecurity measures or after significant changes (e.g., system upgrades, new regulations).
2.	Define roles for review processes:
o	IT Teams: Review system configurations (e.g., firewalls, EDR).
o	Security Teams: Audit patch management and malware scanning schedules.
3.	Review systems and assets such as:
o	Applications (e.g., ERP, email systems).
o	Infrastructure (e.g., servers, databases).
4.	Collaborate with stakeholders to resolve issues identified during reviews.

""",
                        "tools": """

1.	Review Management:
o	Microsoft Planner, Jira for tracking review schedules and progress.
2.	Compliance and Monitoring:
o	Splunk, ManageEngine AD for system auditing.
3.	Access Review:
o	Okta, Active Directory for managing and auditing system access.
4.	Patch Management:
o	Ivanti, Microsoft SCCM for automated patch tracking.


""",
                        "deliverables": """
1.	Periodic Review Reports:
o	Documented findings and action plans from cybersecurity reviews.
2.	Updated Cybersecurity Policies:
o	Revised policies reflecting the latest security standards and practices.
3.	Evidence of Implementation:
o	Logs from reviewed systems and assets.
o	Screenshots of updated configurations for firewalls, EDR, and SIEM systems.
4.	Approval Documentation:
o	Signed approval of updated policies and procedures by executive management.

""",
                     },
                     
           {
                        "name": "2-3-2 Implementing Cybersecurity Requirements for Information Systems and Processing Facilities",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "Ensure the implementation of advanced cybersecurity measures and practices to protect information systems and processing facilities, ensuring availability, reliability, and compliance with organizational policies",
                        "implementation_steps": """

1.1 Redundancy and Failover Mechanisms
1.	Set up redundant systems (e.g., servers, firewalls, network devices) to ensure continuity in case of system failure.
2.	Implement load balancers to distribute traffic across multiple resources and enhance system availability.
1.2 Regular Updates and Patch Management
1.	Use centralized solutions such as:
o	Microsoft WSUS or ManageEngine Patch Manager Plus for automating patch management.
2.	Establish a schedule for checking and applying updates to devices, systems, and applications.
1.3 Comprehensive Backup Strategy
1.	Create regular backups for critical systems and data:
o	Maintain both on-site and off-site backups for disaster recovery.
2.	Test backup restoration processes periodically to ensure quick and reliable recovery.
1.4 High Availability (HA) Configurations
1.	Configure critical systems (e.g., databases, web servers) for High Availability (HA) to minimize downtime.
2.	Implement clustering technologies to ensure seamless failover during system failures.
1.5 Virus Protection Systems
1.	Deploy comprehensive virus protection solutions such as:
o	Symantec Endpoint Protection.
o	Sophos Intercept X.
o	McAfee Total Protection.
2.	Ensure all systems are equipped with up-to-date antivirus software.
1.6 Monitoring Mechanisms
1.	Implement tools for real-time monitoring of system performance, threats, and security breaches.
1.7 Performance Testing
1.	Conduct regular performance tests of security solutions to ensure they handle expected loads effectively.
2.	Simulate high-traffic scenarios to test system reliability and responsiveness.
1.8 Incident Response and Recovery Plans
1.	Develop and document an Incident Response Plan outlining:
o	Procedures for identifying, responding to, and recovering from incidents.
2.	Conduct periodic drills to evaluate plan effectiveness.
1.9 External Storage Media Restrictions
1.	Develop a policy restricting the use of external storage media:
o	Specify exceptions and approval procedures.
2.	Restrict access to external media connections to authorized personnel using role-based permissions.
1.10 Time Synchronization
1.	Select a Time Synchronization Protocol (e.g., NTP, SNTP) for accurate system clock synchronization.
2.	Use reliable time sources such as:
o	Saudi Standards, Metrology, and Quality Organization (time.saso.gov.sa).
o	King Abdulaziz City for Science and Technology (time.isu.net.sa).

""",
                        "examples": """

1.	Redundancy and High Availability:
o	Deploy a load balancer like F5 Networks or HAProxy to handle traffic distribution.
o	Use clustering technologies like Microsoft SQL Server Always On for database availability.
2.	Backup Strategy:
o	Implement Veeam Backup & Replication for seamless data backups and recovery.
o	Store backups in cloud solutions such as AWS S3 or Azure Blob Storage.
3.	Virus Protection:
o	Symantec Endpoint Protection installed on all systems with daily updates scheduled.
4.	External Media Management:
o	Use Endpoint Protector to block unauthorized USB devices and allow only approved ones.
5.	Time Synchronization:
o	Configure servers to sync with time.saso.gov.sa using NTP protocol.

""",
                        "tools": """

1.	Redundancy and High Availability:
o	Load Balancers: F5 Networks, HAProxy.
o	Clustering: VMware vSphere HA, Microsoft SQL Server Always On.
2.	Patch Management:
o	ManageEngine Patch Manager Plus, Microsoft WSUS, Ivanti Patch Management.
3.	Virus Protection:
o	Symantec Endpoint Protection, Sophos Intercept X, Bitdefender GravityZone.
4.	Backup Solutions:
o	Veeam Backup & Replication, AWS Backup, Azure Backup.
5.	Endpoint Security:
o	McAfee Endpoint Security, Symantec Data Loss Prevention.
6.	Time Synchronization:
o	NTP Protocol, SNTP Protocol.


""",
                        "deliverables": """
1.	Implementation Evidence:
o	Documentation confirming the implementation of redundancy, HA configurations, and monitoring mechanisms.
2.	Virus Protection Reports:
o	Up-to-date list of deployed virus protection systems with installation records.
3.	Backup Validation:
o	Logs and reports from successful backup and restoration tests.
4.	Patch Logs:
o	Evidence showing applied patches for all devices, systems, and applications.
5.	External Media Management:
o	Policy restricting external storage use and logs of approved exceptions.
6.	Time Synchronization Reports:
o	Configuration evidence showing reliable time synchronization for all systems.

""",
                     },
                     
           {
                        "name": " 2-3-3 The cybersecurity requirements for protecting information systems and information processing facilities must include at least the following:",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": "2-3-3-1 Advanced Management of Malware and Virus Protection",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "Ensure robust, advanced, and up-to-date malware and virus protection for all servers, workstations, and organizational systems to safeguard against threats, including Advanced Persistent Threats (APTs).",
                        "implementation_steps": """
1.1 Asset Inventory and Categorization
1.	Conduct a comprehensive asset inventory:
o	Include all workstations, servers, systems, and applications.
2.	Categorize assets by domain:
o	Production, Testing, and Development environments.
3.	Organize assets based on their domains and determine associated security risks.
1.2 Define Security Risks and Select Solutions
1.	Identify security risks for each asset and evaluate if current protections address these risks.
2.	Select appropriate solutions to cover remaining vulnerabilities:
o	Endpoint Protection Platforms (EPP) such as Symantec Endpoint Protection or McAfee Endpoint Security.
o	Endpoint Detection and Response (EDR) tools like Carbon Black, Microsoft Defender for Endpoint, or SentinelOne.
o	Antivirus solutions including Bitdefender GravityZone, Sophos Intercept X, or Norton 360 for Business.
o	Threat intelligence services like Recorded Future or ThreatConnect to proactively identify and mitigate risks.
1.3 Plan the Deployment
1.	Develop an implementation strategy, including:
o	A detailed timeline with phases (e.g., pilot testing, full deployment).
o	Assignment of roles and responsibilities for the deployment team.
2.	Outline hardware and software requirements for chosen protection systems.
1.4 Pilot Testing
1.	Select a small subset of workstations and servers for initial testing.
2.	Monitor performance and address any usability or configuration issues.
3.	Adjust installation or configurations as needed based on feedback.
1.5 Full Deployment
1.	Utilize a centralized deployment strategy:
o	Use tools like Microsoft Endpoint Configuration Manager or Windows Server Update Services (WSUS).
2.	Install protection systems manually or through automation across all devices.
3.	Confirm the systems are functioning correctly and regularly receiving updates.
4.	Validate that all configurations and security policies are applied correctly.
1.6 Monitoring and Maintenance
1.	Implement continuous monitoring mechanisms to track system performance and detect anomalies.
2.	Regularly update protection systems and generate reports on system status and incident response.
1.7 Documentation
1.	Maintain detailed records of:
o	The deployment process, configurations, and adjustments.
o	Reports on incidents, updates, and the status of the protection systems.

""",
                        "examples": """
1.	Endpoint Protection Platforms (EPP):
o	Deploy Symantec Endpoint Protection organization-wide to block malware and phishing attempts.
o	Use McAfee Endpoint Security for comprehensive antivirus and anti-malware protection.
2.	EDR Solutions:
o	Install Microsoft Defender for Endpoint to monitor suspicious activities and automate threat responses.
o	Use SentinelOne for advanced malware detection and rollback capabilities.
3.	Threat Intelligence:
o	Leverage Recorded Future to gather actionable intelligence about APT campaigns.
o	Use ThreatConnect to analyze threat data and strengthen defenses.
4.	Centralized Deployment:
o	Implement protection systems using Microsoft Endpoint Configuration Manager to ensure consistency and scalability.
o	Use WSUS for automated software updates across all servers and workstations.

""",
                        "tools": """
1.	Endpoint Protection Platforms (EPP):
o	Symantec Endpoint Protection, McAfee Endpoint Security.
2.	Endpoint Detection and Response (EDR):
o	Carbon Black, SentinelOne, Microsoft Defender for Endpoint.
3.	Threat Intelligence:
o	Recorded Future, ThreatConnect.
4.	Deployment and Update Tools:
o	Microsoft Endpoint Configuration Manager, Windows Server Update Services (WSUS).
5.	Monitoring Tools:
o	Splunk, ManageEngine.


""",
                        "deliverables": """
1.	Documentation:
o	Policies and procedures documenting the deployment and management of malware protection systems.
2.	Protection System Reports:
o	A list of installed antivirus and endpoint protection systems with evidence of APT monitoring capabilities.
3.	Deployment Records:
o	Logs and screenshots of protection systems deployed across all servers, workstations, and systems.
4.	Update Reports:
o	Evidence of periodic updates to protection systems and their successful application.
5.	Monitoring Reports:
o	Regularly generated reports on the status of malware protection systems, including incidents and resolutions.

""",
                     },
                     
           {
                        "name": "2-3-3-2 Restricted Use and Secure Handling of External Storage Media",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To restrict the use of external storage media and ensure secure handling, minimizing risks associated with data breaches, malware, and unauthorized access.",
                        "implementation_steps": """
1.1 Pre-Use Check Mechanisms
1.	Scan for Malware:
o	Use antivirus and antimalware tools to automatically scan external storage devices upon connection.
o	Implement tools like Symantec Endpoint Protection or McAfee Endpoint Security for automated scanning.
2.	Data Integrity Checks:
o	Verify data integrity using checksums or hashes to ensure files haven't been altered or corrupted.
o	Record all scans in an audit log to track storage media usage.
3.	Logging Access:
o	Maintain logs of all external storage device access, detailing:
	Who accessed the device.
	When it was accessed.
	Actions performed on the device.
1.2 Data Erasure Procedures
1.	Define procedures for securely erasing data after storage media use:
o	Use tools such as DBAN (Darik's Boot and Nuke) or Eraser for secure data wiping.
2.	Schedule regular erasure of unused or outdated data on external storage devices.
1.3 Encryption for External Storage
1.	Mandate the use of encryption for all external storage devices.
o	Protect data at rest using encryption tools such as BitLocker or VeraCrypt.
2.	Ensure that encryption policies cover:
o	Portable USB devices.
o	External hard drives.
o	Other removable media.
1.4 Approval Procedures
1.	Define approval procedures for external storage media use:
o	Require submission of requests, including:
	Reason for use.
	Start and end date for access.
	Handling of stored data (e.g., verification and erasure after use).
o	Approvals may be handled via email, internal systems, or formal documentation.
1.5 Role-Based Access Restrictions
1.	Restrict access to external storage media using role-based access control (RBAC):
o	Implement restrictions through a privileged access management system.
o	Ensure external storage functionality is disabled for unauthorized users by default.

""",
                        "examples": """

1.	Pre-Use Malware Scanning:
o	Automatically scan USB devices with McAfee Endpoint Security when connected to workstations or servers.
o	Use logging mechanisms to track and audit usage.
2.	Data Erasure Tools:
o	Securely erase data from external storage devices using tools like DBAN for full disk wiping or Eraser for targeted file deletion.
3.	Encryption:
o	Mandate encryption for USB drives using BitLocker or VeraCrypt to protect sensitive data.
4.	Access Restrictions:
o	Use Active Directory Group Policies to disable external storage functionality for unauthorized users.

""",
                        "tools": """

1.	Antivirus and Antimalware Scanning:
o	Symantec Endpoint Protection, McAfee Endpoint Security.
2.	Data Wiping Tools:
o	DBAN (Darik's Boot and Nuke), Eraser.
3.	Encryption Tools:
o	BitLocker, VeraCrypt.
4.	Access Management:
o	Active Directory Group Policies, Microsoft Intune.
5.	Audit and Logging:
o	Splunk, ManageEngine ADAudit Plus


""",
                        "deliverables": """
1.	Policies and Procedures:
o	Approved policy defining restrictions and secure handling of external storage media.
2.	Audit Logs:
o	Logs showing usage, scanning, and erasure activities for external storage media.
3.	Encryption Evidence:
o	Screenshots or configuration files proving encryption is enabled on external storage devices.
4.	Access Control Reports:
o	Evidence from privileged access management systems (e.g., screenshots) showing restricted external storage functionality for unauthorized users.
5.	Data Erasure Reports:
o	Documentation of secure data wiping activities for external storage devices.

""",
                     },
                     
           {
                        "name": "2-3-3-3 Patch Management for Information Systems, Software, and Devices",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To ensure the timely implementation and management of patches across all systems, software, and devices, minimizing vulnerabilities and ensuring operational stability.",
                        "implementation_steps": """
1.1 Define and Document Patch Management Policies
1.	Create a patch management policy that:
o	Identifies the scope of systems to be patched (workstations, operating systems, network devices, databases, and applications).
o	Establishes timelines for applying patches based on criticality and priority.
2.	Integrate change management procedures into patch management:
o	Require formal approval for all patches, with tracking via email, internal systems, or documented forms.
1.2 Monitor and Identify Required Patches
1.	Use patch management tools to:
o	Monitor vendor alerts for new patches and updates.
o	Track vulnerability notifications from cybersecurity systems and third-party alerts.
2.	Conduct regular vulnerability assessments to identify missing patches.
1.3 Develop an Implementation Strategy
1.	Categorize patches based on criticality:
o	High Priority: Apply within 24-48 hours (e.g., zero-day vulnerabilities).
o	Medium Priority: Apply within 1-2 weeks.
o	Low Priority: Apply during regular maintenance cycles.
2.	Schedule patch deployments to minimize downtime.
1.4 Test and Approve Patches
1.	Test patches in a controlled environment (e.g., sandbox or staging systems).
2.	Document the patch testing process, including:
o	The patch's impact on systems.
o	Any observed issues during testing.
3.	Obtain formal approvals through change management systems.
1.5 Deploy Patches
1.	Deploy patches across all relevant systems using:
o	Automated patch management tools for large-scale updates.
o	Manual installation for critical or custom configurations.
2.	Validate deployment by confirming successful updates on all devices.
1.6 Review and Maintain Patch Implementation
1.	Periodically review patch logs to ensure:
o	All devices, systems, and applications are up to date.
o	Patches have been implemented within the defined timeframes.
2.	Produce reports to track patch compliance and resolve discrepancies.

""",
                        "examples": """

1.	High Priority Patch Deployment:
o	A zero-day vulnerability is detected in a widely used operating system. The organization applies the patch within 24 hours using Microsoft WSUS.
2.	Testing Patches:
o	Before deploying a database update, the IT team uses a staging environment to test compatibility with existing applications.
3.	Approval Process:
o	Patches for critical network devices are submitted through an internal system for approval, including details of the patch's impact and deployment schedule.
o	Jira Service Management or ServiceNow: For tracking patch approvals and implementations.
""",
                        "tools": """

1.	Patch Management Tools:
o	Microsoft WSUS: For managing Windows updates.
o	ManageEngine Patch Manager Plus: For multi-platform patching.
o	Ivanti Patch Management: For automated deployment and tracking.
2.	Monitoring and Alerts:
o	Nessus: For vulnerability assessments.
o	Qualys: For tracking vulnerabilities and patch requirements.
3.	Change Management:


""",
                        "deliverables": """

1.	Policy Documentation:
o	Approved patch management policy, including integration with change management.
2.	Approval Evidence:
o	Documentation of change management approvals for patches, including emails or system logs.
3.	Patch Implementation Reports:
o	Logs showing the scope and status of patch deployments.
o	Screenshots of patch updates applied within the defined timelines.
4.	Vulnerability Tracking Reports:
o	Reports identifying missing patches and timelines for resolution.

""",
                     },
                     
           {
                        "name": "2-3-3-4 Centralized Clock Synchronization with Accurate and Trusted Sources",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To ensure accurate and reliable time synchronization across all systems and devices in the organization by using a centralized server and trusted time sources.",
                        "implementation_steps": """

1.1 Define Requirements
1.	Document the organization's need for centralized clock synchronization in the cybersecurity requirements document.
2.	Obtain approval from the organization's representative for the defined requirements.
1.2 Configure Centralized Time Synchronization
1.	Set up a centralized Network Time Protocol (NTP) server to synchronize time across all systems and devices.
2.	Ensure the central server is configured to use reliable and accurate sources, such as:
o	Saudi Standards, Metrology, and Quality Organization (time.saso.gov.sa).
o	King Abdulaziz City for Science and Technology (time.isu.net.sa).
1.3 Implement Time Synchronization on Systems
1.	For Linux systems, configure the /etc/ntp.conf file with the following commands:
o	server time.saso.gov.sa iburst
o	server time.isu.net.sa iburst
2.	For Windows systems, use the following commands in an administrator command prompt:
o	w32tm /config /manualpeerlist:"time.saso.gov.sa, time.isu.net.sa" /syncfromflags:manual /reliable:YES /update
o	w32tm /resync
1.4 Verify and Monitor Synchronization
1.	Periodically check that all systems and devices are synchronized with the central server.
2.	Review configurations to ensure the time source remains accurate and up-to-date.

""",
                        "examples": """
1.	Linux Time Configuration:
o	Configure the central NTP server using the /etc/ntp.conf file and synchronize with trusted sources (e.g., time.saso.gov.sa and time.isu.net.sa).
2.	Windows Time Configuration:
o	Use w32tm commands to synchronize Windows servers and workstations with the same trusted sources.

""",
                        "tools": """

1.	Time Synchronization Protocols:
o	NTP (Network Time Protocol)
o	SNTP (Simple Network Time Protocol)
2.	Trusted Time Sources:
o	Saudi Standards, Metrology, and Quality Organization (time.saso.gov.sa)
o	King Abdulaziz City for Science and Technology (time.isu.net.sa)
3.	System Utilities:
o	Linux: NTPD, Chrony.
o	Windows: W32Time.


""",
                        "deliverables": """

1.	Policy Documentation:
o	Approved cybersecurity requirements document specifying time synchronization requirements.
2.	Central Server Configuration Evidence:
o	Screenshots or network diagrams showing the presence of a central NTP server in the organization's network.
3.	Time Source Configuration Evidence:
o	Screenshots of the NTP or W32Time configurations showing synchronization with trusted sources like time.saso.gov.sa and time.isu.net.sa.
4.	Monitoring Reports:
o	Logs or reports demonstrating periodic checks and successful synchronization across systems.

""",
                     },
                     
           {
                        "name": "2-3-4 Periodic Review of Cybersecurity Requirements for Information Systems and Processing Facilities",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To ensure the cybersecurity requirements for protecting information systems and processing facilities remain effective, up-to-date, and aligned with organizational goals and evolving threats through periodic reviews.",
                        "implementation_steps": """

1.1 Define a Review Plan
1.	Develop and approve a review schedule specifying intervals for periodic reviews (e.g., annually, biannually).
2.	Document the review plan, including:
o	Scope of the review.
o	Roles and responsibilities for review teams.
1.2 Conduct Periodic Reviews
1.	Assess the current cybersecurity requirements for information systems and processing facilities to ensure:
o	Compliance with regulatory and organizational policies.
o	Alignment with the latest cybersecurity standards and frameworks.
2.	Identify gaps, outdated practices, or areas for improvement.
1.3 Update Cybersecurity Requirements
1.	Document any proposed updates or changes based on review findings.
2.	Secure approval from the organization's head or deputy for the updated requirements.
1.4 Monitor and Track Implementation
1.	Develop a system to track the implementation of recommendations from the review.
2.	Ensure all changes are communicated to relevant stakeholders.
1.5 Document and Archive Results
1.	Keep detailed records of the review process, findings, and approved updates.
2.	Archive review reports for auditing and reference purposes.

""",
                        "examples": """
1.	Annual Review Schedule:
o	Conduct a cybersecurity review every 12 months, evaluating all policies and procedures for protecting information systems and processing facilities.
2.	Review Process:
o	Use a checklist to evaluate compliance with NIST SP 800-53 controls.
o	Assess whether current policies address emerging threats such as ransomware or phishing attacks.
3.	Approval Process:
o	Submit updated requirements via internal systems for approval, ensuring digital signatures from organizational heads.

""",
                        "tools": """

1.	Review Management Tools:
o	Microsoft Planner or Trello for tracking review schedules.
o	Jira or ServiceNow for managing review tasks.
2.	Compliance and Monitoring Tools:
o	Nessus or Qualys for vulnerability assessment during reviews.
o	Splunk or ManageEngine for security log analysis.
3.	Documentation Tools:
o	Microsoft Word or SharePoint for creating and maintaining review documentation.
4.	Regulatory Frameworks:
o	ISO 27001, NIST SP 800-53 for aligning updates with industry standards.

""",
                        "deliverables": """
1.	Approved Review Schedule:
o	A document outlining the periodic review plan and intervals.
2.	Review Reports:
o	Evidence of periodic reviews conducted, including checklists, assessments, and identified gaps.
3.	Updated Cybersecurity Requirements:
o	Approved changes to requirements with formal documentation signed by the organization's head or deputy.
4.	Implementation Tracking Reports:
o	Logs or reports demonstrating the execution of updates and compliance with review findings.

""",
                     },
                     
           {
                        "name": "2-4-1 Cybersecurity Requirements for Protecting Email Services",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To define, document, and approve cybersecurity requirements for protecting email services, ensuring modern and reliable protection mechanisms, secure configurations, and compliance with organizational policies.",
                        "implementation_steps": """
1.1 Develop and Document Email Security Policy
1.	Define the purpose and scope of the email security policy.
2.	Outline policy statements, including:
o	Acceptable Use: Specify permitted and prohibited activities related to email usage.
o	Access Control: Require strong passwords, role-based access control, and multi-factor authentication (MFA).
o	Data Protection: Address handling of sensitive and confidential information.
o	Phishing and Malware Protection: Establish measures to prevent phishing attacks and mitigate malware risks.
1.2 Define Roles and Responsibilities
1.	Assign roles and responsibilities for managing and securing email services:
o	IT Department: Manage technical controls, email infrastructure, and incident response.
o	Management: Oversee enforcement and ensure compliance with policies.
o	Users: Adhere to the acceptable use policy and security guidelines.
2.	Differentiate between:
o	Public Accounts: Accounts intended for external communication.
o	Joint Accounts: Accounts shared by teams or departments.
1.3 Implement Technical Controls
1.	Configure email protection solutions to include:
o	Email Filtering: Block spam, phishing, and malware.
o	Encryption: Secure email content and attachments during transmission.
o	Anti-Virus and Anti-Malware: Detect and mitigate threats on email servers.
o	Backup and Recovery: Ensure email data is backed up and recoverable in case of incidents.
2.	Set limitations for email usage:
o	Attachment Size: Define maximum sizes for incoming and outgoing emails based on user needs and system performance.
o	Mailbox Capacity: Specify quotas for individual mailboxes.
1.4 Secure Email Infrastructure
1.	Design a secure email network infrastructure:
o	Network Segmentation: Isolate email services from other network segments.
o	Firewalls: Restrict traffic to email servers to necessary protocols and ports.
o	DMZ Configuration: Place email servers in a demilitarized zone (DMZ) to enhance security.
2.	Regularly update all systems associated with email services to address vulnerabilities.
1.5 User Awareness and Training
1.	Conduct training programs to educate users about:
o	Recognizing phishing attempts.
o	Secure email handling practices.
2.	Perform simulated phishing tests to assess and improve user awareness.
1.6 Monitoring and Enforcement
1.	Implement email activity monitoring and generate audit logs.
2.	Conduct periodic audits to review:
o	Access rights.
o	Compliance with the email security policy.
3.	Update rules and configurations regularly to align with the latest security standards.
1.7 Review and Update Policy
1.	Schedule regular reviews of the email security policy to ensure relevance and compliance.
2.	Perform compliance checks against regulatory requirements and industry standards.

""",
                        "examples": """

1.	Access Control for Public and Joint Accounts:
o	Public accounts require limited access with strong MFA configurations.
o	Joint accounts are managed with role-based access and strict auditing of usage.
2.	Technical Control Implementation:
o	Deploy Barracuda Email Security Gateway for spam filtering and malware protection.
o	Configure TLS encryption for all outgoing emails.
3.	Email Infrastructure Security:
o	Use a DMZ zone to isolate email servers and limit access via Cisco Firewalls.
o	Regularly patch and update the email server with tools like Microsoft Exchange Update Manager.

""",
                        "tools": """
1.	Email Protection Solutions:
o	Barracuda Email Security Gateway, Cisco Secure Email.
2.	Encryption:
o	TLS (Transport Layer Security), S/MIME.
3.	Backup and Recovery:
o	Veeam Backup for Microsoft 365, Acronis Cyber Backup.
4.	Infrastructure Security:
o	Cisco Firewalls, pfSense for DMZ configurations.
5.	User Awareness:
o	KnowBe4 for phishing simulations, internal training platforms.
6.	Monitoring and Logging:
o	Splunk, ManageEngine ADAudit Plus


""",
                        "deliverables": """
1.	Email Security Policy:
o	Approved document specifying email security requirements.
2.	Configuration Evidence:
o	Screenshots of email protection system settings (e.g., spam filtering, encryption).
3.	Access Control Reports:
o	Logs showing MFA implementation and access restrictions for public and joint accounts.
4.	Infrastructure Security Evidence:
o	Network diagrams showing segmented email services and DMZ placement.
o	Logs from firewalls and email servers proving secure configurations.
5.	Training and Awareness Reports:
o	Documentation of conducted training programs and results of simulated phishing tests.

""",
                     },
                     
           {
                        "name": "2-4-2 Implementing Cybersecurity Requirements for Email Services",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To implement advanced and effective email protection technologies and practices to safeguard the organization’s email services from phishing, spam, malware, and unauthorized access.",
                        "implementation_steps": """
Deploy Secure Email Gateways
1.	Select and deploy a Secure Email Gateway solution:
o	Examples include:
	Proofpoint Email Protection
	Cisco Umbrella
	Barracuda Email Security Gateway
2.	Configure email gateways to:
o	Filter content (e.g., spam, phishing emails).
o	Analyze URLs and attachments using sandboxing and real-time threat intelligence.
1.2 Implement Email Authentication Mechanisms
1.	Enable sender authentication techniques such as:
o	SPF (Sender Policy Framework): To validate the sending mail server.
o	DKIM (DomainKeys Identified Mail): To verify message integrity.
o	DMARC (Domain-based Message Authentication, Reporting, and Conformance): To prevent spoofing and ensure email reliability.
2.	Use tools like:
o	MXToolbox and GlockApps Email Header Analyzer to analyze email headers and detect anomalies.
1.3 Use Advanced Email Protection Technologies
1.	Deploy technologies for:
o	URL and Attachment Analysis:
	Use sandboxing and threat intelligence platforms to detect malicious URLs and attachments in real time.
o	Content Filtering:
	Block spam, phishing, and malware using solutions like:
	Barracuda Email Security Gateway.
	Fortinet FortiMail.
	Cisco Email Security.
	McAfee Email Protection.
2.	Implement antivirus solutions for email servers to scan all inbound and outbound emails.
1.4 Configure Load Balancers
1.	Select a load balancer:
o	Hardware-based solutions: F5 BIG-IP, Citrix ADC, Barracuda Load Balancer.
o	Software-based solutions: NGINX, HAProxy, Apache Traffic Server.
2.	Configure the load balancer:
o	Set Up Listeners: To process incoming email traffic.
o	Define Backend Servers: Assign servers to handle email traffic.
o	Health Checks: Ensure traffic is directed only to healthy servers.
o	Security Enhancements: Enable SSL encryption, IP whitelisting, and firewall rules.
1.5 Deploy Reverse Proxy for Additional Security
1.	Choose a reverse proxy:
o	NGINX, HAProxy, or Apache HTTP Server.
2.	Configure the reverse proxy to:
o	Forward emails securely to the organization’s email servers.
o	Enforce SSL/TLS encryption and apply IP filtering.
1.6 Configure Email Routing and Policies
1.	Define routing rules for incoming and outgoing emails through email gateways.
2.	Enforce security policies within the email gateway:
o	Scan for spam and malware.
o	Apply rules to block suspicious content.
o	Monitor email logs for anomalies.

""",
                        "examples": """
1.	Secure Email Gateway Implementation:
o	Deploy Proofpoint Email Protection to filter spam and phishing emails, and scan attachments for malware.
2.	Email Authentication:
o	Use MXToolbox to verify SPF, DKIM, and DMARC settings for all organizational domains.
3.	Load Balancer Configuration:
o	Set up NGINX to route incoming emails, perform health checks, and enforce IP filtering for added security.

""",
                        "tools": """

1.	Email Security Solutions:
o	Proofpoint Email Protection, Cisco Umbrella, Barracuda Email Security Gateway.
2.	Authentication and Header Analysis:
o	MXToolbox, GlockApps Email Header Analyzer.
3.	Load Balancers:
o	Hardware: F5 BIG-IP, Citrix ADC.
o	Software: NGINX, HAProxy, Apache Traffic Server.
4.	Email Filtering:
o	Fortinet FortiMail, McAfee Email Protection.
5.	Malware and Phishing Analysis:
o	Sandbox environments, Real-time Threat Intelligence.


""",
                        "deliverables": """

1.	Action Plan for Implementation:
o	A documented plan detailing the deployment and configuration of email protection controls.
2.	Secure Email Gateway Evidence:
o	Screenshots or configurations of deployed email gateways (e.g., Proofpoint, Barracuda).
3.	Authentication Evidence:
o	Reports showing SPF, DKIM, and DMARC settings for organizational domains.
4.	Load Balancer and Reverse Proxy Configuration:
o	Evidence of load balancer setup with health checks and security policies.
5.	Monitoring and Filtering Reports:
o	Logs showing the detection and blocking of spam, phishing, and malware.

""",
                     },
                     
           {
                        "name": "2-4-3 The cybersecurity requirements for protecting the email service must include at the least the following:",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },

           {
                        "name": "2-4-3-1 Analyzing and Filtering Email Messages (Phishing and Spam)",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To implement advanced and up-to-date email protection techniques for analyzing and filtering email messages, specifically targeting phishing and spam emails, while maintaining compliance with national regulations and organizational policies.",
                        "implementation_steps": """
1.1 Define Email Protection Requirements
1.	Document technical requirements for email protection, including:
o	Analyzing and filtering emails for phishing and spam.
o	Enabling multi-factor authentication (MFA) for remote and webmail access.
o	Ensuring email archiving and backup solutions are in place.
o	Protecting against Advanced Persistent Threats (APT).
o	Verifying the validity of the organization’s email address domains.
2.	Outline operational and procedural requirements:
o	Conduct training programs and awareness campaigns.
o	Establish incident response mechanisms for reporting and resolving email threats.
o	Define logging and reporting standards for compliance and audits.
1.2 Configure Email Protection Technologies
1.	Deploy advanced email filtering and protection solutions, such as:
o	Proofpoint, Mimecast, or Barracuda Email Security Gateway.
2.	Activate features for:
o	Spam filtering: Set filter levels and customize rules.
o	Phishing detection: Configure settings to detect phishing attempts and define response actions.
o	Attachment scanning: Enable scanning methods and define policies for suspicious attachments.
o	URL filtering: Configure detection and response rules for malicious links.
1.3 Monitor and Enhance Email Security
1.	Periodically review suspicious emails, including:
o	Phishing messages, spam, and unusual patterns.
o	Indicators such as high-volume email spikes, unauthorized email settings changes, and suspicious login attempts.
2.	Regularly update intrusion indicators and adjust configurations to improve accuracy.
1.4 Integrate Email Monitoring with SIEM Solutions
1.	Use SIEM solutions such as:
o	Splunk, IBM QRadar, or LogRhythm to monitor:
	Unusual login activities.
	Unauthorized changes in email settings.
	Spoofing or impersonation attempts.
2.	Integrate email protection systems with the SIEM dashboard for real-time analysis and reporting.
1.5 Review and Update Configurations
1.	Continuously monitor email protection system dashboards for reported threats and adjust settings accordingly.
2.	Update documentation to reflect any configuration changes and inform the team.
3.	Schedule regular reviews to ensure compliance with policies and effectiveness of email filtering mechanisms.

""",
                        "examples": """

1.	Spam and Phishing Detection:
o	Deploy Barracuda Email Security Gateway to block phishing and spam emails, and configure custom spam filtering rules.
o	Enable attachment scanning for malicious files and sandboxing to analyze suspicious links.
2.	SIEM Integration:
o	Use Splunk to detect high-volume email spikes and unauthorized access patterns.
o	Integrate phishing alerts from Proofpoint into IBM QRadar for centralized monitoring.
3.	Email Security Policy Implementation:
o	Activate MFA for all email accounts accessing the organization's domain remotely.
o	Use URL filtering to block links leading to malicious sites and apply user-specific action policies.

""",
                        "tools": """

1.	Email Protection and Filtering Solutions:
o	Proofpoint, Mimecast, Barracuda Email Security Gateway.
2.	SIEM Solutions:
o	Splunk, IBM QRadar, LogRhythm.
3.	Email Filtering Tools:
o	SpamAssassin, Cisco IronPort.
4.	Incident Response Tools:
o	KnowBe4 for simulated phishing campaigns, SecurityScorecard for domain vulnerability monitoring.


""",
                        "deliverables": """

1.	Policy Documentation:
o	Approved email protection policy specifying requirements for filtering and analyzing phishing and spam.
2.	Configuration Evidence:
o	Screenshots of activated email filtering features (e.g., spam detection, phishing analysis).
o	Evidence of implemented URL filtering and attachment scanning configurations.
3.	Monitoring and Reporting Logs:
o	Reports generated by SIEM tools showing suspicious activity patterns and resolved incidents.
4.	Training and Awareness Records:
o	Documentation of user training sessions and simulated phishing test results.
5.	Periodic Review Reports:
o	Evidence of regular reviews, updates to intrusion indicators, and adjustments to configurations.

""",
                     },
                     {
    "name": "2-3-3 Secure Management of Storage Media",
    "description": "",
    "section": "2-3",
    "purpose": "Ensure the secure management of storage media to protect organizational data from unauthorized access and breaches.",
    "implementation_steps": """
1. Define Storage Media Security Policies:
   - Develop a policy for the secure use, storage, and disposal of all storage media.

2. Encrypt Data on Storage Media:
   - Use encryption solutions like BitLocker or VeraCrypt for external and portable storage.

3. Access Control:
   - Limit access to storage media based on roles and responsibilities.

4. Storage Media Disposal:
   - Implement secure destruction processes for end-of-life media (e.g., shredding, degaussing).

5. Labeling and Inventory Management:
   - Label storage media clearly and maintain an updated inventory of all media.

6. Audit and Review:
   - Periodically review compliance with storage media policies.
""",
    "examples": """
- Implement an inventory system for tracking all external drives and portable storage devices.
- Use BitLocker to encrypt sensitive data stored on USB drives and external hard drives.
- Develop a policy for securely disposing of outdated drives using shredding or degaussing services.
""",
    "tools": """
- Encryption Solutions: BitLocker, VeraCrypt.
- Inventory Management: ManageEngine AssetExplorer, SolarWinds Service Desk.
- Secure Disposal Tools: Hard Drive Shredders, Degausser Machines.
- Audit Tools: Qualys Asset Inventory, Nessus.
""",
    "deliverables": """
- Approved Storage Media Policy:
  - Document outlining rules for storage media use, encryption, and disposal.

- Audit Logs:
  - Evidence of periodic audits for compliance with storage media policies.

- Disposal Evidence:
  - Certificates of destruction or shredding logs for disposed media.

- Encryption Reports:
  - Proof of encryption applied to storage devices.
"""
},

           {
                        "name": "2-4-3-2 Multi-Factor Authentication (MFA) for Remote and Webmail Access",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To secure remote and webmail access to the organization’s email services by implementing reliable and advanced multi-factor authentication (MFA) solutions, reducing the risk of unauthorized access.",
                        "implementation_steps": """

1.1 Select an MFA Provider
1.	Evaluate and select an appropriate MFA solution, such as:
o	Google Authenticator: Generates time-based one-time passwords (TOTP).
o	Microsoft Authenticator: Provides app-based authentication and push notifications.
o	Twilio SMS Delivery: Enables SMS-based MFA for seamless integration.
o	Mobile Device Management (MDM) Applications: Enforces device-based authentication for protocols like EWS or Outlook Anywhere.
1.2 Configure MFA Settings
1.	Email Service Configuration:
o	Enable SMS-based MFA or app-based MFA in the email service’s security settings.
o	Configure protocols like EWS and Outlook Anywhere for MDM-based MFA.
2.	Add Users:
o	Register user phone numbers or devices in the email service’s MFA configuration settings.
1.3 Test and Verify MFA Configuration
1.	Conduct testing to ensure:
o	SMS-based MFA delivers codes reliably to user devices.
o	Authentication apps generate accurate and valid one-time passwords (OTP).
o	MDM-enforced policies are effectively restricting access to compliant devices.
1.4 Train and Inform Users
1.	Provide training programs to:
o	Educate users on how to use MFA apps or authenticate via SMS.
o	Address common issues and questions through support channels.
2.	Communicate the importance of MFA for email security.
1.5 Monitor and Improve
1.	Monitor user feedback and resolve any challenges with MFA implementation.
2.	Periodically review and update MFA configurations to ensure:
o	Continued effectiveness.
o	Compliance with organizational policies and standards.

""",
                        "examples": """
1.	SMS-Based MFA:
o	Configure the email service (e.g., Microsoft Exchange) to send SMS-based one-time passwords to users during login.
o	Test the setup by registering a test user and verifying the delivery of OTPs.
2.	App-Based MFA:
o	Use Microsoft Authenticator to enable push-based authentication for email access.
o	Enforce its usage organization-wide and train staff on app setup and troubleshooting.
3.	MDM for Protocol-Specific Authentication:
o	Implement Intune for device-based authentication to manage email access for protocols like EWS and ensure compliance.

""",
                        "tools": """

1.	MFA Providers:
o	Google Authenticator, Microsoft Authenticator, Twilio SMS Delivery.
2.	MDM Solutions:
o	Microsoft Intune, VMware Workspace ONE, MobileIron.
3.	Email Platforms Supporting MFA:
o	Microsoft Exchange, Google Workspace.
4.	Monitoring and Logging:
o	Splunk, ManageEngine ADAudit Plus for tracking MFA activity


""",
                        "deliverables": """

1.	Policy and Procedure Documentation:
o	Approved document outlining MFA requirements and configurations.
2.	Configuration Evidence:
o	Screenshots of email system settings showing activated SMS-based MFA and app-based MFA.
o	Evidence of MDM-enforced device-based authentication for supported protocols.
3.	Test Reports:
o	Logs demonstrating successful MFA tests (e.g., OTP generation, SMS delivery).
4.	User Training Records:
o	Documentation of training sessions and feedback collected.
5.	Monitoring Reports:
o	Logs showing MFA adoption rates and user authentication activity.

""",
                     },
                     
           {
                        "name": "2-4-3-3 Email Archiving and Backup",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To ensure that email services are securely backed up and archived, providing data integrity, compliance with regulatory requirements, and protection against data loss.",
                        "implementation_steps": """

1.1 Define Technologies Compatible with Infrastructure
1.	Assess the organization’s current email systems, storage solutions, and network capabilities to identify compatible archiving and backup technologies.
2.	Choose a suitable solution based on compatibility and scalability:
o	Veritas Enterprise Vault
o	Barracuda Essentials
o	Mimecast
o	Veeam Backup & Replication
o	Backup Exec
3.	Ensure the selected solution can handle the organization’s email volumes effectively.
1.2 Define Retention Policies
1.	Collaborate with the legal compliance team to define retention policies based on legal and regulatory requirements.
2.	Establish retention policies, including:
o	Archiving Retention: Set periods for archived emails based on compliance needs.
o	Backup Retention: Define how long daily, weekly, and monthly backups will be stored.
1.3 Develop a Backup Strategy
1.	Decide on the backup type:
o	Full Disk Backup: For comprehensive backups of email servers.
o	Incremental Backup: For efficiency and reduced storage requirements.
2.	Schedule regular backups to maintain up-to-date copies of email data.
3.	Configure backup tools to integrate seamlessly with the email server for efficient access.
4.	Test the backup system to:
o	Ensure data integrity.
o	Minimize performance impact on email servers.
5.	Monitor backups regularly to confirm their success.
1.4 Implement Email Archiving
1.	Select an appropriate archiving method:
o	Integrated Archiving: Use built-in solutions such as Microsoft 365 or Google Workspace.
o	Third-Party Solutions: Deploy external services like Mimecast, Barracuda, or Zix.
2.	Configure the chosen archiving solution:
o	Define rules for email archiving.
o	Apply retention policies to archived emails to ensure compliance with organizational and legal requirements.
3.	Regularly verify and monitor email archives to ensure:
o	Archives are accessible and accurate.
o	Policies are updated based on changes in compliance requirements.

""",
                        "examples": """
1.	Backup Strategy Implementation:
o	Configure Veeam Backup & Replication to perform weekly incremental backups and monthly full backups of the organization’s email servers.
2.	Retention Policy Enforcement:
o	Use Veritas Enterprise Vault to apply a 7-year retention policy for archived emails as per compliance regulations.
3.	Archiving Solution Configuration:
o	Deploy Mimecast for external email archiving, configuring rules to archive all organizational email automatically and apply retention policies.

""",
                        "tools": """

1.	Backup Solutions:
o	Veeam Backup & Replication, Backup Exec, Barracuda Essentials.
2.	Email Archiving Solutions:
o	Veritas Enterprise Vault, Mimecast, Barracuda Essentials.
3.	Integrated Archiving Options:
o	Microsoft 365, Google Workspace.
4.	Monitoring Tools:
o	Splunk, ManageEngine ADAudit Plus for tracking backup and archiving activities.


""",
                        "deliverables": """

1.	Policy Documentation:
o	Approved document outlining backup and archiving requirements and retention policies.
2.	Configuration Evidence:
o	Screenshots of configured archiving and backup solutions, including capacity and retention settings.
3.	Backup Reports:
o	Logs showing successful backups of email servers with timestamps and volumes.
4.	Archiving Activation Evidence:
o	Screenshots or examples showing the activation of archiving features for all organizational email accounts.
5.	Monitoring Reports:
o	Logs and reports verifying the integrity and compliance of email backups and archives.

""",
                     },
                     
           {
                        "name": " 2-4-3-4 Secure Management and Protection Against Advanced Persistent Threats (APTs)",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To implement advanced technologies and strategies for securing email systems against Advanced Persistent Threats (APTs) and zero-day malware, ensuring organizational email security and resilience against emerging threats.",
                        "implementation_steps": """

1.1 Assess Current Security Posture
1.	Conduct a security audit to identify gaps in email protection against APTs and zero-day malware.
2.	Perform a risk assessment to evaluate potential vulnerabilities and prioritize security measures.
1.2 Select and Deploy Advanced Technologies
1.	Email Protection Technologies:
o	Deploy Advanced Threat Protection (ATP) solutions with:
	Sandboxing: Analyze email attachments in a secure environment.
	URL Filtering: Prevent access to malicious links.
o	Recommended solutions:
	Microsoft Defender for Office 365
	Proofpoint Email Protection
	Mimecast Email Security
2.	Zero-Day Protection Techniques:
o	Threat Intelligence Integration:
	Provides real-time updates and contextual alerts for new threats.
	Tools: Recorded Future, ThreatConnect, Anomali.
o	Behavior-Based Detection:
	Uses machine learning to detect unusual patterns.
	Tools: Darktrace, CylancePROTECT, CrowdStrike Falcon.
3.	Endpoint Detection and Response (EDR):
o	Real-time monitoring and automated responses to threats on endpoints.
o	Tools: Carbon Black, SentinelOne, Microsoft Defender for Endpoint.
4.	Activate and configure features for ATP and zero-day malware detection in deployed solutions.
1.3 Implement Policies and Configurations
1.	Define and document policies for:
o	ATP and zero-day protection.
o	Rules for email filtering and threat detection.
2.	Configure systems to block, quarantine, or escalate suspicious emails.
1.4 Train and Educate Users
1.	Conduct awareness programs to educate users on:
o	Recognizing phishing attempts and suspicious emails.
o	Best practices for handling email attachments and links.
2.	Provide ongoing support channels for resolving user issues.
1.5 Monitor, Review, and Respond
1.	Establish a structured workflow to:
o	Review and analyze suspicious emails flagged by the system.
o	Maintain logs of reviewed emails, actions taken, and outcomes.
2.	Use tools such as Splunk or IBM QRadar to monitor email security incidents.
3.	Regularly review email security configurations and update them based on threat intelligence.
4.	Document all findings and actions taken to ensure compliance and continuous improvement.

""",
                        "examples": """

1.	Sandboxing for Zero-Day Malware:
o	Deploy FireEye Malware Analysis to analyze email attachments in a controlled environment.
o	Identify malicious behavior without exposing systems to threats.
2.	Behavior-Based Detection:
o	Use Darktrace to monitor email traffic and detect unusual patterns indicative of APTs.
3.	Threat Escalation:
o	Configure Proofpoint Threat Response to escalate high-risk emails for immediate investigation by the security team.

""",
                        "tools": """

1.	Sandboxing for Zero-Day Malware:
o	Deploy FireEye Malware Analysis to analyze email attachments in a controlled environment.
o	Identify malicious behavior without exposing systems to threats.
2.	Behavior-Based Detection:
o	Use Darktrace to monitor email traffic and detect unusual patterns indicative of APTs.
3.	Threat Escalation:
o	Configure Proofpoint Threat Response to escalate high-risk emails for immediate investigation by the security team.


""",
                        "deliverables": """

1.	Policy Documentation:
o	Approved document detailing ATP and zero-day protection requirements and configurations.
2.	Configuration Evidence:
o	Screenshots of activated ATP features in email protection systems.
o	Proof of sandboxing, URL filtering, and behavior-based detection configurations.
3.	Monitoring Reports:
o	Logs from SIEM tools showing detected threats and actions taken.
4.	Incident Response Records:
o	Documentation of actions taken on suspicious emails, including escalations and resolutions.
5.	Training Records:
o	Evidence of user training sessions and feedback.

""",
                     },
                     
           {
                        "name": "2-4-3-5 Validation of the Organization’s Email Services Domains (SPF, DKIM, DMARC)",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "To enhance email security by implementing SPF, DKIM, and DMARC, ensuring email domain integrity and protection against spoofing and phishing.",
                        "implementation_steps": """

1.1 Configure SPF Records
1.	Identify authorized mail servers/IPs and define SPF records in DNS.
2.	Validate SPF syntax and functionality using tools like MXToolbox SPF Checker or DMARC Analyzer.
3.	Publish the SPF record and monitor its effectiveness to ensure compliance.
1.2 Set Up DKIM
1.	Generate DKIM keys (public/private) using tools like OpenDKIM or EasyDMARC.
2.	Publish the public key in DNS and configure email servers to sign outgoing messages with the private key.
3.	Test the DKIM setup using GlockApps or Mail Tester to confirm signatures are applied and validated.
1.3 Implement DMARC
1.	Define DMARC policies:
o	None: Monitoring only.
o	Quarantine: Sends non-compliant emails to spam.
o	Reject: Blocks non-compliant emails.
2.	Align DMARC with SPF and DKIM for consistent authentication.
3.	Use DMARC Analyzer or Valimail to monitor and analyze DMARC reports.
1.4 Integrate with Haseen
1.	Connect DMARC reports and email documentation to the Haseen platform using API integrations.
2.	Automate reporting to ensure compliance with organizational and regulatory requirements.
1.5 Monitor and Maintain
1.	Regularly review and update SPF, DKIM, and DMARC records to reflect infrastructure changes.
2.	Monitor email security logs for anomalies or gaps in authentication processes.

""",
                        "examples": """
1.	SPF Record: Configure an SPF record using AWS Route 53, specifying authorized IPs and mail servers.
2.	DKIM: Use OpenDKIM to generate and publish DKIM keys, ensuring outgoing emails are signed and verified.
3.	DMARC: Deploy a quarantine DMARC policy with DMARCian, then monitor reports for compliance and issues.

""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
{
    "name": "2-3-4 Periodic Review of Cybersecurity Requirements for Information Systems",
    "description": "",
    "section": "2-3",
    "purpose": "Ensure that cybersecurity requirements for information systems are reviewed regularly to align with regulatory changes and organizational needs.",
    "implementation_steps": """
1. Develop a Review Plan:
   - Define intervals for periodic review (e.g., quarterly or annually).
   - Document the scope of each review, including covered systems and controls.

2. Conduct Vulnerability Assessments:
   - Use tools like Nessus or Qualys to identify vulnerabilities in systems and networks.

3. Review Compliance with Policies:
   - Verify that current configurations and procedures meet organizational policies and regulatory requirements.

4. Document Findings and Updates:
   - Maintain records of identified gaps and actions taken to address them.

5. Secure Approval for Updates:
   - Submit revised policies and requirements for executive approval.

6. Monitor Implementation:
   - Track the application of updated policies across systems and generate compliance reports.
""",
    "examples": """
- Schedule quarterly reviews of systems using Nessus vulnerability scans.
- Document changes to security configurations based on review findings.
- Update firewall rules and access control policies following review recommendations.
""",
    "tools": """
- Vulnerability Scanners: Nessus, Qualys, Rapid7 InsightVM.
- Compliance Tracking: Splunk, ServiceNow Compliance Manager.
- Documentation Tools: Confluence, SharePoint.
""",
    "deliverables": """
- Compliance Assessment Reports:
  - Detailed findings and recommendations from periodic reviews.

- Policy Update Logs:
  - Evidence of changes made to cybersecurity requirements.

- Approval Records:
  - Signed documents or emails confirming executive approval of updates.

- Monitoring Evidence:
  - Reports from tools like Splunk showing policy enforcement and compliance.
"""
},


                                             {
                        "name": "2-2-3-2 Multi-Factor Authentication (MFA)",
                        "description": "",
                        "section": "2-2-3-2",
                        "purpose": ": Strengthen remote access using MFA.",
                        "implementation_steps": """
1.	Define MFA requirements in the IAM policy.
2.	Enable MFA for all remote access.

""",
                        "examples": """
Two or more authentication factors must be used:
•	Something you know: Password.
•	Something you have: One-Time Password (OTP) via SMS or an authenticator app.
•	Something you are: Biometrics (e.g., fingerprint or facial recognition).
Enable MFA for all systems supporting remote access, such as:
•	Virtual Private Networks (VPNs).

""",
                        "tools": """
•	MFA Providers: Duo Security, Microsoft Authenticator.
•	Monitoring and Logging: Splunk, Microsoft Defender


""",
                        "deliverables": """
•	IAM Policy with MFA Requirements
•	Approved MFA policy.
•	Screenshots of MFA configurations and outcome.  
""",
                     },
                                             {
                        "name": " 2-2-3-3 User Authorization (Least Privilege, Need-to-Know)",
                        "description": "",
                        "section": "2-2-3-3",
                        "purpose": "Control access based on role and business need.",
                        "implementation_steps": """
1.	Use role-based access control (RBAC).
2.	Segregate duties to minimize conflicts of interest.
3.	Manage access through centralized systems (e.g., Active Directory).

""",
                        "examples": """
All employees must be granted access to systems and data based on the following principles:
•	Access to sensitive information is limited to employees with verified business needs (Need-to-Know).
•	Functional duties requiring system access will be limited to authorized personnel only (Least Privilege).
•	Critical tasks must be distributed across multiple roles to ensure checks and balances (Segregation of Duties).

""",
                        "tools": """
Tool1: RBAC: SailPoint, Active Directory.
Tool2: Access Monitoring: Splunk, ManageEngine.


""",
                        "deliverables": """
Deliverable 1:Access Control Policy
Deliverable 2:Role-based access matrix.
Deliverable 3:Evidence of access control configurations.

""",
                     }, 
                                             {
                        "name": " 2-2-3-4 Privileged Access Management (PAM)",
                        "description": "",
                        "section": "2-2-3-4",
                        "purpose": "Protect and monitor privileged accounts.",
                        "implementation_steps": """
1.	Define and document PAM processes:
o	Disable default accounts.
o	Restrict internet and email access for privileged accounts.
2.	Monitor privileged account activity

""",
                        "examples": """
Privileged accounts include:
•	System administrators with root access.
•	Network administrators with access to firewalls and switches.
Ensure privileged accounts are not used for daily tasks.

""",
                        "tools": """
Tool1: PAM Tools: CyberArk, BeyondTrust.
Tool2: Monitoring: Splunk, SIEM solutions.

""",
                        "deliverables": """
•	Approved Privileged Access Management Policy.
•	Logs of privileged account activity

""",
                     }, 
                                             {
                        "name": " 2-2-3-5 Periodic Review of Identity and Access",
                        "description": "",
                        "section": "2-2-3-5",
                        "purpose": "ensures the organization periodically reviews access permissions for all system",
                        "implementation_steps": """
•	Define Review Requirements
•	Define Privileged Access:
1-Identify Personnel with Privileged Access
2-Review and Revoke Access
•	Develop a Plan for Periodic Review

""",
                        "examples": """
Develop a review schedule and define roles for access review:
•	Review all access permissions every 3 months or when a change in employment status occurs.
•	Identify all assets requiring periodic access reviews, including:
o	Applications: HRMS, ERP, email systems.
o	Infrastructure: Servers, databases.
Collaborate with managers and asset owners to review permissions.

""",
                        "tools": """
Tool1:Access Review: SailPoint, Okta, Active Directory.
Tool2:Notifications and Alerts: Microsoft Teams, email platforms


""",
                        "deliverables": """
Deliverable 1:Approved Privileged Access Management Policy.
Deliverable 2:Evidence of Implementation.

""",
                     },  
                                          {
                        "name": " 2-2-4 Periodic Review of IAM Requirements",
                        "description": "",
                        "section": "2-2-4",
                        "purpose": "Ensure IAM controls are reviewed regularly and updated as needed.",
                        "implementation_steps": """
1.	Schedule periodic reviews of IAM policies and access.
2.	Audit IAM configurations and update if necessary.
3.	Document and approve updates to IAM requirements.

""",
                        "examples": """
Example1: Define a periodic review plan for IAM requirements.
•	Example: Conduct reviews quarterly or bi-annually, and after significant organizational changes (e.g., mergers, new regulations).
Example2: Review current IAM policies and configurations:
•	Ensure alignment with principles like Least Privilege and Need-to-Know.
•	Verify compliance with relevant laws (e.g., KSA cybersecurity regulations, GDPR).

""",
                        "tools": """
Tool1:Review Management: Microsoft Planner.
Tool2:Monitoring and Compliance: Splunk, ManageEngine AD 


""",
                        "deliverables": """
Deliverable 1:IAM review reports.
Deliverable 2:Updated IAM policy with signed approval.

""",
                     }, 
                     
           {
                        "name": " 2-13-1: Define, Document, and Approve Cybersecurity Incident and Threat Management Requirements",
                        "description": "",
                        "section": "2-13-1",
                        "purpose": "Create a formal policy that outlines how to handle incidents and threats.",
                        "implementation_steps": """
1.	Develop a Cybersecurity Incident and Threat Management Policy:
o	Include incident response plans, severity classifications, roles, and communication processes.
o	Define mechanisms for notifying the National Cybersecurity Authority (NCA) and sharing intelligence.
2.	get Executive Approval:
o	Obtain formal approval for the policy from organizational leadership.

""",
                        "examples": """
Exampl1:Create a policy that defines how the organization will manage cybersecurity incidents and threats:
•Purpose:
o	To establish a framework for identifying, managing, and responding to cybersecurity incidents and threats to minimize impacts.
•	Scope:
o	This policy applies to all employees, contractors, and third-party vendors.
•	Incident Response Plan:
o	Step-by-step procedures for detecting, containing, eradicating, and recovering from cybersecurity incidents.
•	Threat Intelligence:
o	Collect and handle feeds from Saudi CERT, Haseen, and other platforms.

""",
                        "tools": """
Link:•	Policy Template: https://cdn.nca.gov.sa/api/files/public/upload/6c15978a-f6a1-4024-87b3-c7bdc16f05d0_POLICY_Cybersecurity_Incident_and_Threat_Management_Template_en-.pdf.

""",
                        "deliverables": """
Deliverable1:Approved policy document.
Deliverable2:Evidence of formal approval (e.g., signed document).

""",
                     },
                     
           {
                        "name": " 2-13-2: Implement Incident and Threat Management Requirements",
                        "description": "",
                        "section": "2-13-2",
                        "purpose": "Operationalize the defined requirements to respond effectively to incidents.",
                        "implementation_steps": """
1.	Set Up Incident Response Framework:
o	Create and implement an incident response plan and communication flow.
o	Classify incidents by severity.
2.	Integrate Threat Intelligence Feeds:
3.	Review the Response Plan Periodically:

""",
                        "examples": """
Deploy the organization’s incident response plan to ensure readiness for cybersecurity incidents:
1.	Detection:
o	Use SIEM systems to monitor logs for anomalies.
o	Subscribe to threat intelligence feeds.
2.	Response:
o	Assign incidents to the Incident Response Team (IRT).
o	Follow documented workflows for containment and remediation.
3.	Communication:
o	Notify stakeholders and the National Cybersecurity Authority (NCA) when required.
o	Use secure channels for communication.

""",
                        "tools": """
Tool1:Threat Intelligence Platforms: Saudi CERT, CST news.
Tool2:Communication: Microsoft Outlook.
Tool3:Monitoring and Detection: Splunk, IBM QRadar.
""",
                        "deliverables": """
Deliverable1:Approved incident response plan.
Deliverables2:Sample incident reports.

""",
                     },
                     
           {
                        "name": " 2-13-3: Specific Requirements for Incident and Threat Management",
                        "description": "",
                        "section": "2-13-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": " 2-13-3-1: Incident Response Plans and Escalation Procedures",
                        "description": "",
                        "section": "2-13-3-1",
                        "purpose": "2-13-3-1: Incident Response Plans and Escalation Procedures",
                        "implementation_steps": """
1.	Develop an Incident Response Plan:
o	Include severity classification, roles, escalation steps, and communication channels.
o	Make an incident report upon completion.
2.	Prepare Playbooks:
o	Define specific actions for common incidents (e.g., malware, phishing).
3.	Review the response plan periodically.

""",
                        "examples": """
Establish clear criteria for classifying incidents:
Severity	Impact	Escalation Level
Critical	Severe disruption to critical systems	Notify CISO and NCA
High	Significant impact on departmental systems	Notify IT Head and Management
Medium	Limited impact on isolated systems	Notify IT Support Team
Low	Minimal impact	Handle within SOC
Create a playbooks for Phishing Attack:
1.	Detection:
o	SOC identifies phishing emails through email gateway alerts.
2.	Containment:
o	Block sender and quarantine emails.
o	Notify affected users.
3.	Eradication:
o	Remove malicious emails from mailboxes.
o	Update email filters.
4.	Recovery:
o	Educate users on phishing awareness.
Create an Incident Report:
1. Incident Details
•	Incident ID: INC-2024-001
•	Date & Time: November 18, 2024, 14:32 PM
•	Type: Ransomware Attack
•	Severity: Critical
•	Scope: 5 servers, 20 workstations
2. Incident Summary A ransomware attack was detected via the SIEM system. The attacker exploited a Remote Desktop Protocol (RDP) vulnerability to gain unauthorized access. File encryption activity impacted servers and workstations.
3. Response Team
Name	Role	Contact
John Doe	Incident Lead	Mobile: +966-123-456-789
Sarah Ali	SOC Analyst	sarah.ali@company.com
4. Actions Taken Containment:
•	Disconnected affected systems from the network.
•	Blocked RDP at the firewall.
Removal:
•	Used CrowdStrike to remove malicious files.
•	Restored servers from clean backups.
Approved By:
Maria Hassan, CISO, November 18, 2024

""",
                        "tools": """
•	Communication and Reporting: Microsoft Teams, email.
•	Simulation Tools: Kali Linux, Metasploit.


""",
                        "deliverables": """
•	Approved incident response plan.
•	Playbooks for specific scenarios.
•	A documentation of the incident.
•	Sample incident reports.

""",
                     },
                     
           {
                        "name": " 2-13-3-2: Incident Classification",
                        "description": "",
                        "section": "2-13-3-2",
                        "purpose": "Categorize incidents by severity to prioritize response.",
                        "implementation_steps": """
1.	Define Classification Mechanism:
o	Align with the organization’s risk management framework.
2.	Apply Classification:
o	Assign severity during incident response and document it.

""",
                        "examples": """
Establish criteria for categorizing cybersecurity incidents by severity and impact
Severity Level	Impact	Examples
Critical	Severe business disruption, sensitive data breach	Ransomware attack affecting critical systems
High	Significant departmental impact	Targeted phishing compromising credentials
Medium	Limited impact on isolated systems	Malware detection on a workstation
Low	Minimal or no operational impact	Failed login attempts, suspicious emails

""",
                        "tools": """
•	Classification Framework: NIST Incident Classification.
•	Incident Management: ServiceNow, Jira.


""",
                        "deliverables": """
•	Classification framework document.
•	Incident reports with severity labels.

""",
                     },
                     
           {
                        "name": " 2-13-3-3: Reporting Incidents to NCA",
                        "description": "",
                        "section": "2-13-3-3",
                        "purpose": "Ensure timely notification of cybersecurity incidents to NCA.",
                        "implementation_steps": """
1.	Define Reporting Procedures:
o	Identify stakeholders, reporting timelines, and required information (e.g., date, time, severity, impact).
2.	Use Official Channels:
o	Submit reports via Haseen or NCA’s official email.

""",
                        "examples": """

""",
                        "tools": """
•	Communication: Microsoft Outlook, Haseen Portal.

""",
                        "deliverables": """
•	Procedures for reporting to NCA.
•	Samples of incident notifications sent to NCA

""",
                     },
                     
           {
                        "name": " 2-13-3-4: Sharing Threat Intelligence with NCA",
                        "description": "",
                        "section": "2-13-3-4",
                        "purpose": "Share alerts, breach indicators, and incident reports with NCA.",
                        "implementation_steps": """
1.	Set Up Sharing Procedures:
o	Define the process for sharing indicators, alerts, and reports with NCA.
2.	Maintain Membership:
o	Subscribe to the NCA's threat intelligence programs and platforms.

""",
                        "examples": """
""",
                        "tools": """
•	Threat Intelligence Platforms: Haseen, Saudi CERT.
•	Communication: Microsoft Outlook.


""",
                        "deliverables": """
•	Procedures for sharing intelligence with NCA.
•	Samples of shared reports.

""",
                     },
                     
           {
                        "name": " 2-13-3-5: Collecting and Handling Threat Intelligence Feeds",
                        "description": "",
                        "section": "2-13-3-5",
                        "purpose": "Leverage threat intelligence to enhance incident management.",
                        "implementation_steps": """
1.	Subscribe to Threat Feeds:
o	Use platforms like Haseen, Saudi CERT.
2.	Distribute Alerts:
o	Assign alerts to relevant teams and track resolution.

""",
                        "examples": """
""",
                        "tools": """
•	Threat Feeds: Saudi CERT, Haseen.
•	Incident Management: ServiceNow, Jira.


""",
                        "deliverables": """
•	Evidence of subscription to threat feeds.
•	Sample alerts and resolution reports.

""",
                     },
                     
          {
        "name": "2-13-4: Periodic Review of Cybersecurity Incident and Threat Management",
        "description": "",
        "section": "2-13-4",
        "purpose": "Ensure incident management policies and practices remain effective.",
        "implementation_steps": """
1. Develop a Review Plan:
o Conduct quarterly reviews of incident response effectiveness and compliance.
2. Update Policies:
o Modify policies based on findings or regulatory changes.
3. Document Changes:
o Maintain a log of updates and review findings.

""",
        "examples": "",
        "tools": """
• Review Management: Microsoft Planner, ServiceNow.
• Reporting: Power BI, Tableau.

""",
        "deliverables": """
• Review plan document.
• Compliance reports summarizing findings and updates.

"""
    },
      {
        "name": "2-14-1: Define, Document, and Approve Cybersecurity Requirements for Physical Security",
        "description": "",
        "section": "2-14-1",
        "purpose": "Create a policy that outlines the physical security requirements for protecting information and technology assets.",
        "implementation_steps": """
1. Develop a Physical Security Policy.
   - Include requirements for access control, CCTV monitoring, destruction of classified assets, and device security.
2. Define secure destruction and reuse procedures for classified assets.
3. Secure formal approval from executive management.
    """,
        "examples": """
1. Purpose:
To ensure the physical security of information and technology assets, preventing unauthorized access, loss, theft, and damage.
2. Scope:
This policy applies to all physical locations containing critical assets, including data centers, communication rooms, and disaster recovery centers.
3. Key Requirements:
• Authorized Access:
o Access to sensitive areas must be restricted to authorized personnel only.
o Access must be granted through card readers, biometrics, or other secure mechanisms.
• CCTV Monitoring:
o Surveillance cameras must monitor entry/exit points and critical areas.
o CCTV footage must be archived for at least 90 days.
• Secure Destruction:
o Documents and digital storage media containing classified information must be securely destroyed using shredders or degaussers.
• Device Security:
o All devices and equipment must be secured within the premises with protective measures (e.g., rack locks, enclosures).

    """,
        "tools": """
• Policy Templates: https://cdn.nca.gov.sa/api/files/public/upload/a89027d8-e51d-46d7-a9f8-7f6349c38479_POLICY_Physical_Security_template_en-.pdf.
    """,
        "deliverables": """
- Approved physical security policy.
- Evidence of executive approval (e.g., signed documents or emails).
    """
      },
{
    "name": "2-14-2: Implement Physical Security Requirements",
    "description": "",
    "section": "2-14-2",
    "purpose": "Operationalize the approved physical security requirements to safeguard assets.",
    "implementation_steps": """
1.	Access Controls:
o	Implement access mechanisms (e.g., biometric systems, card readers) for critical areas like data centers.
2.	CCTV Monitoring:
o	Deploy surveillance systems and maintain logs for entry/exit points.
3.	Secure Destruction:
o	Use shredders and degaussing tools for classified documents and storage media.
4.	Action Plan:
o	Develop a detailed implementation plan to ensure compliance.
    """,
    "examples": """
Install physical access systems such as:
o	Card Readers: Assign access cards to authorized personnel.
o	Biometric Scanners: Use fingerprint or facial recognition for high-security zones.
Install CCTV cameras at:
o	Entry/exit points.
o	Inside critical areas like data centers.
Destroy sensitive physical and digital media securely to prevent unauthorized recovery:
o	Paper Shredders: For confidential documents.
o	Degaussers or Hard Drive Crushers: For storage media.
o	Destruction Tools: Shredder machines, degaussers.
    """,
    "tools": """
•	Access Control Systems: HID Access Control, Suprema Biometric Access.
•	CCTV Systems: Hikvision, Axis Communications.

    """,
    "deliverables": """
- Implementation action plan.
- Evidence of physical security controls (e.g., CCTV logs, access logs).
    """
},
{
    "name": " 2-14-3: Include Specific Physical Security Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": " 2-14-3-1: Authorized Access to Sensitive Areas",
                        "description": "",
                        "section": "2-14-3-1",
                        "purpose": "",
                        "implementation_steps": """
•	Action:
o	Define sensitive areas like data centers and disaster recovery rooms.
o	Develop access request forms and approval workflows.
o	Implement access mechanisms and revoke expired permissions.

""",
                        "examples": """
•	Define the scope of sensitive areas requiring restricted access:
o	Data centers.
o	Disaster recovery centers.
•	Create an access request form and approval process:
o	Name of the requester.
o	Role and department.
o	Purpose of access.
o	Duration of access.
•	Limit management of access systems to authorized personnel.
•	Establish strict controls for granting access to third partie:
o	Verify compliance with security requirements.
o	Supervise third-party activities in sensitive areas.
o	Log and monitor all third-party access events.

""",
                        "tools": """
•	Audit and Review Tools: Splunk, Microsoft Excel.
•	Documentation Tools: Microsoft Word, SharePoint.

""",
                        "deliverables": """
•	Access request forms and approval logs.
•	Audit trails of access revocations.

""",
                     },

           {
                        "name": " 2-14-3-2: Facility Entry/Exit Records and CCTV Monitoring",
                        "description": "",
                        "section": "2-14-3-2",
                        "purpose": "",
                        "implementation_steps": """
o	Action:
o	Ensure entry/exit logs are maintained for all facilities.
o	Monitor critical areas with CCTV systems and archive surveillance records.

""",
                        "examples": """
Establish a process to record and monitor entry and exit activities for all critical areas.
1.	Identify key locations requiring entry/exit logs:
o	Data centers.
o	Communication rooms.
o	Main building and branches.
2.	Record required details:
o	Name of entrant.
o	Time of entry and exit.
o	Purpose of visit (for non-employees).
Install and maintain CCTV cameras to monitor entry/exit points and critical areas.
1.	Install cameras at:
o	Entry/exit points.
o	Building corridors.
o	Inside and outside sensitive areas.

""",
                        "tools": """
•	Log Management: Excel, Log Management Systems.
•	Monitoring Systems: Hikvision, Axis.
•	Centralized Monitoring: Milestone Systems, Genetec Security


""",
                        "deliverables": """
•	Evidence of monitoring (e.g., access logs, CCTV footage).
""",
                     },
                     
           {
                        "name": " 2-14-3-3: Protect Surveillance Records",
                        "description": "",
                        "section": "2-14-3-3",
                        "purpose": "",
                        "implementation_steps": """
o	Store access and monitoring logs in secure locations.
o	Ensure retention and backup of surveillance records for compliance.

""",
                        "examples": """
Identify a dedicated, restricted-access area for storage (e.g., CCTV control room or server room).
Equip storage areas with physical security measures:
o	Locked cabinets or safes for physical logs.
o	Access control mechanisms for rooms housing DVR/NVR systems.
Implement measures to secure digital logs and footage from unauthorized access.
o	Encrypt stored surveillance footage and entry/exit logs.
o	Use secure servers with limited access permissions for digital records.
o	Implement a logging system to track who accesses digital records.
Determine the appropriate retention period (e.g., 12 months for logs, 90 days for CCTV footage).
""",
                        "tools": """
•	Digital Encryption: BitLocker, VeraCrypt.
•	Physical Storage: Kensington locks, server cabinets.
•	Backup Tools: Veeam Backup, Acronis.

""",
                        "deliverables": """
•	Archived access logs and evidence of secure storage.
""",
                     },
                     
           {
                        "name": " 2-14-3-4: Secure Destruction of Classified Assets",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
o	Use shredders and disk destruction machines for classified documents and storage media.
o	Document destruction processes for audit purposes.
o	Develop methodology and procedures for the reuse of physical assets.

""",
                        "examples": """
Define the scope of physical assets requiring secure destruction or re-use.
•	Paper documents with sensitive information.
•	Storage media (e.g., hard drives, USB drives, CDs/DVDs).
For Paper Documents:
•	Use industrial-grade shredders.
For Digital Storage Media:
•	Use hard drive degaussers or crushers for physical destruction.
Establish secure methods for re-using physical assets while ensuring classified information is fully removed.
1.	Use data wiping software to overwrite sensitive data.
2.	Ensure compliance with recognized standards for data erasure (e.g., SDAIA Personal Data Destruction, NIST 800-88).

""",
                        "tools": """
•	Destruction Tools: Shredder machines, degaussers.
•	Data Erasure Software: Blancco, DBAN.


""",
                        "deliverables": """
•	Certificates of destruction for physical and digital media.
•	Procedures for reusing physical assets

""",
                     },
                  
           {
                        "name": " 2-14-3-5: Device and Equipment Security",
                        "description": "",
                        "section": "2-14-3-5",
                        "purpose": "",
                        "implementation_steps": """
o	Secure devices in critical areas and maintain them periodically.
o	Define physical security procedures for internal and external stakeholders.

""",
                        "examples": """
List all devices and equipment requiring security measures.
o	Servers, routers, and switches in data centers.
o	Desktops, laptops, and workstations.
o	Backup storage devices.
o	Portable devices like tablets and USB drives.
Install physical security controls for devices located inside/outside critical facilities.
o	Use lockable server racks for data center equipment.
o	Place security locks (e.g., Kensington locks) on workstations and laptops.
o	Install alarm systems for restricted areas.
o	Enclose outdoor equipment in weatherproof, tamper-resistant enclosures.
o	Use surveillance cameras to monitor outdoor areas.
Create a maintenance plan for devices to ensure their operational security.
Schedule periodic inspections of physical equipment.
Include checks for:
o	Tampering signs.
o	Device functionality.
Develop Security Procedures.
Define security protocols for handling and storing devices.
Include procedures for:
o	Moving equipment.
o	Handling portable devices.
""",
                        "tools": """
•	Device Protection: Rack enclosures, locks.
•	Maintenance Tools: Maintenance schedules in Excel or ServiceNow


""",
                        "deliverables": """
•	Maintenance schedules and logs.
•	approved procedures for the security of devices.
•	Evidence of implemented physical security measures.

""",
                     },   
                 
           {
                        "name": " 2-14-4: Periodic Review of Physical Security Requirements",
                        "description": "",
                        "section": "2-14-4",
                        "purpose": "Regularly review and update physical security controls to ensure continued compliance.",
                        "implementation_steps": """
1.	Develop a Review Schedule:
o	Conduct quarterly assessments of physical security measures.
2.	Update Policies:
o	Revise policies based on findings or regulatory changes.
3.	Document Changes:
o	Log updates and ensure formal approval.

""",
                        "examples": """
""",
                        "tools": """
•	Review Management: Microsoft Planner, ServiceNow.
•	Reporting Tools: Power BI, Tableau.


""",
                        "deliverables": """
•	Review reports.
•	Updated policies with evidence of approval.

""",
                     },
                     
           {
                        "name": " 2-15-1: Define and Approve Cybersecurity Requirements for Web Applications",
                        "description": "",
                        "section": "2-15-1",
                        "purpose": "Establish and document security requirements for external web applications",
                        "implementation_steps": """
1.	Develop a Web Application Protection Policy covering:
o	Web Application Firewalls (WAF).
o	Secure protocols (e.g., HTTPS).
o	Multi-factor authentication (MFA).
o	Secure development, testing, and user usage policies.
o	Vulnerability assessments and regular backups.
2.	Obtain formal approval from executive management.
""",
                        "examples": """
1. Purpose:
To ensure the protection of external web applications from cyber threats.
2. Scope:
This policy applies to all external web applications, whether internally developed or procured from third parties.
3. Key Requirements:
- Deploy Web Application Firewalls (WAF) to prevent common web-based attacks.
- Enforce a multi-tier architecture, separating:
  - Database Tier
  - Business Tier
  - Presentation Tier
- Use secure communication protocols (e.g., HTTPS, TLS).
- Implement Multi-Factor Authentication (MFA) for all users.

""",
                        "tools": """
•	Policy Templates: Microsoft Word, SharePoint.

""",
                        "deliverables": """
•  Approved Web Application Protection Policy.
•	Evidence of management approval (e.g., signed document).

""",
                     },
                       
           {
                        "name": " 2-15-2: Implement Cybersecurity Requirements for Web Applications",
                        "description": "",
                        "section": "2-15-2",
                        "purpose": "Deploy security controls to safeguard external web applications.",
                        "implementation_steps": """
1.	Implement WAF: Protect against web-based attacks.
2.	Use HTTPS: Encrypt data during transmission.
3.	Enforce MFA: Secure user authentication.
4.	Conduct vulnerability assessments and regular backups.
5.	Develop an action plan to ensure compliance.

""",
                        "examples": """
Protect web applications from common web-based threats, such as SQL injection and cross-site scripting.
Select and implement a suitable WAF:
o	Configure the WAF to monitor and block malicious traffic.
Encrypt all communications between users and the web application.
o	Obtain and install SSL/TLS certificates for all web applications.
o	Redirect HTTP traffic to HTTPS using web server configurations.
Strengthen user authentication for web applications.
o	Integrate MFA for all user accounts accessing web application

""",
                        "tools": """
•	WAF: AWS WAF, F5 Advanced WAF.
•	SSL/TLS Encryption: Let’s Encrypt, DigiCert.
•	Vulnerability Scanning: Nessus, Qualys.


""",
                        "deliverables": """
•	Screenshots of implemented controls (e.g., WAF configurations, HTTPS links).
•	Evidence of MFA setup.
•	Action plane document.

""",
                     },
                     
           {
                        "name": " 2-15-3: Include Specific Security Requirements",
                        "description": "",
                        "section": "2-15-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                          {
    "name": "2-15-3-1: Web Application Firewalls (WAF)",
    "description": "Identify web applications and deploy WAF for protection and Ensure third-party vendors comply with WAF requirements.",
    "section": "2-15-3",
    "purpose": "",
    "implementation_steps": """
""",
    "examples": """
Choose a WAF solution based on organizational needs.
o Managed WAF: Automated rule sets with minimal configuration (e.g., AWS WAF, Cloudflare).
o Customizable WAF: Allows creating specific rules for enhanced control (e.g., F5 Advanced WAF).
Set up rules to detect and block malicious traffic.
o Enable predefined rules for common attacks (e.g., OWASP Top 10 vulnerabilities).
o Customize rules to address application-specific threats
Verify that third-party providers hosting web applications comply with WAF requirements.
o Request evidence of WAF deployment from vendors.
o Include WAF compliance clauses in service agreements.

""",
    "tools": """
• AWS WAF, F5 Advanced WAF.

""",
    "deliverables": """
• WAF configuration screenshots.
"""
},
                     
           {
                        "name": " 2-15-3-2: Multi-Tier Architecture",
    "description": "• Ensure web applications use a minimum of three tiers:\n1- Database\n2- Business Tier\n3- Presentation Tier\n",

                        "section": "2-15-3-2",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
Define and implement a multi-tier architecture for web applications, separating components into at least three layers:
o	Database Tier: Stores and manages data.
o	Business Tier: Processes application logic.
o	Presentation Tier: Handles user interface and interactions.
Verify that third-party web application providers use multi-tier architecture.
o	Request detailed architecture documentation from vendors.
o	Include multi-tier architecture compliance clauses in service agreements.

""",
                        "tools": """
•	Application Design: Lucidchart, Microsoft Visio.
""",
                        "deliverables": """
•	Web application architecture designs.
""",
                     }, 
                     
           {
                        "name": " 2-15-3-3: Secure Protocols",
                        "description": "Enforce HTTPS and other secure protocols for all web applications and Verify third-party vendor compliance.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
Transition all applications from HTTP to HTTPS for secure communication.
o	Obtain SSL/TLS certificates for web applications.
Use free options (e.g., Let’s Encrypt) or commercial providers (e.g., DigiCert).
o	Configure web servers to enforce HTTPS:
Redirect all HTTP traffic to HTTPS.
Ensure third-party vendors hosting web applications comply with secure protocol requirements.
o	Request documentation or screenshots showing HTTPS implementation.
o	Include HTTPS compliance clauses in contracts or service level agreements (SLAs).

""",
                        "tools": """
•	SSL/TLS Certificates: Let’s Encrypt, DigiCert.
•	Protocol Testing: Qualys SSL Labs, Burp Suite.


""",
                        "deliverables": """
•	Screenshots showing HTTPS in application URLs.
""",
                     },
                     
           {
                        "name": " 2-15-3-4: Secure Usage Policy",
                        "description": "Publish a clear secure usage policy for users and Share the policy on external web applications.",
                        "section": "2-15-3-4",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
Create a detailed policy outlining safe usage practices for web applications.
o	Purpose: Ensure safe and secure use of the organization’s web applications.
o	User Responsibilities:
Use strong, unique passwords for each account.
Enable multi-factor authentication (MFA).
Avoid accessing applications on public or unsecured networks.
o	Prohibited Actions:
Sharing account credentials.
Downloading unauthorized software or plugins.
Attempting to bypass security controls.
o	Incident Reporting:
Steps to report suspicious activity or security issues.
Make the policy accessible to users of the web applications.
o	Publish the policy on the organization’s external website in a visible section.
o	Ensure it is easily accessible to all users, including stakeholders and vendors.

""",
                        "tools": """
•	Policy Templates: Microsoft Word, SharePoint.

""",
                        "deliverables": """
•	Published policy on the organization’s website.
""",
                     },
                     
           {
                        "name": " 2-15-3-5: Multi-Factor Authentication (MFA)",
                        "description": "Enable MFA for all user access to web applications and Include MFA in the application development lifecycle.",
                        "section": "2-15-3-5",
                        "purpose": "",
                        "implementation_steps": """

""",
                        "examples": """
Choose a suitable MFA provider based on the organization’s needs.
o	Okta: Centralized access management with MFA capabilities.
o	Microsoft Authenticator: Secure and user-friendly MFA for Microsoft ecosystems.
o	Duo Security: Supports a wide range of applications with flexible MFA options.
Implement MFA for all external web applications.
o	Enable MFA in the application's authentication settings.
o	Configure supported MFA methods:
SMS-based OTP.
App-based OTP.
Biometric authentication.
o	Test the MFA setup for all user roles:
Regular users.
Privileged users.

""",
                        "tools": """
•	MFA Solutions: Okta, Microsoft Authenticator, Duo Security.

""",
                        "deliverables": """
•	Screenshots of MFA implementation.  
""",
                     },
                     
           {
                        "name": " 2-15-4: Periodic Review of Web Application Security",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "Ensure controls remain effective and updated",
                        "implementation_steps": """
1.	Conduct quarterly assessments of web applications.
2.	Review and update security policies and controls.
3.	Document changes and obtain approvals.

""",
                        "examples": """
""",
                        "tools": """
•	Compliance Tools: ServiceNow, Jira.
•	Reporting: Power BI, Tableau.


""",
                        "deliverables": """
•	Compliance assessment reports.
•	Updated policies with approval evidence.

""",
                     },
                     
                     {
                        "name": "2-12-3: Specific Requirements for Event Logs and Monitoring",
                        "description": "Activate Logs on Critical Information Assets 2-12-3-1",
                        "section": "2-12-3",
                        "purpose": "Activate and monitor event logs on critical systems.",
                        "implementation_steps": """
1. Enable logging on:
   - Servers, databases, network devices, and workstations.
2. Configure SIEM rules to monitor events from critical assets.
""",
                        "examples": """
Example 1: Connect all activated logs to a Security Information and Event Management (SIEM) system for centralized monitoring.
   - Configure Splunk to ingest Syslog data from network devices.
   - Integrate Windows Event Logs and Linux Syslogs with IBM QRadar.
   - Ensure applications and databases send logs to SIEM.

Example 2: Develop rules in SIEM to filter and prioritize logs based on severity.
   - Multiple failed login attempts within a short timeframe.
   - Privilege escalation events.
""",
                        "tools": """
Tool 1: SIEM: Splunk, IBM QRadar.
Tool 2: Asset Logging: Graylog, Syslog-NG.
""",
                        "deliverables": """
Deliverable 1: Screenshot of system logging configurations.
Deliverable 2: SIEM reports showing log activation for critical assets.
""",
                    },
                    {
                        "name": "2-12-3-2: Activate Logs for Remote Access and Privileged Accounts",
                        "description": "Activate and monitor event logs on critical systems.",
                        "section": "2-12-3",
                        "purpose": "Activate and monitor event logs on critical systems.",
                        "implementation_steps": """
1. Enable logs for:
   - Privileged accounts.
   - Remote access events.
2. Configure SIEM rules to monitor changes made by privileged accounts.
""",
                        "examples": """
Example 1: Configure SIEM to generate alerts for high-risk events.
   - Unauthorized remote access: Remote login from an unapproved IP address.
   - Privilege escalation attempts: Sudo command executed on Linux systems.
""",
                        "tools": """
Tool 1: Privileged Account Logging: CyberArk, BeyondTrust.
Tool 2: Remote Access Logging: Cisco AnyConnect, Windows Event Viewer.
""",
                        "deliverables": """
Deliverable 1: Evidence of activated logs for privileged accounts and remote access (e.g., SIEM screenshots).
""",
                    },
                    {
                        "name": "2-12-3-3: Identify Technologies for Log Collection",
                        "description": "Identify technologies required for log collection.",
                        "section": "2-12-3",
                        "purpose": "Identify technologies required for centralized logging.",
                        "implementation_steps": """
1. Define required technologies:
   - SIEM for centralized logging.
2. Connect all critical assets (e.g., applications, databases, network devices) to SIEM.
3. Conduct Periodic Review of Integration
""",
                        "examples": """
1. Regularly review the integration to ensure all new devices and systems are added to the SIEM.
   - Generate an asset inventory report from CMDB.
   - Cross-check the inventory with devices connected to the SIEM.
   - Add any missing devices or systems to the SIEM.
""",
                        "tools": """
Tool 1: SIEM Systems: Splunk, ArcSight.
Tool 2: Log Forwarding: Syslog, Fluentd.
""",
                        "deliverables": """
Deliverable 1: List of devices connected to SIEM.
Deliverable 2: Screenshot of SIEM dashboard showing connected devices.
""",
                    },
                    {
                        "name": "2-12-3-4: Continuous Monitoring of Cybersecurity Events",
                        "description": "Monitor cybersecurity events continuously.",
                        "section": "2-12-3",
                        "purpose": "Ensure continuous monitoring of cybersecurity events.",
                        "implementation_steps": """
1. Assign a 24/7 monitoring team (in-house or outsourced).
2. Ensure the SOC or monitoring provider is located in the Kingdom.
""",
                        "examples": """
Establish a team or outsource to an SOC to handle continuous log monitoring:
   - In-House Monitoring:
     - Create a shift schedule to ensure 24/7 coverage.
   - Outsourced Monitoring:
     - Contract with an SOC provider for real-time monitoring.
     - Ensure the SOC has access to the SIEM system within the organization.
""",
                        "tools": """
Tool 1: Monitoring Tools: Microsoft Sentinel, Splunk.
Tool 2: SOC Providers: STC, Innovative Solution.
Tool 3: Shift Management: Excel, ServiceNow.
""",
                        "deliverables": """
Deliverable 1: Shift breakdown table.
Deliverable 2: Contract with external SOC provider, if applicable.
Deliverable 3: Monitoring procedure document.
""",
                    },
                    {
                        "name": "2-12-3-5: Retention of Logs for at Least 12 Months",
                        "description": "Ensure log retention for at least 12 months.",
                        "section": "2-12-3",                       
                        "purpose": "Ensure log retention for at least 12 months.",
                        "implementation_steps": """
1. Configure SIEM to retain logs for 12+ months.
2. Regularly review stored logs to prevent premature overwriting.
""",
                        "examples": """
1. Periodically review retained logs to ensure compliance with the 12-month requirement.
   - Access historical logs in the SIEM or storage system.
   - Verify logs from at least 12 months ago are accessible.
   - Generate a report confirming retention compliance.
2. Allocate sufficient storage to support 12 months of log retention.
   - Calculate daily log volume (e.g., 5GB of logs per day = 1.8TB annually).
   - Use scalable storage solutions:
     - Local Storage: Network-attached storage (NAS).
     - Cloud Storage: AWS S3, Azure Blob Storage.
""",
                        "tools": """
Tool 1: Storage: AWS S3, Azure Blob Storage.
Tool 2: SIEM Log Management: Splunk, Graylog.
""",
                        "deliverables": """
Deliverable 1: Screenshot of SIEM retention settings.
Deliverable 2: Sample of logs retained for over 12 months.
""",
                    },
                    {
                        "name": "2-12-4: Periodic Review of Event Logs and Monitoring",
                        "description": "Regular review and update of event logging and monitoring policies.",
                        "section": "2-12-4",
                        "purpose": "Regularly review and update event logging requirements.",
                        "implementation_steps": """
1. Conduct quarterly reviews of:
   - Logging configurations.
   - Monitoring practices.
2. Update policies and procedures based on new regulations or organizational needs.
3. Document review findings and approvals.
""",
                        "examples": """
1. Log Retention Compliance:
   - Verify logs are stored for the required 12-month minimum.
   - Sample older logs from SIEM or storage systems.
2. SIEM Configuration:
   - Confirm all critical devices and systems are integrated with the SIEM.
   - Ensure alert rules are effective and up-to-date.
3. Monitoring Effectiveness:
   - Evaluate response times to alerts.
   - Validate SOC performance metrics (e.g., average time to detect and respond).
""",
                        "tools": """
Tool 1: Monitoring and Audit: Splunk, ManageEngine.
Tool 2: Policy Updates: Microsoft Word, SharePoint.
""",
                        "deliverables": """
Deliverable 1: Review report summarizing findings.
Deliverable 2: Compliance report.
Deliverable 3: Updated Event Logs and Monitoring Management Policy.
Deliverable 4: Approved review schedule.
""",
                    },
 {
                        "name": "2-12-3: Specific Requirements for Event Logs and Monitoring",
                        "description": "Activate Logs on Critical Information Assets 2-12-3-1",
                        "section": "2-12-3",
                        "purpose": "Activate and monitor event logs on critical systems.",
                        "implementation_steps": """
1. Enable logging on:
   - Servers, databases, network devices, and workstations.
2. Configure SIEM rules to monitor events from critical assets.
""",
                        "examples": """
Example 1: Connect all activated logs to a Security Information and Event Management (SIEM) system for centralized monitoring.
   - Configure Splunk to ingest Syslog data from network devices.
   - Integrate Windows Event Logs and Linux Syslogs with IBM QRadar.
   - Ensure applications and databases send logs to SIEM.

Example 2: Develop rules in SIEM to filter and prioritize logs based on severity.
   - Multiple failed login attempts within a short timeframe.
   - Privilege escalation events.
""",
                        "tools": """
Tool 1: SIEM: Splunk, IBM QRadar.
Tool 2: Asset Logging: Graylog, Syslog-NG.
""",
                        "deliverables": """
Deliverable 1: Screenshot of system logging configurations.
Deliverable 2: SIEM reports showing log activation for critical assets.
""",
                    },
                    {
                        "name": "2-12-3-2: Activate Logs for Remote Access and Privileged Accounts",
                        "description": "Activate and monitor event logs on critical systems.",
                        "section": "2-12-3",
                        "purpose": "Activate and monitor event logs on critical systems.",
                        "implementation_steps": """
1. Enable logs for:
   - Privileged accounts.
   - Remote access events.
2. Configure SIEM rules to monitor changes made by privileged accounts.
""",
                        "examples": """
Example 1: Configure SIEM to generate alerts for high-risk events.
   - Unauthorized remote access: Remote login from an unapproved IP address.
   - Privilege escalation attempts: Sudo command executed on Linux systems.
""",
                        "tools": """
Tool 1: Privileged Account Logging: CyberArk, BeyondTrust.
Tool 2: Remote Access Logging: Cisco AnyConnect, Windows Event Viewer.
""",
                        "deliverables": """
Deliverable 1: Evidence of activated logs for privileged accounts and remote access (e.g., SIEM screenshots).
""",
                    },
                    {
                        "name": "2-12-3-3: Identify Technologies for Log Collection",
                        "description": "Identify technologies required for log collection.",
                        "section": "2-12-3",
                        "purpose": "Identify technologies required for centralized logging.",
                        "implementation_steps": """
1. Define required technologies:
   - SIEM for centralized logging.
2. Connect all critical assets (e.g., applications, databases, network devices) to SIEM.
3. Conduct Periodic Review of Integration
""",
                        "examples": """
1. Regularly review the integration to ensure all new devices and systems are added to the SIEM.
   - Generate an asset inventory report from CMDB.
   - Cross-check the inventory with devices connected to the SIEM.
   - Add any missing devices or systems to the SIEM.
""",
                        "tools": """
Tool 1: SIEM Systems: Splunk, ArcSight.
Tool 2: Log Forwarding: Syslog, Fluentd.
""",
                        "deliverables": """
Deliverable 1: List of devices connected to SIEM.
Deliverable 2: Screenshot of SIEM dashboard showing connected devices.
""",
                    },
                    {
                        "name": "2-12-3-4: Continuous Monitoring of Cybersecurity Events",
                        "description": "Monitor cybersecurity events continuously.",
                        "section": "2-12-3",
                        "purpose": "Ensure continuous monitoring of cybersecurity events.",
                        "implementation_steps": """
1. Assign a 24/7 monitoring team (in-house or outsourced).
2. Ensure the SOC or monitoring provider is located in the Kingdom.
""",
                        "examples": """
Establish a team or outsource to an SOC to handle continuous log monitoring:
   - In-House Monitoring:
     - Create a shift schedule to ensure 24/7 coverage.
   - Outsourced Monitoring:
     - Contract with an SOC provider for real-time monitoring.
     - Ensure the SOC has access to the SIEM system within the organization.
""",
                        "tools": """
Tool 1: Monitoring Tools: Microsoft Sentinel, Splunk.
Tool 2: SOC Providers: STC, Innovative Solution.
Tool 3: Shift Management: Excel, ServiceNow.
""",
                        "deliverables": """
Deliverable 1: Shift breakdown table.
Deliverable 2: Contract with external SOC provider, if applicable.
Deliverable 3: Monitoring procedure document.
""",
                    },
                    {
                        "name": "2-12-3-5: Retention of Logs for at Least 12 Months",
                        "description": "Ensure log retention for at least 12 months.",
                        "section": "2-12-3",                       
                        "purpose": "Ensure log retention for at least 12 months.",
                        "implementation_steps": """
1. Configure SIEM to retain logs for 12+ months.
2. Regularly review stored logs to prevent premature overwriting.
""",
                        "examples": """
1. Periodically review retained logs to ensure compliance with the 12-month requirement.
   - Access historical logs in the SIEM or storage system.
   - Verify logs from at least 12 months ago are accessible.
   - Generate a report confirming retention compliance.
2. Allocate sufficient storage to support 12 months of log retention.
   - Calculate daily log volume (e.g., 5GB of logs per day = 1.8TB annually).
   - Use scalable storage solutions:
     - Local Storage: Network-attached storage (NAS).
     - Cloud Storage: AWS S3, Azure Blob Storage.
""",
                        "tools": """
Tool 1: Storage: AWS S3, Azure Blob Storage.
Tool 2: SIEM Log Management: Splunk, Graylog.
""",
                        "deliverables": """
Deliverable 1: Screenshot of SIEM retention settings.
Deliverable 2: Sample of logs retained for over 12 months.
""",
                    },
                    {
                        "name": "2-12-4: Periodic Review of Event Logs and Monitoring",
                        "description": "Regular review and update of event logging and monitoring policies.",
                        "section": "2-12-4",
                        "purpose": "Regularly review and update event logging requirements.",
                        "implementation_steps": """
1. Conduct quarterly reviews of:
   - Logging configurations.
   - Monitoring practices.
2. Update policies and procedures based on new regulations or organizational needs.
3. Document review findings and approvals.
""",
                        "examples": """
1. Log Retention Compliance:
   - Verify logs are stored for the required 12-month minimum.
   - Sample older logs from SIEM or storage systems.
2. SIEM Configuration:
   - Confirm all critical devices and systems are integrated with the SIEM.
   - Ensure alert rules are effective and up-to-date.
3. Monitoring Effectiveness:
   - Evaluate response times to alerts.
   - Validate SOC performance metrics (e.g., average time to detect and respond).
""",
                        "tools": """
Tool 1: Monitoring and Audit: Splunk, ManageEngine.
Tool 2: Policy Updates: Microsoft Word, SharePoint.
""",
                        "deliverables": """
Deliverable 1: Review report summarizing findings.
Deliverable 2: Compliance report.
Deliverable 3: Updated Event Logs and Monitoring Management Policy.
Deliverable 4: Approved review schedule.
""",
                    },
                             
                ]
                
            },
        ],
    },
{
    "name": "3 - Cybersecurity Resilience",
    "subdomains": [
        {
            "name": "3-1 Cybersecurity Resilience Aspects of Business Continuity Management (BCM)",
            "controls": [
                
           {
                        "name": "3-1-1: Define, Document, and Approve Cybersecurity Requirements for BCM",
                        "description": "",
                        "section": "3-1",
                        "purpose": "Create a comprehensive policy covering BCM's cybersecurity aspects",
                        "implementation_steps": """
•	Define cybersecurity requirements, including:
o	Continuity of cybersecurity systems.
o	Incident response plans.
o	Disaster recovery plans.
•	Document and approve these requirements through executive management.

""",
                        "examples": """
Purpose:
To integrate cybersecurity resilience into the organization’s BCM framework, ensuring operational continuity during disruptions.
Scope:
This policy applies to all critical systems, information assets, and stakeholders involved in BCM.
Key Requirements:
o	High availability for cybersecurity systems.
o	Cyber incident response plans.
o	Disaster recovery procedures.
o	Periodic testing of BCM plans.

""",
                        "tools": """
•	Policy Drafting: Microsoft Word.

""",
                        "deliverables": """
•	Approved Cybersecurity BCM Policy.
•	Evidence of approval (e.g., signed document, email).

""",
                     },
                     
           {
                        "name": " 3-1-2: Implement Cybersecurity Requirements for BCM",
                        "description": "",
                        "section": "3-1",
                        "purpose": "Operationalize BCM policies to protect the organization from disruptions.",
                        "implementation_steps": """
1.	Develop an action plan for cybersecurity requirements in BCM.
2.	Implement and document BCM-related controls, such as:
o	Business continuity plans.
o	Cybersecurity incident response plans.
o	Disaster recovery plans.
3.	Test disaster recovery plans and report results.

""",
                        "examples": """
Outline specific tasks, timelines, and responsibilities to implement cybersecurity requirements in BCM.
•	Define objectives for cybersecurity resilience.
•	Assign tasks to relevant teams:
o	IT team: Implement disaster recovery systems.
o	Security team: Monitor incident response activities.
o	Business Continuity team: Coordinate recovery efforts.
•	Set deadlines for key activities:
o	Implement cybersecurity systems.
o	Test recovery plans.
Incorporate approved cybersecurity requirements into the organization’s BCM framework.
•	Incident Response Plans: Integrate cybersecurity-related scenarios, including ransomware or DDoS attacks.
•	Continuity Plans: Ensure critical cybersecurity systems (e.g., firewalls, SIEM) are part of BCM.
•	Disaster Recovery Plans: Add steps for restoring cybersecurity systems and ensuring data integrity.

""",
                        "tools": """
•	Project Management: Microsoft Project, Trello.
•	Simulation and Testing: IBM Resilient, Tabletop Simulators.


""",
                        "deliverables": """
•	Action plan document.
•	Approved business continuity and disaster recovery plans.
•	Test reports for recovery plans.

""",
                     },
                     
           {
                        "name": " 3-1-3: Include Key Cybersecurity Requirements in BCM",
                        "description": "",
                        "section": "3-1",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
           {
                        "name": "3-1-3-1: Ensure Continuity of Cybersecurity Systems and Procedures",
                        "description": "",
                        "section": "3-1",
                        "purpose": "",
                        "implementation_steps": """
•	Laws and regulations must be defined.
•	Identify high-risk cybersecurity incidents and include them in BCM.
•	Conduct a Business Impact Analysis (BIA) for critical systems.
•	Develop plans ensuring cybersecurity services continuity.

""",
                        "examples": """
Identify and document critical cybersecurity systems and processes essential for continuity.
•	Identify high-risk cybersecurity incidents that could disrupt operations.
•	Define critical cybersecurity systems, such as:
o	Firewalls
o	SIEM systems
o	Identity and Access Management (IAM)
Assess the impact of potential disruptions to critical cybersecurity systems.
•	Identify the organization’s critical systems and their importance.
•	Estimate downtime tolerances for each system.
•	Analyze the impact of cybersecurity incidents on operations.
Create continuity plans to ensure uninterrupted operations of cybersecurity systems.
•	Implement high-availability configurations for critical systems.
•	Define failover mechanisms to alternate systems or sites.
•	Establish backup and restore procedures for cybersecurity systems and data.
•	Identify key personnel responsible for cybersecurity systems during incidents.
•	Define responsibilities for maintaining and restoring system availability.

""",
                        "tools": """
•	BIA Tools: RiskWatch, Resolver.
•	High Availability Solutions: VMware vSphere, Azure Site Recovery.
•	Backup Solutions: Veeam, Acronis.


""",
                        "deliverables": """
•	Business continuity management program.
•	Continuity plans with risk and impact assessments.
•	Reports on the implementation of BCP tests.

""",
                     },
                     
           {
                        "name": "3-1-3-2: Develop Response Plans for Cybersecurity Incidents",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Create response plans covering:
o	Incident types and severity classifications.
o	Incident phases: detection, containment, recovery, and review.
o	Roles and responsibilities.
•	Periodically review and update response plans.

""",
                        "examples": """
Identify and document the essential elements of a cybersecurity incident response plan that aligns with business continuity objectives.
Requirements Example:
•	Classify incidents by severity:
o	Low: Minor phishing attempts.
o	Medium: Malware detected in non-critical systems.
o	High: Ransomware attack affecting critical systems.
•	Define roles and responsibilities:
o	IT Team: Containment and eradication.
o	BCM Team: Recovery coordination.
o	Leadership: Communication with stakeholders.
•	Map incidents to response phases:
o	Planning and Preparation.
o	Detection and Analysis.
o	Containment, Eradication, and Recovery.
o	Post-Incident Review and Learning.

""",
                        "tools": """
•	Incident Response Playbooks: NCA Playbooks, ServiceNow.
•	Reporting and Monitoring Tools: Jira, Splunk.
•	Risk Management Tools: Resolver, SAP GRC
""",
                        "deliverables": """
•	Incident response plans.
•	Incident reports including containment and recommendations.

""",
                     },
                     
           {
                        "name": "3-1-3-3: Develop Disaster Recovery Plans",
                        "description": "",
                        "section": "3-1",
                        "purpose": "",
                        "implementation_steps": """
1.	Identify disaster recovery team and risks.
2.	Conduct a Business Impact Analysis for critical systems.
3.	Define backup and restore procedures.
4.	Establish and test a disaster recovery center.

""",
                        "examples": """
Create a comprehensive plan to restore critical systems after an incident.
•	Disaster Recovery Team:
o	Identify team members and their responsibilities.
•	Backup and Storage Procedures:
o	Define data backup schedules and storage locations (on-site/off-site/cloud).
•	Recovery Steps:
o	Detailed instructions for restoring systems and services.
•	Alternate Site Procedures:
o	Steps to activate the disaster recovery center (if applicable).
•	Communication Plan:
o	Notify stakeholders about recovery progress.
Set up a secondary site or recovery infrastructure for critical systems.
•	Identify location (on-premises, off-site, or cloud-based).
•	Configure systems for data replication.
•	Ensure network connectivity between the primary and recovery sites.
Assess the impact of potential disasters on business operations.
•	Identify critical business processes and their dependencies.
•	Quantify potential losses (financial, operational, reputational).
•	Use findings to prioritize recovery efforts.

""",
                        "tools": """
•	Cloud-Based Recovery: Microsoft Azure Site Recovery, AWS Disaster Recovery.
•	Disaster Recovery Testing: AWS Disaster Recovery


""",
                        "deliverables": """
•	Disaster recovery plans.
•	Test reports for disaster recovery processes.

""",
                     },
                     
           {
                        "name": " 3-1-4: Periodic Review of BCM Cybersecurity Requirements",
                        "description": "",
                        "section": "3-1",
                        "purpose": "Ensure BCM cybersecurity policies remain relevant and effective.",
                        "implementation_steps": """
1.	Review cybersecurity requirements periodically or after changes in laws.
2.	Document updates and obtain formal approval for revised policies.

""",
                        "examples": """

""",
                        "tools": """
•	Compliance Management: ServiceNow, SAP GRC.
•	Reporting Tools: Power BI, Tableau.


""",
                        "deliverables": """
•	Review schedule.
•	Compliance assessment reports.
•	Updated and approved policies.

""",
                     },
            ]
            
        }
        
    ]
    
},
 {
    "name": "4 - Third-Party and Cloud Computing Cybersecurity",
    "subdomains": [
        {
            "name": "4-1: Third-Party Cybersecurity",
            "controls": [
                
           {
                        "name": "4-1-1: Define Cybersecurity Requirements for Third-Party Contracts",
                        "description": "",
                        "section": "4-1",
                        "purpose": "Develop a comprehensive policy covering cybersecurity requirements for third-party agreements.",
                        "implementation_steps": """
Implementation Steps:
•	Include requirements in contracts for:
o	Confidentiality clauses.
o	Cyber incident management.
o	Data protection standards.
•	Define third-party risk assessment procedures.
•	Obtain executive approval for the policy.

""",
                        "examples": """
•	Purpose:
	To protect organizational assets by defining cybersecurity requirements for third-party contracts 	and agreements.
•	Scope:
	This policy applies to all third-party vendors, service providers, and contractors engaged by the 	organization.
•	Requirements:
	Contracts must include:
   		- Non-disclosure agreements (NDA).
   		- Secure data handling and removal clauses.
   		- Incident management procedures.
	All third-party services must undergo a cybersecurity risk assessment.

""",
                        "tools": """
•	Documentation: Microsoft Word, SharePoint.

""",
                        "deliverables": """
•	Approved Third-Party Cybersecurity Policy.
•	Evidence of executive approval (e.g., signed document, email).

""",
                     },
                     
           {
                        "name": " 4-1-2: Ensure Specific Cybersecurity Requirements in Contracts",
                        "description": "",
                        "section": "4-1",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": "4-1-2-1: Confidentiality and Secure Data Removal",
                        "description": "1.	Add non-disclosure clauses to all third-party agreements. \n 2.	Ensure contracts require secure removal of organizational data upon service termination.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
•	Confidentiality Clause:
	The third party agrees to maintain the confidentiality of all organizational data and information 	accessed during the agreement. No information shall be disclosed without prior written approval 	from the organization.
•	Secure Data Removal Clause:
	Upon termination of the contract, the third party must securely delete or destroy all 		organizational data within 30 days. A certificate of secure data removal must be submitted to the 	organization as evidence of compliance.

""",
                        "tools": """
•	Documentation: Microsoft Word, SharePoint.

""",
                        "deliverables": """
•	Signed contracts with confidentiality and secure data removal clauses.
""",
                     },
                     
           {
                        "name": " 4-1-2-2: Incident Communication Procedures",
                        "description": "1.	Define communication protocols for cybersecurity incidents in contracts. \n2.	Include escalation mechanisms and reporting timelines.",
                        "section": "4-1",
                        "purpose": "",
                        "implementation_steps": """

""",
                        "examples": """
The third party is required to:
•	Report cybersecurity incidents affecting the organization within 24 hours of detection.
•	Provide detailed incident reports, including:
-	Incident classification (e.g., Low, Medium, High, Critical).
-	Initial assessment of the scope and impact.
-	Steps taken for containment and mitigation.

""",
                        "tools": """
•	Communication Tools: ServiceNow, Slack.
""",
                        "deliverables": """
•	Procedures for incident communication in signed contracts.
""",
                     },
                     
           {
                        "name": " 4-1-2-3: Compliance with Policies and Regulations",
                        "description": "1.	Ensure contracts obligate third parties to comply with: \n o	Organizational policies.\no	Relevant laws and regulations.\n2.	Include compliance clauses in all agreements.",
                        "section": "4-1",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
The third party shall:
•	Adhere to the organization’s cybersecurity policies and procedures.
•	Comply with applicable laws and regulations.
•	Submit to periodic audits by the organization or authorized third parties to ensure compliance.

""",
                        "tools": """
•	Compliance Assessment: RiskWatch, SAP GRC.

""",
                        "deliverables": """
•	Signed agreements with compliance clauses.
""",
                     },
                     
           {
                        "name": " 4-1-3: Additional Cybersecurity Requirements for IT Outsourcing and Managed Services",
                        "description": "",
                        "section": "4-1",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": " 4-1-3-1: Cybersecurity Risk Assessment",
                        "description": "1.	Conduct third-party risk assessments before signing agreements or when regulations change. \n 2.	Identify and mitigate risks associated with third-party services.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
Perform a comprehensive evaluation of the third party’s cybersecurity practices
Steps:
•	Use questionnaires or interviews to gather information about:
o	Data handling and protection measures.
o	Access control and authentication protocols.
•	Assess risks based on:
o	Potential impact on the organization.
o	Likelihood of a security breach.

""",
                        "tools": """
•	Risk Assessment Tools: RiskWatch, Microsoft Excel.

""",
                        "deliverables": """
•	Third-party risk assessment reports.
""",
                     },
                     
           {
                        "name": " 4-1-3-2: Managed Services Centers in Saudi Arabia",
                        "description": "1.	Ensure managed service centers are located within Saudi Arabia. \n 2.	Require remote access to services to be restricted within the Kingdom.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """
•	SLA Monitoring Tools: Jira, ServiceNow.

""",
                        "deliverables": """
•	Evidence of service centers and remote access compliance.
""",
                     },
                     
           {
                        "name": " 4-1-4: Periodic Review of Third-Party Cybersecurity Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": ": Regularly review and update cybersecurity requirements for third-party agreements.",
                        "implementation_steps": """
1.	Conduct periodic reviews based on a documented schedule.
2.	Update contracts to align with regulatory changes.

""",
                        "examples": """
""",
                        "tools": """
•	Compliance Management: SAP GRC, Tableau.

""",
                        "deliverables": """
•	Updated policies with review logs.
•	Compliance assessment reports.

""",
                     },
                     
           {
                        "name": "4-2-1 Cybersecurity Requirements for Hosting and Cloud Computing Services",
                        "description": "Define and document cybersecurity requirements for using hosting and cloud computing services.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
Key Requirements:
•	Include clauses in contracts for:
o	Data hosting and location.
o	Data retrieval and secure removal upon service termination.
o	Non-disclosure agreements.
o	Service Level Agreements (SLAs).
•	Classify data before hosting.

""",
                        "examples": """
Create a detailed policy document covering all necessary requirements.
•	Contract Requirements:
o	Include clauses for data security, confidentiality, and compliance with KSA regulations.
o	Ensure Service Level Agreements (SLAs) and Non-Disclosure Agreements (NDAs) are included.
•	Hosting Location:
o	Specify that all data and systems must be hosted within Saudi Arabia.
•	Data Handling:
o	Require procedures for secure data removal and retrieval upon service termination.
•	Data Classification:
o	Ensure data is classified according to sensitivity before being hosted on cloud services.
•	Access Control:
o	Mandate strict access control mechanisms, including Multi-Factor Authentication (MFA).
•	Incident Response:
o	Define responsibilities and response times for cybersecurity incidents.

""",
                        "tools": """
•	Policy Templates: Microsoft Word.

""",
                        "deliverables": """
•	Cybersecurity policy with hosting and cloud requirements.
•	Signed contracts with clauses for location, data protection, and SLAs.

""",
                     },
                     
           {
                        "name": "4-2-2 Implementation of Hosting and Cloud Security Requirements",
                        "description": "Enforce cybersecurity measures for cloud and hosting services.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
Key Implementation Steps:
•	Ensure hosting location is within KSA.
•	Activate and monitor event logs for hosted assets.
•	Encrypt data stored in, transmitted to, or from the cloud.
•	Perform regular backups and secure them.
•	Maintain separation between the organization’s virtual environment and others.

""",
                        "examples": """
Verify that all hosted data and systems are located in Saudi Arabia.
•	Include location-specific clauses in the service contract:
o	Data and system hosting must be within the KSA.
o	Hosting provider must comply with NCA guidelines.
•	Request confirmation from the cloud service provider of data hosting location.
•	Conduct site verification or request documentation confirming data storage location.

""",
                        "tools": """
•	Event Monitoring: Splunk, Elastic Stack.
•	Encryption: BitLocker, AWS Key Management Service (KMS).
•	Backup Management: Veeam, Azure Backup.


""",
                        "deliverables": """
•	Action plan for implementing cybersecurity requirements.
•	Contracts with hosting providers ensuring compliance with cybersecurity standards.

""",
                     },
                     
           {
                        "name": "4-2-3 Specific Hosting and Cloud Computing Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": "4-2-3-1 Data Classification and Retrieval",
                        "description": "Classify data before hosting and ensure data is retrievable after service termination.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Classify data based on sensitivity and importance.
•	Ensure retrievability through agreed procedures with service providers.

""",
                        "examples": """
•	Identify and categorize data based on its sensitivity and importance to the organization.
o	Identify Data:
List all data assets intended for cloud hosting, including documents, databases, and media.
o	Classify Data:
Assign classification levels based on organizational policies (e.g., Confidential, Internal, Public).
•	Develop procedures to ensure the organization can retrieve data in a usable format after service termination.
o	Include retrieval requirements in the service contract:
Data must be returned in a usable format (e.g., .CSV, .SQL backup).
o	Ensure secure deletion of the organization's data from the provider’s servers.
Develop an internal plan for validating retrieved data:
o	Confirm data integrity and completeness.
Test retrieval processes during the service period.

""",
                        "tools": """
•	Classification Tools: Varonis, Microsoft Information Protection.
•	Policy Drafting: SharePoint, Microsoft Word

""",
                        "deliverables": """
•	Classified data list.
•	Procedures for secure data retrieval.

""",
                     },
                     
           {
                        "name": "4-2-3-2 Environment Separation",
                        "description": "Ensure organizational environments are separated from others in the cloud.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Define separation requirements (e.g., virtual servers, networks).
•	Include environment separation clauses in contracts.

""",
                        "examples": """
•	Specify the need for isolated virtual environments to protect the organization’s data and infrastructure.
o	Document Requirements:
o	Define the separation scope (e.g., virtual servers, databases, storage, networks).
o	Include technical specifications like Virtual Private Clouds (VPCs), firewalls, and isolated network segments.
•	Incorporate in Contracts:
o	Add clauses in contracts requiring environment separation.

""",
                        "tools": """

•	Network Isolation: VMware vSphere, Microsoft Azure Virtual Networks.

""",
                        "deliverables": """
•	Contract clauses ensuring environment separation.
•	Evidence of implemented separation.

""",
                     },
                     
           {
                        "name": "4-2-3-3 Hosting Within KSA",
                        "description": "Store and host data within Saudi Arabia.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Include location requirements in service contracts.
•	Verify hosting location is within KSA.

""",
                        "examples": """
""",
                        "tools": """
•	Cloud providers with local compliance (e.g., STC Cloud, AWS KSA).

""",
                        "deliverables": """
•	Contracts with hosting location clauses.
•	Evidence of data storage within KSA.

""",
                     },
                     
           {
                        "name": "4-2-4 Periodic Review of Cloud Cybersecurity Requirements",
                        "description": "Regularly review and update cloud computing and hosting policies.",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
Key Review Steps:
•	Conduct annual reviews or when laws change.
•	Document updates and secure formal approval.

""",
                        "examples": """
""",
                        "tools": """
•	Compliance Management: SAP GRC, LogicGate.
•	Policy Management: Confluence, SharePoint


""",
                        "deliverables": """
•	Reviewed and updated policy.
•	Documentation of changes with formal approval.

""",
                     },
                     
                
                        ]
        }
    ]
},
{
    "name": "5 - Industrial Control Systems Cybersecurity(ICS)",
    "subdomains": [
        {
            "name": "5-1:Industrial Control Systems (ICS) Protection",
            "controls": [
                
           {
                        "name": "Industrial Control Systems (ICS) Protection",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Develop a comprehensive ICS/OT cybersecurity policy.
•	Include:
o	Protection of ICS/OT networks.
o	Access control measures.
o	Incident response protocols specific to ICS.
•	Secure formal approval from executive management.

""",
                        "examples": """
•	Identify ICS/OT Cybersecurity Requirements:
o	Determine requirements for:
o	Protecting industrial networks.
o	Managing access to ICS/OT systems.
o	Incident response protocols specific to industrial environments.
•	Develop ICS/OT Cybersecurity Policy:
o	Create a formal policy covering:
o	Network segmentation.
o	Physical and logical security measures.
o	Cybersecurity incident management for ICS/OT systems.

""",
                        "tools": """
•	ICS Policy Templates: https://cdn.nca.gov.sa/api/files/public/upload/4ae174c2-06e2-4e10-ba70-4e7547b8f984_POLICY_Cybersecurity_Industrial_Controls_Systems_template_en-.pdf
•	Document Collaboration Tools: SharePoint, Google Workspace.


""",
                        "deliverables": """
•	Approved ICS/OT cybersecurity policy.
•	Formal approval document.
""",
                     },
                     
           {
                        "name": "5-1-2 Implement ICS/OT Cybersecurity Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Apply documented cybersecurity requirements for ICS/OT protection.
•	Develop an action plan for implementation.
•	Integrate cybersecurity measures into ICS/OT operational procedures for compliance.

""",
                        "examples": """
Create a comprehensive plan to address all cybersecurity requirements for ICS/OT.
•	Identify all ICS/OT systems within the organization.
•	Define specific security measures based on risk assessments, including physical and logical controls.
•	Outline responsibilities for implementing and maintaining cybersecurity requirements.

""",
                        "tools": """
•	Monitoring and Testing: SolarWinds, Nessus.
•	Access Management: Okta, CyberArk.


""",
                        "deliverables": """
•	Action plan for ICS/OT cybersecurity.
•	ICS/OT protection procedure documents.

""",
                     },
                     
           {
                        "name": " 5-1-3 Specific ICS/OT Cybersecurity Requirements",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
""",
                     },
                     
           {
                        "name": "5-1-3-1 Network Segmentation",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Define and isolate ICS/OT networks.
•	Physically and logically segment ICS networks from corporate and external networks.
•	Document risk analysis and segmentation strategies.

""",
                        "examples": """
•	Identify and document all ICS/OT and corporate networks within the organization.
o	Conduct a network inventory to identify all devices and connections.
o	Create a detailed network topology diagram.
•	Isolate ICS/OT networks from corporate networks using physical and logical methods.
o	Set up physical firewalls between ICS/OT and corporate networks.
o	Use VLANs and industrial demilitarized zones (IDMZ) for virtual segmentation.
o	Restrict inter-network traffic to only necessary communications.

""",
                        "tools": """
•	Network Mapping: SolarWinds, Nmap.
•	Firewall and Segmentation: Palo Alto, Cisco VLANs.


""",
                        "deliverables": """
•	Segmentation policy and network design plan.
""",
                     },
                     
           {
                        "name": "5-1-3-2 Segmentation with External Networks",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Restrict ICS/OT network connectivity with external networks.
•	Isolate industrial systems and networks from external networks:
o	 The Internet.
o	 Remote Access.
o	 Wireless Network.
•	 Conduct risk analysis before establishing any external connection.

""",
                        "examples": """
Isolate ICS/OT systems and networks from external networks using physical and logical means.
•	Use firewalls and industrial demilitarized zones (IDMZ) to separate external traffic.
•	Implement secure remote access solutions such as VPNs and jump servers.
•	Configure wireless networks with secure protocols (e.g., WPA3, NCS-1:2020).

""",
                        "tools": """
•	VPN Solutions: Cisco AnyConnect, FortiClient
•	Wireless Security Tools: Aruba Networks, RADIUS Authentication.


""",
                        "deliverables": """
•	Approved external network segmentation plan.
""",
                     },
                     
           {
                        "name": "5-1-3-3 Continuous Monitoring",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Enable cybersecurity event logs on ICS/OT systems.
•	Link logs to a SIEM system for centralized monitoring.
•	Assign a dedicated team for 24/7 log monitoring.

""",
                        "examples": """
•	Configure industrial network systems to enable event logging.
o	Identify critical ICS/OT systems and devices requiring event logging.
o	Enable logging features on these systems (e.g., firewalls, routers, PLCs).
•	Connect the ICS/OT event logs to a centralized SIEM for monitoring and analysis.
o	Select a SIEM system qualified for ICS/OT environments.
o	Integrate logs from ICS/OT devices into the SIEM.
•	Establish a team to monitor the cybersecurity logs and respond to incidents.
o	Assign dedicated personnel to review logs 24/7.
o	Train the team to identify and respond to potential threats.

""",
                        "tools": """
•	Logging Systems: Siemens WinCC, Rockwell.
•	SIEM Integration: Splunk, ArcSight.


""",
                        "deliverables": """
•	Monitoring logs and configurations.
•	Team schedules for continuous monitoring.

""",
                     },
                     
           {
                        "name": "5-1-3-4 Isolation of Safety Instrumented Systems (SIS)",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Isolate SIS systems from engineering and other industrial systems.
•	Define and assess risks for connected SIS systems.
•	Physically or logically separate SIS networks.

""",
                        "examples": """
•	Catalog and assess all SIS systems in the organization.
o	Create an inventory of all SIS devices, including their connections to other systems.
o	Conduct a risk assessment to identify potential cyber threats and vulnerabilities associated with SIS.
•	Apply isolation measures to SIS systems based on risk assessment findings.
o	Physical Isolation: Separate SIS physically from other networks using air gaps or dedicated hardware.
o	Logical Isolation: Use VLANs, firewalls, or DMZs to segment SIS from other systems

""",
                        "tools": """
•	Monitoring: Splunk, IBM QRadar.

""",
                        "deliverables": """
•	Approved SIS network isolation design.
""",
                     },
                     
           {
                        "name": "5-1-3-5 Restriction on External Storage Media",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Prevent unauthorized use of external storage via configuration.
•	Develop and enforce approval procedures for storage media usage.

""",
                        "examples": """
•	Implement automatic restrictions on industrial systems to prevent unauthorized use of external storage media.
o	Use endpoint protection tools to disable external storage media access on ICS systems.
•	Develop and enforce a process for requesting and approving the use of external storage media.
o	Require users to submit a formal request, including justification and usage duration.
o	Limit approvals to designated personnel with documented procedures.

""",
                        "tools": """
•	Endpoint Protection: Symantec Endpoint Protection, McAfee

""",
                        "deliverables": """
•	Procedures for storage media restrictions.
•	Configuration screenshots of implemented controls.

""",
                     },
                     
           {
                        "name": "5-1-3-6 Mobile Device Restrictions",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Restrict connectivity of mobile devices to ICS/OT networks.
•	Implement authentication mechanisms for authorized devices.

""",
                        "examples": """
•	Configure technical restrictions to prevent unauthorized mobile devices from connecting to ICS networks.
o	Deploy network access control (NAC) solutions to enforce device authentication.
o	Use advanced authentication mechanisms (e.g., MAC-based authentication, RADIUS).
•	stablish a process for requesting and approving mobile device connectivity.
o	Require submission of a formal request, detailing the reason and duration of connectivity.
o	Ensure approvals are limited to critical, temporary needs.
•	Scan and configure mobile devices before allowing connectivity to ICS networks.
o	Scan devices for malware using mobile device security tools.

""",
                        "tools": """
•	Mobile Security: Microsoft Intune, Sophos Mobile.

""",
                        "deliverables": """
•	Procedures for mobile device restrictions.
•	Screenshots showing restricted connectivity.

""",
                     },
                     
           {
                        "name": "5-1-3-7 Secure Configuration and Hardening",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Conduct periodic reviews of ICS/OT systems for secure configurations.
•	Develop and apply system hardening standards.

""",
                        "examples": """
•	Conduct regular reviews to ensure compliance with secure configuration and hardening standards.
o	Schedule periodic configuration reviews.
o	Use automated tools or manual assessments to identify deviations from standards.
•	Establish secure configuration and hardening guidelines for ICS, in collaboration with system providers and manufacturers.
o	Create system-specific hardening guidelines (e.g., disabling unused ports, ensuring secure authentication).
o	Align guidelines with regulatory requirements and industry standards.
•	Apply secure configuration settings and hardening measures to all ICS systems.
o	Disable unused services and ports.
o	Enforce secure password policies and multi-factor authentication.
o	Apply patches and updates as part of secure configuration.

""",
                        "tools": """
•	Vulnerability Scanning: Nessus, Qualys, Tenable.

""",
                        "deliverables": """
•	Hardening review reports.
""",
                     },
                     
           {
                        "name": "5-1-3-8 Vulnerability Management",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Perform vulnerability assessments for ICS/OT systems.
•	Develop and implement plans to address vulnerabilities.

""",
                        "examples": """
•	Plan and conduct regular vulnerability assessments for ICS/OT systems.
o	Develop an assessment schedule (e.g., quarterly, semi-annually).
o	Conduct non-invasive scans to identify vulnerabilities.
•	Assess the impact of identified vulnerabilities on ICS/OT systems and operations.
o	Categorize vulnerabilities by severity (e.g., low, medium, high, critical).
o	Develop a contingency plan for high-severity vulnerabilities.
•	Address vulnerabilities through mitigation, patching, or configuration changes.
o	Prioritize remediation based on severity and risk assessment.

""",
                        "tools": """
•	Patch Management: Ivanti, ManageEngine.
•	Vulnerability Scanning: Nessus, Qualys, Tenable. 


""",
                        "deliverables": """
•	Vulnerability assessment reports.
•	Risk mitigation plans.

""",
                     },
                     
           {
                        "name": "5-1-3-9 Patch Management",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Identify critical ICS/OT systems.
•	Develop approved procedures and plans for the management of patches.
•	Schedule and apply patches after testing their impact.

""",
                        "examples": """
•	Create a detailed inventory of all ICS/OT systems that require patch management.
o	List ICS/OT systems, including PLCs, SCADA systems, and HMIs.
•	Create a structured plan for testing, approving, and applying patches.
o	Define roles and responsibilities for patch management.
o	Outline patch testing procedures to ensure compatibility.
•	Evaluate patches in a lab or test environment before deployment.
o	Simulate the production environment in a secure testing area.
o	Apply patches and monitor for compatibility or performance issues.
o	Deploy patches to production systems following successful testing.

""",
                        "tools": """
•	Patch Management: Ivanti, ManageEngine.
•	Testing Tools: VMware, Hyper-V


""",
                        "deliverables": """
•	Patch management reports.
•	Patch deployment logs.

""",
                     },
                     
           {
                        "name": "5-1-3-10 Malware Protection",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Deploy and update antivirus/malware protection tools for ICS/OT.
•	Periodically review malware protection measures.

""",
                        "examples": """
•	Install and configure cybersecurity applications on ICS/OT systems.
o	Test applications in a simulated environment to ensure compatibility.
o	Deploy tools to production systems incrementally to monitor for issues.
•	Set up monitoring systems to detect and respond to threats in real-time.
o	Enable logging for malware detection and response events.
o	Integrate logs with the organization's SIEM for centralized monitoring.
•	Regularly update cybersecurity applications and review their effectiveness.
o	Schedule updates for antivirus definitions and malware protection tools.

""",
                        "tools": """
•	Monitoring Tools: Splunk, QRadar, SolarWinds.
•	Antivirus and Malware Tools: Symantec Industrial Control System Protection, Trend Micro Industrial Security.
•	Update Tools: McAfee ePO, Sophos Central.


""",
                        "deliverables": """
•	Reports on antivirus updates.
•	Malware protection procedures.

""",
                     },
                     
           {
                        "name": "5-1-4 Periodic Review of ICS/OT Cybersecurity",
                        "description": "",
                        "section": "2-2-3",
                        "purpose": "",
                        "implementation_steps": """
•	Review ICS/OT policies and procedures annually or upon regulatory changes.
•	Document and approve updates.

""",
                        "examples": """
""",
                        "tools": """

""",
                        "deliverables": """
•	Updated ICS/OT policy.
•	Review logs and formal approval records.


""",
                     },
            ]
        }
    ]
}
]






# Function to populate the database
def populate_database():
    for domain_data in data:
        domain, created = Domain.objects.get_or_create(name=domain_data['name'])
        if created:
            print(f"Created new domain: {domain.name}")
        else:
            print(f"Domain already exists: {domain.name}")

        for subdomain_data in domain_data['subdomains']:
            subdomain, created = Subdomain.objects.get_or_create(name=subdomain_data['name'], domain=domain)
            if created:
                print(f"  Created new subdomain: {subdomain.name} under domain {domain.name}")
            else:
                print(f"  Subdomain already exists: {subdomain.name} under domain {domain.name}")

            for control_data in subdomain_data['controls']:
                control, created = Control.objects.get_or_create(
                    name=control_data['name'],
                    description=control_data['description'],
                    section=control_data['section'],
                    purpose=control_data['purpose'],
                    implementation_steps=control_data['implementation_steps'],
                    examples=control_data['examples'],
                    tools=control_data['tools'],
                    deliverables=control_data['deliverables'],
                    subdomain=subdomain
                )
                if created:
                    print(f"    Created new control: {control.name} under subdomain {subdomain.name}")
                else:
                    print(f"    Control already exists: {control.name} under subdomain {subdomain.name}")

# Run the function to populate the database
populate_database()

