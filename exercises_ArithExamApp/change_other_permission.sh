#Imagine you have a project file called /tmp/program.py. Your task is to make this file executable for other users without overriding previous permissions. Use the chmod command and symbolic mode to do the task.

solve() {
    chmod o+x /tmp/program.py

}