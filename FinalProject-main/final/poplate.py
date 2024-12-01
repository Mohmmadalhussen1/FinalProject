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
                
            ],
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

