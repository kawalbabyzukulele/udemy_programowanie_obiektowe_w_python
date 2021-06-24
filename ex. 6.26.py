import datetime

class CustomDate:
    custom_date_objects = []
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        try:
            datetime.datetime(int(year), int(month), int(day))
        except:
            raise ValueError("To nie przejdzie")
        self.date = "{}-{}-{}".format(self.day, self.month, self.year)
        CustomDate.custom_date_objects.append(self)


    def straight_date(self):
        if len(str(self.day)) == 1:
            self.day = str("0{}".format(self.day))
        if len(str(self.month)) == 1:
            self.month = str("0{}".format(self.month))
        print("{}-{}-{}".format(self.day, self.month, self.year))

    @classmethod
    def from_text(cls, text):
        text = text.split("-")
        try:
            datetime.datetime(int(text[2]), int(text[1]), int(text[0]))
            object = CustomDate(text[0], text[1], text[2])
            object.straight_date()
        except:
            raise ValueError("To nie przejdzie")


    @classmethod
    def dates_from_file(cls, file_name):
        with open(file_name, 'r') as open_file:
            lines = open_file.read().splitlines()

        for line in lines:
            line = line.split("-")
            print(line)
            try:
                datetime.datetime(int(line[2]), int(line[1]), int(line[0]))
                object = CustomDate(line[0], line[1], line[2])
            except:
                raise ValueError("To nie przejdzie")
            finally:
                continue





a = CustomDate(29, 3, 1999)
print(a.date)

CustomDate.custom_date_objects = []
file = "daty.txt"
CustomDate.dates_from_file(file_name=file)

for object in CustomDate.custom_date_objects:
    object.straight_date()

CustomDate.from_text("5-10-2002")
CustomDate.from_text("15-10-2002")
CustomDate.from_text("5-13-2002")
