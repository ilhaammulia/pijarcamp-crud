import pymysql
from settings import *

class DBConnect:
    def __init__(self):
        self.open()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS produk(produk_id INT AUTO_INCREMENT PRIMARY KEY, nama_produk VARCHAR(255), keterangan TEXT, harga INT(20), jumlah INT(6))")
        self.connection.commit()
        self.close()
    
    def open(self):
        self.connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.connection.close()

class Product(DBConnect):
    def __init__(self, produk_id = None, nama_produk = None, keterangan = None, harga = None, jumlah = None):
        self.id = produk_id
        self.name = nama_produk
        self.description = keterangan
        self.price = harga
        self.stock = jumlah
    
    @classmethod
    def find_all(cls):
        try:
            connect = DBConnect()
            connect.open()
            connect.cursor.execute("SELECT * FROM produk")
            result = connect.cursor.fetchall()
            connect.close()
            return [
                cls(x[0], x[1], x[2], x[3], x[4])
                for x in result
            ]
        except Exception as err:
            print(err)
            raise err
    
    @classmethod
    def find_one(cls, produk_id):
        try:
            connect = DBConnect()
            connect.open()
            connect.cursor.execute("SELECT * FROM produk WHERE produk_id=%s", (produk_id,))
            result = connect.cursor.fetchone()
            connect.close()
            if result:
                return cls(result[0], result[1], result[2], result[3], result[4])
        except Exception as err:
            print(err)
            raise err
    
    def save(self):
        try:
            self.open()
            self.cursor.execute("INSERT INTO produk(nama_produk, keterangan, harga, jumlah) VALUES (%s, %s, %s, %s)", (self.name, self.description, self.price, self.stock,))
            self.connection.commit()
            self.cursor.execute("SELECT LAST_INSERT_ID()")
            self.id = self.cursor.fetchone()
            self.close()
            return True
        except Exception as err:
            print(err)
            raise err
    
    def update(self):
        try:
            self.open()
            self.cursor.execute("UPDATE produk SET nama_produk=%s, keterangan=%s, harga=%s, jumlah=%s WHERE produk_id=%s", (self.name, self.description, self.price, self.stock, self.id,))
            self.connection.commit()
            self.close()
            return True
        except Exception as err:
            print(err)
            raise err
    
    @classmethod
    def delete(cls, produk_id):
        try:
            connect = DBConnect()
            connect.open()
            connect.cursor.execute("DELETE FROM produk WHERE produk_id=%s", (produk_id,))
            connect.connection.commit()
            connect.close()
            return cls()
        except Exception as err:
            print(err)
            raise err
    
    def __bool__(self):
        return None not in [self.id, self.name, self.description, self.price, self.stock]