import json

from app import app

def test_predict():
    test_client = app.test_client()

    payload = json.dumps({  
        "CHAS":{  
            "0":0
        },
        "RM":{  
            "0":6.575
        },
        "TAX":{  
            "0":296.0
        },
        "PTRATIO":{  
            "0":15.3
        },
        "B":{  
            "0":396.9
        },
        "LSTAT":{  
            "0":4.98
        }
    })

    response = test_client.post("/predict", headers = { "Content-Type": "application/json" }, data = payload)
    assert response.status_code == 200