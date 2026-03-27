USE Master;
GO
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'SecureDB')
CREATE DATABASE SecureDB;
GO
USE SecureDB;
GO

-- إنشاء جدول سجلات التدقيق  
IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'AuditLog')
CREATE TABLE AuditLog (
    LogID INT IDENTITY(1,1) PRIMARY KEY,
    Action NVARCHAR(100),
    TableName NVARCHAR(100),
    ActionTime DATETIME DEFAULT GETDATE(),
    UserHash VARBINARY(64)
);
GO