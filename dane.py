map = [[[0,1,0,1,"a"],[0,1,1,0,"b"]],
       [[1,0,0,1,"c"],[1,0,1,0,"d"]]]

def comandy(x, y):
    e = True
    while e == True:
        c = input(">: ")
        match c:
            # gora
            case "g":
                if map[x][y][0] == 1:
                    x = x - 1
                    print(map[x][y])
                else:
                    print("nie")
            # dol
            case "d":
                if map[x][y][1] == 1:
                    x = x + 1
                    print(map[x][y])
                else:
                    print("nie")
            # lewo
            case "l":
                if map[x][y][2] == 1:
                    y = y - 1
                    print(map[x][y])
                else:
                    print("nie")
            # prawo
            case "p":
                if map[x][y][3] == 1:
                    y = y + 1
                    print(map[x][y])
                else:
                    print("nie")
            # stop
            case "s":
                e = False
            # info
            case "i":
                print("opcje: ")
                for h in range(0,4):
                    match h:
                        case 0:
                            if map[x][y][h] == 1:
                                print("gora")
                        
                        case 1:
                            if map[x][y][h] == 1:
                                print("dol")

                        case 2:
                            if map[x][y][h] == 1:
                                print("lewo")

                        case 3:
                            if map[x][y][h] == 1:
                                print("prawo")