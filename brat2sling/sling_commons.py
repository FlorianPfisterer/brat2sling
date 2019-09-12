import sling


def load_commons_store():
    commons = sling.Store()
    commons.load('sling_schemas/meta-schema.sling')
    commons.load('sling_schemas/document-schema.sling')
    commons.load('sling_schemas/recipe-schema.sling')
    return commons


def export_commons_store():
    store = load_commons_store()
    store.freeze()
    store.save('./commons.sling', binary=True)


if __name__ == '__main__':
    export_commons_store()
