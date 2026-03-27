###  Getting Started: How to Run SentinAI

This guide will walk you through the steps to set up and run the SentinAI agent on your local machine.

#### 1. Prerequisites
Before you begin, ensure you have the following installed:
* **Python 3.8 or higher**: [Download here](https://www.python.org/downloads/)
* **Microsoft SQL Server**: (Express or Developer edition)
* **SQL Server Management Studio (SSMS)**: To manage your database.

---

#### 2. Database Setup
You must prepare the database environment so the agent can monitor it.
1.  Open **SSMS** and connect to your instance.
2.  Go to the `SQL_Scripts` folder in this project.
3.  Run the scripts in the following order:
    * Execute `01_Database_Setup.sql` to create the database and audit tables.
    * Execute `02_Security_Keys.sql` to set up the Master Key and Symmetric Key.

---

#### 3. Environment Configuration
The agent needs to know how to connect to **your** specific SQL Server instance.
1.  Locate the `settings.ini` file (the agent will create this automatically on the first run, or you can create it manually).
2.  Ensure the `server` name matches your SQL instance (e.g., `localhost` or `YourComputerName\InstanceName`).
3.  **Default Credentials**: The initial login is:
    * **Username**: `admin`
    * **Password**: `admin123`

---

#### 4. Installation
Open your terminal (PowerShell or Command Prompt) and follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/mohamedtahoun1/SentinAI-Project.git
    cd SentinAI-Project
    ```

2.  **Install Required Libraries**:
    Run the following command to install all dependencies listed in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

---

#### 5. Running the Agent
Once the libraries are installed and the database is ready, start the agent by running:
```bash
python Agent/my_agent.py
```

---

#### 6. Troubleshooting
* **ODBC Driver Error**: Ensure you have the **ODBC Driver 17 for SQL Server** installed. If not, the connection will fail.
* **Authentication Failed**: Check the `settings.ini` file to verify your username and password.
* **Symmetric Key Missing**: If the dashboard shows 0% health, run the `03_Fix_Compliance.sql` script in your SQL Server.

---

