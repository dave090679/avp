import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA
class kpmEditBox(UIA):
	def _get_name(self):
		return self.UIAElement.CachedAutomationID

class kpmbutton(UIA):
	def _get_name(self):
		return self.firstChild.name

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.UIAElement.CurrentName == "KasperskyLab.Kpm.UI.Database.ViewModel.DatabaseViewModel":
			clslist.insert(0,kpmbutton)
		elif obj.name == "" and obj.role == controlTypes.ROLE_EDITABLETEXT:
			clslist.insert(0,kpmEditBox)
