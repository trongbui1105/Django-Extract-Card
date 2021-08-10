# Django Vietnamese ID card OCR
## The system extracts information from personal card
- Creating by a team of student at CTU 
- Text detection is based CTPN and text recognition is based crnn and ctc belong to vietocr systems.  
- This is a scientific research project about the topic of optical character recognition 

## Installation
Creation of virtual environments is done by executing the command venv:
```bash
python3 -m venv env
```

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:
```bash
source env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements:
```bash
pip3 install -r requirements.txt
```      
## Download model 
   https://drive.google.com/drive/folders/1qCuRMkrO7jE1UK5n_nyrtFg0I1slWm5X?usp=sharing
   After downloading, add 2 models to folder ocr/checkpoints for implementation

## Usage
Run the project with this command. Then open http://localhost:8000 in your browser to see the website.

```bash
python3 manage.py runserver
``` 
            
## Creator
 - Bùi Quốc Trọng                  >  email: buiquoctrong110500@gmail.com
 - Nguyễn Nhĩ Thái                 >  email: nguyennhithai4620@gmail.com
 - Trương Hoàng Thuận
 - Võ Thành Long


