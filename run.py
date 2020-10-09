from controller.controller import Controller
from model.types import Base
from model.engine import engine
import os


if __name__ == '__main__':
    # 모든 테이블을 만듭니다. 처음에 한 번 실행하고 주석처리 하면 됩니다.
    # Base.metadata.create_all(engine)

    controller = Controller()
    try:
        for year in [2017, 2018, 2019]:
            for month in [i for i in range(1, 13)]:
                controller.save_all_in_month(year, month)
                controller.commit()
                print(f'{year} {month} 저장 완료')
    except:
        os.system('afplay /System/Library/Sounds/Sosumi.aiff')






