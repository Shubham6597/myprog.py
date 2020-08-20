import pyttsx3
import os

pyttsx3.speak("Welcome to my windows tools")

print("Write exit or quit, whenever the job is done", end='\n')

while True:

    print("Tell me what should I run for you : ", end='')
    q = input()

    p = q.lower()

    # print(p)

    if ("not" in p) or ("don't" in p) or ("do not" in p):
        print("Plz not include words like not, don't and do not")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p) or ("google" in p)):
        os.system("chrome")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("firefox" in p) or ("mozilla" in p)):
        os.system("firefox")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
        os.system("notepad")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("play" in p)) and ("player" in p) and ("media" in p):
        os.system("wmplayer")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("show" in p)) and ("accessibility options" in p):
        os.system("utilman")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("add hardware wizard" in p):
        os.system("hdwwiz")

    elif (("uninstall" in p) or ("remove" in p) or ("change" in p) or ("repair" in p) or ("feature" in p)) and ("program" in p):
        os.system("appwiz.cpl")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("show" in p)) and ("administrative tools" in p):
        os.system("control admintools")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("user" in p) and ("account" in p):
        os.system("netplwiz")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("authorization " in p) and (("manage" in p) or ("manmager" in p)):
        os.system("azman.msc")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("automatic" in p) and ("update" in p):
        os.system("control wuaucpl.cpl")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p) or ("setup" in p)) and (("backup" in p) or ("back up" in p) or ("restore" in p)):
        os.system("sdclt")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("calculator" in p) or ("calculate" in p) or ("calculation" in p)):
        os.system("calc")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("character" in p) or ("map" in p):
        os.system("charmap")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ((("check" in p) and ("disk" in p)) or ("chkdsk" in p)):
        os.system("chkdsk")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ((("color" in p) and ("manage" in p)) or ("color management" in p)):
        os.system("colorcpl.exe")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("command prompt" in p) or ("cmd" in p)):
        os.system("cmd")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("control panel" in p):
        os.system("control")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p) or ("set" in p)) and (("date and time properties" in p) or ("date" in p) or ("time" in p)):
        os.system("timedate.cpl")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("device manager" in p):
        os.system("hdwwiz")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("disk cleanup utility" in p) or (("disk" in p) and ("cleanup" in p))):
        os.system("cleanmgr")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("disk defragmenter" in p):
        os.system("dfrgui")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("disk" in p) and ("partition" in p) or ("diskpart" in p)):
        os.system("diskpart")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("documents" in p) or ("document" in p)):
        os.system("explorer Documents")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("driver" in p) and ("verifier" in p)):
        os.system("verifier")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("play" in p)) and ("player" in p):
        os.system("dvdplay")

    elif (("change" in p) or ("launch" in p) or ("open" in p) or ("close" in p)) and ("firewall" in p):
        os.system("firewall.cpl")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("folders properties" in p):
        os.system("control folders")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("change" in p)) and ("keyboard" in p) and ("properties" in p):
        os.system("control keyboard")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("paint" in p):
        os.system("mspaint")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("mouse properties" in p):
        os.system("control mouse")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("excel" in p):
        os.system("Excel")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("powerpoint" in p) or ("power point" in p)):
        os.system("powerpnt")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("ms word" in p) or ("msword" in p) or ("microsoft word" in p)):
        os.system("winword")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("on screen" in p) and ("keyboard" in p):
        os.system("osk")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("print" in p) and ("management" in p):
        os.system("PrintManagement")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("remote desktop" in p):
        os.system("mstsc")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("resource monitor" in p):
        os.system("resmon")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("shared folder wizard" in p) or ("share folder wizard" in p)):
        os.system("shrpubw")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("go to" in p)) and ("shared folders" in p):
        os.system("fsmgmt.msc")

    elif (("run" in p) or ("launch" in p) or ("do" in p) or ("execute" in p)) and (("shut down" in p) or ("turn off" in p)):
        os.system("shutdown")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("sound recorder" in p) or (("record" in p) and ("sound" in p))):
        os.system("soundrecorder")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("sound" in p) and ("volume" in p):
        os.system("sndvol")

    elif (("show" in p) or ("launch" in p) or ("open" in p) or ("display" in p)) and ("system information" in p):
        os.system("msinfo32")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("show" in p)) and (("task manager" in p) or ("taskmgr" in p)):
        os.system("taskmgr")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("explorer" in p):
        os.system("explorer.exe")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("windows update" in p):
        os.system("wuapp")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("check" in p)) and ("windows" in p) and ("version" in p):
        os.system("winver")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("wordpad" in p) or ("word pad" in p)):
        os.system("write")

    elif (("edit" in p) or ("see" in p) or ("open" in p) or ("check" in p)) and (("environment variables" in p) or ("environmental variables" in p) or ("environment variable" in p) or ("environmental variable" in p)):
        os.system("SystemPropertiesAdvanced")

    elif (("run" in p) or ("launch" in p) or ("open" in p)) and (("downloads" in p) or ("download" in p)):
        os.system("explorer Downloads")

    elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("virtualbox" in p) or ("virtual box" in p)):
        os.system("VirtualBox")

    elif ("options" in p):
        print("""Accessibility Options
Add Hardware Wizard
Administrative tools
Advanced User Accounts Control Panel
Authorization Manager
Automatic Update
Backup and Restore Utility
Calculator
Character Mao
Check Disk Utility
Chrome
Color Management
Command Prompt
Control Panel
Date and Time Properties
Device Manager
Disk Cleanup Utility
Disk Defragmenter
Disk Partition Manager
Documents (open 'My Documents' folder)
Downloads (open 'Downloads' folder)
Driver Verifier Utility
DVD Player
Edit Environment Variables
firefox
Firewall Control Panel
Folders Properties
Keyboard Properties
Microsoft Paint
Mouse Properties
notepad
On Screen Keyboard
Print Management
Program and Features
Remote Desktop
Resource Monitor
Shared Folder Wizard
Shared Folders
Shut Down Windows
Sound Recorder
Sound Volume
System Information
Task Manager
VirtualBox
Windows Explorer
windows media player
Windows Update
Windows Version
WordPad""")

    elif ("exit" in p) or ("quit" in p):
        break

    else:
        pyttsx3.speak("Wrong input")
        print('dont support(type "options" to check what you can open)')
