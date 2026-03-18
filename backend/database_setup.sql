-- Create Database
CREATE DATABASE IF NOT EXISTS asset_management;
USE asset_management;

-- Users Table
CREATE TABLE IF NOT EXISTS tbl_user(
    User_id INT PRIMARY KEY AUTO_INCREMENT,
    User_name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    user_type VARCHAR(20) NOT NULL,
    Phone_no VARCHAR(15),
    Email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Category Table
CREATE TABLE IF NOT EXISTS tbl_category(
    Category_id INT PRIMARY KEY AUTO_INCREMENT,
    Category_name VARCHAR(100) NOT NULL,
    Category_description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Asset Table
CREATE TABLE IF NOT EXISTS tbl_asset(
    Sl_no INT PRIMARY KEY AUTO_INCREMENT,
    Product_ID VARCHAR(50) NOT NULL,
    Product_name VARCHAR(100) NOT NULL,
    Category_ID INT NOT NULL,
    Manufacturer VARCHAR(100),
    Vendor VARCHAR(100),
    Price DECIMAL(10,2),
    Bill_no INT,
    Purchase_date DATE,
    expiry_date DATE,
    custodian VARCHAR(100),
    Department VARCHAR(100),
    Location VARCHAR(100),
    Warranty_period VARCHAR(100),
    Stock_register_no VARCHAR(100),
    Description VARCHAR(255),
    Status VARCHAR(20),
    Qr_code_value VARCHAR(255) UNIQUE,
    Created_by INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (Category_ID) REFERENCES tbl_category(Category_id) ON DELETE RESTRICT,
    FOREIGN KEY (Created_by) REFERENCES tbl_user(User_id) ON DELETE SET NULL,
    INDEX idx_category (Category_ID),
    INDEX idx_created_by (Created_by),
    INDEX idx_status (Status)
);

-- QR Code Table
CREATE TABLE IF NOT EXISTS tbl_qr(
    Qr_id INT PRIMARY KEY AUTO_INCREMENT,
    Product_id INT,
    Qr_value VARCHAR(255) UNIQUE,
    Generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (Product_id) REFERENCES tbl_asset(Sl_no) ON DELETE CASCADE,
    INDEX idx_product_id (Product_id)
);

-- Asset Expiry/Disposal Table
CREATE TABLE IF NOT EXISTS tbl_asset_expiry(
    disposal_id INT PRIMARY KEY AUTO_INCREMENT,
    Asset_id INT NOT NULL,
    Disposal_type VARCHAR(50),
    Stored_at VARCHAR(100),
    Sale_price DECIMAL(10,2),
    Recipient_details VARCHAR(255),
    Approved_by VARCHAR(100),
    Custodian_at_disposal VARCHAR(100),
    remarks VARCHAR(255),
    Document_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (Asset_id) REFERENCES tbl_asset(Sl_no) ON DELETE CASCADE,
    INDEX idx_asset_id (Asset_id)
);

-- Feedback Table
CREATE TABLE IF NOT EXISTS tbl_feedback(
    feedback_id INT PRIMARY KEY AUTO_INCREMENT,
    Asset_id INT,
    user_id INT,
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (Asset_id) REFERENCES tbl_asset(Sl_no) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES tbl_user(User_id) ON DELETE SET NULL,
    INDEX idx_asset_id (Asset_id),
    INDEX idx_user_id (user_id)
);

-- Report Table
CREATE TABLE IF NOT EXISTS tbl_report(
    report_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_id INT,
    user_id INT,
    report_type VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (asset_id) REFERENCES tbl_asset(Sl_no) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES tbl_user(User_id) ON DELETE SET NULL,
    INDEX idx_asset_id (asset_id),
    INDEX idx_user_id (user_id)
);

-- Notification Table
CREATE TABLE IF NOT EXISTS tbl_notification(
    notification_id INT PRIMARY KEY AUTO_INCREMENT,
    asset_id INT,
    message VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (asset_id) REFERENCES tbl_asset(Sl_no) ON DELETE CASCADE,
    INDEX idx_asset_id (asset_id),
    INDEX idx_created_at (created_at)
);

-- Insert test admin user (password: admin123)
INSERT IGNORE INTO tbl_user (User_id, User_name, password_hash, user_type, Email) 
VALUES (1, 'admin', '$2b$12$Dme3.xjNzM7fP2P.ZqQPvOz/nV8qgL7D3x4Y5z9K2m1L4n0P8q5Li', 'Admin', 'admin@gmail.com');
