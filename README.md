SentinAI: Intelligent SQL Security Guardian
AI-Powered Compliance Monitoring for SQL Server (Law 151/2020)
وصف المشروع
هذا المشروع عبارة عن AI Agent تجريبي (Prototype) تم بناؤه باستخدام مكتبة LangChain ولغة Python لمراقبة أمن وقواعد بيانات SQL Server. الهدف الأساسي هو التأكد من مطابقة إعدادات قاعدة البيانات للمتطلبات التقنية لـ قانون حماية البيانات الشخصية المصري (رقم 151 لسنة 2020).

ماذا تفعل الأداة؟
فحص التشفير: التأكد من وجود ونشاط مفاتيح التشفير المتماثلة (Symmetric Keys) لحماية البيانات الحساسة.
مراقبة السجلات (Auditing): التحقق من وجود جدول AuditLog الذي يسجل عمليات الدخول والتعديل.
تحليل المخاطر ذكياً: تحليل وقت العمليات للكشف عن الأنشطة المشبوهة في الأوقات غير العادية.
التحديث القانوني: القدرة على سحب تحديثات القوانين من المواقع الرسمية (Web Scraping).

⚠️ إبراء ذمة وتوضيح تقني :
هذه الأداة حالياً هي نسخة تجريبية بدائية (Basic MVP) تم تطويرها لإثبات المفهوم (Proof of Concept). لتصبح أداة صالحة للاستخدام في بيئات العمل الحقيقية (Production)، يجب تطوير الآتي:
تشفير كلمات المرور: حالياً يتم تخزين الإعدادات في ملفات نصية، ويجب الانتقال لـ Vaults مؤمنة.
دعم بيئات متعددة: دعم Cloud Databases و Docker.
نظام تنبيهات متطور: ربط الأداة بـ Email أو Slack لإرسال تنبيهات فورية عند حدوث اختراق.


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Project Overview
SentinAI is an experimental AI Agent built with LangChain and Python to monitor SQL Server security. It focuses on automating technical compliance with the Egyptian Data Protection Law (Law 151/2020).

Core Functionalities
Encryption Audit: Checks for active Symmetric Keys (AES_256) to ensure data-at-rest protection.
Integrity Monitoring: Verifies the existence of AuditLog tables for traceability.
AI Risk Forensics: Analyzes operation timestamps to detect suspicious behavior during off-hours.
Legal Intelligence: Includes a Web Scraping module to monitor official regulatory updates.

⚠️ Technical Disclaimer
This tool is a primitive prototype designed for educational and demonstration purposes. For real-world production environments, significant enhancements are required:
Secrets Management: Moving from plain-text config files to secure Secret Vaults.
Scalability: Implementation of multi-database support and containerization (Docker).
Advanced Alerting: Integrating real-time notification systems (SMTP/Webhooks) for instant violation reporting.

