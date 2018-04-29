const shell = require('shelljs')

let server = null

before(() => {
  shell.cd('../../api')
  shell.exec('source ../venv/bin/activate')
  server = shell.exec('python manage.py runserver', { async: true })
})

after(() => {
  server.kill()
})
