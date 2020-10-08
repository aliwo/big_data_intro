from datetime import timedelta, datetime


class DateHelper:

    @classmethod
    def first2last_date(cls, dt):
        '''
        dt 로 받은 달의 첫 날과 마지막 날을 date 로 리턴 합니다.
        :return: (date, date)
        '''
        return datetime(dt.year, dt.month, 1), cls.last_day_of_month(dt)

    @classmethod
    def last_day_of_month(self, any_day):
        '''
        user 클래스에서 가져왔습니다. user 클래스의 원래 함수는 삭제하기!
        '''
        next_month = any_day.replace(day=28) + timedelta(days=4)
        return next_month - timedelta(days=next_month.day)
