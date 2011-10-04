import wx
import contest3

##########################################################################################

short_app_name = "LongPal"
long_app_name = "Longest Palindrome"

##########################################################################################
class _MainWindow(wx.Frame):
    """
    Main Window
    """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(500, 300))

        self.CreateStatusBar()

        self.Layout()
        self.Show(True)
        
        print contest3.contest3("aa")
        print contest3.contest3("ada")
        print contest3.contest3("Short string, no pals")
        print contest3.contest3("!amanaplanacanalpanama")
        print contest3.contest3("amanaplanacanalpanama")
        print contest3.contest3("momadam nogon")
        print contest3.contest3('issiaiifinginfkoldlfdldfsjdfayimoraissmarttramssiaromiyaf')
        print contest3.contest3('issiaiifinginfkoldlfdldfsjdfayimoraissmart!tramssiaromiyaf')
    #-------------------------------------------------------------------------------------
##########################################################################################
app = wx.App(False)
frame = _MainWindow(None, long_app_name)
app.MainLoop()
##########################################################################################
