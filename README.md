# django-login-logout-auth

1)src - project directory <br>

2)mystie - main login stuffs

### Templates
 contain html files
 <ul>
  <li>mysite</li>
  <ol>
    <li>home.html</li>
    <li>login.html</li>
    <li>register.html</li>
  </ol>
  <li>registration</li>
  <ol>
    <li>logged_out.html</html>
  </ol>
  
 </ul>
 
 ### URLS :

src urls :
   ```
   from django.contrib.auth import views as auth_views
   ```
   will import the authentication stuff
   <br>
   for r'^login/' we used template name : 'mysite/login.html'
   for r'^logout/' we used template name : 'registration/logged_out.html'
   <br>
   
   
   including mysite urls with
   ```
   url(r'^',include('mysite.urls')
   ```
   
mysite urls :

 for r'^$' it will call home.html <br>
 for r'^register' it will call register.html

### Forms :

```
from django import forms
```
username = forms.charField(required = true, max_length = 32, lable = "username")


   

 
 
