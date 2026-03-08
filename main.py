from flask import Flask, json,request,jsonify, send_file
from ingest import process_document
from brain import get_vectorstore,search_and_answer
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/nexus', methods=['POST'])
def nexus():
    try:
        data = request.form 
        session_id = data.get('session_id', 'user_1')

        if 'file' in request.files:
            uploaded_file = request.files['file']
            if uploaded_file.filename != '':
                file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
                uploaded_file.save(file_path)
                chunks = process_document(file_path) 
                vector_store = get_vectorstore()
                vector_store.add_documents(chunks)

        query = data.get('query')
        if query:
            answer = search_and_answer(query, session_id=session_id)
            return jsonify({"response": answer, "session_id": session_id})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status_code": 500, "status": f"Internal Server Error: {str(e)}"})
    
if __name__ == '__main__':    
    app.run(host="0.0.0.0",port=3400,debug=True)