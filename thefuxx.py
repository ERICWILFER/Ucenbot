import sqlite3
from thefuzz import fuzz, process
conn = sqlite3.connect("db.sqlite3")
c = conn.cursor()

sql_query = "SELECT books FROM library"

c.execute(sql_query)

results = c.fetchall()
# print(results)
results_list = [' '.join(map(str, list(i))) for i in results]
# print(results_list)
conn.close()



print(process.extractOne("the art love", results_list, scorer=fuzz.token_sort_ratio))

