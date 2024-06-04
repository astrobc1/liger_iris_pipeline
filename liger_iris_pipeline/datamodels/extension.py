import os.path
from asdf.extension import AsdfExtension
from asdf import util

SCHEMA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "schemas"))

# Just a unique label, it is not a real URL
URL_PREFIX = "http://oirlab.ucsd.edu/schemas/"


class BaseExtension(AsdfExtension):
    """
    This asdf extension provides url mapping for the asdf resolver

    This is needed so that the asdf resolver can find the datamodel schemas
    in the jwst package.  This base extension needs to be imported in the
    jwst package __init__ and have an entry_points entry in setup.py
    """

    @property
    def types(self):
        return []

    @property
    def tag_mapping(self):
        return []

    @property
    def url_mapping(self):
        return [(URL_PREFIX, util.filepath_to_url(SCHEMA_PATH) + "/{url_suffix}")]
