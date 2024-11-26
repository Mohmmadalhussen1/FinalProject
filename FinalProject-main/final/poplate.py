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
                        "name": "2-12-1: Define and Approve Cybersecurity Requirements for Event Logs and Monitoring",
                        "description": "Establish a policy to define the scope, retention, and monitoring of event logs.",
                        "section": "2-12-1",
                        "purpose": "Establish a policy to define the scope, retention, and monitoring of event logs.",
                        "implementation_steps": """
1. Develop an Event Logs and Monitoring Management Policy.
2. Define assets requiring logging (e.g., critical systems, privileged accounts).
3. Set the retention period (minimum 12 months).
4. Obtain approval from executive management.
""",
                        "examples": """
Example 1: Network devices (e.g., routers, firewalls).
Example 2: Applications (e.g., ERP, HRMS).
""",
                        "tools": """
Tool 1: Documentation Tools (e.g., Microsoft Word, SharePoint).
Tool 2: Logging Configuration Tools (e.g., Splunk, Graylog).
""",
                        "deliverables": """
Deliverable 1: Event Logs and Monitoring Management Policy.
Deliverable 2: Signed Approval Document.
""",
                    },
                    {
                        "name": "2-12-2: Implement Event Logs and Monitoring Management",
                        "description": "Establish a policy to define the scope, retention, and monitoring of event logs.",
                        "section": "2-12-2",
                        "purpose": "Activate and monitor event logs on critical systems.",
                        "implementation_steps": """
1. Scope Definition:
   - Use asset and risk registers to determine logging scope.

2. Event Log Activation:
   - Enable logging on:
     - Network devices.
     - Applications.
     - Databases.
     - Servers.
     - Workstations.

3. Monitoring and Retention:
   - Connect logs to a SIEM system for real-time monitoring.
   - Ensure retention for at least 12 months.
   - Assign a team for continuous monitoring or outsource to a Security Operations Center (SOC).
""",
                        "examples": """
Example 1: Network Devices:
   - Log events such as login attempts, configuration changes, and traffic anomalies.

Example 2: Servers and Applications:
   - Enable audit logs to capture login attempts, file access, and administrative actions.

Example 3: Set Up a SIEM System:
   - Action: Integrate all critical assets with a Security Information and Event Management (SIEM) system for centralized monitoring.

Example 4: Define Monitoring Teams:
   - Action: Assign a team for 24/7 monitoring or contract a Security Operations Center (SOC) for continuous log analysis.
""",
                        "tools": """
Tool 1: SIEM Systems: Splunk, IBM QRadar, ArcSight.
Tool 2: Asset Management: ServiceNow CMDB, SolarWinds.
Tool 3: Monitoring: ManageEngine, Microsoft Sentinel.
""",
                        "deliverables": """
Deliverable 1: Logs showing active monitoring through SIEM.
Deliverable 2: Report detailing the connection of all assets to SIEM.
Deliverable 3: Monitoring team schedule (e.g., shift breakdown table).
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
                ],
            },
        ],
    },
]

# Function to populate the database
def populate_database():
    for domain_data in data:
        domain, created = Domain.objects.get_or_create(name=domain_data['name'])
        
        for subdomain_data in domain_data['subdomains']:
            subdomain, created = Subdomain.objects.get_or_create(name=subdomain_data['name'], domain=domain)
            
            for control_data in subdomain_data['controls']:
                Control.objects.get_or_create(
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

# Run the function to populate the database
populate_database()
