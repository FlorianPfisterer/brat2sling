
"""Maps brat frame names to SLING frame types (schema)"""

UNKNOWN_FRAME = 'UNKNOWN_FRAME'
ACTION = 'Action'
ENTITY = 'Entity'
FRAME = 'PrimaryFrame'
INPUT = 'Input'
LOCATION = 'Location'
UTENSIL = 'Utensil'
CONDITION = 'CONDITION'

BRAT_TO_SLING_FRAME = {
    'Divide': '/recipes/divide',
    'Merge': '/recipes/merge',
    UNKNOWN_FRAME: '/recipes/action',    # generic action
    'LocationChange': '/recipes/location-change',
    'OrientationChange': '/recipes/orientation-change',
    'MatterStateChange': '/recipes/matter-state-change',
    'ShapeChange': '/recipes/shape-change',
    'TemperatureChange': '/recipes/temperature-change',
    'Generate': '/recipes/generate',
    'SizeChange': '/recipes/size-change',

    ENTITY: '/recipes/entity'
}

BRAT_TO_SLING_RELATION = {
    INPUT: '/recipes/action/input',
    LOCATION: '/recipes/action/location',
    UTENSIL: '/recipes/action/utensil',
    CONDITION: '/recipes/action/condition'
}

