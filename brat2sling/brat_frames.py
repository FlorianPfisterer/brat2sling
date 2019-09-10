
"""Maps brat frame names to SLING frame types (schema)"""

UNKNOWN_FRAME = 'UNKNOWN_FRAME'
ACTION = 'Action'
ENTITY = 'Entity'
FRAME = 'PrimaryFrame'
INPUT = 'Input'
LOCATION = 'Location'

BRAT_TO_SLING_FRAME = {
    'Divide': '/recipes/divide',
    'Merge': '/recipes/merge',
    UNKNOWN_FRAME: '/recipes/action'    # generic action

    # TODO
    """'LocationChange': '/recipes/divide',
    'OrientationChange': '/recipes/divide',
    'MatterStateChange': '/recipes/divide',
    'ShapeChange': '/recipes/divide',
    'TemperatureChange': '/recipes/divide',
    'Generate': '/recipes/divide',
    'SizeChange': '/recipes/divide'"""
}

BRAT_TO_SLING_RELATION = {
    INPUT: '/recipes/action/input',
    LOCATION: '/recipes/action/location'

    # TODO utensil, condition, ...
}

