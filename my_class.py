class tickets:
    def __init__(self, name_owner, transport, cl, time_ti_buy, price):
        self.name_owner = name_owner
        self.transport = transport
        self.cl = cl
        self.time_ti_buy = time_ti_buy
        self.price = price

    def to_dict(self):
        return {
            "name_owner": self.name_owner,
            "transport": self.transport,
            "cl": self.cl,
            "time_ti_buy": self.time_ti_buy,
            "price": self.price,
        }

    def __str__(self):
        return f"Имя: {self.name_owner}, тип транспорта: {self.transport}, класс: {self.cl}, время покупки: {self.time_ti_buy}, цена: {self.price}"


class one_time(tickets):
    def __init__(self, name_owner, transport, cl, time_ti_buy, price):
        super().__init__(name_owner, transport, cl, time_ti_buy, price)

    def to_dict(self):
        one_time_dict = super().to_dict()
        return one_time_dict

    def __str__(self):
        return super().__str__()


class many_time(tickets):
    def __init__(self, name_owner, transport, cl, time_ti_buy, price, col_use):
        super().__init__(name_owner, transport, cl, time_ti_buy, price)
        self.col_use = col_use

    def to_dict(self):
        many_time_dict = super().to_dict()
        many_time_dict.update({
            "col_use": self.col_use,
        })
        return many_time_dict

    def __str__(self):
        return f"Имя: {self.name_owner}, тип транспорта: {self.transport}, класс: {self.cl}, время покупки: {self.time_ti_buy}, цена: {self.price}, количество использований: {self.col_use}"


class subscription(tickets):
    def __init__(self, name_owner, transport, cl, time_ti_buy, price, col_day):
        super().__init__(name_owner, transport, cl, time_ti_buy, price)
        self.col_day = col_day

    def to_dict(self):
        subscription_dict = super().to_dict()
        subscription_dict.update({
            "col_day": self.col_day,
        })
        return subscription_dict

    def __str__(self):
        return f"Имя: {self.name_owner}, тип транспорта: {self.transport}, класс: {self.cl}, время покупки: {self.time_ti_buy}, цена: {self.price}, количество дней: {self.col_day}"


class preferential(tickets):
    def __init__(self, name_owner, transport, cl, time_ti_buy, price, reason):
        super().__init__(name_owner, transport, cl, time_ti_buy, price)
        self.reason = reason

    def to_dict(self):
        preferential_dict = super().to_dict()
        preferential_dict.update({
            "col_day": self.reason,
        })
        return preferential_dict

    def __str__(self):
        return f"Имя: {self.name_owner}, тип транспорта: {self.transport}, класс: {self.cl}, время покупки: {self.time_ti_buy}, цена: {self.price}, причина: {self.reason}"
