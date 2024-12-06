from Flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
taskIdControl = 1

@app.route('/tasks', methods=['POST'])
def createTask():
  global taskIdControl
  data = request.get_json()
  newTask = Task(id=taskIdControl, title=data['title'], description=data['description'])
  tasks.append(newTask)
  taskIdControl += 1
  return jsonify({
    'message': 'Nova tarefa criada com sucesso.'
  }), 201

@app.route('/tasks', methods=['GET'])
def listTasks():
  task_list = []
  for task in tasks:
    task_list.append(task.toDictionary())

  return jsonify({
    'tasks': task_list,
    'total_tasks': len(task_list)
  })

@app.route('/tasks/<int:taskId>', methods=['GET'])
def infoTask(taskId):
  for task in tasks:
    if task.id == taskId:
      return jsonify({
        'task': task.toDictionary()
      })
  return jsonify({
    'message': 'Tarefa não encontrada.'
  }), 404

@app.route('/tasks/<int:taskId>', methods=['PUT'])
def updateTask(taskId):
  toBeUpdatedTask = None

  for task in tasks:
    if task.id == taskId:
      toBeUpdatedTask = task
      break

  if toBeUpdatedTask is None:
    return jsonify({
      'message': 'Tarefa não encontrada.'
    }), 404

  data = request.get_json()
  task.title = data['title']
  task.description = data['description']
  task.closed = data['closed']

  return jsonify({
    'message': 'Tarefa atualizada com sucesso.'
  })

@app.route('/tasks/<int:taskId>', methods=['DELETE'])
def deleteTask(taskId):
  toBeDeletedTask = None

  for task in tasks:
    if task.id == taskId:
      toBeDeletedTask = task
      break

  if not toBeDeletedTask:
    return jsonify({
      'message': 'Tarefa não encontrada.'
    }), 404

  tasks.remove(toBeDeletedTask)
  return jsonify({
    'message': 'Tarefa removida com sucesso.'
  })

if __name__ == '__main__':
  app.run(debug=True)
