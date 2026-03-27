USE SecureDB;
GO

-- إنشاء الماستر كي 
IF NOT EXISTS (SELECT * FROM sys.symmetric_keys WHERE name LIKE '%MS_DatabaseMasterKey%')
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'SqlPass2026!';
GO

-- إنشاء المفتاح المتماثل 
IF NOT EXISTS (SELECT * FROM sys.symmetric_keys WHERE name = 'UserKey')
CREATE SYMMETRIC KEY UserKey  
WITH ALGORITHM = AES_256  
ENCRYPTION BY MASTER KEY;
GO