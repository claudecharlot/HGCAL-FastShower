
# FIXME: find a better way to import
try:
    # Standalone imports
    from geometry_cfg import *
    from shower_cfg import *
    from generation_cfg import *
    from display_cfg import *
except ImportError:
    # CMSSW imports
    from HGCalSimulation.FastShower.geometry_cfg import *
    from HGCalSimulation.FastShower.shower_cfg import *
    from HGCalSimulation.FastShower.generation_cfg import *
    from HGCalSimulation.FastShower.display_cfg import *

events = 1
debug = False
