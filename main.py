import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
Size=18
Wood=Size//3
l=1
k=1
print(Fore.CYAN+'==^^*****HAPPY CHRISTMAS**^^==') 
for i in range(Size):
    print((' ' * (Size - i)) + (Fore.GREEN+'#' * ((2 * i) + 1)))
    
for i in range(Wood):
     print(('  '*((Size-1)//2))+(Fore.BLUE+'!' * Wood) )

print(' '*16+ '======')

for i in range(l):
    for j in range(k):
        print(Fore.YELLOW+'^^'*19)
        print(Fore.YELLOW+'**'*19)
      
       
