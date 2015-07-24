# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class EditorCollectionPlugin(octoprint.plugin.TemplatePlugin):
	def templatehook(self, *args, **kwargs):
		return [
			('EditorCollection', dict(), dict(div=lambda x: "settings_plugin_" + x))
		]

	def get_template_configs(self):
		return [
			dict(type="settings", custom_bindings=False)
		]

	def get_update_information(self):
		return dict(
			editorcollection=dict(
				displayName="Editor Collection Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="Salandora",
				repo="OctoPrint-EditorCollection",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/Salandora/OctoPrint-EditorCollection/archive/{target_version}.zip"
			)
		)


# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Editor Collection"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = EditorCollectionPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.ui.web.templatetypes": __plugin_implementation__.templatehook,
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
