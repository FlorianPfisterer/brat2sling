
"""Maps brat frame names to SLING frame types (schema)"""

BRAT_TO_SLING_FRAME = {
    'Divide': '/recipes/divide',
    'Merge': '/recipes/merge'

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
    'Input': '/recipes/action/input',
    'Location': '/recipes/action/location'

    # TODO utensil, condition, ...
}

