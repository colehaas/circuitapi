from django.db import models

# These models mirror the Clinical Trials API Study Structure found here: 
# https://clinicaltrials.gov/api/info/study_structure 

# Types and character limits can be found here: 
# https://prsinfo.clinicaltrials.gov/definitions.html


### Study Structure ###

## Protocol Section ##

# Identification Module # 

#class NCTIdAlias(models.Model):
    #NCTIdAlias = models.CharField(max_length=30)

class IdentificationModule(models.Model):
    NCTId = models.CharField(max_length=30, null=True)
    #NCTIdAliasList = models.ForeignKey(NCTIdAlias)
    BriefTitle = models.CharField(max_length=300, null=True)
    OfficialTitle = models.CharField(max_length=600, null=True)
    Acronym = models.CharField(max_length=14, null=True)

# Status Module # 

class StatusModule(models.Model):
    StatusVerifiedDate = models.CharField(max_length=20, blank=True)
    OverallStatus = models.CharField(max_length=30, blank=True)
    WhyStopped = models.CharField(max_length=30, blank=True)
    StartDate = models.CharField(max_length=20, blank=True)
    PrimaryCompletionDate = models.CharField(max_length=20, blank=True)
    CompletionDate = models.CharField(max_length=20, blank=True)

class SponsorCollaboratorsModule(models.Model):
    pass



## Derived Section ##

