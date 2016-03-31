##How to

###Enable followers
* In ```openacademy.py```, add ```_inherit = ["mail.thread"]``` to ```class OpenAcademySession(models.Model)```
* In ```__openerp__.py```, change ```'depends': ["base"]``` to ```'depends': ["base","mail"]```
* In ```openacademy_views.xml```, add ```<div class="oe_chatter">
                        <field name="message_follower_ids" widget="mail_followers"/>
                        <field name="message_ids" widget="mail_thread"/>
                    </div> ```
