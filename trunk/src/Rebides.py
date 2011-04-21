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
        self.pane_statistics = wx.Panel(self, -1)
        self.sizer_5_staticbox = wx.StaticBox(self.pane_statistics, -1, "Group by")
        self.sizer_6_staticbox = wx.StaticBox(self.pane_statistics, -1, "Count")
        self.sizer_7_staticbox = wx.StaticBox(self.pane_statistics, -1, "Options")
        self.sizer_4_staticbox = wx.StaticBox(self.pane_statistics, -1, "Years")
        
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
        self.Http = wx.Menu()
        self.StartServer = wx.MenuItem(self.Http, wx.NewId(), "Start Server", "", wx.ITEM_NORMAL)
        self.Http.AppendItem(self.StartServer)
        self.StopServer = wx.MenuItem(self.Http, wx.NewId(), "Stop Server", "", wx.ITEM_NORMAL)
        self.Http.AppendItem(self.StopServer)
        self.Rebides_menubar.Append(self.Http, "Http")
        self.SetMenuBar(self.Rebides_menubar)
        # Menu Bar end
        self.Rebides_statusbar = self.CreateStatusBar(1, 0)
        self.chk_year_0 = wx.CheckBox(self.pane_statistics, -1, "2000")
        self.chk_year_1 = wx.CheckBox(self.pane_statistics, -1, "2001")
        self.chk_year_2 = wx.CheckBox(self.pane_statistics, -1, "2002")
        self.chk_year_3 = wx.CheckBox(self.pane_statistics, -1, "2003")
        self.chk_year_4 = wx.CheckBox(self.pane_statistics, -1, "2004")
        self.chk_year_5 = wx.CheckBox(self.pane_statistics, -1, "2005")
        self.chk_year_6 = wx.CheckBox(self.pane_statistics, -1, "2006")
        self.chk_year_7 = wx.CheckBox(self.pane_statistics, -1, "2007")
        self.chk_year_8 = wx.CheckBox(self.pane_statistics, -1, "2008")
        self.chk_year_9 = wx.CheckBox(self.pane_statistics, -1, "2009")
        self.chk_gb_year = wx.CheckBox(self.pane_statistics, -1, "Year")
        self.chk_gb_establishment_type = wx.CheckBox(self.pane_statistics, -1, "Establishment Type")
        self.chk_gb_establishment = wx.CheckBox(self.pane_statistics, -1, "Establishment")
        self.chk_gb_grade = wx.CheckBox(self.pane_statistics, -1, "Degree")
        self.chk_gb_course = wx.CheckBox(self.pane_statistics, -1, "Course")
        self.chk_gb_teacher = wx.CheckBox(self.pane_statistics, -1, "Teacher")
        self.chk_gb_category = wx.CheckBox(self.pane_statistics, -1, "Category")
        self.chk_gb_system = wx.CheckBox(self.pane_statistics, -1, "System")
        self.radio_box_1 = wx.RadioBox(self.pane_statistics, -1, "", choices=["Teacher", "Establishment", "Category", "System", "Establishment Type", "Degree", "Course"], majorDimension=0, style=wx.RA_SPECIFY_ROWS)
        self.btn_statistics = wx.Button(self.pane_statistics, -1, "Generate Statistics")
        self.btn_list = wx.Button(self.pane_statistics, -1, "Generate List")

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
        self.Bind(wx.EVT_MENU, self.evt_start_server, self.StartServer)
        self.Bind(wx.EVT_MENU, self.evt_stop_server, self.StopServer)
        self.Bind(wx.EVT_BUTTON, self.evt_generate_statistics, self.btn_statistics)
        self.Bind(wx.EVT_BUTTON, self.evt_generate_lists, self.btn_list)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("Rebides")
        self.Rebides_statusbar.SetStatusWidths([825])
        # statusbar fields
        Rebides_statusbar_fields = ["Ready"]
        for i in range(len(Rebides_statusbar_fields)):
            self.Rebides_statusbar.SetStatusText(Rebides_statusbar_fields[i], i)
        self.radio_box_1.SetToolTipString("Select which counter to be shown")
        self.radio_box_1.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.StaticBoxSizer(self.sizer_7_staticbox, wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.StaticBoxSizer(self.sizer_6_staticbox, wx.VERTICAL)
        sizer_5 = wx.StaticBoxSizer(self.sizer_5_staticbox, wx.VERTICAL)
        sizer_4 = wx.StaticBoxSizer(self.sizer_4_staticbox, wx.VERTICAL)
        sizer_4.Add(self.chk_year_0, 0, 0, 0)
        sizer_4.Add(self.chk_year_1, 0, 0, 0)
        sizer_4.Add(self.chk_year_2, 0, 0, 0)
        sizer_4.Add(self.chk_year_3, 0, 0, 0)
        sizer_4.Add(self.chk_year_4, 0, 0, 0)
        sizer_4.Add(self.chk_year_5, 0, 0, 0)
        sizer_4.Add(self.chk_year_6, 0, 0, 0)
        sizer_4.Add(self.chk_year_7, 0, 0, 0)
        sizer_4.Add(self.chk_year_8, 0, 0, 0)
        sizer_4.Add(self.chk_year_9, 0, 0, 0)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_5.Add(self.chk_gb_year, 0, 0, 0)
        sizer_5.Add(self.chk_gb_establishment_type, 0, 0, 0)
        sizer_5.Add(self.chk_gb_establishment, 0, 0, 0)
        sizer_5.Add(self.chk_gb_grade, 0, 0, 0)
        sizer_5.Add(self.chk_gb_course, 0, 0, 0)
        sizer_5.Add(self.chk_gb_teacher, 0, 0, 0)
        sizer_5.Add(self.chk_gb_category, 0, 0, 0)
        sizer_5.Add(self.chk_gb_system, 0, 0, 0)
        sizer_3.Add(sizer_5, 1, wx.EXPAND, 0)
        sizer_6.Add(self.radio_box_1, 0, 0, 0)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_8.Add(self.btn_statistics, 0, wx.EXPAND, 0)
        sizer_8.Add(self.btn_list, 0, wx.EXPAND, 0)
        sizer_7.Add(sizer_8, 1, wx.EXPAND, 0)
        sizer_3.Add(sizer_7, 1, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        self.pane_statistics.SetSizer(sizer_2)
        sizer_1.Add(self.pane_statistics, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def evt_exit(self, event): # wxGlade: MyFrame.<event_handler>
        self.close_window()
        event.Skip()

    def evt_tnotithespy(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.make_teachers_graph('tnotithespy')
        event.Skip()

    def evt_tnotpiapy(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.make_teachers_graph('tnotpiapy')
        event.Skip()

    def evt_tnotpeapy(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.make_teachers_graph('tnotpeapy')
        event.Skip()

    def evt_tnotpdapy(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.make_teachers_graph('tnotpdapy')
        event.Skip()

    def evt_tnotpdpeapy(self, event): # wxGlade: MyFrame.<event_handler>
        self.main.make_teachers_graph('tnotpdpeapy')
        event.Skip()

    def evt_loipy(self, event): # wxGlade: MyFrame.<event_handler>
        x = MyGraphs(self)
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
        self.set_status_bar_ready(False)
        self.main.collect_data(0)
        self.set_status_bar_ready(True)
        event.Skip()
        
    def evt_collect_2001(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(1)
        self.set_status_bar_ready(True)
        event.Skip()
        
    def evt_collect_2002(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(2)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2003(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(3)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2004(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(4)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2005(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(5)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2006(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(6)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2007(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(7)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2008(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(8)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_2009(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.collect_data(9)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_collect_all(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        for i in range(10):
            self.main.collect_data(i)
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_start_server(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        
        # perguntar se querem gerar as páginas HTML
        dial = wx.MessageDialog(None,\
            'Do you wish to generate HTML pages?', 'HTML',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        ret = dial.ShowModal()
        if ret == wx.ID_YES:
            self.main.http_start_server(True)
        else:
            self.main.http_start_server(False)
        pass
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_stop_server(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        self.main.http_stop_server()
        self.set_status_bar_ready(True)
        event.Skip()

    def evt_generate_statistics(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        
        count_values = {
            0         : 'teacher',
            1         : 'establishment',
            2         : 'category',
            3         : 'system',
            4         : 'establishment_type',
            5         : 'grade',
            6         : 'course'}
        
        # recolhe os valores dos objectos
        years, groupby = self.get_object_values()
        count = count_values.get(self.radio_box_1.GetSelection())
        
        # check years
        years_ok = self.check_true_value(years)
        
        if years_ok == False:
            dial = wx.MessageDialog(None, 'You need to choose at least one year option!', 'Years',
                wx.OK | wx.ICON_EXCLAMATION)
            ret = dial.ShowModal()
            self.set_status_bar_ready(True)
            return
            
        # check groupby
        groupby_ok = self.check_true_value(groupby)
        
        if groupby_ok == False:
            dial = wx.MessageDialog(None, 'You need to choose at least one group by option!', 'Group By',
                wx.OK | wx.ICON_EXCLAMATION)
            ret = dial.ShowModal()
            self.set_status_bar_ready(True)
            return

        
        # get statistics based on criteria
        self.main.get_statistics(years, groupby, count)
        
        # set status bar text
        self.set_status_bar_ready(True)
        event.Skip()
    pass
    
    def check_true_value(self, data):
        # inicia o valor de has_true a falso
        has_true = False
        
        # procura valores de true
        for i in data:
            if i[1] == True:
                has_true = True
            pass
        pass
        
        # retorna a informação se contém algum a true
        return has_true
    pass
    
    def get_object_values(self):
        # years data
        years = []
        years.append([0, self.chk_year_0.GetValue()])
        years.append([1, self.chk_year_1.GetValue()])
        years.append([2, self.chk_year_2.GetValue()])
        years.append([3, self.chk_year_3.GetValue()])
        years.append([4, self.chk_year_4.GetValue()])
        years.append([5, self.chk_year_5.GetValue()])
        years.append([6, self.chk_year_6.GetValue()])
        years.append([7, self.chk_year_7.GetValue()])
        years.append([8, self.chk_year_8.GetValue()])
        years.append([9, self.chk_year_9.GetValue()])
        
        # group by data
        groupby = []
        groupby.append(['category', self.chk_gb_category.GetValue()])
        groupby.append(['course', self.chk_gb_course.GetValue()])
        groupby.append(['establishment', self.chk_gb_establishment.GetValue()])
        groupby.append(['establishment_type', self.chk_gb_establishment_type.GetValue()])
        groupby.append(['grade', self.chk_gb_grade.GetValue()])
        groupby.append(['system', self.chk_gb_system.GetValue()])
        groupby.append(['teacher', self.chk_gb_teacher.GetValue()])
        groupby.append(['year', self.chk_gb_year.GetValue()])
        
        # retorna os valores
        return years, groupby
    pass
        
    # set status bar text
    def set_status_bar_ready(self, ready):
        if ready == True:
            self.Rebides_statusbar.SetStatusText("Ready", 0)
            pass
        else:
            self.Rebides_statusbar.SetStatusText("Working...", 0)
            pass
        pass
    pass

    def evt_generate_lists(self, event): # wxGlade: MyFrame.<event_handler>
        self.set_status_bar_ready(False)
        
        count_values = {
            0         : 'teacher',
            1         : 'establishment',
            2         : 'category',
            3         : 'system',
            4         : 'establishment_type',
            5         : 'grade',
            6         : 'course'}
        
        # recolhe os valores dos objectos
        years, groupby = self.get_object_values()
        
        # check years
        years_ok = self.check_true_value(years)
        
        if years_ok == False:
            dial = wx.MessageDialog(None, 'You need to choose at least one year option!', 'Years',
                wx.OK | wx.ICON_EXCLAMATION)
            ret = dial.ShowModal()
            self.set_status_bar_ready(True)
            return
            
        # check groupby
        groupby_ok = self.check_true_value(groupby)
        
        if groupby_ok == False:
            dial = wx.MessageDialog(None, 'You need to choose at least one group by option!', 'Group By',
                wx.OK | wx.ICON_EXCLAMATION)
            ret = dial.ShowModal()
            self.set_status_bar_ready(True)
            return

        
        # get statistics based on criteria
        self.main.get_lists(groupby, years)
        
        # set status bar text
        self.set_status_bar_ready(True)
        event.Skip()
    pass

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
