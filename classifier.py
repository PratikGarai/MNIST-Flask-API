from PIL import Image
import urllib.request
import io
import pickle
import numpy

class Classifier : 
    def __init__(self):
        self.model = pickle.load(open('./model_training/model.sav', 'rb'))
    
    def classify(self, URL):
        with urllib.request.urlopen(URL) as url:
            f = io.BytesIO(url.read())
        img = Image.open(f)
        # img.show()
        img = img.resize((28,28))
        img = img.convert('L')

        arr = numpy.array(img)
        arr = arr.reshape(1, -1)

        result = self.model.predict(arr)[0]
        print("Predicted result : ", result)
        return result

def main() :
    c = Classifier()
    url = "https://raw.githubusercontent.com/PratikGarai/MNIST-Flask-API/master/test_images/01.png"
    c.classify(url)

if __name__=='__main__':
    main()