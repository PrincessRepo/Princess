######################################################################################################################################################
##
## USER VARIABLES
##
######################################################################################################################################################

import os, xbmc, xbmcaddon

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B][COLOR blue]Actualizador Auto Cleaner[/COLOR][/B]'
HOME           = xbmc.translatePath('special://home/')
PLUGIN         = os.path.join(HOME,     'addons',    ADDON_ID)

