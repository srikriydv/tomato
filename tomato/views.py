from django.shortcuts import render
from service.models import Login
from django.core.files.storage import FileSystemStorage # file system for temporary
from PIL import Image
import numpy as np
import tensorflow as tf 
import os

lists = os.listdir(os.getcwd())
model=tf.keras.models.load_model(os.getcwd()+str('/Betatomatoes.h5'))
# print(model)
# print(class_names)
def index(request):
    try:
        class_names=['Bacterial Spot','Early Blight','Healthy','Late Blight','Leaf Mold','Septoria Leaf Spot','Spider Mite','Target Spot','Tomato Molaz','Tomato Yellow Leaf']
        if request.method == "POST" and request.FILES['upload']:
            image = request.FILES['upload'] # real file is here
            fss = FileSystemStorage()
            file = fss.save(image.name, image)
            image = np.array(Image.open(image).convert("RGB").resize((256,256))) # output is in matrix form.
            # image=image/255
            img_arry=tf.expand_dims(image,0)
            predictions = model.predict(img_arry)
            print(predictions)
            predicted_class = class_names[np.argmax(predictions[0])]
            confidence = round(100*(np.max(predictions[0])))

            # print(predicted_class)
            file_url = fss.url(file)
            data = {'file_url':file_url,
                    'predict':predicted_class,
                    'confidence' : confidence,
                }
        return render(request, "index.html",data)
    except:
        pass
    return render(request, "index.html")