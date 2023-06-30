from __future__ import print_function, division, absolute_import
from . import cascade
from .precipitation import *
from .temperature import *
from .radiation import *
from .humidity import *
from .wind import *
from .data_io import *
from .util.util import distribute_equally
from .station import Station
from .stationstatistics import StationStatistics

columns_daily = [
    'tmean',
    'tmin',
    'tmax',
    'precip',
    'glob',
    'ssd',
    'hum',
    'wind',
]

columns_hourly = [
    'temp',
    'precip',
    'glob',
    'hum',
    'wind',
]


class Options:  # (deprecated)
    TEMP_SINE_CURVE = 'sine'
    TEMP_LINEAR = 'linear'
    EQUAL_DISTRIBUTION = 'equal'
    PREC_CASCADE = 'cascade'
    PREC_MASTER_STATION = 'masterstation'
    HUMIDITY_MINIMAL = 'minimal'
    HUMIDITY_DEWPOINT_REGRESSION = 'dewpoint_regression'
    HUMIDITY_MIN_MAX = 'min_max'
    HUMIDITY_LINEAR_DEWPOINT_VARIATION = 'linear_dewpoint_variation'
    WIND_FITTED_COSINE = 'cosine'
    WIND_RANDOM_EXPONENTIAL = 'random'
    POT_RAD = 'pot_rad'
    POT_RAD_VIA_SSD = 'pot_rad_via_ssd'
    POT_RAD_VIA_BC = 'pot_rad_via_bc'
