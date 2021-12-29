from Room import Room
from Wall import Wall


class Room3(Room):
    def __init__(self, cur, conn):
        super().__init__()
        walls = [[0, 0, 20, 600],
                 [780, 0, 20, 250],
                 [780, 350, 20, 250],
                 [20, 0, 760, 20],
                 [20, 580, 760, 20],
                 [80, 100, 400, 20],
                 [80, 100, 20, 400],
                 [680, 20, 20, 80],
                 [660, 100, 60, 20],
                 [700, 100, 20, 380],
                 [240, 200, 480, 20],
                 [160, 220, 20, 80],
                 [380, 220, 20, 180],
                 [400, 480, 20, 100],
                 [100, 380, 80, 20],
                 [240, 380, 60, 20],
                 [240, 300, 20, 100],
                 [20, 480, 100, 20],
                 [180, 480, 40, 20],
                 [200, 480, 20, 100],
                 [300, 380, 20, 100],
                 [280, 480, 240, 20],
                 [500, 300, 20, 200],
                 [520, 300, 80, 20],
                 [520, 420, 80, 20],
                 [380, 380, 60, 20],
                 [420, 300, 20, 100],
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
            x = item[0]
            y = item[1]
            width = item[2]
            height = item[3]
            temp = (3, x, y, width, height)
            cur.execute("INSERT or REPLACE into rooms VALUES (?,?,?,?,?);", temp)
            conn.commit()
            cur.execute("SELECT * FROM rooms;")
            all_result = cur.fetchall()
            print(all_result)
