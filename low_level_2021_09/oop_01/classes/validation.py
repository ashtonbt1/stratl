from abc import ABC, abstractmethod

def control_print_len(text, max_len=70):
    if isinstance(text, str) and isinstance(max_len, int) and max_len > 10:
        return f"{text[:int(max_len/3)]}...{text[-int(max_len/3):]}"
    else:
        return text

REQ_ERROR = ValueError("Value is required")

class Validator(ABC):

    def __set_name__(self, owner, name):
        self.private_name = '_' + name
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)
    
    @abstractmethod
    def validate(self, value):
        pass

class OneOf(Validator):

    def __init__(self, required=False, *options):
        self.required = required
        self.options = set(options)
    
    def validate(self, value):
        if self.required and value is None:
            raise REQ_ERROR
        elif value is None:
            return None
        if value not in self.options:
            raise ValueError(f"Expected {value!r} to be one of {control_print_len(str(self.options))!r}")


class Number(Validator):

    def __init__(self, required=False, minvalue=None, maxvalue=None, types=(int, float)):
        self.required = required
        self.minvalue = minvalue
        self.maxvalue = maxvalue
        self.types = types

    def validate(self, value):
        if self.required and value is None:
            raise REQ_ERROR
        elif value is None:
            return None
        if not isinstance(value, self.types):
            raise TypeError(f"Expected {value!r} to be in {self.types!r}")
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(
                f"Expected {value!r} to be at least {self.minvalue!r}"
            )
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(
                f"Expected {value!r} to be no more than {self.maxvalue!r}"
            )


class String(Validator):

    def __init__(self, required=False, minsize=None, maxsize=None, predicate=None):
        self.required = required
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if self.required and value is None:
            raise REQ_ERROR
        elif value is None:
            return None
        if not isinstance(value, str):
            raise TypeError(f"Expected {value!r} to be a str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(
                f"Expected length of {value!r} to be no smaller than {self.minsize!r}"
            )
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(
                f"Expected length of {value!r} to be no larger than {self.maxsize!r}"
            )
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(
                f"Expected {self.predicate} to be true for {value!r}"
            )


class D20(Number):
    def __init__(self):
        super().__init__(minvalue=1, maxvalue=20, types=(int))
