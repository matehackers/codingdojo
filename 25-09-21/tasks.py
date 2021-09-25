
def divideTasks(input):
  lines = input.split("\n")
  tasks = lines[0].split(' ')
  done_tasks = lines[1].split(' ')

  n, m = int(tasks[0]), int(tasks[1])

  c_tasks = []
  a_tasks = []
  is_chef = True

  for i in range(1, n+1):
    task_id = str(i)
    if task_id not in done_tasks:
      if is_chef:
        c_tasks.append(task_id)
      else:
        a_tasks.append(task_id)
      is_chef = not is_chef

  if n <= m:
    return "\n\n"
  else:
    return ' '.join(c_tasks) + "\n" + ' '.join(a_tasks) + "\n"
