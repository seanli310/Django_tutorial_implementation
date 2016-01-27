Interact with Database
----------------------------------------------------------------------

Install MySQL from website

-Configure MySQL and Terminal;

-Install MySQLdb class driver
 http://www.djangoproject.com/r/python-mysql/
----------------------------------------------------------------------
from django.shortcuts import render_to_response
import MySQLdb

-Connect the database with python

def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})
    

----------------------------------------------------------------------
-Using Django to rewrite:

from django.shortcuts import render_to_response
from mysite.books.models import Book

def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})


----------------------------------------------------------------------
+ MVC pattern
- M 代表模型（Model），即数据存取层。 该层处理与数据相关的所有事务：    如何存取、如何验证有效性、包含哪些行为以及数据之间的关系等。

- T 代表模板(Template)，即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显示。

- V 代表视图（View），即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看作模型与模板之间的桥梁。
----------------------------------------------------------------------
+ MVC pattern example: // refer from Internet.

## MVC Pattern
+ Model-View-Controller
  - Model: represent object, can have logic to update controller if its data changes
  - View: represent visualization of data from Model
  - Controller: act on Model and View, control data flow into Model and update View when data changes

+ Structure
  - app: models, views, controllers
  - config: global server configurations
  - lib: assorted libraries

+ Procedure
  - server routes the request to certain controller
  - controller interprets the request, load reqested information from models
  - controller passes information from model to view
  - final view is sent to user
----------------------------------------------------------------------
+ Model

``` 
   public class Student{
       private String id;
       private String name;

       public String getId(){
           return id;
       }

       public String getName(){
           return name;
       }

       public void setId(String id){
           this.id = id;
       }

       public void setName(String name){
           this.name = name;
       }	
    }
```
----------------------------------------------------------------------
+ View

``` 
    public class StudentView{
	   public void printInfo(String studentName, String studentId){
	        System.out.println("Student: " + studentName);
	        System.out.println("Student ID: " + studentId);
	   }
    }
```
----------------------------------------------------------------------
+ Controller

``` 
   public class StudentController{
	   private Student model;
	   private StudentView view;

	   public StudentController(Student model, StudentView view){
	   	   this.model = model;
	   	   this.view = view;
	   }

	   public void setStudentName(String name){
	   	   model.setName(name);
	   }

	   public void setStudentId(String id){
	   	   model.setId(id);
	   }

	   public String getStudentName(){
	   	   return model.getName();
	   }

	   public String getStudentId(){
	   	   return model.getId();
	   }

	   public void updateView(){
	   	   view.printInfo(model.getName(), model.getId());
	   }
    }
```

---------------------------------------------------------------------

Setting the Django setting.py to configure the MySQL properly:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '/home/django/mydata.db',
		DATABASE_USER = ''
		DATABASE_PASSWORD = ''
		DATABASE_HOST = ''
		DATABASE_PORT = ''
    }
}

>>> from django.db import connection
>>> cursor = connection.cursor()

