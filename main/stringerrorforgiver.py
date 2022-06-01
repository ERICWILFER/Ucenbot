import sqlite3
from thefuzz import fuzz, process

def forgive_bookname(inp):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    sql_query = "SELECT books FROM library"
    c.execute(sql_query)
    results = c.fetchall()
    # print(results)
    results_list = [' '.join(map(str, list(i))) for i in results]
    # print(results_list)
    conn.close()
    result = process.extractOne(inp, results_list, scorer=fuzz.token_sort_ratio)
    return result[0]
    
def forgive_authorname(inp):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    sql_query = "SELECT author FROM library"
    c.execute(sql_query)
    results = c.fetchall()
    # print(results)
    results_list = [' '.join(map(str, list(i))) for i in results]
    # print(results_list)
    conn.close()
    result = process.extractOne(inp, results_list, scorer=fuzz.token_sort_ratio)
    return result[0]



