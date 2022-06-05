from abc import ABCMeta, abstractmethod


class WorkerA(metaclass=ABCMeta):
    """
    Abstraction for first worker
    """
    @abstractmethod
    def do_stuff_a(self):
        pass


class WorkerB(metaclass=ABCMeta):
    """
        Abstraction for second worker
    """
    @abstractmethod
    def do_stuff_b(self):
        pass


class AbstractSchool(metaclass=ABCMeta):
    """
    Abstract factory for out products
    """
    @abstractmethod
    def create_worker_a(self) -> WorkerA:
        pass

    def create_worker_b(self) -> WorkerB:
        pass


class GoodWorkerA(WorkerA):
    def do_stuff_a(self):
        print('I do staff A good')


class GoodWorkerB(WorkerB):
    def do_stuff_b(self):
        print('I do staff B good')


class GoodSchool(AbstractSchool):
    def create_worker_a(self) -> GoodWorkerA:
        return GoodWorkerA()

    def create_worker_b(self) -> GoodWorkerB:
        return GoodWorkerB()


class BadWorkerA(WorkerA):
    def do_stuff_a(self):
        print('I do staff A bad')


class BadWorkerB(WorkerB):
    def do_stuff_b(self):
        print('I do staff B bad')


class BadSchool(AbstractSchool):
    def create_worker_a(self) -> BadWorkerA:
        return BadWorkerA()

    def create_worker_b(self) -> BadWorkerB:
        return BadWorkerB()


if __name__ == '__main__':
    def do_all_work(worker_a: WorkerA, worker_b: WorkerB):
        worker_a.do_stuff_a()
        worker_b.do_stuff_b()

    def get_workers(school: AbstractSchool) -> (WorkerA, WorkerB):
        return school.create_worker_a(), school.create_worker_b()

    def main_work(workers_type: str):
        if workers_type == 'good':
            school = GoodSchool()
        elif workers_type == 'bad':
            school = BadSchool()
        else:
            raise ValueError(f'We don\'t have school to teach {workers_type} workers')

        do_all_work(*get_workers(school))

    main_work('bad')


