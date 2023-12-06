from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    #CREATE
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        with CONN:
            CURSOR.execute(sql)
        CONN.commit()
        

    #SAVE
    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """
#the 'with' statement is used with CONN to create a database connection.
#when the block is exited, the '__exit__' method of the connection is called,ensuring that the connection is properly closed
#helps to avoid issues related to resource leaks or improper cleanup
        with CONN:
            CURSOR.execute(sql, (self.name, self.album))
            self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]
        CONN.commit()
                

    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song



        
