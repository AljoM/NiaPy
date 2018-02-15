"""Implementation of benchmarks utility function."""

from . import Rastrigin, Rosenbrock, Griewank, \
    Sphere, Ackley, Schwefel, Schwefel221, \
    Schwefel222, Whitley

__all__ = ['Utility']


# pylint: disable=too-many-return-statements
class Utility(object):

    def __init__(self):
        pass

    # pylint: disable=inconsistent-return-statements
    def get_benchmark(self, benchmark, Upper=None, Lower=None):
        if not isinstance(benchmark, ''.__class__):
            return benchmark
        else:
            if benchmark == 'rastrigin':
                if Lower is None and Upper is None:
                    return Rastrigin()
                elif Lower is not None and Upper is not None:
                    return Rastrigin(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'rosenbrock':
                if Lower is None and Upper is None:
                    return Rosenbrock()
                elif Lower is not None and Upper is not None:
                    return Rosenbrock(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'griewank':
                if Lower is None and Upper is None:
                    return Griewank()
                elif Lower is not None and Upper != None:
                    return Griewank(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'sphere':
                if Lower is None and Upper is None:
                    return Sphere()
                elif Lower is not None and Upper is not None:
                    return Sphere(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'ackley':
                if Lower is None and Upper is None:
                    return Ackley()
                elif Lower is not None and Upper is not None:
                    return Ackley(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'schwefel':
                if Lower is None and Upper is None:
                    return Schwefel()
                elif Lower is not None and Upper is not None:
                    return Schwefel(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'schwefel221':
                if Lower is None and Upper is None:
                    return Schwefel221()
                elif Lower is not None and Upper is not None:
                    return Schwefel221(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'schwefel222':
                if Lower is None and Upper is None:
                    return Schwefel222()
                elif Lower is not None and Upper is not None:
                    return Schwefel222(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            elif benchmark == 'whitley':
                if Lower is None and Upper is None:
                    return Whitley()
                elif Lower is not None and Upper is not None:
                    return Whitley(Lower, Upper)
                else:
                    self.__raiseLowerAndUpperNotDefined()
            else:
                raise TypeError('Passed benchmark is not defined!')

    @classmethod
    def __raiseLowerAndUpperNotDefined(cls):
        raise TypeError('Upper and Lower value must be defined!')