## 어디서부터 한지 모르겠으니까 다시 해보자
## 좋은 코드 _ 복사
## 거의 완전 완성 되어감!!!

grid = [["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]]

for row in grid:
    print(' '.join(row))

print('\n================================\n')



for i in range(1, 10) :
    
    if i % 2 == 1 :
        if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X") :
            print("축하합니다~ X가 이겼습니다.")
            break
        else :    
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
        
    elif i % 2 == 0 :
        if (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O") :
            print("축하합니다~ O가 이겼습니다.")
            break
            
        else :
            print("O의 턴입니다.")
            x = int(input("행 번호를 선택하세요 (0-2): "))
            y = int(input("열 번호를 선택하세요 (0-2): "))
            print('\n================================\n')
            if grid[x][y] != "-" :
                        print("놓을 수 없는 자리입니다. 다시 골라주십시오.")
                        x = int(input("행 번호를 선택하세요 (0-2): "))
                        y = int(input("열 번호를 선택하세요 (0-2): "))
                        print('\n================================\n')
                        grid[x][y] = 'O'
            
            else :
                grid[x][y] = 'O'  

            
            for row in grid:
                print(' '.join(row))

    # elif grid[x][y] != "-" :
    # elif grid[x][y] == "X" or grid[x][y] == "0" :
        # print("놓을 수 없는 자리입니다. 다시 골라주십시오.")
    
    # elif "-" not in grid : 
        # if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") :
    #         print("축하합니다~ X가 이겼습니다.")
    
        # elif (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") :
        #     print("축하합니다~ O가 이겼습니다.")
        
    else : 
        print("비겼습니다.")
                

    # elif "-" not in grid :      # grid에 "-" 없이 다 채워졌으면
    #     if (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") :
    #             print("축하합니다~ X가 이겼습니다.")
         
    #     elif (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") :
    #             print("축하합니다~ O가 이겼습니다.")
