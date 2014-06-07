# -*- encoding: utf-8 -*-#appModules/avpui.py#A part of NonVisual Desktop Access (NVDA)#Copyright (C) 2006-2012 NVDA Contributors#This file is covered by the GNU General Public License.#See the file COPYING for more details.import appModuleHandlerimport apiimport controlTypes
from NVDAObjects.UIA import UIAclass avplistitem(UIA):	def _get_name(self):		l = list()		for x in self.children:			l.append(x.name)		return '; '.join(l)class  avpunlabeledbutton(UIA):
	def _get_name(self):
		if self.firstChild: return self.firstChild.name
	def _get_description(self):
		if self.firstChild:			if self.firstChild.next: return self.firstChild.next.name
class avpdataitem(UIA):	def _get_name(self):		l = list()		for x in range(self.childCount):			l2 = list()			s = ''			if  self.parent.firstChild.children[x].name != u'':				s =  self.parent.firstChild.children[x].name			else:				s =  self.parent.firstChild.children[x].lastChild.previous.name			s += ': '			for y in self.children[x].children:				if y.name:					l2.append(y.name)			s += ', '.join(l2)			l.append(s)		return '; '.encode('utf-8').join(l)class AppModule(appModuleHandler.AppModule):	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_BUTTON and obj.name == '':
			clslist.insert(0,avpunlabeledbutton)
		elif obj.role == controlTypes.ROLE_DATAITEM:			clslist.insert(0, avpdataitem)		elif obj.role == controlTypes.ROLE_LISTITEM:			clslist.insert(0, avplistitem)