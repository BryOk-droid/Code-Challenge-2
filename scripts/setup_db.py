import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.resolve()))


from lib.db.connection import get_connection


def main():
   schema_path = Path(__file__).parent / '../lib/db/schema.sql'
   sql = Path(schema_path).read_text()


   conn = get_connection()
   conn.executescript(sql)
   conn.close()
   print("✅ Database schema created (tables defined).")


if __name__ == '__main__':
   main()