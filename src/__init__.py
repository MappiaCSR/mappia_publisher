# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MappiaPublisher
                                 A QGIS plugin
 Publish your maps easily
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-12-09
        copyright            : (C) 2019 by Danilo/CSR UFMG
        email                : danilo@csr.ufmg.br
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'Danilo/CSR UFMG'
__date__ = '2019-12-09'
__copyright__ = '(C) 2019 by Danilo/CSR UFMG'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MappiaPublisher class from file MappiaPublisher.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from src.mappia_publisher import MappiaPublisherPlugin
    return MappiaPublisherPlugin()
