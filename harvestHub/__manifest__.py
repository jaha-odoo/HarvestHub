{
    'name':'Harvest Hub',
    'depends': ['base','mail'],
    'author':'jatin',
    'installable':True,
    'data':[
        'security/ir.model.access.csv',
        'views/harvest_farmer.xml',
        'views/harvest_menu.xml',
    ],
    'application':True,
}