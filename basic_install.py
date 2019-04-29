import subprocess
import tkinter

top=tkinter.Tk()
def magicweb():
    subprocess.call ([r"your own file location\your own file location\Siemens\MagicWeb\MagicWebClient.bat"])
    print ("magicweb \n\n")
def onbase():
    subprocess.call ([r"your own file location\OnBase 2018\OnBaseInstall.bat"])
    print ("Onbase \n\n")
def dragon():
    subprocess.call ([r"your own file location\Dragon Network\12.51.217.164_DMNE_2.7.5_FullClient_ENU\DNS12_DVD1\Dragon2.7.5InstallACH.bat"])
    print ("Dragon \n\n")
def anyconnect():
    subprocess.call ([r"your own file location\VPN\Any Connect\anyconnect-Windows.exe"])
    print ("Any Connect \n\n")
def nexthink():
    subprocess.call ([r"your own file location\NexThink\NexThink.bat"])
    print ("NexThink \n\n")
def imprivata():
    subprocess.call ([r"your own file location\your own file location\Setup Files\Imprivata_Central\Imprivata_Central.exe"])
    print ("Imprivata Central")
def syngo():
    subprocess.call ([r"your own file location\ClinicalSD\V36E\Install_ClinicalSD.bat"])
    print ("Syngo")

magicweb_b = tkinter.Button(top, text ="Magicweb", command = magicweb)
onbase_b = tkinter.Button(top, text="Onbase", command = onbase)
dragon_b = tkinter.Button(top, text="Dragon", command = dragon)
anyconnect_b = tkinter.Button(top, text="Any Connect",command = anyconnect)
nexthink_b = tkinter.Button(top, text = "NexThink",command = nexthink)
imprivata_b = tkinter.Button(top, text = "Imprivata", command = imprivata)
syngo_b = tkinter.Button(top, text = "Syngo", command = syngo)
magicweb_b.pack()
onbase_b.pack()
dragon_b.pack()
anyconnect_b.pack()
nexthink_b.pack()
imprivata_b.pack()
syngo_b.pack()

top.mainloop()
##Written by Nate, nexthink.bat written by jack


#antiquated non graphical program

#i = 1
#selection = 1
#print ("0: No More Programs \n1: Magicweb \n2: Onbase Install \n3: Dragon \n4: Any connect \n5: NexThink \n6: Imprivata Central \n7: Syngo")
#while (i > 0):
    #selection = int(input ("Which program would you like to install\n"))
    #if selection == 1:
        #subprocess.call ([r"your own file location\your own file location\Siemens\MagicWeb\MagicWebClient.bat"])
        #print ("magicweb \n\n")
    #elif selection == 2:
        #subprocess.call ([r"your own file location\OnBase 2018\OnBaseInstall.bat"])
        #print ("Onbase \n\n")
    #elif selection == 3:
        #subprocess.call ([r"your own file location\Dragon Network\12.51.217.164_DMNE_2.7.5_FullClient_ENU\DNS12_DVD1\Dragon2.7.5InstallACH.bat"])
        #print ("Dragon \n\n")
    #elif selection == 4:
        #subprocess.call ([r"your own file location\VPN\Any Connect\anyconnect-Windows.exe"])
        #print ("Any Connect \n\n")
    #elif selection == 5:
        #subprocess.call ([r"your own file location\NexThink\NexThink.bat"])
        #print ("NexThink \n\n")
    #elif selection == 6: 
        #subprocess.call ([r"your own file location\your own file location\Setup Files\Imprivata_Central\Imprivata_Central.exe"])
        #print ("Imprivata Central")
    #elif selection == 7: 
        #subprocess.call ([r"your own file location\ClinicalSD\V36E\Install_ClinicalSD.bat"])
        #print ("Syngo")
    #elif selection == 0:
     ### reset loop and exit program
        #print ("Done \n\n") 
        #i = 0    



