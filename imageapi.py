from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {"namevalley":
            {
                "blue":
                {
                    "1":
                    {
                        "image_id": 1,
                        "imagelink": "https://i.ibb.co/f4P136b/blueback.jpg"
                    },
                    "2":
                    {
                        "image_id": 2,
                        "imagelink": "https://i.ibb.co/tJDQNxX/6-blue-doll.png"
                    },
                    "3":
                    {
                        "image_id": 3,
                        "imagelink": "https://i.ibb.co/GPrXvyG/5-blue-lemon.png"
                    },
                    "4":
                    {
                        "image_id": 4,
                        "imagelink": "https://i.ibb.co/K24YvqL/4-blue-donot.png"
                    },
                },
                "pink":
                {
                    "1":
                    {
                        "image_id": 1,
                        "imagelink": "https://i.ibb.co/QNCLTqk/7-pink-pineapple.png"
                    },
                    "2":
                    {
                        "image_id": 2,
                        "imagelink": "https://i.ibb.co/Q9Q8ynD/8-pink-doll.png"
                    },
                    "3":
                    {
                        "image_id": 3,
                        "imagelink": "https://i.ibb.co/Yf6yMMg/9-pink-pineapple.png"
                    },
                    "4":
                    {
                        "image_id": 4,
                        "imagelink": "https://i.ibb.co/YpSQ02Q/pinkback.jpg"
                    },
                },
            },
            }
