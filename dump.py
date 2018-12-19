import wx
class Frame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent,-1, "Payment Register", size = (600,400))
        menu = wx.Menu() 
        menu.Append(1001, "&Register") 
        menu.Append(2002, "&Search") 
        menu.Append(3003, "&Exit") 
        menubar = wx.MenuBar() 
        menubar.Append(menu, "&Menu") 
		
        self.SetMenuBar(menubar) 
        self.Bind(wx.EVT_MENU, self.OnNewWindow, id = 1001) 
        self.Bind(wx.EVT_MENU, self.OnNewWindow1, id = 2002) 
        self.Bind(wx.EVT_MENU, self.OnExit, id = 3003) 
        
        self.panel = wx.Panel(self)     
        self.quote = wx.StaticText(self.panel, label="Your quote:")
        self.result = wx.StaticText(self.panel, label="")
        self.result.SetForegroundColour(wx.RED)
        self.button = wx.Button(self.panel, label="Save")
        self.lblname = wx.StaticText(self.panel, label="Your name:")
        self.editname = wx.TextCtrl(self.panel, size=(140, -1))

        # Set sizer for the frame, so we can change frame size to match widgets
        self.windowSizer = wx.BoxSizer()
        self.windowSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND)        

        # Set sizer for the panel content
        self.sizer = wx.GridBagSizer(5, 5)
        self.sizer.Add(self.quote, (0, 0))
        self.sizer.Add(self.result, (0, 1))
        self.sizer.Add(self.lblname, (1, 0))
        self.sizer.Add(self.editname, (1, 1))
        self.sizer.Add(self.button, (2, 0), (1, 2), flag=wx.EXPAND)

        # Set simple sizer for a nice border
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        # Use the sizers
        self.panel.SetSizerAndFit(self.border)  
        self.SetSizerAndFit(self.windowSizer)  

        # Set event handlers
        self.button.Bind(wx.EVT_BUTTON, self.OnButton)

    def OnButton(self, e):
        self.result.SetLabel(self.editname.GetValue())

    def OnExit(self, evt): 
      self.Close(True)  
		
    def OnNewWindow(self, evt): 
      win = wx.MDIChildFrame(self, -1, "Child Window")
      win.Show(True) 

    def OnNewWindow1(self, evt): 
      win = wx.MDIChildFrame(self, -2, "Child Window")
      win.Show(True) 

app = wx.App(False)
frame = Frame(None)
frame.Show()
app.MainLoop()
