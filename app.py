from flask import Flask, request

app = Flask(__name__)

#Create the idea repository

ideas = {
    1 : {
        "id" : 1, 
        "idea_name" : "Mrinal Devnath",
        "idea_description" : "Details about ONDC",
        "idea_author" : "Mrinal"
    }, 
    2:{
        "id" : 2,
        "idea_name" : "Anjali Prajapati",
        "idea_description" : "Details about saving soil",
        "idea_author" : "Anjali"
    }
}

'''
Create a restful endpoint for fetching all the ideas
'''

@app.get('/ideaapp/api/v1/ideas')
def get_all_ideas():
    #Logic to fetch all the ideas
    return ideas

''' 
Create a restful endpoint for creating a new idea 
'''

@app.post('/ideaapp/api/v1/ideas')
def create_idea():
    #Logic to create new idea
    try:
        #first read the request body

        request_body = request.get_json()

        #check if the idea id passes is not present already
        if request_body["id"] and request_body["id"] in ideas:
            return "ideas with the same id   is already present ", 400
        
        #Insert the passed idea in the ideas dictionary 
        ideas[request_body["id"]] = request_body

        #return the response saying idea got saved 
        return "ideas created and saved successfully.", 201
    
    except KeyError:
        return "id is missing..", 400
    
    except:
        return "Some internal server error", 500
    
'''
End point to fetch idea based on the idea id 
'''
app.get("/ideaapp/api/v1/ideas/<idea_id>")
def get_idea(idea_id):
    try:
        if int(idea_id) in ideas:
            ideas[int(idea_id)] = request.get_json()
            return ideas[int(idea_id)], 200 
        else:
            return "Idea id passed is not present", 400 
    except:
        return "Some internal error happened", 500 
    
'''
End point to Delete an idea
'''
@app.delete('/ideaapp/api/v1/ideas/<ideas_id>')
def del_idea(ideas_id):
    try:
        if int(ideas_id) in ideas:
            ideas.pop(int(ideas_id))
            return "idea got successfully removed. "
        
        else:
            return "Idea id passed is not present", 400 
        
    except:
        return "Some internal error happened", 500 
if __name__ == '__main__':
    app.run(port=3020)