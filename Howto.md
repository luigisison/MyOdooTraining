##How to

###Enable followers
* In ```openacademy.py```, add ```_inherit = ["mail.thread"]``` to ```class OpenAcademySession(models.Model)```
* In ```__openerp__.py```, change ```'depends': ["base"]``` to ```'depends': ["base","mail"]```
