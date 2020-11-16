"""
  Przyklad porownujacy subprocess.Popen z subprocess.run
"""

import subprocess


def run_and_wait():
  completed_process = subprocess.run(["ping", "127.0.0.1"])
  print(completed_process)
  print("DONE!")


def run_and_no_wait():
  task = subprocess.Popen(["ping", "127.0.0.1"])
  print("DONE! almost...")
  print(task.pid)
  # task.terminate()
  return_code = task.wait(5) # 3
  print(return_code)


# run_and_wait()
run_and_no_wait()