import time

print('''      .--.   |V|
     /    \ _| /
     q .. p \ /
      \--/  //
jgs  __||__//
    /.    _/
   // \  /
  //   ||
  \\  /  \
   )\|    |
  / || || |
  |/\| || |
     | || |
     \ || /
   __/ || \__
  \____/\____/
  


''')

print('''            .-""""-.       .-""""-.
           /        \     /        \
          /_        _\   /_        _\
         // \      / \\ // \      / \\
         |\__\    /__/| |\__\    /__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        \
  /_        _\|  /_        _\|  /_        _\
 // \      / \\ // \      / \\ // \      / \\
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
 jgs  |  |           |  |           |  |
      |  |           |  |           |  |


''')

print("We want to welcome you to our humble galaxy, where we aliens all live in peace!")
actual_password = "WALL-E"
entered_password = input('''What is your alien password ? Remember, you have one try otherwise you will be returned to your galaxy immediately!
                \n\nPlease Enter Your Authorized Password (1 try remaining): ''')
if entered_password == actual_password:
    print("Welcome to the galaxy of Obwinox, where peace is a protocol and a standard met at all times! ")
else:
    print("You have entered the wrong password, returning you to your origin galaxy within 3 seconds.")
    N=0
    for N in range(1,4):
        time.sleep(1)
        print(str(N)+"\n\n\n")
        N+=1
    print("You have been returned to your galaxy due to non-compliance.")





