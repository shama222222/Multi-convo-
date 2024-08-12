import requests
import time
import sys
from platform import system
import os
import http.server
import socketserver
import threading
BOLD = '\033[1m'
CYAN = '\033[96m'
logo =("""\x1b[1;36m

\033[1;35m. __        ________   ______   ________  __    __  _______
\033[1;34m./  |      /        | /      \ /        |/  \  /  |/       \
\033[1;33m.$$ |      $$$$$$$$/ /$$$$$$  |$$$$$$$$/ $$  \ $$ |$$$$$$$  |
\033[1;32m.$$ |      $$ |__    $$ | _$$/ $$ |__    $$$  \$$ |$$ |  $$ |
\033[1;39m.$$ |      $$    |   $$ |/    |$$    |   $$$$  $$ |$$ |  $$ |
\033[1;38m.$$ |      $$$$$/    $$ |$$$$ |$$$$$/    $$ $$ $$ |$$ |  $$ |
\033[1;37m.$$ |_____ $$ |_____ $$ \__$$ |$$ |_____ $$ |$$$$ |$$ |__$$ |
\033[1;36m.$$       |$$       |$$    $$/ $$       |$$ | $$$ |$$    $$/
\033[1;35m.$$$$$$$$/ $$$$$$$$/  $$$$$$/  $$$$$$$$/ $$/   $$/ $$$$$$$/                          >


\033[1;35m.______   _______   __    __   ______   __      __
\033[1;34m. /      \ /       \ /  |  /  | /      \ /  \    /  |
\033[1;33m./$$$$$$  |$$$$$$$  |$$ |  $$ |/$$$$$$  |$$  \  /$$/
\033[1;32m.$$ |__$$ |$$ |__$$ |$$ |__$$ |$$ |__$$ | $$  \/$$/
\033[1;37m.$$    $$ |$$    $$< $$    $$ |$$    $$ |  $$  $$/
\033[1;36m.$$$$$$$$ |$$$$$$$  |$$$$$$$$ |$$$$$$$$ |   $$$$/
\033[1;35m.$$ |  $$ |$$ |__$$ |$$ |  $$ |$$ |  $$ |    $$ |
\033[1;34m.$$ |  $$ |$$    $$/ $$ |  $$ |$$ |  $$ |    $$ |
\033[1;33m.$$/   $$/ $$$$$$$/  $$/   $$/ $$/   $$/     $$/
-----------------------------------------
\033[1;32m.Author      :  𝖳𝖧𝖤 𝖴𝖭𝖡𝖤𝖠𝖳𝖠𝖡𝖫𝖤 𝖫𝖤𝖦𝖤𝖭𝖣 𝖡𝖮𝖸 𝖠𝖡𝖧𝖠𝖸
 \033[1;34mGithub       :  https://github.com/Akabhay11       |
 \033[1;35m.Facebook  : https://www.facebook.com/profile.php?id=100036389929808&mibextid=ZbWKwL
 \033[1;30mTool Name : 𝖬𝖴𝖫𝖳𝖨 𝖳𝖮𝖪𝖤𝖭 𝖢𝖮𝖭𝖵𝖮 𝖳𝖮𝖮𝖫     |
 \033[1;34mType type. : 𝗙𝗔𝗧𝗜𝗠𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 𝗞𝗘 𝗟𝗜𝗬𝗘 𝗙𝗥𝗘𝗘 𝗛𝗔𝗜    |
--------------------------------------------
\033[1;32m.𝗙𝗔𝗧𝗜𝗠𝗔 𝗞𝗜 𝗖𝗛𝗨𝗖𝗛𝗜 🥺𝗗𝗕𝗔 𝗙𝗜𝗥 𝗕𝗔𝗛𝗨𝗧 𝗧𝗘𝗝 𝗖𝗛𝗔𝗟𝗘𝗚𝗔
--------------------------------------------""" )
def cls():
        if system() == 'Linux':
            os.system('clear')
        else:
            if system() == 'Windows':
                os.system('cls')
cls()
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"H")
def execute_server():
    PORT = 4000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print("Server running at http://localhost:{}".format(PORT))
        httpd.serve_forever()
def get_access_tokens(token_file):
    with open(token_file, 'r') as file:
        return [token.strip() for token in file]
def send_messages(convo_id, tokens, messages, haters_name, speed):
    headers = {
        'Content-type': 'application/json',
    }
    num_tokens = len(tokens)
    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)
    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = tokens[token_index]
                message = messages[message_index].strip()
                url = "https://graph.facebook.com/v17.0/{}/".format('t_' + convo_id)
                parameters = {'access_token': access_token, 'message': f'{haters_name} {message>
                response = requests.post(url, json=parameters, headers=headers)
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                if response.ok:
                    print("\033[1;33m[+] ABH4Y | DON TOOL KE DWARA MESSAGE BHEJA GYA BHOSDI KE >
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}>
                    print("\033[1;32m  - Time: {}".format(current_time))
                else:
                    print("\033[1;32m[x] MESSEGE FAIL HO GYA BHOSDI KE TOKAN SAHI DAL  {} of Co>
                        message_index + 1, convo_id, token_index + 1, f'{haters_name} {message}>
                    print(" \033[1;34m - Time: {}".format(current_time))
                time.sleep(speed)
            print("\n\033[1;33m[+] All messages sent. Restarting the process...\n")
        except Exception as e:
            print("\033[1;35m[!] An error occurred: {}".format(e))
            def main():
    print(logo)
    print(' \033[1;35m[+] 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗡𝗔𝗠𝗘 ')
    token_file = input(BOLD + CYAN + "=>").strip()
    tokens = get_access_tokens(token_file)
    print(' \033[1;34m[+] 𝗖𝗢𝗡𝗩𝗢 𝗜𝗗 ')
    convo_id = input(BOLD + CYAN + "=>").strip()
    print(' \033[1;33m[+] 𝗠𝗘𝗦𝗦𝗘𝗚𝗘 𝗙𝗜𝗟𝗘 ')
    messages_file = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;32m[+] 𝗛𝗔𝗧𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘 ')
    haters_name = input(BOLD + CYAN + "=> ").strip()
    print(' \033[1;36m[+] 𝗦𝗣𝗘𝗘𝗗 𝗦𝗘𝗖𝗢𝗡𝗗' )
    speed = int(input(BOLD + CYAN + "======> ").strip())
    with open(messages_file, 'r') as file:
        messages = file.readlines()
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()
    send_messages(convo_id, tokens, messages, haters_name, speed)
if __name__ == '__main__':
    main()
