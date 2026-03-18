import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='etern@lly123', database='asset_management', port=3306)
cur = conn.cursor(dictionary=True)
cur.execute('SELECT a.*, c.Category_name FROM tbl_asset a LEFT JOIN tbl_category c ON a.Category_ID = c.Category_id ORDER BY a.Sl_no DESC')
rows = cur.fetchall()
for row in rows:
    name = row['Product_name']
    qr = f"ID:{row['Qr_code_value']}"
    qr += f"\nItem:{str(row['Product_name'])[:18]}"
    qr += f"\nCat:{str(row['Category_name'])[:12]}"
    if row.get('Manufacturer'): qr += f"\nMfr:{str(row['Manufacturer'])[:10]}"
    if row.get('Vendor'): qr += f"\nVdr:{str(row['Vendor'])[:10]}"
    if row.get('Price'): qr += f"\nPrice:{row['Price']}"
    if row.get('Bill_no'): qr += f"\nBill:{str(row['Bill_no'])[:8]}"
    if row.get('Purchase_date'): qr += f"\nBuy:{row['Purchase_date']}"
    qr += f"\nExp:{row['expiry_date']}"
    if row.get('Warranty_period'): qr += f"\nWar:{str(row['Warranty_period'])[:8]}"
    if row.get('custodian'): qr += f"\nCust:{str(row['custodian'])[:10]}"
    if row.get('Department'): qr += f"\nDept:{str(row['Department'])[:10]}"
    if row.get('Location'): qr += f"\nLoc:{str(row['Location'])[:10]}"
    if row.get('Stock_register_no'): qr += f"\nReg:{str(row['Stock_register_no'])[:8]}"
    print(f"--- {name} (Category: {row['Category_name']}) ---")
    print(f"  QR data length: {len(qr)} chars")
    print(f"  QR data: {repr(qr)}")
    print()
conn.close()
