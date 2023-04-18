from flask import Flask, request, jsonify
from ai_training import Trainer
import logging

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    config = request.json
    trainer = Trainer()
    result = trainer.train(config)
    logging.info(f"Received config: {config}")
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
