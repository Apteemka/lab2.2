class UserData:
    def __init__(self, name, age):
        self.user_name=name
        self.Age=age

    def PrintInfo(self):
        print(f"User:{self.user_name}, Age:{self.Age}")


def process_data(dataList):
    Result=[]
    for pos in DataList:
        if pos.Age < 18:
            Result.append(pos.user_name.upper())
    return Result