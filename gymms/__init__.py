# Ensure PyMySQL is used as the MySQL driver
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass
