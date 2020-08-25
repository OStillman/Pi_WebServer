import sqlite3

class PresenceActions():
    def __init__(self):
        self.db = sqlite3.connect('DB/webserver.db')

    def checkPresence(self, member, new_status):
        check_cursor = self.db.cursor()
        check_cursor.execute('''
            SELECT * FROM presence
            WHERE name = ?;
            ''', (member, ))
        output = check_cursor.fetchone()
        print(output)
        if output[1] == new_status:
            print("Same status")
            return True
        else:
            print("Status changed")
            self.updatePresence(member, new_status)
            return False

    def updatePresence(self, member, new_status):
        add_cursor = self.db.cursor()
        print(member)
        print(new_status)
        add_cursor.execute('''
        UPDATE presence
        SET status = ?
        WHERE name = ?;
        ''', (new_status, member))
        self.db.commit()
