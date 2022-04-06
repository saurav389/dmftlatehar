from unicodedata import name
from django.urls import path
from django.contrib.auth import views 
from .views import (
                    homeView,
					teamView,
					projectView,
					HighPriorityView,
					LowPriorityView,
					aboutdmft,
					directlyAffectedArea,
					indirectAffectedArea,
					pressRelease,
					photoGallery,
					AnnualreportView,
					AuditreportView
					)

urlpatterns = [
	path('',homeView,name='home'),
	path('team/',teamView,name='team'),
	path('dmft',aboutdmft,name='dmft'),
	path('directaffectedarea',directlyAffectedArea,name='directaffectedarea'),
	path('indirectaffectedarea',indirectAffectedArea,name='indirectaffectedarea'),
	path('project/',projectView,name='project'),
	path('highpriority/',HighPriorityView,name='highpriority'),
	path('lowpriority/',LowPriorityView,name='lowpriority'),
	path('press/',pressRelease,name='press'),
	path('photo/',photoGallery,name='photo'),
	path('annualreport/',AnnualreportView,name='annualreport'),
	path('auditreport/',AuditreportView,name='auditreport')
]

