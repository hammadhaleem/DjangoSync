from django.db import models

# Create your models here.
'''
threads					
	sno					auto increment
	message 			text 			
	item_id				varchar 200		
	visible_id			int 		
	timestamp			time		
	moderation			boolean		
	created_by_user		varchar 200		
	parent_id			int Default =0 	
	url					text		
					

					
liked_by					
	sno			int 		
	userid		varchar 200		
				

#Later stages Phase II 
visible_to_users				
	visible_id		int 		
	userid			varchar		


report_abuse_thread 					
	sno			int 		
	userid		varchar 200		
	comment		text		
					
alerts_users					
	sno					int 		
	isread				boolean		
	userid				varchar 200		
	forum_main_sno		int 		
'''