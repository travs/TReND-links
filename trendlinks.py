#!/usr/bin/env python

import models, app

if __name__ == '__main__':
  try:
    models.initialize()
    models.User.create_user(
        email='trav221@gmail.com',
        password='password',
        admin=True
    )
  except ValueError:
    pass
  app.run(debug=DEBUG, host=HOST, port=PORT)

