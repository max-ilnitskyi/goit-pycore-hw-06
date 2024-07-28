from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if value.isdecimal() and len(value) == 10:
            super().__init__(value)
        else:
            raise ValueError("Wrong phone")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            self.phones.append(Phone(phone))
        except Exception as e:
            print(e)

    def remove_phone(self, record_phone):
        self.phones = [phone for phone in self.phones if phone.value != record_phone]

    def edit_phone(self, oldRecordPhone, newRecordPhone):
        try:
            self.phones = [
                Phone(newRecordPhone) if phone.value == oldRecordPhone else phone
                for phone in self.phones
            ]
        except Exception as e:
            print(e)

    def find_phone(self, recordPhone):
        for phone in self.phones:
            if phone.value == recordPhone:
                return phone

        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, record_name):
        try:
            return self.data[record_name]
        except Exception:
            return None

    def delete(self, record_name):
        try:
            del self.data[record_name]
        except Exception:
            pass
