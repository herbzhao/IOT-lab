import time
import sqlite3


sqlite_file = 'templog.sqlite'		# name of the sqlite database file
table_name = 'tempearture_log'		# name of the table to be created
index_column = 'index_column'				# column with primary key
field_type = 'INTEGER'

column_1 = 'time_stamp'				#name of column
column_2 = 'running_time'			
column_3 = 'temperature'

#datatype = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB



# Connecting to the database file
conn = sqlite3.connect(sqlite_file)

c = conn.cursor()  # create a cursor, so we can modify the database


# create a database with 3 columns
#c.execute("CREATE TABLE {tn}({idc} 'INTEGER' PRIMARY KEY, {cn1} TEXT, {cn2} TEXT)"\
#		.format(tn=table_name, idc=index_column, cn1 = column_1, cn2 = column_2))

# add another column to database
#c.execute("ALTER TABLE {tn} ADD COLUMN {cn3} REAL" \
#		.format(tn = table_name,  cn3 = column_3))


#add row data to database
#c.execute("INSERT OR IGNORE INTO {tn} ({cn1},{cn2},{cn3}) VALUES (datetime('now'),{cv2},{cv3})"\
#		.format (tn = table_name, cn1 = column_1, cn2 = column_2, cn3 = column_3, \
#				 cv2 = "3", cv3 = 28.8))



#Retrive data from database using SELECT
#c.execute("SELECT {idc}, {cn3} FROM {tn}"\
#		.format (cn1 = column_1, cn3 = column_3, tn = table_name, idc = index_column))

#Retrive data from database using SELECT
c.execute("SELECT {idc}, {cn3} FROM {tn}"\
	.format (idc = 'index_column', cn3 = 'temperature', tn = 'tempearture_log' ))

#print c.fetchall()
#print type(c.fetchall())

#headings = [('ID','TEMP')]

#print headings
#print type(headings)

data = []
rows = c.fetchall()
for row in rows:
	row_data = [row[0],row[1]]
	data.append(row_data)

print data

#Retrive data from database using SELECT and print lines by lines
#results = c.execute("SELECT {cn1}, {cn3} FROM {tn} WHERE {idc} in (2,3)"\
#		.format (cn1 = column_1, cn3 = column_3, tn = table_name, idc = index_column))
		
#for row in results:
#   print "TIME = ", row[0]
#   print "TEMP = ", row[1], "\n"


# Committing changes and closing the connection to the database file
conn.commit()
conn.close()





