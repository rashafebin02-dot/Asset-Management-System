Asset Management System (AssetMS) 📦
A comprehensive web-based solution for tracking, managing, and monitoring organizational assets with integrated QR code technology. AssetMS streamlines the inventory process by allowing admins and staff to generate unique QR codes for physical assets, track warranty expiries, and manage stock via a modern dashboard.

🚀 Key Features
🔐 Role-Based Access Control
Admin Dashboard: Full control to manage categories, view all assets, generate system-wide reports, handle user feedback, and monitor key performance indicators (KPIs).
User/Staff Dashboard: Personal workspace to register new assets, view assigned items, and report issues.
📷 Advanced QR Code Technology
Auto-Generation: Automatically generates unique QR codes for every asset added to the system.
Customization: Supports three QR styles:
Standard: High-contrast standard QR.
Alphabet-Center: Embeds a category character (e.g., 'L' for Laptop) in the center.
Logo-Center: Allows uploading a custom image/logo to be embedded in the QR code.
Print-Ready: Dedicated printing interface with customizable dimensions (cm) for label printing.
🛠 Asset Management
Detailed Tracking: Records product name, manufacturer, vendor, price, bill number, purchase date, warranty period, location, and custodian.
Bulk Upload: Supports adding multiple assets at once via Excel (.xlsx) import.
Expiry Monitoring: distinct sections for tracking expired assets and warranty statuses.
Export: Download full asset reports and user lists as Excel files.
💻 Modern UI/UX
Responsive design using a custom "Slate & Indigo" CSS theme.
Interactive sidebar navigation.
Real-time flash messages for user feedback.
Free QR Tool: A public-facing tool for generating custom QR codes without logging in.
🛠 Technologies Used
Backend: Python (Flask)
Database: MySQL
Frontend: HTML5, CSS3, JavaScript
Libraries:
Python: pandas (Data export/import), mysql-connector-python (DB connection), flask-bcrypt (Security), qrcode (Backend generation).
JavaScript: qrcode.js (Client-side rendering).
