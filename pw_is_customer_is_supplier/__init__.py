# -*- coding: utf-8 -*-
from . import models

def update_existing_partners(cr, registry):
    # This hooks for update existing partner
    cr.execute("UPDATE res_partner SET customer='t' where customer_rank > 0;")
    cr.execute("UPDATE res_partner SET supplier='t' where supplier_rank > 0;")
