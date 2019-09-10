import sling


def load_commons_store():
    commons = sling.Store()
    commons.load('sling_schemas/meta-schema.sling')
    commons.load('sling_schemas/document-schema.sling')
    commons.load('sling_schemas/recipe-schema.sling')
    return commons


if __name__ == '__main__':
    print(load_commons_store())