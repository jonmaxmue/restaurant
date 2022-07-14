
class ModelFieldPermission:

    def allowed_to_edit(self, data, allowed_fields):
        for key, value in data.items():
            if hasattr(self, key):
                if type(value) == dict and "id" in value and "type" in value:
                    status = getattr(getattr(self, key), "id")
                    value = value["id"]
                else:
                    status = getattr(self, key)

                if str(value) != str(status) and key not in allowed_fields:
                    return False
        return True