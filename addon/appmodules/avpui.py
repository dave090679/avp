# -*- encoding: utf-8 -*-#appModules/avpui.py#A part of NonVisual Desktop Access (NVDA)#Copyright (C) 2006-2012 NVDA Contributors#This file is covered by the GNU General Public License.#See the file COPYING for more details.import appModuleHandlerimport apiimport controlTypes
from NVDAObjects.UIA import UIAclass avptablecell(UIA):	def _get_name(self):		l = list()		for x in self.children:			childname = x.name			if childname:				l.append(childname) 		return ', '.encode('utf-8').join(l)	def _get_columnHeaderText(self):		colname1 = self.parent.parent.firstChild.children[self.columnNumber -1].name		if  colname1 != u'':			s =  colname1		else:			try:				colname2 =  self.parent.parent.firstChild.children[self.columnNumber -1].lastChild.previous.name			except:				colname2 = ''			s = colname2		return sclass avplistitem(UIA):	def _get_name(self):		l = list()		for x in self.children:			l.append(x.name)		return '; '.join(l)class  avpunlabeledbutton(UIA):
	def _get_name(self):
		l = list()		for x in self.children:			childname = x.name			if childname != '':				l.append(childname)		try:			s = l[0]		except:			s = ''		return s
	def _get_description(self):
		l = list()		for x in self.children:			childname = x.name			if childname != '':				l.append(childname)		try:			s = l[1]		except:			s = ''		return sclass avpdataitem(UIA):	def _get_name(self):		l = list()		for x in self.children:			childname = x.name			childheader = x.columnHeaderText			if childname:				s = ''				if childheader:					s += childheader+': '				s += childname				l.append(s) 		return '; '.encode('utf-8').join(l)class AppModule(appModuleHandler.AppModule):	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_BUTTON:
			clslist.insert(0,avpunlabeledbutton)
		elif obj.role == controlTypes.ROLE_DATAITEM:			clslist.insert(0, avpdataitem)		elif obj.role == controlTypes.ROLE_LISTITEM:			clslist.insert(0, avplistitem)		elif obj.parent.role == controlTypes.ROLE_DATAITEM and obj.UIAElement.CurrentClassName == 'ContentPresenter':			clslist.insert(0,avptablecell)