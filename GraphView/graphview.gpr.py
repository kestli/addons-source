register(VIEW, 
         id    = 'graphview',
         name  = _("Graph View"),
         category = ("Ancestry", _("Charts")),
         description =  _("Dynamic graph of relations"),
         version = '1.0.45',
         gramps_target_version = "5.0",
         status = STABLE,
         fname = 'graphview.py',
         authors = ["Gary Burton"],
         authors_email = ["gary.burton@zen.co.uk"],
         viewclass = 'GraphView',
  )
