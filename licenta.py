
import win32gui
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import subprocess
import time
import math
import PySimpleGUI as sg
import os
import glob
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#gaseste fereastra scrcpy cu device-ul android
hwnd = win32gui.FindWindow(None,'GM1900')

font = ImageFont.truetype('arial.ttf', 30)

# formula rgb->gray  : gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.587, 0.114])

def screenshot( windowTitle = None ):
    if windowTitle:
        hwnd = win32gui.FindWindow(None, windowTitle)
        if hwnd:
            #seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            #returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r ,b)
            #Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            #print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            return im

        else:
            print('Window not found!')

    else:
        im = pyautogui.screenshot()
        return im




def screenshot_test_youtube(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            # returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r, b)
            # Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            # print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            # print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            im=im.crop((311,75,347,119))
            # im.save("D:/LICENTA/script_python/imagini/verificare_youtube.jpg")
            #im.show()
            # im_conexiune.save("D:/LICENTA/script_python/imagini/verificare_conexiune.jpg")
            # im_conexiune = mpimg.imread("D:/LICENTA/script_python/imagini/verificim1 = im.crop((l-31,350-t,1070-r,b-511))
            # im_conexiune = screeare_conexiune.jpg")
            # imgplot = plt.imshow(im_conexiune)
            # plt.show()

            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im



def screenshot_test_gmail(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            # returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r, b)
            # Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            #print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            # print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            im=im.crop((9,662,344,702))

            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

def screenshot_test_chat(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            # returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r, b)
            # Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            # print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            # print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            im = im.crop((315, 410, 333, 426))

            return im


        else:
            print('Window not found!')

    else:
        im = pyautogui.screenshot()
        return im

def screenshot_test_emag(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            # returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r, b)
            # Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            # print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            # print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            im=im.crop((15, 95, 233, 140))

            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im

def screenshot_test_maps(window_title=None):
    if window_title:
        hwnd = win32gui.FindWindow(None, window_title)
        if hwnd:
            # seteaza fereastra  in prim plan
            win32gui.SetForegroundWindow(hwnd)
            # returneaza coordonatele ferestrei
            l, t, r, b = win32gui.GetClientRect(hwnd)
            print(l, t, r, b)
            # Convert client coordinates to screen coords
            l, t = win32gui.ClientToScreen(hwnd, (l, t))
            # print(l,t)
            r, b = win32gui.ClientToScreen(hwnd, (r - l, b - t))
            # print(r,b)
            im = pyautogui.screenshot(region=(l, t, r, b))
            print(l, t, r, b)
            im=im.crop((4, 710, 99, 758))

            return im
        else:
            print('Window not found!')
    else:
        im = pyautogui.screenshot()
        return im




def testare_conexiune_date_mobile():
    i = 0
    list = []
    cmd = 'adb shell dumpsys telephony.registry'
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line = process.stdout.readline().strip().decode('utf-8')
        list.append(line)
        # print(line)
        if not line:
            break

    # print(list)
    if 'mDataConnectionState=2' in list:
        i = 1
        a = "Conexiune mobila detectata"
        print("Conexiune mobila detectata")

    else:
        a = "Nu exista conexiune mobila"
        print("Nu exista conexiune mobila")

    return i

def testare_conexiune_wifi():
    j = 0
    list1 = []
    cmd1 = 'adb shell dumpsys wifi  | find "Wi-Fi"'
    process = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        line1 = process.stdout.readline().strip().decode('utf-8')
        list1.append(line1)
        # print(line)
        if not line1:
            break

    # print(list1)
    if 'Wi-Fi is enabled' in list1:
        j = 1
        b = "Conexiune wifi detectata"
        print("Conexiune wifi detectata")

    else:
        b = "Nu exista conexiune wifi"
        print("Nu exista conexiune wifi")

    return j






def deblocare_telefon(tasta1,tasta2,tasta3,tasta4,nume_test):
    im_curent = screenshot('GM1900')
    # im_curent.show()
    # conversie img in sir
    im_curent1 = np.asarray(im_curent)
    print(im_curent1)
    im_curent1 = rgb2gray(im_curent1)
    print(im_curent1)

    total = sum(abs(im_curent1))
    print(total)
    total = sum(abs(total))
    print("total")
    print(total)

    if total < 100 or total==37809623.15769965:
        subprocess.call("adb shell input keyevent 26", shell=True)

    else:
        subprocess.call("adb shell input keyevent 26", shell=True)
        time.sleep(1)
        subprocess.call("adb shell input keyevent 26", shell=True)

    time.sleep(2)

    # update GUI
    rezultat = 'Rulare test '+nume_test+''

    window['-deblocare-'].update(rezultat)
    window['-Internet-'].update(rezultat)
    window['-Rezultat-'].update(rezultat)
    window['-Path-'].update(rezultat)

    window.refresh()

    time.sleep(3)

    header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

    d = ImageDraw.Draw(header_im)
    d.text((5, 5), "Stare intiala - Telefon Blocat", font=font, fill=(0, 0, 0))

    # if header_im:
    # header_im.show()

    im = screenshot('GM1900')
    im_final = Image.new('RGB', (589, 1088), (255, 255, 255))
    im_final.paste(header_im, (0, 0))
    im_final.paste(im, (0, 61))

    diff = 700001
    while diff > 700000:
        xc1 = math.trunc(rezolutie_x * 0.5)
        print(xc1)
        xc1 = str(xc1)
        yc1 = math.trunc(rezolutie_y * 0.8)
        yc1 = str(yc1)
        yc2 = str(math.trunc(rezolutie_y * 0.15))
        string = "adb shell input touchscreen swipe " + xc1 + " " + yc1 + " " + xc1 + " " + yc2
        print(string)
        subprocess.call(string, shell=True)
        #subprocess.call("adb shell input swipe 541 1844 541 844", shell=True)
        time.sleep(3)
        if diff > 700000:
            im_curent = screenshot('GM1900')
            im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_deblocare.jpg")
            im_curent1 = np.asarray(im_curent)
            im_test = np.asarray(im_test)

            im_curent1 = rgb2gray(im_curent1)
            im_test = rgb2gray(im_test)
            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_deblocare.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_deblocare.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            diff = im_curent1 - im_test
            # print (diff)
            diff = sum(abs(diff))
            diff = sum(abs(diff))
            print(diff)




        tasta1 = "adb shell input keyevent " + tasta1
        subprocess.call(tasta1, shell=True)
        time.sleep(1)
        tasta2 = "adb shell input keyevent " + tasta2
        subprocess.call(tasta2, shell=True)
        time.sleep(1)
        tasta3 = "adb shell input keyevent " + tasta3
        subprocess.call(tasta3, shell=True)
        time.sleep(1)
        tasta4 = "adb shell input keyevent " + tasta4
        subprocess.call(tasta4, shell=True)
        time.sleep(2)

        print("Validare deblocare ")

        #update GUI ->validare deblocare
        rezultat = 'Pass'
        window['-deblocare-'].update(rezultat)
        window.refresh()


        return im_final


#im_final = deblocare_telefon('8', '16', '16', '16', 'Youtube')

#subprocess.call('adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "about:newtab" --activity-clear-task', shell=True)


rezolutie = subprocess.Popen("adb shell wm size", stdout=subprocess.PIPE)
rezolutie = rezolutie.stdout.read()

print(rezolutie)
rezolutie_x = int(rezolutie[15:19])

print(rezolutie_x)

rezolutie_y = int(rezolutie[20:24])




sg.change_look_and_feel('SystemDefault')

layout = [[sg.Text("Teste:", size=(12, 1)), sg.Text("", size=(2, 1)), sg.Text("Rezultate:", size=(10, 1)), sg.Text("", size=(22, 1)),sg.Text("Istoric:", size=(10, 1)),sg.Text("Procentaj:", size=(7, 1)),sg.Text("Ultima rulare:", size=(15, 1))],
          [sg.Button("Test Youtube", size=(12, 1)), sg.Text("", size=(2, 1)),sg.Button("Raportul ultimului test rulat", size=(33, 1)),sg.Text("Youtube:", size=(10, 1)),sg.Input(key='-Youtube%-', enable_events=True, size=(8, 1)),sg.Input(key='-YoutubeD-', enable_events=True)],
          [sg.Button("Test Gmail", size=(12, 1)), sg.Text("", size=(2, 1)),sg.Button("Directorul cu rapoarte", size=(33, 1)),sg.Text("Gmail:", size=(10, 1)),sg.Input(key='-Gmail%-', enable_events=True, size=(8, 1)),sg.Input(key='-GmailD-', enable_events=True)],
          [sg.Button("Test Chat", size=(12, 1)), sg.Text("", size=(2, 1)), sg.Text("Deblocare:", size=(8, 1)),sg.Input('Inca nu s-au rulat teste', key='-deblocare-', enable_events=True,size=(27,1)),sg.Text("Chat:", size=(10, 1)),sg.Input(key='-Chat%-', enable_events=True, size=(8, 1)),sg.Input(key='-ChatD-', enable_events=True)],
          [sg.Button("Test eMAG", size=(12, 1)), sg.Text("", size=(2, 1)), sg.Text("Conexiune internet:", size=(14, 1)),sg.Input('Inca nu s-au rulat teste', key='-Internet-',enable_events=True, size=(20,1)),sg.Text("eMAG:", size=(10, 1)),sg.Input(key='-eMAG%-', enable_events=True, size=(8, 1)),sg.Input(key='-eMAGD-', enable_events=True)],
          [sg.Button("Test Maps", size=(12, 1)), sg.Text("", size=(2, 1)), sg.Text("Rezultat final:", size=(10, 1)),sg.Input('Inca nu s-au rulat teste', key='-Rezultat-',enable_events=True,size=(25,1)),sg.Text(" Maps:", size=(10, 1)),sg.Input(key='-Maps%-', enable_events=True, size=(8, 1)),sg.Input(key='-MapsD-', enable_events=True)],
          [sg.Text("", size=(12, 1)), sg.Text("", size=(2, 1)), sg.Text("Test recent:", size=(12, 1)),sg.Input('Inca nu s-au rulat teste', key='-Path-', size=(38, 1))],
          [sg.Text("", size=(30, 20)),sg.Image(r'D:\LICENTA\script_python\imagini\a.png')],]

window = sg.Window("Testare Android",layout,icon=r'D:\LICENTA\script_python\imagini\logo.ico',size=(900, 440))

#window.read()

#GUI LOOP - for reading buttons
while True:
    event, values = window.read()

    list_of_files = glob.glob('D:\LICENTA\script_python\\teste\*')
    #print(list_of_files)
    total_youtube_stats = sum('Youtube' in s for s in list_of_files)
    total_chat_stats = sum('Chat' in s for s in list_of_files)
    total_gmail_stats = sum('Gmail' in s for s in list_of_files)
    total_emag_stats = sum('eMAG' in s for s in list_of_files)
    total_maps_stats = sum('Maps' in s for s in list_of_files)

    pass_youtube_stats = sum('Youtube_Pass' in s for s in list_of_files)
    pass_chat_stats = sum('Chat_Pass' in s for s in list_of_files)
    pass_gmail_stats = sum('Gmail_Pass' in s for s in list_of_files)
    pass_emag_stats = sum('eMAG_Pass' in s for s in list_of_files)
    pass_maps_stats = sum('Maps_Pass' in s for s in list_of_files)


    procent_youtube_stats = pass_youtube_stats / total_youtube_stats
    procent_youtube_stats = str(procent_youtube_stats * 100)[0:4] + '%'
    #print(procent_youtube_stats)

    procent_chat_stats = pass_chat_stats / total_chat_stats
    procent_chat_stats = str(procent_chat_stats * 100)[0:4] + '%'

    procent_gmail_stats = pass_gmail_stats / total_gmail_stats
    procent_gmail_stats = str(procent_gmail_stats * 100)[0:4] + '%'

    procent_emag_stats = pass_emag_stats / total_emag_stats
    procent_emag_stats = str(procent_emag_stats * 100)[0:4] + '%'

    procent_maps_stats = pass_maps_stats / total_maps_stats
    procent_maps_stats = str(procent_maps_stats * 100)[0:4] + '%'


    window['-Youtube%-'].update(procent_youtube_stats)

    window['-Gmail%-'].update(procent_gmail_stats)

    window['-Chat%-'].update(procent_chat_stats)

    window['-eMAG%-'].update(procent_emag_stats)

    window['-Maps%-'].update(procent_maps_stats)


    list_of_files_youtube = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Youtube_*')
    #print(list_of_files_youtube)
    latest_file = max(list_of_files_youtube, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[-10:-8] + ":" + latest_file[-8:-6] + ":" + latest_file[-6:-4]
    #print(latest_file)
    window['-YoutubeD-'].update(latest_file)

    list_of_files_chat = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Chat_*')
    # print(list_of_files_chat)
    latest_file = max(list_of_files_chat, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[-10:-8] + ":" + latest_file[ -8:-6] + ":" + latest_file[-6:-4]
    #print(latest_file)
    window['-ChatD-'].update(latest_file)


    list_of_files_gmail = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Gmail_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_gmail, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[-10:-8] + ":" + latest_file[ -8:-6] + ":" + latest_file[-6:-4]
    #print(latest_file)
    window['-GmailD-'].update(latest_file)

    list_of_files_emag = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_eMAG_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_emag, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[-10:-8] + ":" + latest_file[-8:-6] + ":" + latest_file[-6:-4]
    # print(latest_file)
    window['-eMAGD-'].update(latest_file)

    list_of_files_maps = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Maps_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_maps, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-MapsD-'].update(latest_file)


    # window.refresh()




    # Test youtube - daca se apasa butonul
    if event == "Test Youtube":

        #functie de deblocare ecran
        im_final = deblocare_telefon('8', '16', '16', '16', 'Youtube')

        im1 = screenshot('GM1900')
        header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

        d = ImageDraw.Draw(header_im)
        d.text((5, 5), "Telefon deblocat cu succes", font=font, fill=(0, 0, 0))

        # if header_im:
        #     header_im.show()

        im_final1 = Image.new('RGB', (589, 1088), (255, 255, 255))
        im_final1.paste(header_im, (0, 0))
        im_final1.paste(im1, (0, 61))
        time.sleep(2)

        #Testare conexiune internet
        #Testare conexiune date mobile

        i = testare_conexiune_date_mobile()

        #Testare conexiune wi-fi
        j = testare_conexiune_wifi()

        #Daca se detecteaza conexiune la internet se continua testul
        #Daca nu exista conexiune testul este declarat picat
        if i == 1 or j == 1:
            # update GUI ->validare conexiune internet
            rezultat = 'Pass'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Conexiune internet validata", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            time.sleep(3)

            # click google chrome
            subprocess.call(
                'adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "about:newtab" --activity-clear-task',
                shell=True)

            # subprocess.call("adb shell am start -n com.android.chrome/com.google.android.apps.chrome.Main", shell=True)
            time.sleep(6)

            # click URL-bar
            xc1 = math.trunc(rezolutie_x * 0.29)

            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.08)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)

            # subprocess.call(" adb shell input tap 562 743",shell=True )

            time.sleep(2)

            # introducere site www.yotube.com
            subprocess.call("adb shell input keyevent 51 51 51 56 53 43 49 48 49 30 33 56 31 43 41", shell=True)

            time.sleep(2)

            # screenshot
            im3 = screenshot('GM1900')

            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "URL-bar deschis", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final3 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final3.paste(header_im, (0, 0))
            im_final3.paste(im3, (0, 61))
            # im_final2.show()

            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)


            time.sleep(2)

            # #im_curent2 = screenshot_test_youtube('GM1900')
            # #im_curent2.show()
            #
            # time.sleep(2)
            #
            # # click primul videocllip din homepage
            # subprocess.call("adb shell input tap 555 844",shell=True )
            #
            # time.sleep(2)

            # click primul videocllip din homepage

            xc1 = math.trunc(rezolutie_x * 0.5)
            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.3)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(5)

            # screenshot stare finala
            im4 = screenshot('GM1900')

            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Videoclip incarcat cu succes", font=font, fill=(0, 0, 0))
            im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final4.paste(header_im, (0, 0))
            im_final4.paste(im4, (0, 61))
            # #im4.show()
            # im_final4.show()

            time.sleep(2)

            im_curent = screenshot_test_youtube('GM1900')
            im_test = Image.open("D:/LICENTA/script_python/imagini/verificare_youtube.jpg")
            # im_test.show()
            # im_curent.show()
            im_curent1 = np.asarray(im_curent)
            print(im_curent1)
            im_test = np.asarray(im_test)
            print("im array")
            print(im_test)

            im_curent1 = rgb2gray(im_curent1)
            print(im_curent1)
            im_test = rgb2gray(im_test)
            print("im rgb")
            print(im_test)


            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                print('aaa')
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_youtube.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_youtube.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            print("bbb")

            diff = im_curent1 - im_test
            print("d1")
            print(diff)
            diff = sum(abs(diff))
            print("d2")
            print(diff)
            diff = sum(abs(diff))
            print(diff)

            if diff < 32000:
                print("Test youtube - PASS")

                # im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
                # im_final4.paste(header_im, (0, 0))
                # im_final4.paste(im4, (0, 61))

                im_list = [im_final1, im_final2, im_final3, im_final4]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Youtube_Pass_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Pass'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Youtube_Pass'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Youtube_Pass' + date + filename2
                window['-Path-'].update(rezultat)



            else:
                print("Test youtube - FAIL")

                # im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
                # im_final4.paste(header_im, (0, 0))
                # im_final4.paste(im4, (0, 61))

                im_list = [im_final1, im_final2, im_final3, im_final4]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Youtube_Fail_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Fail'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Youtube_Fail'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Youtube_Fail' + date + filename2
                window['-Path-'].update(rezultat)

            time.sleep(5)

            # inchidere aplicatie
            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
            xc1 = math.trunc(rezolutie_x * 0.44)
            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.9)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)








        else:
            # update GUI ->validare conexiune internet
            rezultat = 'Fail'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Nu exista conexiune la internet", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            print("Test youtube - FAIL")



            im_list = [im_final1, im_final2]
            now = datetime.now()
            date = now.strftime("%Y%m%d%H%M%S")
            print(date)
            filename = "D:\LICENTA\script_python\\teste\PDF_test_Youtube_Fail_"
            filename2 = ".pdf"
            print(filename2)
            filename = filename + date + filename2
            im_final.save((filename))
            pdf1 = filename
            im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
            window.find_element('-Rezultat-')
            rezultat = 'Fail'
            window['-Rezultat-'].update(rezultat)
            rezultat = 'PDF_test_Youtube_Fail'
            window.find_element('-Path-')
            rezultat = 'PDF_test_Youtube_Fail' + date + filename2
            window['-Path-'].update(rezultat)



    # Test Gmail - daca se apasa butonul
    if event == "Test Gmail":
        # functie de deblocare ecran
        im_final = deblocare_telefon('8', '16', '16', '16', 'Gmail')

        im1 = screenshot('GM1900')
        header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

        d = ImageDraw.Draw(header_im)
        d.text((5, 5), "Telefon deblocat cu succes", font=font, fill=(0, 0, 0))


        im_final1 = Image.new('RGB', (589, 1088), (255, 255, 255))
        im_final1.paste(header_im, (0, 0))
        im_final1.paste(im1, (0, 61))
        time.sleep(2)

        # Testare conexiune internet
        # Testare conexiune date mobile

        i = testare_conexiune_date_mobile()

        # Testare conexiune wi-fi
        j = testare_conexiune_wifi()

        # Daca se detecteaza conexiune la internet se continua testul
        # Daca nu exista conexiune testul este declarat picat
        if i == 1 or j == 1:
            # update GUI ->validare conexiune internet
            rezultat = 'Pass'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Conexiune internet validata", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            # deschidere aplicatia Gmail
            subprocess.call('adb shell am start -n com.google.android.gm/.ConversationListActivityGmail', shell=True)

            time.sleep(3)
            im3 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Aplicatie Gmail deschisa", font=font, fill=(0, 0, 0))

            im_final3 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final3.paste(header_im, (0, 0))
            im_final3.paste(im3, (0, 61))

            # click buton "Compose" pentru a creea un mail nou
            xc1 = math.trunc(rezolutie_x * 0.76)
            # print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.877)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(2)

            # click sectiunea " To: "
            xc1 = math.trunc(rezolutie_x * 0.297)
            # print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.21)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(2)

            # introducerea adresei de mail a destinatarului
            subprocess.call("adb shell input keyevent 40 29 49 46 29 41 49 47 29 48 8 7 77 53 29 36 43 43 56 31 43 41 ",
                            shell=True)

            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)

            # click sectiunea " Subject: "
            xc1 = math.trunc(rezolutie_x * 0.153)
            # print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.283)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(2)

            # introducerea Subiectului
            subprocess.call("adb shell input keyevent 40 37 31 33 42 48 29 62 9 7 9 9 ", shell=True)
            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)

            # click sectiunea "Compose email"
            xc1 = math.trunc(rezolutie_x * 0.124)
            # print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.356)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(2)

            # introducerea textului mail-ului
            subprocess.call("adb shell input keyevent 48 33 47 48 62 35 41 29 37 40 ",
                            shell=True)
            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)

            # screenshot
            im4 = screenshot('GM1900')

            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Text mail creat: ", font=font, fill=(0, 0, 0))

            im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final4.paste(header_im, (0, 0))
            im_final4.paste(im4, (0, 61))

            time.sleep(3)

            # click "Send"
            xc1 = math.trunc(rezolutie_x * 0.823)
            # print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.075)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)

            time.sleep(2)

            im5 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Mail trimis:", font=font, fill=(0, 0, 0))

            # if header_im:
            # header_im.show()

            im_final5 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final5.paste(header_im, (0, 0))
            im_final5.paste(im5, (0, 61))

            # im.save("D:/LICENTA/script_python/imagini/verificare_youtube.jpg")
            # im.show()
            # im_gm.save("D:/LICENTA/script_python/imagini/gm.jpg")
            # im = mpimg.imread("D:/LICENTA/script_python/imagini/gm.jpg")
            # imgplot = plt.imshow(im_gm)
            # plt.show()
            # im_gm_test = im_gm.crop((9, 662, 344, 702))
            # im_gm_test.save("D:/LICENTA/script_python/imagini/verificare_gmail.jpg")
            # im_gm_test.show()

            im_curent = screenshot_test_gmail('GM1900')
            im_test = Image.open("D:/LICENTA/script_python/imagini/verificare_gmail.jpg")
            # im_test.show()
            # im_curent.show()
            im_curent1 = np.asarray(im_curent)
            im_test = np.asarray(im_test)

            im_curent1 = rgb2gray(im_curent1)
            im_test = rgb2gray(im_test)

            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                print('aaa')
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_gmail.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_gmail.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            print("bbb")

            diff = im_curent1 - im_test
            print(diff)
            diff = sum(abs(diff))
            diff = sum(abs(diff))
            print(diff)

            if diff < 9000:
                print("Test Gmail - PASS")


                im_list = [im_final1, im_final2, im_final3, im_final4,im_final5]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Gmail_Pass_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Pass'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Gmail_Pass'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Gmail_Pass' + date + filename2
                window['-Path-'].update(rezultat)



            else:
                print("Test Gmail - FAIL")



                im_list = [im_final1, im_final2, im_final3, im_final4,im_final5]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Gmail_Fail_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Fail'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Gmail_Fail'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Gmail_Fail' + date + filename2
                window['-Path-'].update(rezultat)

            time.sleep(5)

            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
            xc1 = math.trunc(rezolutie_x * 0.44)
            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.9)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

        else:
            # update GUI ->validare conexiune internet
            rezultat = 'Fail'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Nu exista conexiune la internet", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            print("Test Gmail - FAIL")


            im_list = [im_final1, im_final2]
            now = datetime.now()
            date = now.strftime("%Y%m%d%H%M%S")
            print(date)
            filename = "D:\LICENTA\script_python\\teste\PDF_test_Gmail_Fail_"
            filename2 = ".pdf"
            print(filename2)
            filename = filename + date + filename2
            im_final.save((filename))
            pdf1 = filename
            im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
            window.find_element('-Rezultat-')
            rezultat = 'Fail'
            window['-Rezultat-'].update(rezultat)
            rezultat = 'PDF_test_Gmail_Fail'
            window.find_element('-Path-')
            rezultat = 'PDF_test_Gmail_Fail' + date + filename2
            window['-Path-'].update(rezultat)






    # Test Chat - daca se apasa butonul
    if event == "Test Chat":
        # functie de deblocare ecran
        im_final = deblocare_telefon('8', '16', '16', '16', 'Chat')

        im1 = screenshot('GM1900')
        header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

        d = ImageDraw.Draw(header_im)
        d.text((5, 5), "Telefon deblocat cu succes", font=font, fill=(0, 0, 0))


        im_final1 = Image.new('RGB', (589, 1088), (255, 255, 255))
        im_final1.paste(header_im, (0, 0))
        im_final1.paste(im1, (0, 61))

        # Testare conexiune internet
        # Testare conexiune date mobile

        i = testare_conexiune_date_mobile()

        # Testare conexiune wi-fi
        j = testare_conexiune_wifi()

        # Daca se detecteaza conexiune la internet se continua testul
        # Daca nu exista conexiune testul este declarat picat
        if i == 1 or j == 1:
            # update GUI ->validare conexiune internet
            rezultat = 'Pass'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Conexiune internet validata", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            # deschidere aplicatie whatsapp
            subprocess.call('adb shell am start -n com.whatsapp/com.whatsapp.Main', shell=True)
            time.sleep(2)

            im3 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Aplicatie Whatsapp deschisa", font=font, fill=(0, 0, 0))

            im_final3 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final3.paste(header_im, (0, 0))
            im_final3.paste(im3, (0, 61))

            time.sleep(2)

            xc1 = math.trunc(rezolutie_x * 0.83)

            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.06)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

            time.sleep(2)
            subprocess.call("adb shell input keyevent 41 29 46 37 42 29 ", shell=True)
            time.sleep(2)

            im4 = screenshot('GM1900')

            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Cautare contact: ", font=font, fill=(0, 0, 0))

            im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final4.paste(header_im, (0, 0))
            im_final4.paste(im4, (0, 61))

            time.sleep(2)

            xc1 = math.trunc(rezolutie_x * 0.58)

            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.13)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

            xc1 = math.trunc(rezolutie_x * 0.45)

            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.96)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

            time.sleep(2)
            subprocess.call("adb shell input keyevent 48 33 47 48 62 31 36 29 48  ", shell=True)
            time.sleep(2)

            im5 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Compunere mesaj:", font=font, fill=(0, 0, 0))

            im_final5 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final5.paste(header_im, (0, 0))
            im_final5.paste(im5, (0, 61))

            xc1 = math.trunc(rezolutie_x * 0.91)

            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.6)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)
            time.sleep(4)

            # time.sleep(2)
            # im_chat=screenshot("GM1900")
            #
            # im_chat.save("D:/LICENTA/script_python/imagini/chat.jpg")
            # im = mpimg.imread("D:/LICENTA/script_python/imagini/chat.jpg")
            # imgplot = plt.imshow(im_chat)
            # plt.show()
            # im_chat_test = im_chat.crop((315, 410, 333, 426))
            # im_chat_test.save("D:/LICENTA/script_python/imagini/verificare_chat.jpg")
            # im_chat_test.show()

            im6 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Mesaj trimis:", font=font, fill=(0, 0, 0))

            im_final6 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final6.paste(header_im, (0, 0))
            im_final6.paste(im6, (0, 61))

            im_curent = screenshot_test_chat('GM1900')

            im_test = Image.open("D:/LICENTA/script_python/imagini/verificare_chat.jpg")
            # im_test.show()
            # im_curent.show()
            im_curent1 = np.asarray(im_curent)
            im_test = np.asarray(im_test)

            im_curent1 = rgb2gray(im_curent1)
            im_test = rgb2gray(im_test)

            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                print('aaa')
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_chat.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_chat.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            print("bbb")

            diff = im_curent1 - im_test
            print(diff)
            diff = sum(abs(diff))
            diff = sum(abs(diff))
            print(diff)

            if diff < 1200:
                print("Test chat - PASS")

                # im_final5 = Image.new('RGB', (589, 1088), (255, 255, 255))
                # d = ImageDraw.Draw(header_im)
                # d.text((5, 5), "Test Pass:", font=font, fill=(0, 0, 0))
                # im_final5.paste(header_im, (0, 0))
                # im_final5.paste(im5, (0, 61))

                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5,im_final6]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Chat_Pass_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Pass'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Chat_Pass'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Chat_Pass' + date + filename2
                window['-Path-'].update(rezultat)



            else:
                print("Test Chat - FAIL")


                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5,im_final6]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Chat_Fail_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Fail'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Chat_Fail'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Chat_Fail' + date + filename2
                window['-Path-'].update(rezultat)

            time.sleep(5)

            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
            xc1 = math.trunc(rezolutie_x * 0.44)
            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.9)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

        else:

            # update GUI ->validare conexiune internet
            rezultat = 'Fail'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Nu exista conexiune la internet", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)


            print("Test Chat - FAIL")

            im_list = [im_final1, im_final2]
            now = datetime.now()
            date = now.strftime("%Y%m%d%H%M%S")
            print(date)
            filename = "D:\LICENTA\script_python\\teste\PDF_test_Chat_Fail_"
            filename2 = ".pdf"
            print(filename2)
            filename = filename + date + filename2
            im_final.save((filename))
            pdf1 = filename
            im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
            window.find_element('-Rezultat-')
            rezultat = 'Fail'
            window['-Rezultat-'].update(rezultat)
            rezultat = 'PDF_test_Chat_Fail'
            window.find_element('-Path-')
            rezultat = 'PDF_test_Chat_Fail' + date + filename2
            window['-Path-'].update(rezultat)



    # Test eMAG - daca se apasa butonul
    if event == "Test eMAG":
        # functie de deblocare ecran
        im_final = deblocare_telefon('8', '16', '16', '16', 'eMAG')

        im1 = screenshot('GM1900')
        header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

        d = ImageDraw.Draw(header_im)
        d.text((5, 5), "Telefon deblocat cu succes", font=font, fill=(0, 0, 0))

        im_final1 = Image.new('RGB', (589, 1088), (255, 255, 255))
        im_final1.paste(header_im, (0, 0))
        im_final1.paste(im1, (0, 61))

        # Testare conexiune internet
        # Testare conexiune date mobile

        i = testare_conexiune_date_mobile()

        # Testare conexiune wi-fi
        j = testare_conexiune_wifi()

        # Daca se detecteaza conexiune la internet se continua testul
        # Daca nu exista conexiune testul este declarat picat
        if i == 1 or j == 1:
            # update GUI ->validare conexiune internet
            rezultat = 'Pass'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Conexiune internet validata", font=font, fill=(0, 0, 0))
            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            # click google chrome
            subprocess.call(
               'adb shell am start -n com.android.chrome/org.chromium.chrome.browser.ChromeTabbedActivity -d "about:newtab" --activity-clear-task',
               shell=True)

            time.sleep(6)

            # click URL-bar
            xc1 = math.trunc(rezolutie_x * 0.29)

            #print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.08)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)

            time.sleep(2)

            # introducere site www.emag.ro
            subprocess.call("adb shell input keyevent 51 51 51 56 33 41 29 35 56 46 43", shell=True)

            time.sleep(2)

            # screenshot
            im3 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "URL-bar deschis", font=font, fill=(0, 0, 0))
            im_final3 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final3.paste(header_im, (0, 0))
            im_final3.paste(im3, (0, 61))


            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)

            time.sleep(9)

            #click pe bara de cautare
            xc1 = math.trunc(rezolutie_x * 0.42)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.19)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)

            time.sleep(2)

            #introducere nume produs dorit
            subprocess.call("adb shell input keyevent 40 29 44 48 43 44", shell=True)
            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)
            time.sleep(4)

            # screenshot
            im4 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Rezultate cautare produse", font=font, fill=(0, 0, 0))
            im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final4.paste(header_im, (0, 0))
            im_final4.paste(im4, (0, 61))

            time.sleep(2)
            #selectare primul produs gasit
            xc1 = math.trunc(rezolutie_x * 0.25)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.53)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(2)

            # screenshot
            im5 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Selectare produs", font=font, fill=(0, 0, 0))
            im_final5 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final5.paste(header_im, (0, 0))
            im_final5.paste(im5, (0, 61))

            time.sleep(4)

            # adaugare in cos
            xc1 = math.trunc(rezolutie_x * 0.5)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.97)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            print(string)
            subprocess.call(string, shell=True)
            time.sleep(6)

            # screenshot
            im6 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Produs adaugat in cos", font=font, fill=(0, 0, 0))
            im_final6 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final6.paste(header_im, (0, 0))
            im_final6.paste(im6, (0, 61))


            #im_emag=screenshot("GM1900")

            # im_emag.save("D:/LICENTA/script_python/imagini/emag.jpg")
            # im = mpimg.imread("D:/LICENTA/script_python/imagini/emag.jpg")
            # imgplot = plt.imshow(im_emag)
            # plt.show()
            # im_emag_test = im_emag.crop((15, 95, 233, 140))
            # im_emag_test.save("D:/LICENTA/script_python/imagini/verificare_emag.jpg")
            # im_emag_test.show()

            im_curent = screenshot_test_emag('GM1900')
            im_test = Image.open("D:/LICENTA/script_python/imagini/verificare_emag.jpg")
            # im_test.show()
            #im_curent.show()
            im_curent1 = np.asarray(im_curent)
            im_test = np.asarray(im_test)

            im_curent1 = rgb2gray(im_curent1)
            im_test = rgb2gray(im_test)

            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                print('aaa')
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_youtube.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_youtube.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            print("bbb")

            diff = im_curent1 - im_test
            print(diff)
            diff = sum(abs(diff))
            diff = sum(abs(diff))
            print(diff)

            if diff < 19000:
                print("Test eMAG - PASS")


                # vizualizare cos
                xc1 = math.trunc(rezolutie_x * 0.49)
                xc1 = str(xc1)
                yc1 = math.trunc(rezolutie_y * 0.23)
                yc1 = str(yc1)
                string = "adb shell input tap " + xc1 + " " + yc1
                print(string)
                subprocess.call(string, shell=True)
                time.sleep(4)

                # screenshot
                im7 = screenshot('GM1900')
                header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
                d = ImageDraw.Draw(header_im)
                d.text((5, 5), "Vizualizare cos produse", font=font, fill=(0, 0, 0))
                im_final7 = Image.new('RGB', (589, 1088), (255, 255, 255))
                im_final7.paste(header_im, (0, 0))
                im_final7.paste(im7, (0, 61))

                # stergere element din cos
                xc1 = math.trunc(rezolutie_x * 0.93)
                xc1 = str(xc1)
                yc1 = math.trunc(rezolutie_y * 0.63)
                yc1 = str(yc1)
                string = "adb shell input tap " + xc1 + " " + yc1
                print(string)
                subprocess.call(string, shell=True)
                time.sleep(2)

                # screenshot
                im8 = screenshot('GM1900')
                header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
                d = ImageDraw.Draw(header_im)
                d.text((5, 5), " Golire cos produse ", font=font, fill=(0, 0, 0))
                im_final8 = Image.new('RGB', (589, 1088), (255, 255, 255))
                im_final8.paste(header_im, (0, 0))
                im_final8.paste(im8, (0, 61))

                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5,im_final6,im_final7,im_final8]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_eMAG_Pass_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Pass'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_eMAG_Pass'
                window.find_element('-Path-')
                rezultat = 'PDF_test_eMAG_Pass' + date + filename2
                window['-Path-'].update(rezultat)



            else:
                print("Test eMAG - FAIL")

                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5,im_final6]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_eMAG_Fail_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Fail'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_eMAG_Fail'
                window.find_element('-Path-')
                rezultat = 'PDF_test_eMAG_Fail' + date + filename2
                window['-Path-'].update(rezultat)

            time.sleep(5)

            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
            xc1 = math.trunc(rezolutie_x * 0.44)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.9)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

        else:
            # update GUI ->validare conexiune internet
            rezultat = 'Fail'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Nu exista conexiune la internet", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            print("Test eMAG - FAIL")

            im_list = [im_final1, im_final2]
            now = datetime.now()
            date = now.strftime("%Y%m%d%H%M%S")
            print(date)
            filename = "D:\LICENTA\script_python\\teste\PDF_test_eMAG_Fail_"
            filename2 = ".pdf"
            print(filename2)
            filename = filename + date + filename2
            im_final.save((filename))
            pdf1 = filename
            im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
            window.find_element('-Rezultat-')
            rezultat = 'Fail'
            window['-Rezultat-'].update(rezultat)
            rezultat = 'PDF_test_eMAG_Fail'
            window.find_element('-Path-')
            rezultat = 'PDF_test_eMAG_Fail' + date + filename2
            window['-Path-'].update(rezultat)

    # Test Maps - daca se apasa butonul
    if event == "Test Maps":
        # functie de deblocare ecran
        im_final = deblocare_telefon('8', '16', '16', '16', 'Maps')

        im1 = screenshot('GM1900')
        header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

        d = ImageDraw.Draw(header_im)
        d.text((5, 5), "Telefon deblocat cu succes", font=font, fill=(0, 0, 0))

        im_final1 = Image.new('RGB', (589, 1088), (255, 255, 255))
        im_final1.paste(header_im, (0, 0))
        im_final1.paste(im1, (0, 61))

        # Testare conexiune internet
        # Testare conexiune date mobile

        i = testare_conexiune_date_mobile()

        # Testare conexiune wi-fi
        j = testare_conexiune_wifi()

        # Daca se detecteaza conexiune la internet se continua testul
        # Daca nu exista conexiune testul este declarat picat
        if i == 1 or j == 1:
            # update GUI ->validare conexiune internet
            rezultat = 'Pass'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Conexiune internet validata", font=font, fill=(0, 0, 0))

            # if header_im:
            #     header_im.show()

            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            # deschidere aplicatie Maps
            subprocess.call('adb shell am start -n com.google.android.apps.maps/com.google.android.maps.MapsActivity',shell=True)
            time.sleep(2)

            #click search bar
            xc1 = math.trunc(rezolutie_x * 0.34)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.08)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)
            time.sleep(2)

            # introducere destinatie
            subprocess.call("adb shell input keyevent 44 40 29 54 54 29 62 46 43 41 29 42 37 29", shell=True)

            im3 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Introducere destinatie", font=font, fill=(0, 0, 0))
            im_final3 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final3.paste(header_im, (0, 0))
            im_final3.paste(im3, (0, 61))
            time.sleep(2)

            # apasare Enter
            subprocess.call("adb shell input keyevent 66", shell=True)
            time.sleep(2)

            # selectare destinatie
            xc1 = math.trunc(rezolutie_x * 0.74)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.6)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

            # screenshot
            im4 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Selectare destinatie", font=font, fill=(0, 0, 0))
            im_final4 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final4.paste(header_im, (0, 0))
            im_final4.paste(im4, (0, 61))
            time.sleep(2)

            # click "Directions"
            xc1 = math.trunc(rezolutie_x * 0.21)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.21)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)
            time.sleep(2)

            # selectare trasee ce presupun mijloc de transport în comun
            xc1 = math.trunc(rezolutie_x * 0.38)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.18)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)
            time.sleep(2)

            im5 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Trasee identificate:", font=font, fill=(0, 0, 0))
            im_final5 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final5.paste(header_im, (0, 0))
            im_final5.paste(im5, (0, 61))

            # selectare primul traseu gasit
            xc1 = math.trunc(rezolutie_x * 0.52)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.42)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)
            time.sleep(2)

            im6 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))
            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Traseu selectat:", font=font, fill=(0, 0, 0))
            im_final6 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final6.paste(header_im, (0, 0))
            im_final6.paste(im6, (0, 61))

            # im_maps=screenshot("GM1900")
            #
            # im_maps.save("D:/LICENTA/script_python/imagini/maps.jpg")
            # im = mpimg.imread("D:/LICENTA/script_python/imagini/maps.jpg")
            # imgplot = plt.imshow(im_maps)
            # plt.show()
            # im_maps_test = im_maps.crop((4, 710, 99, 758))
            # im_maps_test.save("D:/LICENTA/script_python/imagini/verificare_maps.jpg")
            # im_maps_test.show()

            im_curent = screenshot_test_maps('GM1900')
            im_test = Image.open("D:/LICENTA/script_python/imagini/verificare_maps.jpg")
            # im_test.show()
            #im_curent.show()
            im_curent1 = np.asarray(im_curent)
            im_test = np.asarray(im_test)

            im_curent1 = rgb2gray(im_curent1)
            im_test = rgb2gray(im_test)

            if len(im_test) != len(im_curent1) and len(im_test[0]) != len(im_curent1[0]):
                print('aaa')
                im_curent.save(r"D:\LICENTA\script_python\imagini\test_gmail.jpg")
                im_test = Image.open(r"D:\LICENTA\script_python\imagini\test_gmail.jpg")
                im_test = np.asarray(im_test)
                im_test = rgb2gray(im_test)

            print("bbb")

            diff = im_curent1 - im_test
            print(diff)
            diff = sum(abs(diff))
            diff = sum(abs(diff))
            print(diff)

            if diff < 15000:
                print("Test Maps - PASS")

                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5, im_final6]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Maps_Pass_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Pass'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Maps_Pass'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Maps_Pass' + date + filename2
                window['-Path-'].update(rezultat)



            else:
                print("Test Maps - FAIL")

                im_list = [im_final1, im_final2, im_final3, im_final4, im_final5, im_final6]
                now = datetime.now()
                date = now.strftime("%Y%m%d%H%M%S")
                print(date)
                filename = "D:\LICENTA\script_python\\teste\PDF_test_Maps_Fail_"
                filename2 = ".pdf"
                print(filename2)
                filename = filename + date + filename2
                im_final.save((filename))
                pdf1 = filename
                im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
                window.find_element('-Rezultat-')
                rezultat = 'Fail'
                window['-Rezultat-'].update(rezultat)
                rezultat = 'PDF_test_Maps_Fail'
                window.find_element('-Path-')
                rezultat = 'PDF_test_Maps_Fail' + date + filename2
                window['-Path-'].update(rezultat)

            time.sleep(5)

            subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
            xc1 = math.trunc(rezolutie_x * 0.44)
            print(xc1)
            xc1 = str(xc1)
            yc1 = math.trunc(rezolutie_y * 0.9)
            yc1 = str(yc1)
            string = "adb shell input tap " + xc1 + " " + yc1
            subprocess.call(string, shell=True)

        else:

            # update GUI ->validare conexiune internet
            rezultat = 'Fail'
            window['-Internet-'].update(rezultat)
            window.refresh()

            im2 = screenshot('GM1900')
            header_im = Image.new('RGB', (589, 60), color=(255, 255, 255))

            d = ImageDraw.Draw(header_im)
            d.text((5, 5), "Nu exista conexiune la internet", font=font, fill=(0, 0, 0))
            im_final2 = Image.new('RGB', (589, 1088), (255, 255, 255))
            im_final2.paste(header_im, (0, 0))
            im_final2.paste(im2, (0, 61))
            time.sleep(2)

            print("Test Chat - FAIL")

            im_list = [im_final1, im_final2]
            now = datetime.now()
            date = now.strftime("%Y%m%d%H%M%S")
            print(date)
            filename = "D:\LICENTA\script_python\\teste\PDF_test_Maps_Fail_"
            filename2 = ".pdf"
            print(filename2)
            filename = filename + date + filename2
            im_final.save((filename))
            pdf1 = filename
            im_final.save(pdf1, "PDF", resolution=100.0, save_all=True, append_images=im_list)
            window.find_element('-Rezultat-')
            rezultat = 'Fail'
            window['-Rezultat-'].update(rezultat)
            rezultat = 'PDF_test_Maps_Fail'
            window.find_element('-Path-')
            rezultat = 'PDF_test_Maps_Fail' + date + filename2
            window['-Path-'].update(rezultat)



    # GUI -> daca se apasa butonul "Raportul ultimului test rulat"
    if event == "Raportul ultimului test rulat":
        list_of_files = glob.glob("D:\LICENTA\script_python\\teste\*")
        latest_file = max(list_of_files,key=os.path.getctime)
        #print(latest_file)
        os.startfile(latest_file)

    # GUI -> daca se apasa butonul "Directorul cu rapoarte"
    if event == "Directorul cu rapoarte":
        FILEBROWSER_PATH= os.path.join(os.getenv('WINDIR'),'explorer.exe')
        subprocess.run([FILEBROWSER_PATH,"D:\LICENTA\script_python\\teste"])





























    #GUI -> daca se apasa windows "X" sa inchida aplicatia
    if event == 'Exit' or event == sg.WIN_CLOSED:
        window.close()
        break

    list_of_files = glob.glob('D:\LICENTA\script_python\\teste\*')
    # print(list_of_files)
    total_youtube_stats = sum('Youtube' in s for s in list_of_files)
    total_chat_stats = sum('Chat' in s for s in list_of_files)
    total_gmail_stats = sum('Gmail' in s for s in list_of_files)
    total_emag_stats = sum('eMAG' in s for s in list_of_files)
    total_maps_stats = sum('Maps' in s for s in list_of_files)

    pass_youtube_stats = sum('Youtube_Pass' in s for s in list_of_files)
    pass_chat_stats = sum('Chat_Pass' in s for s in list_of_files)
    pass_gmail_stats = sum('Gmail_Pass' in s for s in list_of_files)
    pass_emag_stats = sum('eMAG_Pass' in s for s in list_of_files)
    pass_maps_stats = sum('Maps_Pass' in s for s in list_of_files)

    procent_youtube_stats = pass_youtube_stats / total_youtube_stats
    procent_youtube_stats = str(procent_youtube_stats * 100)[0:4] + '%'
    # print(procent_youtube_stats)

    procent_chat_stats = pass_chat_stats / total_chat_stats
    procent_chat_stats = str(procent_chat_stats * 100)[0:4] + '%'

    procent_gmail_stats = pass_gmail_stats / total_gmail_stats
    procent_gmail_stats = str(procent_gmail_stats * 100)[0:4] + '%'

    procent_emag_stats = pass_emag_stats / total_emag_stats
    procent_emag_stats = str(procent_emag_stats * 100)[0:4] + '%'

    procent_maps_stats = pass_maps_stats / total_maps_stats
    procent_maps_stats = str(procent_maps_stats * 100)[0:4] + '%'

    window['-Youtube%-'].update(procent_youtube_stats)

    window['-Gmail%-'].update(procent_gmail_stats)

    window['-Chat%-'].update(procent_chat_stats)

    window['-eMAG%-'].update(procent_emag_stats)

    window['-Maps%-'].update(procent_maps_stats)

    list_of_files_youtube = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Youtube_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_youtube, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-YoutubeD-'].update(latest_file)

    list_of_files_chat = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Chat_*')
    # print(list_of_files_chat)
    latest_file = max(list_of_files_chat, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-ChatD-'].update(latest_file)

    list_of_files_gmail = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Gmail_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_gmail, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-GmailD-'].update(latest_file)

    list_of_files_emag = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_eMAG_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_emag, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-eMAGD-'].update(latest_file)

    list_of_files_maps = glob.glob('D:\LICENTA\script_python\\teste\PDF_test_Maps_*')
    # print(list_of_files_youtube)
    latest_file = max(list_of_files_maps, key=os.path.getctime)
    latest_file = latest_file[-18:-14] + "-" + latest_file[-14:-12] + "-" + latest_file[-12:-10] + " " + latest_file[
                                                                                                         -10:-8] + ":" + latest_file[
                                                                                                                         -8:-6] + ":" + latest_file[
                                                                                                                                        -6:-4]
    # print(latest_file)
    window['-MapsD-'].update(latest_file)

    window.refresh()

