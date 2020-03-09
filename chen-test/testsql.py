import pymysql

def getConnect():
    try:
        connect = pymysql.connect('172.10.23.61', 'root', 'Docker@387q!', 'ops', 5408)
        return connect
    except Exception as e:
        print( e )

def selectByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor( pymysql.cursors.DictCursor )
        cursor.execute( sql, params )
        result = cursor.fetchall()
        return result
    except Exception as e:
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)

def updateByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor( pymysql.cursors.DictCursor )
        count = cursor.execute( sql, params )
        connect.commit()
        return count
    except Exception as e:
        connect.rollback()
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)