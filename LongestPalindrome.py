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
        
        contest3.contest3("Short string, no pals")
        contest3.contest3("amanaplanacanalpanama")
        contest3.contest3("momadam noggon")
        contest3.contest3('issiaiifinginfkoldlfdldfsjdfayimoraissmarttramssiaromiyaf')
    #-------------------------------------------------------------------------------------
##########################################################################################
app = wx.App(False)
frame = _MainWindow(None, long_app_name)
app.MainLoop()
##########################################################################################
