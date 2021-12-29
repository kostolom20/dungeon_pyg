from Room import Room
from Wall import Wall


class Room2(Room):

    def __init__(self, cur, conn):
        super().__init__()
        walls = [[0, 0, 20, 600],
                 [780, 0, 20, 440],
                 [780, 540, 20, 60],
                 [20, 0, 760, 20],
                 [20, 580, 760, 20],
                 [20, 120, 80, 20],
                 [80, 100, 20, 80],
                 [80, 260, 20, 120],
                 [80, 460, 20, 40],
                 [100, 340, 60, 20],
                 [20, 480, 80, 20],
                 [160, 100, 20, 480],
                 [300, 20, 20, 480],
                 [240, 140, 60, 20],
                 [240, 240, 60, 20],
                 [240, 360, 60, 20],
                 [240, 480, 60, 20],
                 [320, 340, 60, 20],
                 [380, 220, 20, 160],
                 [380, 120, 100, 20],
                 [440, 20, 20, 100],
                 [460, 140, 20, 200],
                 [460, 420, 20, 40],
                 [380, 460, 100, 20],
                 [380, 480, 20, 100],
                 [480, 440, 60, 20],
                 [540, 100, 20, 380],
                 [560, 100, 160, 20],
                 [560, 180, 50, 20],
                 [560, 280, 50, 20],
                 [560, 380, 50, 20],
                 [600, 400, 10, 20],
                 [520, 520, 20, 60],
                 [540, 520, 70, 20],
                 [680, 200, 80, 20],
                 [740, 220, 20, 80],
                 [680, 300, 100, 20],
                 [720, 320, 20, 100],
                 [680, 400, 20, 100],
                 [700, 400, 20, 20]
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
            x = item[0]
            y = item[1]
            width = item[2]
            height = item[3]
            temp = (2, x, y, width, height)
            cur.execute("INSERT or REPLACE into rooms VALUES (?,?,?,?,?);", temp)
            conn.commit()
            cur.execute("SELECT * FROM rooms;")
            all_result = cur.fetchall()
            print(all_result)
