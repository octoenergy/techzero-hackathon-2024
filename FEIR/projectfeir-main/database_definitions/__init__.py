from .db import db, app
from .appliance_specifications import ApplianceSpecifications
from .audit_outcomes import AuditOutcome
from .consumer_business import ConsumerBusiness
from .consumer_site import ConsumerSite
from .supplier_business import SupplierBusiness
from .supplier_consumer_partnerships import SupplierConsumerPartnerships
from .supplier_consumer_transaction import SupplierConsumerTransaction
from .supplier_product import SupplierProduct

with app.app_context():
    db.create_all()
    
    
