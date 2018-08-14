"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

"""
import sched, time


def job1(text):
    print('job1 ' + text)


def job2(text):
    print('job2 ' + text)


def job_scheduler(function, arg, n_milisec):
    s.enter(n_milisec/1000., 1, function, argument=(arg,))
    s.run()


if __name__ == '__main__':
    s = sched.scheduler(time.time, time.sleep)
    print(time.ctime())
    job_scheduler(job1, 'prueba1', 4000)
    print(time.ctime())
    job_scheduler(job2, 'prueba2', 2000)
    print(time.ctime())
