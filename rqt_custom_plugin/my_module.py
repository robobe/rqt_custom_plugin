import rclpy
from ament_index_python import get_resource

import os
from qt_gui.plugin import Plugin
from python_qt_binding import loadUi
from python_qt_binding.QtWidgets import QWidget
import logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(lineno)s - %(message)s')
log = logging.getLogger(__name__)

class MyPlugin(Plugin):
    def __init__(self, context):
        super(MyPlugin, self).__init__(context)
        self._widget = QWidget()
        self.setObjectName('MyPlugin')
        # Get resource folder for loading ui file
        _, package_path = get_resource('packages', 'rqt_custom_plugin')
        ui_file = os.path.join(package_path, 'share', 'rqt_custom_plugin', 'resource', 'MyPlugin.ui')
        loadUi(ui_file, self._widget)
        
        self._widget.setObjectName('MyPluginUi')
        
        # bind gui button
        self._widget.Test.pressed.connect(self._test_handler)
        
        context.add_widget(self._widget)

    def _test_handler(self):
        log.info("Test button press")
