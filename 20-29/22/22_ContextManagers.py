# Context-Managers: Custom Before & After Functionality.
import contextlib, time, traceback

# CONTEXT-MANAGER
#----------------------------------------------------------------------------------
@contextlib.contextmanager
def time_it():
    start = time.time() # BEFORE
    yield
    end = time.time()   # AFTER
    timer = end - start
    print(f'Timer: {timer:.5f} seconds')


@contextlib.contextmanager
def try_except(debug=False):
    try:
        yield
    except:
        if debug:
            print(traceback.format_exc())

# # Comprehension
# with time_it():
#     result = [i * 2 for i in range(10000000)]
#
# # Loop
# with time_it():
#     result = []
#     for i in range(10000000):
#         result.append(i * 2)

with try_except():
    print(1/0)

with try_except(debug=True):
    print(1/0)

with try_except():
    print(1/0)

with try_except():
    print(1/0)

with try_except():
    print(1/0)

with try_except():
    print(1/0)

with try_except():
    print(1/0)