const spawner = require('child_process').spawn;
const prompt = window.prompt('Enter Prompt')

const python_process = spawner('python',['./main.py',prompt]);

