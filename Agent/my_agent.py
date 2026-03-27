import pyodbc
import time
import configparser
import os
import logging
import requests  # للميزة الجديدة: Web Scraping
import getpass   # المكتبة المسؤولة عن إخفاء الباسورد
from bs4 import BeautifulSoup # للميزة الجديدة: Web Scraping
from datetime import datetime

# --- 1. إعداد محرك الذاكرة الخارجية (Logging Engine) ---
logging.basicConfig(
    filename='agent_intelligence.log', # الملف الذي سيجمع البيانات للـ ML
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def log_event(message, level="INFO"):
    if level == "INFO":
        logging.info(message)
    else:
        logging.warning(message)

# --- 2. نظام إدارة المستخدمين وتصاريح الدخول ---
def load_all_settings():
    config = configparser.ConfigParser()
    settings_file = 'settings.ini'
    if not os.path.exists(settings_file):
        # إنشاء ملف الإعدادات الافتراضي مع بيانات قاعدة البيانات والمستخدمين
        config['DATABASE'] = {
            'server': 'B2-3\\ESPRESS2',
            'database': 'SecureDB',
            'driver': 'ODBC Driver 17 for SQL Server'
        }
        config['USERS'] = {
            'admin': 'admin123',  
            'mohamed': 'pass2026'
        }
        with open(settings_file, 'w') as f:
            config.write(f)
    config.read(settings_file)
    return config

def login_system():
    config = load_all_settings()
    if 'USERS' not in config:
        # حماية إضافية في حالة تلف ملف الـ ini
        config['USERS'] = {'admin': 'admin123'}
    
    users_list = config['USERS']
    
    # --- شعار SentinAI الجديد ---
    print("""
    ***************************************************
         _____            _   _             _____ 
        / ____|          | | (_)           / ____|
       | (___  ___ _ __ | |_ _ _ __   _ _| |     
        \___ \/ _ \ '_ \| __| | '_ \ / _` | |     
        ____) |  __/ | | | |_| | | | | (_| | |____ 
       |_____/ \___|_| |_|\__|_|_| |_|\__,_|\_____|
                                                   
               >> THE INTELLIGENT GUARDIAN <<
    ***************************************************
    """)
    print(f" [!] System Initialization... [OK]")
    print(f" [!] Loading SentinAI Core... [OK]")
    print("-" * 51)
    
    attempts = 3
    while attempts > 0:
        user = input("  Enter Username: ")
        password = getpass.getpass("  Enter Password: ")
        
        if user in users_list and users_list[user] == password:
            print(f"\n [SUCCESS] SentinAI Authenticated: Welcome, {user}!")
            log_event(f"User '{user}' logged in.")
            return True, user
        else:
            attempts -= 1
            print(f" [!] Access Denied. Attempts left: {attempts}")
            log_event(f"Failed login attempt for: {user}", "WARNING")
            
    print("\n [CRITICAL] SentinAI Locked: Unauthorized Access Detected.")
    return False, None

# --- 3. محرك اكتشاف الأنماط (الذكاء الزمني) ---
def analyze_risk(action_time):
    hour = action_time.hour
    if 0 <= hour <= 5:
        return "HIGH RISK (Suspicious Hours)"
    return "NORMAL"

# --- 4. التحديث التلقائي للقوانين (Web Scraping) ---
def check_legal_updates():
    try:
        url = "https://www.sdaia.gov.sa/ar/SDAIA/Pages/Regulations.aspx"
        response = requests.get(url, timeout=5)
        if "تعديل" in response.text or "جديد" in response.text:
            return True
        return False
    except:
        return False

# --- 5. التعلم من قرار البشر (Human-in-the-loop) ---
def collect_feedback():
    print("\n--- SENTINAI TRAINING MODE (Feedback) ---")
    event_id = input("Enter Event Date/ID to label: ")
    is_correct = input("Was the AI risk assessment correct? (y/n): ").lower()
    status = "True_Positive" if is_correct == 'y' else "False_Positive"
    log_event(f"FEEDBACK: Event {event_id} marked as {status}")
    print(f"SentinAI memory updated: This pattern is now known as {status}.")

# --- 6. الاتصال بقاعدة البيانات ---
def get_db_connection():
    try:
        config = load_all_settings()
        db_config = config['DATABASE']
        conn_str = (
            f"DRIVER={{{db_config['driver']}}};"
            f"SERVER={db_config['server']};"
            f"DATABASE={db_config['database']};"
            "Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        return conn
    except Exception as e:
        log_event(f"DATABASE CONNECTION ERROR: {str(e)}", "ERROR")
        return None

# --- 7. فحص حالة الامتثال مع "التنبيه الذكي" ---
def get_compliance_status():
    report = {}
    try:
        conn = get_db_connection()
        if not conn: return {"ERROR": "Database Connection Failed"}
        
        cursor = conn.cursor()
        
        # فحص وجود مفتاح التشفير
        cursor.execute("SELECT name FROM sys.symmetric_keys WHERE name = 'UserKey'")
        row = cursor.fetchone()
        
        if row:
            report['encryption'] = {"status": "PASS", "evidence": "AES_256 Key Active"}
        else:
            # --- ميزة التنبيه الذكي برمجياً ---
            report['encryption'] = {"status": "FAIL", "evidence": "CRITICAL: Key Deleted!"}
            
            # تسجيل الحدث في جدول AuditLog فوراً لكي يظهر في خيار 3
            try:
                insert_query = """
                INSERT INTO AuditLog (Action, TableName, ActionTime, UserHash)
                VALUES (?, ?, ?, ?)
                """
                cursor.execute(insert_query, ('DROP_KEY_VIOLATION', 'SymmetricKeys', datetime.now(), 0x000000))
                conn.commit()
                log_event("SentinAI auto-logged a security violation: Key Missing", "WARNING")
            except:
                pass # في حال فشل التسجيل لا نعطل البرنامج

        # فحص وجود جدول سجلات التدقيق
        cursor.execute("SELECT name FROM sys.tables WHERE name = 'AuditLog'")
        audit_row = cursor.fetchone()
        report['audit'] = {
            "status": "PASS" if audit_row else "FAIL", 
            "evidence": "AuditLog Active" if audit_row else "Table Missing"
        }
        
        conn.close()
        log_event(f"Compliance Check Executed - Status: {report['encryption']['status']}")
        return report
    except Exception as e:
        log_event(f"Compliance Check Error: {str(e)}", "ERROR")
        return {"ERROR": str(e)}

# --- 8. تتبع التغييرات وتحليل المخاطر ---
def get_change_history():
    changes = []
    try:
        conn = get_db_connection()
        if not conn: return []
        
        cursor = conn.cursor()
        query = """
        SELECT TOP 5 
            Action, 
            TableName, 
            ActionTime, 
            CONVERT(VARCHAR(MAX), UserHash, 2) as UserID 
        FROM AuditLog 
        ORDER BY ActionTime DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            changes.append({
                "action": row[0],
                "table": row[1],
                "date": row[2],
                "user": row[3] if row[3] else "Unknown"
            })
        conn.close()
        log_event("Change History Retrieved by User")
        return changes
    except Exception as e:
        log_event(f"History Retrieval Error: {str(e)}", "ERROR")
        return []

# --- 9. تشغيل الإيجينت ---
def run_agent_v6():
    authenticated, current_user = login_system()
    if not authenticated:
        return

    while True:
        report = get_compliance_status()
        if "ERROR" in report:
            print(f"\n[!] Error: {report['ERROR']}")
            break

        passed = sum(1 for k in report if report[k]['status'] == "PASS")
        score = int((passed / len(report)) * 100)

        print(f"\n" + "="*50)
        print(f" SENTINAI DASHBOARD | SYSTEM HEALTH: {score}%")
        print(f" ACTIVE SESSION: {current_user}")
        print("="*50)
        print(" 1. Execute Live Audit")
        print(" 2. Generate Compliance log (.txt)")
        print(" 3. AI Risk Forensics (LOGs)")
        print(" 4. Legal Intelligence (Web Scraping)")
        print(" 5. Human Training Mode")
        print(" 6. Access Intelligence Memory")
        print(" 0. Shutdown SentinAI")
        
        choice = input("\n Command >> ")

        if choice == '1':
            log_event("User Selected: Live Audit")
            for k, v in report.items(): print(f" [{v['status']}] {k.upper()}: {v['evidence']}")
            
        elif choice == '2':
            log_event("User Selected: Export Report")
            with open("SentinAI_Compliance_Report.txt", "w") as f:
                f.write(f"SENTINAI COMPLIANCE REPORT\nScore: {score}%\nAdmin: {current_user}\nDate: {time.ctime()}")
            print(" Done: SentinAI_Compliance_Report.txt")
            
        elif choice == '3':
            log_event("User Selected: Track Changes")
            print("\n--- ANALYZING RECENT CHANGES (AI RISK) ---")
            history = get_change_history()
            if not history:
                print(" No records found.")
            else:
                for change in history:
                    risk_assessment = analyze_risk(change['date'])
                    print(f" EVENT: {change['action']} | BY: {change['user']}")
                    print(f" TIME: {change['date']} | AI RISK: {risk_assessment}")
                    print("-" * 30)
                    
        elif choice == '4':
            log_event("User Selected: Web Scraping Updates")
            print("\n Scanning official portals...")
            if check_legal_updates():
                print(" [ALERT] New legal amendments detected!")
            else:
                print(" [OK] No new legal updates found.")

        elif choice == '5':
            collect_feedback()

        elif choice == '6':
            print("\n--- SENTINAI INTELLIGENCE MEMORY ---")
            if os.path.exists('agent_intelligence.log'):
                with open('agent_intelligence.log', 'r') as f:
                    for line in f.readlines()[-10:]: print(line.strip())

        elif choice == '0':
            print("\n Shutting down SentinAI... Goodbye.")
            break

if __name__ == "__main__":
    run_agent_v6()