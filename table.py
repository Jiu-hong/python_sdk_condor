# export class CalltableSerialization {
#     private fields: Field[] = []
#     private currentOffset = 0

from cl_number import CLU16, CLU32


class CalltableSerialization:
    def __init__(self):
        self.fields = []
        self.currentOffset = 0
        #     / **
        #     * Adds a field to the call table.
        #     *
        #     * @ param index - The field index.
        #     * @ param value - The field value as a byte array.
        #     * @ returns The current instance of `CalltableSerialization`.
        #     * @ throws An error if the fields are not added in the correct index order.
        #     * /
        #     addField(index: number, value: Uint8Array): CalltableSerialization {
        #         if (this.fields.length != = index) {
        #             throw new Error('Add fields in correct index order.')
        #         }
        #         const field = new Field(index, this.currentOffset, value)
        #         this.fields.push(field)
        #         this.currentOffset += value.length

        #         return this
        #     }
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
        calltableBytes += CLU32(len(self.fields)).serialize()

        for field in self.fields:
            calltableBytes += CLU16(field[0]).serialize()
            calltableBytes += CLU32(field[1]).serialize()
            payloadBytes += field[2]
        calltableBytes += CLU32(self.currentOffset).serialize()

        return calltableBytes + payloadBytes
