import json
import logging
import traceback

class UserModel(json.JSONEncoder):
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @classmethod
    def generate_model(cls, item):
        try:
            id = item["id"]["S"]
            firstname = item["firstname"]["S"]
            lastname = item["lastname"]["S"]
            return cls(id, firstname, lastname)
        except KeyError:
            traceback.print_exc()
            logging.error("ITEMS ERROR: Cannot create User models from JSON.")

    def __str__(self):
        return "\n*****Users: *****\n{}".format(self.toJSON())