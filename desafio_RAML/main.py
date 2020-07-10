
doc = '''

#%RAML 1.0
title: Desafio RESTful API Modeling Language (RAML)
baseUri: https://api.codenation.com
mediaType: application/json

types:
  Auth:
    type: object
    discriminator: token
    properties:
      token : string
      
  Agent:
    type: object
    discriminator: agent
    properties: 
      agent_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "name"
      status:
        type: boolean
        required: true
        example: true
      environment:
        type: string
        required: true
        example: "Environment"
      version:
        type: string
        required: true
        example: "version"
      address:
          type: string
          required: true
          example: 192.168.0.1
      user_id:
          type: integer
          required: true
          example: 1
    example:
      agent_id: 1
      user_id: 1
      name: "Name"
      status: true
      environment: "Environment"
      version: "version"
      address: 192.168.0.1
    
  Event:
    type: object
    discriminator: event
    properties:
      event_id:
        type: integer
        required: true
        example: 1
      level:
        type: string
        required: true
        example: "Caution"
      payload:
        type: string
        required: true
        example: "Example"
      shelved:
        type: boolean
        required: true
        example: true
      data:
        type: datetime
        required: true
        example:  "2015-12-26T16:12:18Z"
      agent_id:
        type: integer
        required: true
        example: 1
    example:
      event_id: 1
      agent_id: 1
      level: "Caution"
      payload: "Example"
      shelved: "Example"
      data: "2020-05-15"
      
  Group:
    type: object
    discriminator: group
    properties: 
      group_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "Name"
    example:
      group_id: 1
      name: "Name"
  
  User:
    type: object
    discriminator: user
    properties: 
      user_id:
        type: integer
        required: true
        example: 1
      name:
        type: string
        required: true
        example: "Name"
      password:
        type: string
        required: true
        example: "Senha"
      email:
        type: string
        required: true
        example: "texte@teste.com.br"
      date:
        type: date-only
        required: true
        example: "2020-05-15"
      group_id:
        type: integer
        required: true
        example: 1
    example:
      user_id: 1
      name: "Name"
      password: "Senha"
      email:  "texte@teste.com.br"
      date: "2020-05-15 22:59" 
      group_id: 1 
       
  Response:
    discriminator: response
    properties: 
      message:
        type: string
        example: "Message Example"
  
securitySchemes: 
  JWT:
    description: Autenticação JWT
    type: x-{other}
    describedBy: 
      headers: 
        Authorization:
          description: X-AuthToken
          type: string
          required: true
      responses: 
        201:
          body:
            application/json:
              description: Token generated
        401:
          body:
            application/json:
              description: Unauthorized
        400:
          body:
            application/json:
              description: Expired Token
    settings: 
      roles: []
    
/auth/token:
  
  post:
    description: Return token
    body: 
      application/json:
        type: Auth
        username: string
        password: string
    responses: 
        201:
          body:
            application/json:
              description: Token generated
        401:
          body:
            application/json:
              description: Unauthorized
        400:
          body:
            application/json:
              description: Expired Token
    securedBy: [JWT]
    
/agents:
  get:
    description: Return list of agents
    responses: 
        200:
          body:
            type: Response
            example:
              message: List
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
    securedBy: JWT
  
  post:
    description: Creating a new agent
    body:
      application/json:
        example: {            
            "agent_id": 1,
            "user_id": 1,
            "name": "Name",
            "status": true,
            "environment": "Environment",
            "version": "version",
            "address": 192.168.0.1
        }
    responses: 
      201:
        body:
          type: Response
          example:
            message: Created
      401:
        body:
          type: Response
          example:
            message: Unauthorized
    securedBy: [JWT]
    
  /{id}:
    get:
      description: Agent details
      responses: 
        200:
          body:
            type: Response
            example:
              message: Created
        401:
         body:
           type: Response
           example:
             message: Unauthorized
        404:
           body:
             type: Response
             example:
               message: Not Found
      securedBy: [JWT]
    
    put:
      responses: 
        200:
          body:
            type: Response
            example:
              message: Changed
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
      
    delete:
      description: Delete Agent
      responses: 
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
      
  /{id}/events:
    get:
      description: List of events
      responses: 
        200:
          body:
            type: Event[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    post:
      body:
        application/json:
          example: {            
               "event_id": 1,
               "agent_id": 1,
               "name": "Name",
               "level": "caution",
               "payload": "Example",
               "shelve": true
          }
        201:
          body:
            type: Response
            example:
              message: Created
        401:
           body:
           type: Response
           example:
             message: Unauthorized
        404:
          body:
            type: Response
            example:
             message: Not Found
      securedBy: JWT
    
    put:
      description: Update
      body:
        type: Event 
        200:
          body:
            type: Response
            example:
              message: Update
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      responses:
        200:
          body:
            type: Event
        400:
          body:
            type: Response
            example:
              message: Bad request
      securedBy: JWT
    
    delete:
      description: Delete Event
      body:
        application/json:
          properties:
            example: {
            }

        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      responses:
        200:
          body:
            type: Deleted
        400:
          body:
            type: Response
            example:
              message: Bad request
        404:
          body:
            type: Response
            example:
              message: Not Found
    
      securedBy: [JWT]
    
/groups:
  get:
    description: Group list
    responses:
      200:
        body:
          type: Group[]
      401:
        body:
          type: Response
          example:
            message: Not found
    securedBy: [JWT]
  post:
    description: Create Group
    body:
      application/json:
        properties: 
          example: {
              "group_id": 1,
              "name": "group"
            }
        example: {
              "group_id": 1,
              "name": "group"
            }
    responses:
      201:
        body:
          type: Group
      401:
        body:
          type: Response
          example:
            message: Unauthorized
    securedBy: [JWT]

  /{id}:
    get:
      description: Group detail
      responses:
        200:
          body:
            type: Group[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      description: Edit Group
      body:
        type: Group
      responses:
        200:
          body:
            type: Group
        401:
          body:
            type: Response
            example:
              message: Unauthorized
      securedBy: [JWT]
    delete:
      description: Delete Group
      responses:
        204:
          body:
            type: Response
            example:
              message: Deleted
        400:
          body:
            type: Response
            example:
              message: Bad request
      securedBy: [JWT]
/users:
  get:
    description: User list
    responses:
      200:
        body:
          type: User[]
    securedBy: [JWT]
  post:
    description: Create User
    body:
      application/json:
        properties:
          example: {
              "user_id": 1,
              "name": "name",
              "email": "email",
              "last_login": "2019-11-20",
              "group_id": 1
            }
    responses:
      201:
        body:
          type: User
      401:
        body:
          type: Response
          example:
            message: Unauthorized
      404:
        body:
          type: Response
          example:
            message: Not Found
    securedBy: [JWT]

  /{id}:
    get:
      description: User detail
      responses:
        200:
          body:
            type: User[]
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    put:
      description: Edit User
      body:
        type: User
      responses:
        200:
          body:
            type: User
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]
    delete:
      responses:
        200:
          body:
            type: Response
            example:
              message: Deleted
        401:
          body:
            type: Response
            example:
              message: Unauthorized
        404:
          body:
            type: Response
            example:
              message: Not Found
      securedBy: [JWT]





  


'''
