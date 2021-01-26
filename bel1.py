import os, time, getpass, sys, itertools, threading

print('\033[1;35m|------------|')
user = input('\033[1;31m| username : | ' )
print('\033[1;33m|------------|')


print('\033[1;35m|------------|')
sandi = input('\033[1;31m| password : | ')
print('\033[1;33m|------------|')

if user == 'abdul' and sandi == 'malik':

  print('ACCESS GRANTED')
else:
   print(exit())
   print('ACCESS DENIED')
exit

localtime = time.asctime( time.localtime(time.time()) )
print ("\033[1;34m|----------------------|")
print("\033[1;31m|LOCAL TIME INDONESIA :|",  localtime)
print ("\033[1;33m|----------------------|")

print("    \033[1;35m|---------------------------------------|")
print("    \033[1;34m|          Authour : Mr.BearV1          |")
print("    \033[1;31m| Github : https://github.com/mr.bearv1 |")
print("    \033[1;32m|           WA : 085727721692           |")
print("    \033[1;33m|---------------------------------------|")
print('\n')


done = False

#animasi loading
def animate():
    for c in itertools.cycle(['Indonesia-cyber-security', 'iNdonesia-cyber-security', 'inDonesia-cyber-security', 'indOnesia-cyber-security', 'indoNesia-cyber-security', 'indonEsia-cyber-security', 'indoneSia-cyber-security', 'indonesIa-cyber-security', 'indonesiA-cyber-security', 'indonesia-Cyber-security', 'indonesia-cYber-security', 'indonesia-cyBer-security', 'indonesia-cybEr-security', 'indonesia-cybeR-security', 'indonesia-cyber-Security', 'indonesia-cyber-sEcurity', 'indonesia-cyber-seCurity', 'indonesia-cyber-secUrity', 'indonesia-cyber-secuRity', 'indonesia-cyber-securIty', 'indonesia-cyber-securiTy', 'indonesia-cyber-securitY']):
        if done:
            break
        sys.stdout.write('\r\033[1;33m|TUNNGU SEBENTAR :|' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

#proses lama disini

time.sleep(30)
done = True

sl
