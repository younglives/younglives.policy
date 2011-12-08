""" Default content structure. """


from younglives.content.interfaces import *

STRUCTURE = [
             
    {'title' : 'Staff Intranet', 
     'id' : 'intranet', 
     'type' : 'Folder',
     'interfaces' : [IIntranetFolderMarker,],
     'subfolder' :[]},
             
    {'title' : 'Young Lives', 
     'id' : 'young-lives', 
     'type' : 'HomePage',
     'subfolder' :[]},
             
    {'title' : 'Who we are', 
     'id' : 'who-we-are', 
     'type' : 'Folder', 
     'transition' : 'publish',
     'interfaces' : [IWhoWeAreFolderMarker, ISiteTabMarker],
     'allowed_types' : ['Folder', 'Document', 'Topic'],
     'subfolder' : [
               
        {'title' : 'Young Lives partners', 
         'id' : 'young-lives-partners', 
         'type' : 'Document',
         'transition' : 'publish',},
         
        {'title' : 'Young Lives people', 
         'id' : 'young-lives-people', 
         'type' : 'Document',
         'transition' : 'publish',}, 
         
        {'title' : 'International Advisory Board', 
         'id' : 'international-advisory-board', 
         'type' : 'Document',
         'transition' : 'publish',},
         
        {'title' : 'Funders', 
         'id' : 'funders', 
         'type' : 'Document',
         'transition' : 'publish',},  
         
        {'title' : 'Links', 
         'id' : 'links', 
         'type' : 'Document',
         'transition' : 'publish',},  
         
        {'title' : 'Find out more', 
         'id' : 'find-out-more', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [ 
         
            {'title' : 'Contact details and map', 
             'id' : 'contact-details', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
            {'title' : 'Sign up for e-newsletter', 
             'id' : 'sign-up-for-e-newsletter', 
             'type' : 'Folder',
             'transition' : 'publish',},  
             
            {'title' : 'Sign up for e-alerts', 
             'id' : 'sign-up-for-e-alerts', 
             'type' : 'Folder',
             'transition' : 'publish',},  
             
            {'title' : 'Media enquiries', 
             'id' : 'media-enquiries', 
             'type' : 'Document',
             'transition' : 'publish',},
        
        ]},
        
    ]}, 
     
    {'title' : 'What we do', 
     'id' : 'what-we-do', 
     'type' : 'Folder', 
     'transition' : 'publish',
     'interfaces' : [IWhatWeDoFolderMarker, ISiteTabMarker],
     'allowed_types' : ['Folder', 'Document', 'Topic'],
     'subfolder' : [
                   
        {'title' : 'Our policy work', 
         'id' : 'our-policy-work', 
         'type' : 'Folder',
         'transition' : 'publish', 
         'subfolder' : [
                       
            {'title' : 'International priorities', 
             'id' : 'international-priorities', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Country priorities', 
             'id' : 'country-priorities', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Policy engagement', 
             'id' : 'policy-engagement', 
             'type' : 'Document',
             'transition' : 'publish',},
        ]}, 
         
        {'title' : 'Our methods', 
         'id' : 'our-methods', 
         'type' : 'Folder',
         'transition' : 'publish', 
         'subfolder' : [
                       
            {'title' : 'Household and child survey', 
             'id' : 'household-and-child-survey', 
             'type' : 'Folder',
             'transition' : 'publish',
             'subfolder' : [
                            
                {'title' : 'Questionnaires Sampling and attrition', 
                 'id' : 'questionnaires-sampling-and-attrition', 
                 'type' : 'Document',
                 'transition' : 'publish',},
                            
            ]},
             
            {'title' : 'Qualitative sub-sample research', 
             'id' : 'qualitative-sub-sample-research', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Research into policy and practice', 
             'id' : 'research-into-policy-and-practice', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Ethics', 'id' : 'ethics', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Methods toolkit', 
             'id' : 'methods-toolkit', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'FAQs', 'id' :
             'faqs', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Glossary A-Z', 
             'id' : 'glossary-a-z', 
             'type' : 'Document',
             'transition' : 'publish',},
        ]}, 
            
        {'title' : 'Access our data', 
         'id' : 'access-our-data', 
         'type' : 'Folder', 
         'transition' : 'publish',
         'subfolder' : [
                       
            {'title' : 'Link to ESDS data archive', 
             'id' : 'link-to-esds-data-archive', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Protocols for access', 
             'id' : 'protocols-for-access', 
             'type' : 'Document',
             'transition' : 'publish',},
            
        ]}, 
         
        {'title' : 'Data visualisation', 
         'id' : 'data-visualisation', 
         'type' : 'Folder',
         'transition' : 'publish', 
         'subfolder' : [
             
            {'title' : 'Virtual village', 
             'id' : 'virtual-village', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Round 3 data graphs and figures', 
             'id' : 'round-3-data-graphs-and-figures', 
             'type' : 'Document',
             'transition' : 'publish',},
        ]}, 
         
        {'title' : 'Children\'s voices', 
         'id' : 'childrens-voices', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
         
            {'title' : 'Child profiles', 
             'id' : 'child-profiles', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
            {'title' : 'Snapshots from Peru', 
             'id' : 'snapshots-from-peru', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
            {'title' : 'Short stories from Ethiopia', 
             'id' : 'short-stories-from-ethiopia', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'India participation film', 
             'id' : 'india-participation-film', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Vietnam diary and young journalists competition', 
             'id' : 'vietnam-diary-and-young-journalists-competition', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
            {'title' : 'Photo gallery', 
             'id' : 'photo-gallery', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
        ]},
         
        {'title' : 'News and events Media highlights and enquiries', 
         'id' : 'news-and-events-media-highlights-and-enquiries', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
                        
                {'title' : 'Events archive', 
                 'id' : 'events-archive', 
                 'type' : 'Folder',
                 'transition' : 'publish',
                 'subfolder' : [
                                
                    {'title' : 'Focus On Children conference', 
                     'id' : 'focus-on-children-conference', 
                     'type' : 'Document',
                     'transition' : 'publish',},
                     
                    {'title' : 'Netherlands roadshow', 
                     'id' : 'netherlands-roadshow', 
                     'type' : 'Document',
                     'transition' : 'publish',},
                     
                    {'title' : 'Sweden roadshow', 
                     'id' : 'sweden-roadshow', 
                     'type' : 'Document',
                     'transition' : 'publish',},
                     
                    {'title' : 'Global Challenges symposium', 
                     'id' : 'global-challenges-symposium', 
                     'type' : 'Document',
                     'transition' : 'publish',},            
                            
            ]},    
            
            {'title' : 'News archive', 
             'id' : 'news-archive', 
             'type' : 'Folder',
             'transition' : 'publish',},
             
            {'title' : 'Podcasts', 
             'id' : 'podcasts', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Media enquiries', 
             'id' : 'media-enquiries', 
             'type' : 'Document',
             'transition' : 'publish',},
             
        {'title' : 'Current findings', 
         'id' : 'current-findings', 
         'type' : 'Document',
         'transition' : 'publish',},
                        
        ]},
         
    ]},
    
    {'title' : 'Where we work', 
     'id' : 'where-we-work', 
     'type' : 'Folder',
     'transition' : 'publish',
     'interfaces' :[IWhereWeWorkFolderMarker, ISiteTabMarker,],
     'subfolder' : [
               
        {'title' : 'Ethiopia', 
         'id' : 'ethiopia', 
         'type' : 'Document',
         'transition' : 'publish',},
         
        {'title' : 'India', 
         'id' : 'india', 
         'type' : 'Document',
         'transition' : 'publish',}, 
         
        {'title' : 'Peru', 
         'id' : 'peru', 
         'type' : 'Document',
         'transition' : 'publish',},
         
        {'title' : 'Vietnam', 
         'id' : 'vietnam', 
         'type' : 'Document',
         'transition' : 'publish',},
         
    ]},
    
    {'title' : 'Our themes', 
     'id' : 'our-themes', 
     'type' : 'Folder',
     'transition' : 'publish',
     'interfaces' :[IOurThemesFolderMarker, ISiteTabMarker],
     'subfolder' : [
               
        {'title' : 'Dynamics of childhood poverty', 
         'id' : 'dynamics-of-childhood-poverty', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
                        
            {'title' : 'Livelihoods', 
             'id' : 'livelihoods', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Poverty cycles', 
             'id' : 'poverty-cycles', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Shocks', 
             'id' : 'shocks', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Economic growth', 
             'id' : 'economic-growth', 
             'type' : 'Document',
             'transition' : 'publish',},  
             
            {'title' : 'Social protection', 
             'id' : 'social-protection', 
             'type' : 'Document',
             'transition' : 'publish',}, 
             
            {'title' : 'Access to basic services', 
             'id' : 'access-to-basic-services', 
             'type' : 'Document',
             'transition' : 'publish',}, 
             
            {'title' : 'Migration', 
             'id' : 'migration', 
             'type' : 'Document',
             'transition' : 'publish',}, 
                   
        ]},   
         
        {'title' : 'Children\'s experience of poverty', 
         'id' : 'childrens-experience-of-poverty', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
                        
            {'title' : 'Risk and resilience', 
             'id' : 'risk-and-resilience', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Health and nutrition', 
             'id' : 'health-and-nutrition', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Psychosocial well-being', 
             'id' : 'psychosocial-well-being', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Children\'s views of poverty', 
             'id' : 'childrens-views-of-poverty', 
             'type' : 'Document',
             'transition' : 'publish',},  
             
            {'title' : 'Relationships and support', 
             'id' : 'relationships-and-support', 
             'type' : 'Document',
             'transition' : 'publish',}, 
             
            {'title' : 'Life events', 
             'id' : 'life-events', 
             'type' : 'Document',
             'transition' : 'publish',}, 
                   
        ]},
         
        {'title' : 'School, work, time use', 
         'id' : 'school-work-time-use', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
                        
            {'title' : 'Early education and care', 
             'id' : 'early-education-and-care', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'School access and quality', 
             'id' : 'school-access-and-quality', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Learning and outcomes', 
             'id' : 'learning-and-outcomes', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Education transitions', 
             'id' : 'education-transitions', 
             'type' : 'Document',
             'transition' : 'publish',},  
             
            {'title' : 'Children\'s work', 
             'id' : 'childrens-work', 
             'type' : 'Document',
             'transition' : 'publish',}, 
             
            {'title' : 'Children\'s time use', 
             'id' : 'childrens-time-use', 
             'type' : 'Document',
             'transition' : 'publish',}, 
                   
        ]}, 
         
        {'title' : 'Cross-cutting analysis', 
         'id' : 'cross-cutting-analysis', 
         'type' : 'Folder',
         'transition' : 'publish',
         'subfolder' : [
                        
            {'title' : 'Inequalities and social exclusion', 
             'id' : 'inequalities-and-social-exclusion', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Ethnicity/caste', 
             'id' : 'ethnicity-caste', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Gender', 
             'id' : 'gender', 
             'type' : 'Document',
             'transition' : 'publish',},
             
            {'title' : 'Urban/rural location', 
             'id' : 'urban-rural-location', 
             'type' : 'Document',
             'transition' : 'publish',},  
             
            {'title' : 'Wealth inequalities', 
             'id' : 'wealth-inequalities', 
             'type' : 'Document',
             'transition' : 'publish',}, 
             
            {'title' : 'Policy evaluation', 
             'id' : 'policy-evaluation', 
             'type' : 'Document',
             'transition' : 'publish',}, 
                   
        ]}, 
         
    ]},
     
    {'title' : 'Our publications', 
     'id' : 'our-publications', 
     'type' : 'Folder',
     'transition' : 'publish',
     'interfaces' :[IOurPublicationsFolderMarker, ISiteTabMarker,],
     'subfolder' : [
               
        {'title' : 'Working papers', 
         'id' : 'working-papers', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Technical notes', 
         'id' : 'technical-notes', 
         'type' : 'Folder',
         'transition' : 'publish',}, 
         
        {'title' : 'Policy papers', 
         'id' : 'policy-papers', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Journal articles and other publications', 
         'id' : 'journal-articles-and-other-publications', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Country reports', 
         'id' : 'country-reports', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Student papers', 
         'id' : 'student-papers', 
         'type' : 'Folder',
         'transition' : 'publish',}, 
         
        {'title' : 'Conference presentations', 
         'id' : 'conference-presentations', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Project documents', 
         'id' : 'project-documents', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
        {'title' : 'Key findings sheets', 
         'id' : 'key-findings-sheets', 
         'type' : 'Folder',
         'transition' : 'publish',},
         
    ]},
     
]
