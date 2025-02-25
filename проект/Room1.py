from Room import Room
from Wall import Wall


class Room1(Room):

    def __init__(self, cur, conn):
        super().__init__()

        walls = [[0, 0, 20, 600],
                 [780, 0, 20, 250],
                 [780, 350, 20, 250],
                 [20, 0, 760, 20],
                 [20, 580, 760, 20],
                 [240, 100, 20, 180],
                 [240, 360, 20, 80],
                 [20, 100, 160, 20],
                 [160, 100, 20, 80],
                 [160, 280, 20, 120],
                 [80, 200, 20, 200],
                 [80, 360, 80, 20],
                 [20, 480, 100, 20],
                 [260, 380, 100, 20],
                 [320, 380, 20, 220],
                 [320, 380, 100, 20],
                 [420, 380, 20, 140],
                 [420, 380, 60, 20],
                 [320, 200, 20, 100],
                 [320, 20, 20, 100],
                 [340, 280, 200, 20],
                 [520, 300, 20, 300],
                 [500, 480, 40, 20],
                 [540, 460, 40, 20],
                 [400, 100, 20, 100],
                 [420, 180, 100, 20],
                 [480, 20, 20, 80],
                 [500, 80, 40, 20],
                 [580, 180, 20, 20],
                 [600, 100, 20, 100],
                 [620, 100, 100, 20],
                 [680, 200, 100, 20],
                 [700, 220, 20, 120],
                 [670, 320, 50, 20],
                 [670, 340, 50, 50],
                 [670, 380, 50, 20],
                 [700, 380, 20, 120],
                 [660, 480, 50, 20]
                 ]
        room = 1
        iteration = 0
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3])
            self.wall_list.add(wall)
            x = item[0]
            y = item[1]
            width = item[2]
            height = item[3]
            iteration += 1
            temp = (room, iteration, x, y, width, height)
            cur.execute(f"SELECT ITERATION FROM rooms WHERE ITERATION = '{iteration}'")
            if cur.fetchone() is None:
                cur.execute("INSERT or IGNORE INTO rooms VALUES (?,?,?,?,?,?)", temp)
                conn.commit()
                print('Добавил новую строчку')
                print("Room:", temp[0], "Iteration:", temp[1], "X:", temp[2], "Y:", temp[3], "WIDTH:", temp[4], "HEIGHT:", temp[5])
            else:
                print('Такая запись уже есть')


