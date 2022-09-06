from deta import Deta, Base
import models

deta = Deta('a0mjrz1q_kKFkJbj9CucTeUN98FPhkYRaSQS4FmfH')
db_users = deta.Base('Users')
db_tasks = deta.Base('Tasks')


if __name__ == '__main__':
    print('Base de datos creada')
