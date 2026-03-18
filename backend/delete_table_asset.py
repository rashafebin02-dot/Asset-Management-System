import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='etern@lly123', database='asset_management', port=3306)
cur = conn.cursor()
cur.execute("DELETE FROM tbl_asset WHERE Product_name = 'table'")
conn.commit()
print(f"Deleted {cur.rowcount} row(s)")
conn.close()
