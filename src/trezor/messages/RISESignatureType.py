# Automatically generated by pb2py
# fmt: off
import protobuf as p


class RISESignatureType(p.MessageType):

    def __init__(
        self,
        public_key: bytes = None,
    ) -> None:
        self.public_key = public_key

    @classmethod
    def get_fields(cls):
        return {
            1: ('public_key', p.BytesType, 0),
        }
