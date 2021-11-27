# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import scipy.io as sio

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Mat File Viewer", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )

        # Grid
        self.m_grid1.CreateGrid( 5, 5 )
        self.m_grid1.EnableEditing( True )
        self.m_grid1.EnableGridLines( True )
        self.m_grid1.EnableDragGridSize( False )
        self.m_grid1.SetMargins( 0, 0 )

        # Columns
        self.m_grid1.EnableDragColMove( False )
        self.m_grid1.EnableDragColSize( True )
        self.m_grid1.SetColLabelSize( 30 )
        self.m_grid1.SetColLabelValue( 0, u"1" )
        self.m_grid1.SetColLabelValue( 1, u"2" )
        self.m_grid1.SetColLabelValue( 2, u"3" )
        self.m_grid1.SetColLabelValue( 3, u"4" )
        self.m_grid1.SetColLabelValue( 4, u"5" )
        self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.m_grid1.EnableDragRowSize( True )
        self.m_grid1.SetRowLabelSize( 80 )
        self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        bSizer1.Add( self.m_grid1, 1, wx.ALL|wx.EXPAND, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"Load Mat", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Variable:", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        m_choice1Choices = []
        self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
        self.m_choice1.SetSelection( 0 )
        bSizer2.Add( self.m_choice1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button2.Bind( wx.EVT_BUTTON, self.load_mat )
        self.m_choice1.Bind(wx.EVT_CHOICE,self.fill_grid)
    def __del__( self ):
        pass


    def get_variable_name(self,mat_dict: dict):
        variable_ls=[]
        for vari in mat_dict.keys():
            if vari.startswith('__'):
                pass
            else:
                variable_ls.append(vari)
        return variable_ls
    
    def fill_grid(self,event=None):
        sel_num=self.m_choice1.GetCurrentSelection()
        sel_variname=self.m_choice1.GetString(sel_num)
        data_arr=self.mat_dict[sel_variname]
        # delete current grid
        curcol_num=self.m_grid1.GetNumberCols()
        self.m_grid1.DeleteCols(pos=0,numCols=curcol_num)
        currow_num=self.m_grid1.GetNumberRows()
        self.m_grid1.DeleteRows(pos=0,numRows=currow_num)
        # new a grid
        row1_num,col1_num=data_arr.shape[0],data_arr.shape[1]
        self.m_grid1.AppendCols(col1_num)
        self.m_grid1.AppendRows(row1_num)
        # set values in grid
        for i in range(row1_num):
            for j in range(col1_num):
                self.m_grid1.SetCellValue(i,j,s="{}".format(data_arr[i,j]))
                
        # set columns labels
        for j in range(col1_num):
                self.m_grid1.SetColLabelValue(j,"{}".format(j+1))
        

    # Virtual event handlers, overide them in your derived class
    def load_mat( self, event ):
        with wx.FileDialog(self, "Open .mat file", wildcard="mat files (*.mat)|*.mat",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return 
            pathname = fileDialog.GetPath()
            self.mat_dict=sio.loadmat(pathname)
            vari_ls=self.get_variable_name(self.mat_dict)
            if len(vari_ls)>0:
                self.m_choice1.SetItems(vari_ls)
                self.m_choice1.SetSelection(0)
                self.fill_grid()
            
            
            # set frame title
            self.SetTitle('Mat File Viewer-{}'.format(pathname))
        event.Skip()


if __name__ == '__main__':
    app = wx.App()
    main_win = MyFrame1(None)
    main_win.Show()
    app.MainLoop()