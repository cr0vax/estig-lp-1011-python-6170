#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Mar 23 22:03:50 2011

import wx
from Main import Main

# begin wxGlade: extracode
# end wxGlade



class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # iniciar ligação ao código aplicacional
        self.main = Main()
        
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.Rebides_menubar = wx.MenuBar()
        self.File = wx.Menu()
        self.Exit = wx.MenuItem(self.File, wx.NewId(), "Exit", "", wx.ITEM_NORMAL)
        self.File.AppendItem(self.Exit)
        self.Rebides_menubar.Append(self.File, "File")
        self.Data = wx.Menu()
        CollectByYear = wx.Menu()
        self.Collect2000 = wx.MenuItem(CollectByYear, wx.NewId(), "2000", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2000)
        self.Collect2001 = wx.MenuItem(CollectByYear, wx.NewId(), "2001", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2001)
        self.Collect2002 = wx.MenuItem(CollectByYear, wx.NewId(), "2002", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2002)
        self.Collect2003 = wx.MenuItem(CollectByYear, wx.NewId(), "2003", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2003)
        self.Collect2004 = wx.MenuItem(CollectByYear, wx.NewId(), "2004", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2004)
        self.Collect2005 = wx.MenuItem(CollectByYear, wx.NewId(), "2005", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2005)
        self.Collect2006 = wx.MenuItem(CollectByYear, wx.NewId(), "2006", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2006)
        self.Collect2007 = wx.MenuItem(CollectByYear, wx.NewId(), "2007", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2007)
        self.Collect2008 = wx.MenuItem(CollectByYear, wx.NewId(), "2008", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2008)
        self.Collect2009 = wx.MenuItem(CollectByYear, wx.NewId(), "2009", "", wx.ITEM_NORMAL)
        CollectByYear.AppendItem(self.Collect2009)
        self.Data.AppendMenu(wx.NewId(), "Collect By Year", CollectByYear, "")
        self.CollectAll = wx.MenuItem(self.Data, wx.NewId(), "Collect All", "", wx.ITEM_NORMAL)
        self.Data.AppendItem(self.CollectAll)
        self.Rebides_menubar.Append(self.Data, "Data")
        self.Statistics = wx.Menu()
        Counters = wx.Menu()
        self.tnotithespy = wx.MenuItem(Counters, wx.NewId(), "Total number of teachers in the higher education system per year", "Total number of teachers in the higher education system per year", wx.ITEM_NORMAL)
        Counters.AppendItem(self.tnotithespy)
        self.tnotpiapy = wx.MenuItem(Counters, wx.NewId(), "Total number of teachers per institution and per year", "", wx.ITEM_NORMAL)
        Counters.AppendItem(self.tnotpiapy)
        self.tnotpeapy = wx.MenuItem(Counters, wx.NewId(), "Total number of teachers per establishment and per year", "", wx.ITEM_NORMAL)
        Counters.AppendItem(self.tnotpeapy)
        self.tnotpdapy = wx.MenuItem(Counters, wx.NewId(), "Total number of teachers per degree and per year", "", wx.ITEM_NORMAL)
        Counters.AppendItem(self.tnotpdapy)
        self.tnotpdpeapy = wx.MenuItem(Counters, wx.NewId(), "Total number of teachers per degree, per establishment and per year", "", wx.ITEM_NORMAL)
        Counters.AppendItem(self.tnotpdpeapy)
        self.Statistics.AppendMenu(wx.NewId(), "Counters", Counters, "")
        Lists = wx.Menu()
        self.loipy = wx.MenuItem(Lists, wx.NewId(), "List of institutions per year", "", wx.ITEM_NORMAL)
        Lists.AppendItem(self.loipy)
        self.loiepy = wx.MenuItem(Lists, wx.NewId(), "List of institutions/establishments per year", "", wx.ITEM_NORMAL)
        Lists.AppendItem(self.loiepy)
        self.lohoadpy = wx.MenuItem(Lists, wx.NewId(), "List of holders of a degree per year", "", wx.ITEM_NORMAL)
        Lists.AppendItem(self.lohoadpy)
        self.Statistics.AppendMenu(wx.NewId(), "Lists", Lists, "")
        self.Rebides_menubar.Append(self.Statistics, "Statistics")
        self.Http = wx.Menu()
        self.StartServer = wx.MenuItem(self.Http, wx.NewId(), "Start Server", "", wx.ITEM_NORMAL)
        self.Http.AppendItem(self.StartServer)
        self.StopServer = wx.MenuItem(self.Http, wx.NewId(), "Stop Server", "", wx.ITEM_NORMAL)
        self.Http.AppendItem(self.StopServer)
        self.Rebides_menubar.Append(self.Http, "Http")
        self.SetMenuBar(self.Rebides_menubar)
        # Menu Bar end

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_MENU, self.evt_exit, self.Exit)
        self.Bind(wx.EVT_MENU, self.evt_collect_2000, self.Collect2000)
        self.Bind(wx.EVT_MENU, self.evt_collect_2001, self.Collect2001)
        self.Bind(wx.EVT_MENU, self.evt_collect_2002, self.Collect2002)
        self.Bind(wx.EVT_MENU, self.evt_collect_2003, self.Collect2003)
        self.Bind(wx.EVT_MENU, self.evt_collect_2004, self.Collect2004)
        self.Bind(wx.EVT_MENU, self.evt_collect_2005, self.Collect2005)
        self.Bind(wx.EVT_MENU, self.evt_collect_2006, self.Collect2006)
        self.Bind(wx.EVT_MENU, self.evt_collect_2007, self.Collect2007)
        self.Bind(wx.EVT_MENU, self.evt_collect_2008, self.Collect2008)
        self.Bind(wx.EVT_MENU, self.evt_collect_2009, self.Collect2009)
        self.Bind(wx.EVT_MENU, self.evt_collect_all, self.CollectAll)
        self.Bind(wx.EVT_MENU, self.evt_tnotithespy, self.tnotithespy)
        self.Bind(wx.EVT_MENU, self.evt_tnotpiapy, self.tnotpiapy)
        self.Bind(wx.EVT_MENU, self.evt_tnotpeapy, self.tnotpeapy)
        self.Bind(wx.EVT_MENU, self.evt_tnotpdapy, self.tnotpdapy)
        self.Bind(wx.EVT_MENU, self.evt_tnotpdpeapy, self.tnotpdpeapy)
        self.Bind(wx.EVT_MENU, self.evt_loipy, self.loipy)
        self.Bind(wx.EVT_MENU, self.evt_loiepy, self.loiepy)
        self.Bind(wx.EVT_MENU, self.evt_lohoadpy, self.lohoadpy)
        self.Bind(wx.EVT_MENU, self.evt_start_server, self.StartServer)
        self.Bind(wx.EVT_MENU, self.evt_stop_server, self.StopServer)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Rebides")
        self.SetSize((687, 405))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def evt_exit(self, event): # wxGlade: MyFrame.<event_handler>
        self.close_window()
        event.Skip()

    def evt_tnotithespy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_tnotithespy' not implemented!"
        event.Skip()

    def evt_tnotpiapy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_tnotpiapy' not implemented!"
        event.Skip()

    def evt_tnotpeapy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_tnotpeapy' not implemented!"
        event.Skip()

    def evt_tnotpdapy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_tnotpdapy' not implemented!"
        event.Skip()

    def evt_tnotpdpeapy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_tnotpdpeapy' not implemented!"
        event.Skip()

    def evt_loipy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_loipy' not implemented!"
        event.Skip()

    def evt_loiepy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_loiepy' not implemented!"
        event.Skip()

    def evt_lohoadpy(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_lohoadpy' not implemented!"
        event.Skip()

    def evt_collect_data(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_collect_data' not implemented"
        event.Skip()

    def evt_collect_2000(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(0)
        event.Skip()
        
    def evt_collect_2001(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(1)
        event.Skip()
        
    def evt_collect_2002(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(2)
        event.Skip()

    def evt_collect_2003(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(3)
        event.Skip()

    def evt_collect_2004(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(4)
        event.Skip()

    def evt_collect_2005(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(5)
        event.Skip()

    def evt_collect_2006(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(6)
        event.Skip()

    def evt_collect_2007(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(7)
        event.Skip()

    def evt_collect_2008(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(8)
        event.Skip()

    def evt_collect_2009(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.collect_data(9)
        event.Skip()

    def evt_collect_all(self, event): # wxGlade: MyFrame.<event_handler>
        for i in range(10):
            self.main.collect_data(i)
            
        event.Skip()

    def evt_start_server(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_start_server' not implemented"
        event.Skip()

    def evt_stop_server(self, event): # wxGlade: MyFrame.<event_handler>
        print "Event handler `evt_stop_server' not implemented"
        event.Skip()

# end of class MyFrame
    def close_window(self):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Quit',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.Destroy()
        pass
    pass


class Rebides(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        Rebides = MyFrame(None, -1, "")
        self.SetTopWindow(Rebides)
        Rebides.Show()
        return 1

# end of class Rebides

if __name__ == "__main__":
    Rebides = Rebides(0)
    Rebides.MainLoop()
