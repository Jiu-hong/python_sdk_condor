class CalltableSerialization:
    def __init__(self):
        self.fields = []
        self.currentOffset = 0

    def addField(self, index, value):
        if len(self.fields) != index:
            raise Exception("Add fields in correct index order.")
        field = (index, self.currentOffset, value)
        self.fields.append(field)
        self.currentOffset += len(value)
        return self

    def to_bytes(self):
        calltableBytes = b''  # []
        payloadBytes = b''  # []
        # calltableBytes += CLU32(len(self.fields)).serialize()
        calltableBytes += len(self.fields).to_bytes(4, byteorder='little')

        for field in self.fields:

            calltableBytes += field[0].to_bytes(2, byteorder='little')

            calltableBytes += field[1].to_bytes(4, byteorder='little')
            payloadBytes += field[2]

        calltableBytes += self.currentOffset.to_bytes(4, byteorder='little')

        return calltableBytes + payloadBytes
