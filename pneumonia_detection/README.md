# Pneumonia Detection

Detects pneumonia from x-ray images of lungs.


When a person is infected with penumonia, infiltrates, such as pleural fluids, are present in the lungs, which can be identified from lung x-rays. 

The model is trained on two classes of such lung x-rays - normal and pneumonic - and predicts if the input x-ray image is normal or pneumonic.


Parameters : 1,119,554

Accuracy : ~83%

Model file is included, accuracy can be improved.


Code can be run as GUI or CLI.
CLI : `python cli.py --type {image, folder} --model_path /path/to/model/to/be/used --path /path/to/image/OR/folder/of/images`

GUI : `python gui.py`
