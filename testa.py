if self.data.tag == TAG.CLResult.value:
    if isinstance(self, CLResult):
        tuple_value = self.data  # tuple
        ok_value = tuple_value[0].value
        err_value = tuple_value[1].value
        return {json_type: {'ok': get_deep_json(ok_value), 'err': get_deep_json(err_value)}}
