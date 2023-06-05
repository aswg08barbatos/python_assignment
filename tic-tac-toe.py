## 어디서부터 한지 모르겠으니까 다시 해보자
## 좋은 코드 _ 복사
## 거의 완전 완성 되어감!!! _ 복사 _ 복사

grid = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

for row in grid:
    print(' '.join(row))

print('\n================================\n')


def resultWin(x, y) :
    if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or \
     (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X") or \
     (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or \
     (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O") :
        return True

    else :
        return False

def turn() :
    i



for i in range(1, 10) :
    
    if i % 2 == 1 :
        print("X의 턴입니다.")
        x = int(input("행 번호를 선택하세요 (0-2): "))
        y = int(input("열 번호를 선택하세요 (0-2): "))
        print('\n================================\n')
        if grid[x][y] == "X" or grid[x][y] == "0" :
                print("놓을 수 없는 자리입니다. 다시 골라주십시오.")
                x = int(input("행 번호를 선택하세요 (0-2): "))
                y = int(input("열 번호를 선택하세요 (0-2): "))
                print('\n================================\n')
                grid[x][y] = 'X'
        else :
            grid[x][y] = 'X'
            
        
        for row in grid:
            print(' '.join(row))              
        
        if resultWin(x, y) :
            print("축하합니다~ X가 이겼습니다.")
            break
         
    
    elif i % 2 == 0 :
            
        print("O의 턴입니다.")
        x = int(input("행 번호를 선택하세요 (0-2): "))
        y = int(input("열 번호를 선택하세요 (0-2): "))
        print('\n================================\n')
        # if grid[x][y] != "-" :
        if grid[x][y] == "X" or grid[x][y] == "0" :
                    print("놓을 수 없는 자리입니다. 다시 골라주십시오.")
                    x = int(input("행 번호를 선택하세요 (0-2): "))
                    y = int(input("열 번호를 선택하세요 (0-2): "))
                    print('\n================================\n')
                    grid[x][y] = 'O'
        
        else :
            grid[x][y] = 'O'  

        
        for row in grid:
            print(' '.join(row))

        if resultWin(x, y) :
            print("축하합니다~ O가 이겼습니다.")
            break
    # elif for bar in grid :
    #         if bar != "-" :
        
    #             if resultWin(x, y) :
    #                 print("축하합니다~ X가 이겼습니다.")

    #             elif resultWin(x, y) :
    #                 print("축하합니다~ O가 이겼습니다.")
                    
    #             else :
    #                 print("비겼습니다.")

    

            
                        
