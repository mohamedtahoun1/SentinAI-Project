SentinAI: Intelligent SQL Security Guardian
AI-Powered Compliance Monitoring for SQL Server (Law 151/2020)

Project Overview
SentinAI is an experimental AI Agent built with LangChain and Python to monitor SQL Server security. It focuses on automating technical compliance with the Egyptian Data Protection Law (Law 151/2020).

Core Functionalities
Encryption Audit: Checks for active Symmetric Keys (AES_256) to ensure data-at-rest protection.
Integrity Monitoring: Verifies the existence of AuditLog tables for traceability.
AI Risk Forensics: Analyzes operation timestamps to detect suspicious behavior during off-hours.
Legal Intelligence: Includes a Web Scraping module to monitor official regulatory updates.

Technical Disclaimer
This tool is a primitive prototype designed for educational and demonstration purposes. For real-world production environments, significant enhancements are required:
Secrets Management: Moving from plain-text config files to secure Secret Vaults.
Scalability: Implementation of multi-database support and containerization (Docker).
Advanced Alerting: Integrating real-time notification systems (SMTP/Webhooks) for instant violation reporting.
