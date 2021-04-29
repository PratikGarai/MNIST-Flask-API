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
        img.show()
        img = img.resize((28,28))
        img = img.convert('L')

        arr = numpy.array(img)
        arr = arr.reshape(1, -1)

        result = self.model.predict(arr)[0]
        print("Predicted result : ", result)
        return result

def main() :
    c = Classifier()
    
    # Result 0
    url = "https://raw.githubusercontent.com/tphinkle/tphinkle.github.io/master/images/2017-8-15/mnist_1.png"
    # Result 4
    url = "https://user-images.githubusercontent.com/379372/31909713-d9046856-b7ef-11e7-98fe-8a1e133c0010.png"
    # Result 7
    url = "https://machinelearningmastery.com/wp-content/uploads/2019/02/sample_image.png" 
    c.classify(url)

main()